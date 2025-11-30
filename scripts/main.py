#!/usr/bin/env python3
"""
Personal Trainer Agent - Main Orchestrator
Coordinates workout generation, progress tracking, and exercise recommendations.
"""

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Optional

from workout_generator import WorkoutGenerator
from exercise_library import ExerciseLibrary
from progress_tracker import ProgressTracker


class PersonalTrainerAgent:
    """Main orchestrator for the Personal Trainer Agent."""

    def __init__(self, data_dir: Optional[str] = None):
        """Initialize the Personal Trainer Agent.

        Args:
            data_dir: Directory for storing user data. Defaults to ~/.personal-trainer
        """
        self.data_dir = Path(data_dir or os.environ.get(
            'TRAINER_DATA_DIR',
            os.path.expanduser('~/.personal-trainer')
        ))
        self.data_dir.mkdir(parents=True, exist_ok=True)

        self.workout_generator = WorkoutGenerator()
        self.exercise_library = ExerciseLibrary()
        self.progress_tracker = ProgressTracker(self.data_dir)

        self.user_profile: dict = {}
        self._load_user_profile()

    def _load_user_profile(self) -> None:
        """Load user profile from disk if it exists."""
        profile_path = self.data_dir / 'profile.json'
        if profile_path.exists():
            with open(profile_path, 'r') as f:
                self.user_profile = json.load(f)

    def _save_user_profile(self) -> None:
        """Save user profile to disk."""
        profile_path = self.data_dir / 'profile.json'
        with open(profile_path, 'w') as f:
            json.dump(self.user_profile, f, indent=2)

    def assess_user(
        self,
        goal: str,
        experience_level: str,
        equipment: str,
        days_per_week: int,
        session_duration: int = 60,
        limitations: Optional[list] = None
    ) -> dict:
        """Perform initial user assessment.

        Args:
            goal: Primary fitness goal (muscle_building, fat_loss, strength, endurance)
            experience_level: beginner, intermediate, or advanced
            equipment: full_gym, home_gym, bodyweight, or limited
            days_per_week: Training frequency (2-6)
            session_duration: Minutes per session (30-90)
            limitations: List of injuries or health considerations

        Returns:
            Assessment results and recommended program type
        """
        self.user_profile = {
            'goal': goal,
            'experience_level': experience_level,
            'equipment': equipment,
            'days_per_week': days_per_week,
            'session_duration': session_duration,
            'limitations': limitations or [],
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat()
        }

        # Determine recommended split
        split_recommendations = {
            2: 'full_body',
            3: 'full_body',
            4: 'upper_lower',
            5: 'upper_lower_ppl',
            6: 'ppl'
        }

        recommended_split = split_recommendations.get(days_per_week, 'full_body')
        self.user_profile['recommended_split'] = recommended_split

        self._save_user_profile()

        return {
            'profile': self.user_profile,
            'recommended_split': recommended_split,
            'message': f"Assessment complete. Recommended: {recommended_split} split, "
                      f"{days_per_week}x/week for {goal.replace('_', ' ')}."
        }

    def generate_workout_plan(
        self,
        weeks: int = 4,
        split_type: Optional[str] = None
    ) -> dict:
        """Generate a complete workout plan.

        Args:
            weeks: Number of weeks for the program
            split_type: Override the recommended split if desired

        Returns:
            Complete workout plan with all sessions
        """
        if not self.user_profile:
            return {'error': 'Please complete assessment first'}

        split = split_type or self.user_profile.get('recommended_split', 'full_body')

        plan = self.workout_generator.generate_plan(
            split_type=split,
            experience_level=self.user_profile['experience_level'],
            goal=self.user_profile['goal'],
            equipment=self.user_profile['equipment'],
            weeks=weeks,
            limitations=self.user_profile.get('limitations', [])
        )

        # Save the current plan
        plan_path = self.data_dir / 'current_plan.json'
        with open(plan_path, 'w') as f:
            json.dump(plan, f, indent=2)

        return plan

    def get_exercise_info(self, exercise_name: str) -> dict:
        """Get detailed information about an exercise.

        Args:
            exercise_name: Name of the exercise

        Returns:
            Exercise details including instructions and form cues
        """
        return self.exercise_library.get_exercise(exercise_name)

    def get_exercise_alternatives(
        self,
        exercise_name: str,
        reason: str = 'general'
    ) -> list:
        """Get alternative exercises.

        Args:
            exercise_name: Name of the exercise to find alternatives for
            reason: Why alternatives are needed (injury, equipment, preference)

        Returns:
            List of alternative exercises
        """
        return self.exercise_library.get_alternatives(exercise_name, reason)

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
            Confirmation and any insights
        """
        return self.progress_tracker.log_workout(exercises, notes)

    def get_progress_report(
        self,
        exercise: Optional[str] = None,
        period: str = 'month'
    ) -> dict:
        """Get progress report.

        Args:
            exercise: Specific exercise to report on, or None for overall
            period: Time period (week, month, quarter, year)

        Returns:
            Progress report with trends and insights
        """
        return self.progress_tracker.get_report(exercise, period)

    def check_plateau(self, exercise: str) -> dict:
        """Check if user has hit a plateau on an exercise.

        Args:
            exercise: Exercise to check

        Returns:
            Plateau analysis and recommendations
        """
        return self.progress_tracker.detect_plateau(exercise)

    def recommend_deload(self) -> dict:
        """Check if a deload week is recommended.

        Returns:
            Deload recommendation with reasoning
        """
        weeks_trained = self.progress_tracker.get_consecutive_weeks()
        fatigue_score = self.progress_tracker.estimate_fatigue()

        should_deload = weeks_trained >= 6 or fatigue_score > 7

        return {
            'recommend_deload': should_deload,
            'weeks_since_last_deload': weeks_trained,
            'fatigue_score': fatigue_score,
            'message': "Time for a deload week!" if should_deload
                      else f"Keep training. Deload in ~{6 - weeks_trained} weeks."
        }


def main():
    """Example usage of the Personal Trainer Agent."""
    trainer = PersonalTrainerAgent()

    # Assess user
    assessment = trainer.assess_user(
        goal='muscle_building',
        experience_level='intermediate',
        equipment='full_gym',
        days_per_week=4,
        session_duration=60,
        limitations=[]
    )
    print(f"Assessment: {assessment['message']}")

    # Generate plan
    plan = trainer.generate_workout_plan(weeks=4)
    print(f"Generated {len(plan.get('weeks', []))} week program")

    # Get exercise info
    squat_info = trainer.get_exercise_info('barbell_squat')
    print(f"Squat targets: {squat_info.get('primary_muscles', [])}")


if __name__ == '__main__':
    main()
