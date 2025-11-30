#!/usr/bin/env python3
"""
Progress Tracker Module
Tracks workouts, analyzes progress, and detects plateaus.
"""

import json
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional
from collections import defaultdict


class ProgressTracker:
    """Tracks workout progress and provides analytics."""

    def __init__(self, data_dir: Path):
        """Initialize the progress tracker.

        Args:
            data_dir: Directory for storing progress data
        """
        self.data_dir = data_dir
        self.workouts_file = data_dir / 'workouts.json'
        self.workouts = self._load_workouts()

    def _load_workouts(self) -> list:
        """Load workouts from disk."""
        if self.workouts_file.exists():
            with open(self.workouts_file, 'r') as f:
                return json.load(f)
        return []

    def _save_workouts(self) -> None:
        """Save workouts to disk."""
        with open(self.workouts_file, 'w') as f:
            json.dump(self.workouts, f, indent=2)

    def log_workout(
        self,
        exercises: list,
        notes: Optional[str] = None
    ) -> dict:
        """Log a completed workout.

        Args:
            exercises: List of dicts with exercise, sets, reps, weight
            notes: Optional notes about the session

        Returns:
            Confirmation and insights
        """
        workout = {
            'date': datetime.now().isoformat(),
            'exercises': exercises,
            'notes': notes
        }

        self.workouts.append(workout)
        self._save_workouts()

        # Generate insights
        insights = self._generate_workout_insights(exercises)

        return {
            'status': 'logged',
            'workout_number': len(self.workouts),
            'exercises_logged': len(exercises),
            'insights': insights
        }

    def _generate_workout_insights(self, exercises: list) -> list:
        """Generate insights from the logged workout."""
        insights = []

        for exercise in exercises:
            exercise_name = exercise.get('exercise', exercise.get('name', ''))
            history = self._get_exercise_history(exercise_name)

            if len(history) >= 2:
                prev = history[-2]
                curr = exercise

                # Check for PR
                prev_weight = prev.get('weight', 0)
                curr_weight = curr.get('weight', 0)

                if curr_weight > prev_weight:
                    insights.append(
                        f"PR on {exercise_name}! {prev_weight} -> {curr_weight}"
                    )

                # Check for rep PR at same weight
                if curr_weight == prev_weight:
                    prev_reps = prev.get('reps', 0)
                    curr_reps = curr.get('reps', 0)
                    if curr_reps > prev_reps:
                        insights.append(
                            f"Rep PR on {exercise_name}! {prev_reps} -> {curr_reps} reps"
                        )

        if not insights:
            insights.append("Solid workout! Keep pushing.")

        return insights

    def _get_exercise_history(self, exercise_name: str) -> list:
        """Get history for a specific exercise."""
        history = []
        for workout in self.workouts:
            for exercise in workout.get('exercises', []):
                name = exercise.get('exercise', exercise.get('name', ''))
                if name.lower() == exercise_name.lower():
                    exercise_with_date = exercise.copy()
                    exercise_with_date['date'] = workout['date']
                    history.append(exercise_with_date)
        return history

    def get_report(
        self,
        exercise: Optional[str] = None,
        period: str = 'month'
    ) -> dict:
        """Get progress report.

        Args:
            exercise: Specific exercise to report on
            period: Time period (week, month, quarter, year)

        Returns:
            Progress report with trends
        """
        # Calculate date range
        now = datetime.now()
        period_days = {
            'week': 7,
            'month': 30,
            'quarter': 90,
            'year': 365
        }
        days = period_days.get(period, 30)
        start_date = now - timedelta(days=days)

        # Filter workouts in period
        period_workouts = [
            w for w in self.workouts
            if datetime.fromisoformat(w['date']) >= start_date
        ]

        report = {
            'period': period,
            'total_workouts': len(period_workouts),
            'start_date': start_date.isoformat(),
            'end_date': now.isoformat()
        }

        if exercise:
            report['exercise'] = exercise
            report['exercise_data'] = self._get_exercise_report(exercise, period_workouts)
        else:
            report['summary'] = self._get_overall_summary(period_workouts)

        return report

    def _get_exercise_report(self, exercise_name: str, workouts: list) -> dict:
        """Get detailed report for a specific exercise."""
        entries = []

        for workout in workouts:
            for ex in workout.get('exercises', []):
                name = ex.get('exercise', ex.get('name', ''))
                if name.lower() == exercise_name.lower():
                    entries.append({
                        'date': workout['date'],
                        'weight': ex.get('weight', 0),
                        'reps': ex.get('reps', 0),
                        'sets': ex.get('sets', 0)
                    })

        if not entries:
            return {'error': 'No data for this exercise'}

        weights = [e['weight'] for e in entries if e['weight']]

        return {
            'total_sessions': len(entries),
            'starting_weight': weights[0] if weights else 0,
            'current_weight': weights[-1] if weights else 0,
            'max_weight': max(weights) if weights else 0,
            'weight_gain': (weights[-1] - weights[0]) if len(weights) >= 2 else 0,
            'trend': 'improving' if len(weights) >= 2 and weights[-1] > weights[0] else 'stable',
            'history': entries
        }

    def _get_overall_summary(self, workouts: list) -> dict:
        """Get overall summary of workouts."""
        if not workouts:
            return {'message': 'No workouts in this period'}

        # Count exercises
        exercise_counts = defaultdict(int)
        muscle_groups = defaultdict(int)

        for workout in workouts:
            for ex in workout.get('exercises', []):
                name = ex.get('exercise', ex.get('name', ''))
                exercise_counts[name] += 1

        return {
            'workouts_completed': len(workouts),
            'unique_exercises': len(exercise_counts),
            'most_frequent': sorted(
                exercise_counts.items(),
                key=lambda x: x[1],
                reverse=True
            )[:5],
            'consistency_score': self._calculate_consistency(workouts)
        }

    def _calculate_consistency(self, workouts: list) -> float:
        """Calculate consistency score (0-100)."""
        if not workouts:
            return 0

        if len(workouts) < 2:
            return 100

        # Get workout dates
        dates = sorted([
            datetime.fromisoformat(w['date']).date()
            for w in workouts
        ])

        # Calculate average gap between workouts
        gaps = []
        for i in range(1, len(dates)):
            gap = (dates[i] - dates[i-1]).days
            gaps.append(gap)

        avg_gap = sum(gaps) / len(gaps)

        # Score based on average gap (ideal is 1-3 days)
        if avg_gap <= 3:
            return 100
        elif avg_gap <= 5:
            return 80
        elif avg_gap <= 7:
            return 60
        else:
            return max(0, 100 - (avg_gap * 5))

    def detect_plateau(self, exercise_name: str) -> dict:
        """Detect if user has hit a plateau.

        Args:
            exercise_name: Exercise to check

        Returns:
            Plateau analysis and recommendations
        """
        history = self._get_exercise_history(exercise_name)

        if len(history) < 4:
            return {
                'plateau_detected': False,
                'message': 'Not enough data to detect plateau (need 4+ sessions)'
            }

        # Look at last 4 sessions
        recent = history[-4:]
        weights = [h.get('weight', 0) for h in recent]

        # Check if weight has been stagnant
        weight_range = max(weights) - min(weights)
        is_plateau = weight_range <= 5  # Less than 5lb variation

        result = {
            'plateau_detected': is_plateau,
            'sessions_analyzed': len(recent),
            'weight_range': weight_range,
            'recent_weights': weights
        }

        if is_plateau:
            result['recommendations'] = [
                'Consider a deload week (reduce weight by 40%)',
                'Try changing rep range (if doing 8-12, try 4-6)',
                'Add a variation of this exercise',
                'Increase training frequency for this muscle',
                'Check your nutrition and sleep',
                'Try different tempo (slow negatives)'
            ]
        else:
            result['message'] = 'No plateau detected. Keep progressing!'

        return result

    def get_consecutive_weeks(self) -> int:
        """Get number of consecutive weeks trained."""
        if not self.workouts:
            return 0

        # Get unique weeks with workouts
        weeks = set()
        for workout in self.workouts:
            date = datetime.fromisoformat(workout['date'])
            week_num = date.isocalendar()[1]
            year = date.year
            weeks.add((year, week_num))

        # Count consecutive weeks from most recent
        sorted_weeks = sorted(weeks, reverse=True)
        consecutive = 1

        for i in range(1, len(sorted_weeks)):
            prev_year, prev_week = sorted_weeks[i-1]
            curr_year, curr_week = sorted_weeks[i]

            # Check if consecutive
            if prev_year == curr_year and prev_week - curr_week == 1:
                consecutive += 1
            elif prev_year - curr_year == 1 and prev_week == 1 and curr_week >= 51:
                consecutive += 1
            else:
                break

        return consecutive

    def estimate_fatigue(self) -> float:
        """Estimate current fatigue level (1-10 scale).

        Based on recent training volume and frequency.
        """
        if not self.workouts:
            return 1

        # Look at last 2 weeks
        two_weeks_ago = datetime.now() - timedelta(days=14)
        recent = [
            w for w in self.workouts
            if datetime.fromisoformat(w['date']) >= two_weeks_ago
        ]

        if not recent:
            return 1

        # Calculate fatigue factors
        workout_count = len(recent)
        total_sets = sum(
            sum(ex.get('sets', 3) for ex in w.get('exercises', []))
            for w in recent
        )

        # Normalize to 1-10 scale
        workout_fatigue = min(workout_count / 2, 5)  # Max 5 from frequency
        volume_fatigue = min(total_sets / 50, 5)  # Max 5 from volume

        return round(workout_fatigue + volume_fatigue, 1)

    def get_personal_records(self) -> dict:
        """Get all-time personal records for each exercise."""
        records = {}

        for workout in self.workouts:
            for ex in workout.get('exercises', []):
                name = ex.get('exercise', ex.get('name', ''))
                weight = ex.get('weight', 0)

                if name not in records or weight > records[name]['weight']:
                    records[name] = {
                        'weight': weight,
                        'reps': ex.get('reps', 0),
                        'date': workout['date']
                    }

        return records
