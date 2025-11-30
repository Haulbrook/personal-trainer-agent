#!/usr/bin/env python3
"""
Workout Generator Module
Generates customized workout plans based on user parameters.
"""

from typing import Optional


class WorkoutGenerator:
    """Generates workout plans based on user profile and goals."""

    def __init__(self):
        """Initialize the workout generator with exercise templates."""
        self.splits = {
            'full_body': self._get_full_body_template(),
            'upper_lower': self._get_upper_lower_template(),
            'ppl': self._get_ppl_template(),
            'upper_lower_ppl': self._get_upper_lower_ppl_template()
        }

        self.rep_schemes = {
            'strength': {'sets': 4, 'reps': '4-6', 'rest': '3-5 min'},
            'muscle_building': {'sets': 3, 'reps': '8-12', 'rest': '60-90 sec'},
            'fat_loss': {'sets': 3, 'reps': '12-15', 'rest': '30-60 sec'},
            'endurance': {'sets': 2, 'reps': '15-20', 'rest': '30 sec'}
        }

    def generate_plan(
        self,
        split_type: str,
        experience_level: str,
        goal: str,
        equipment: str,
        weeks: int = 4,
        limitations: Optional[list] = None
    ) -> dict:
        """Generate a complete workout plan.

        Args:
            split_type: Type of training split
            experience_level: User's experience level
            goal: Primary fitness goal
            equipment: Available equipment
            weeks: Number of weeks for the program
            limitations: Any injuries or limitations

        Returns:
            Complete workout plan dictionary
        """
        limitations = limitations or []

        # Get base template
        template = self.splits.get(split_type, self.splits['full_body'])

        # Adjust for experience level
        template = self._adjust_for_experience(template, experience_level)

        # Adjust for equipment
        template = self._adjust_for_equipment(template, equipment)

        # Adjust for limitations
        template = self._adjust_for_limitations(template, limitations)

        # Apply rep scheme based on goal
        rep_scheme = self.rep_schemes.get(goal, self.rep_schemes['muscle_building'])
        template = self._apply_rep_scheme(template, rep_scheme)

        # Build weekly structure
        plan = {
            'split_type': split_type,
            'goal': goal,
            'experience_level': experience_level,
            'weeks': []
        }

        for week_num in range(1, weeks + 1):
            week = {
                'week_number': week_num,
                'sessions': template['sessions'],
                'notes': self._get_week_notes(week_num, weeks)
            }
            plan['weeks'].append(week)

        return plan

    def _get_full_body_template(self) -> dict:
        """Get full body workout template."""
        return {
            'name': 'Full Body',
            'days_per_week': 3,
            'sessions': [
                {
                    'name': 'Full Body A',
                    'exercises': [
                        {'name': 'Squat', 'type': 'compound', 'muscle': 'legs'},
                        {'name': 'Bench Press', 'type': 'compound', 'muscle': 'chest'},
                        {'name': 'Barbell Row', 'type': 'compound', 'muscle': 'back'},
                        {'name': 'Overhead Press', 'type': 'compound', 'muscle': 'shoulders'},
                        {'name': 'Plank', 'type': 'core', 'muscle': 'core'}
                    ]
                },
                {
                    'name': 'Full Body B',
                    'exercises': [
                        {'name': 'Deadlift', 'type': 'compound', 'muscle': 'legs'},
                        {'name': 'Incline Press', 'type': 'compound', 'muscle': 'chest'},
                        {'name': 'Pull-ups', 'type': 'compound', 'muscle': 'back'},
                        {'name': 'Dumbbell Lunges', 'type': 'compound', 'muscle': 'legs'},
                        {'name': 'Face Pulls', 'type': 'isolation', 'muscle': 'shoulders'}
                    ]
                }
            ]
        }

    def _get_upper_lower_template(self) -> dict:
        """Get upper/lower split template."""
        return {
            'name': 'Upper/Lower',
            'days_per_week': 4,
            'sessions': [
                {
                    'name': 'Upper A',
                    'exercises': [
                        {'name': 'Bench Press', 'type': 'compound', 'muscle': 'chest'},
                        {'name': 'Barbell Row', 'type': 'compound', 'muscle': 'back'},
                        {'name': 'Overhead Press', 'type': 'compound', 'muscle': 'shoulders'},
                        {'name': 'Pull-ups', 'type': 'compound', 'muscle': 'back'},
                        {'name': 'Face Pulls', 'type': 'isolation', 'muscle': 'shoulders'},
                        {'name': 'Tricep Pushdown', 'type': 'isolation', 'muscle': 'triceps'},
                        {'name': 'Bicep Curl', 'type': 'isolation', 'muscle': 'biceps'}
                    ]
                },
                {
                    'name': 'Lower A',
                    'exercises': [
                        {'name': 'Squat', 'type': 'compound', 'muscle': 'quads'},
                        {'name': 'Romanian Deadlift', 'type': 'compound', 'muscle': 'hamstrings'},
                        {'name': 'Leg Press', 'type': 'compound', 'muscle': 'quads'},
                        {'name': 'Leg Curl', 'type': 'isolation', 'muscle': 'hamstrings'},
                        {'name': 'Calf Raises', 'type': 'isolation', 'muscle': 'calves'}
                    ]
                },
                {
                    'name': 'Upper B',
                    'exercises': [
                        {'name': 'Incline Dumbbell Press', 'type': 'compound', 'muscle': 'chest'},
                        {'name': 'Cable Row', 'type': 'compound', 'muscle': 'back'},
                        {'name': 'Dumbbell Shoulder Press', 'type': 'compound', 'muscle': 'shoulders'},
                        {'name': 'Lat Pulldown', 'type': 'compound', 'muscle': 'back'},
                        {'name': 'Lateral Raises', 'type': 'isolation', 'muscle': 'shoulders'},
                        {'name': 'Skull Crushers', 'type': 'isolation', 'muscle': 'triceps'},
                        {'name': 'Hammer Curl', 'type': 'isolation', 'muscle': 'biceps'}
                    ]
                },
                {
                    'name': 'Lower B',
                    'exercises': [
                        {'name': 'Deadlift', 'type': 'compound', 'muscle': 'posterior'},
                        {'name': 'Front Squat', 'type': 'compound', 'muscle': 'quads'},
                        {'name': 'Walking Lunges', 'type': 'compound', 'muscle': 'legs'},
                        {'name': 'Leg Extension', 'type': 'isolation', 'muscle': 'quads'},
                        {'name': 'Seated Calf Raise', 'type': 'isolation', 'muscle': 'calves'}
                    ]
                }
            ]
        }

    def _get_ppl_template(self) -> dict:
        """Get Push/Pull/Legs split template."""
        return {
            'name': 'Push/Pull/Legs',
            'days_per_week': 6,
            'sessions': [
                {
                    'name': 'Push',
                    'exercises': [
                        {'name': 'Bench Press', 'type': 'compound', 'muscle': 'chest'},
                        {'name': 'Incline Dumbbell Press', 'type': 'compound', 'muscle': 'chest'},
                        {'name': 'Overhead Press', 'type': 'compound', 'muscle': 'shoulders'},
                        {'name': 'Cable Fly', 'type': 'isolation', 'muscle': 'chest'},
                        {'name': 'Lateral Raises', 'type': 'isolation', 'muscle': 'shoulders'},
                        {'name': 'Tricep Pushdown', 'type': 'isolation', 'muscle': 'triceps'},
                        {'name': 'Overhead Tricep Extension', 'type': 'isolation', 'muscle': 'triceps'}
                    ]
                },
                {
                    'name': 'Pull',
                    'exercises': [
                        {'name': 'Barbell Row', 'type': 'compound', 'muscle': 'back'},
                        {'name': 'Pull-ups', 'type': 'compound', 'muscle': 'back'},
                        {'name': 'Seated Cable Row', 'type': 'compound', 'muscle': 'back'},
                        {'name': 'Face Pulls', 'type': 'isolation', 'muscle': 'rear_delts'},
                        {'name': 'Barbell Curl', 'type': 'isolation', 'muscle': 'biceps'},
                        {'name': 'Hammer Curl', 'type': 'isolation', 'muscle': 'biceps'}
                    ]
                },
                {
                    'name': 'Legs',
                    'exercises': [
                        {'name': 'Squat', 'type': 'compound', 'muscle': 'quads'},
                        {'name': 'Romanian Deadlift', 'type': 'compound', 'muscle': 'hamstrings'},
                        {'name': 'Leg Press', 'type': 'compound', 'muscle': 'quads'},
                        {'name': 'Leg Curl', 'type': 'isolation', 'muscle': 'hamstrings'},
                        {'name': 'Leg Extension', 'type': 'isolation', 'muscle': 'quads'},
                        {'name': 'Calf Raises', 'type': 'isolation', 'muscle': 'calves'}
                    ]
                }
            ]
        }

    def _get_upper_lower_ppl_template(self) -> dict:
        """Get hybrid 5-day template."""
        ul = self._get_upper_lower_template()
        ppl = self._get_ppl_template()

        return {
            'name': 'Upper/Lower + PPL',
            'days_per_week': 5,
            'sessions': ul['sessions'][:2] + ppl['sessions']
        }

    def _adjust_for_experience(self, template: dict, level: str) -> dict:
        """Adjust template based on experience level."""
        if level == 'beginner':
            # Reduce volume for beginners
            for session in template['sessions']:
                session['exercises'] = session['exercises'][:5]
        elif level == 'advanced':
            # Could add more exercises or advanced techniques
            pass
        return template

    def _adjust_for_equipment(self, template: dict, equipment: str) -> dict:
        """Adjust exercises based on available equipment."""
        substitutions = {
            'bodyweight': {
                'Bench Press': 'Push-ups',
                'Barbell Row': 'Inverted Row',
                'Squat': 'Bodyweight Squat',
                'Deadlift': 'Single Leg RDL',
                'Overhead Press': 'Pike Push-ups',
                'Leg Press': 'Bulgarian Split Squat',
                'Lat Pulldown': 'Pull-ups',
                'Cable Row': 'Inverted Row',
                'Leg Curl': 'Nordic Curl',
                'Leg Extension': 'Sissy Squat'
            },
            'home_gym': {
                'Leg Press': 'Goblet Squat',
                'Lat Pulldown': 'Pull-ups',
                'Cable Row': 'Dumbbell Row',
                'Cable Fly': 'Dumbbell Fly',
                'Leg Curl': 'Dumbbell Leg Curl',
                'Leg Extension': 'Dumbbell Step-up'
            }
        }

        if equipment in substitutions:
            subs = substitutions[equipment]
            for session in template['sessions']:
                for exercise in session['exercises']:
                    if exercise['name'] in subs:
                        exercise['name'] = subs[exercise['name']]

        return template

    def _adjust_for_limitations(self, template: dict, limitations: list) -> dict:
        """Adjust exercises based on user limitations."""
        limitation_subs = {
            'lower_back': {
                'Deadlift': 'Hip Thrust',
                'Barbell Row': 'Chest Supported Row',
                'Squat': 'Leg Press'
            },
            'knee': {
                'Squat': 'Box Squat',
                'Lunges': 'Step-ups',
                'Leg Extension': 'Terminal Knee Extension'
            },
            'shoulder': {
                'Overhead Press': 'Landmine Press',
                'Bench Press': 'Floor Press',
                'Lateral Raises': 'Cable Lateral Raise'
            }
        }

        for limitation in limitations:
            if limitation in limitation_subs:
                subs = limitation_subs[limitation]
                for session in template['sessions']:
                    for exercise in session['exercises']:
                        if exercise['name'] in subs:
                            exercise['name'] = subs[exercise['name']]

        return template

    def _apply_rep_scheme(self, template: dict, rep_scheme: dict) -> dict:
        """Apply rep scheme to all exercises."""
        for session in template['sessions']:
            for exercise in session['exercises']:
                if exercise['type'] == 'compound':
                    exercise['sets'] = rep_scheme['sets']
                    exercise['reps'] = rep_scheme['reps']
                    exercise['rest'] = rep_scheme['rest']
                else:
                    # Isolation exercises get slightly higher reps
                    exercise['sets'] = rep_scheme['sets']
                    exercise['reps'] = '10-15'
                    exercise['rest'] = '60 sec'

        return template

    def _get_week_notes(self, week_num: int, total_weeks: int) -> str:
        """Get notes for a specific week."""
        if week_num == 1:
            return "Focus on form. Use moderate weights to learn movements."
        elif week_num == total_weeks:
            return "Final week! Push hard but consider a deload after this."
        elif week_num % 4 == 0:
            return "Deload week if needed. Reduce volume by 40%."
        else:
            return "Progressive overload. Try to beat last week's numbers."
