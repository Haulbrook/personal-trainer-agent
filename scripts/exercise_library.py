#!/usr/bin/env python3
"""
Exercise Library Module
Comprehensive database of exercises with instructions and alternatives.
"""

from typing import Optional


class ExerciseLibrary:
    """Database of exercises with detailed information."""

    def __init__(self):
        """Initialize the exercise library."""
        self.exercises = self._build_exercise_database()

    def get_exercise(self, name: str) -> dict:
        """Get detailed information about an exercise.

        Args:
            name: Name of the exercise

        Returns:
            Exercise details or error dict if not found
        """
        # Normalize name
        normalized = name.lower().replace(' ', '_').replace('-', '_')

        if normalized in self.exercises:
            return self.exercises[normalized]

        # Try fuzzy match
        for key, exercise in self.exercises.items():
            if normalized in key or key in normalized:
                return exercise

        return {'error': f'Exercise "{name}" not found in library'}

    def get_alternatives(
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
        exercise = self.get_exercise(exercise_name)

        if 'error' in exercise:
            return []

        alternatives = exercise.get('alternatives', [])

        # Filter by reason if needed
        if reason == 'equipment':
            # Prefer bodyweight or dumbbell alternatives
            return [alt for alt in alternatives
                    if any(eq in alt.lower() for eq in ['dumbbell', 'bodyweight', 'band'])]

        return alternatives

    def get_exercises_by_muscle(self, muscle: str) -> list:
        """Get all exercises targeting a specific muscle.

        Args:
            muscle: Target muscle group

        Returns:
            List of exercises targeting that muscle
        """
        results = []
        for name, exercise in self.exercises.items():
            if muscle.lower() in [m.lower() for m in exercise.get('primary_muscles', [])]:
                results.append({
                    'name': exercise['name'],
                    'type': exercise.get('type', 'unknown')
                })
        return results

    def _build_exercise_database(self) -> dict:
        """Build the comprehensive exercise database."""
        return {
            # CHEST EXERCISES
            'bench_press': {
                'name': 'Bench Press',
                'primary_muscles': ['chest', 'triceps', 'front_delts'],
                'type': 'compound',
                'equipment': ['barbell', 'bench'],
                'instructions': [
                    'Lie on bench with eyes under the bar',
                    'Grip bar slightly wider than shoulder width',
                    'Unrack and position bar over chest',
                    'Lower bar to mid-chest with control',
                    'Press bar up and slightly back',
                    'Lock out arms at top'
                ],
                'form_cues': [
                    'Keep shoulder blades pinched together',
                    'Maintain arch in lower back',
                    'Keep feet flat on floor',
                    'Elbows at 45-75 degree angle',
                    'Touch chest, don\'t bounce'
                ],
                'alternatives': [
                    'Dumbbell Bench Press',
                    'Push-ups',
                    'Machine Chest Press',
                    'Floor Press'
                ]
            },

            'incline_dumbbell_press': {
                'name': 'Incline Dumbbell Press',
                'primary_muscles': ['upper_chest', 'front_delts', 'triceps'],
                'type': 'compound',
                'equipment': ['dumbbells', 'incline_bench'],
                'instructions': [
                    'Set bench to 30-45 degree incline',
                    'Sit with dumbbells on thighs',
                    'Kick dumbbells up as you lie back',
                    'Press dumbbells up and together',
                    'Lower with control to chest level',
                    'Repeat for desired reps'
                ],
                'form_cues': [
                    'Keep back flat against bench',
                    'Don\'t let dumbbells drift too far apart',
                    'Control the negative portion',
                    'Full range of motion'
                ],
                'alternatives': [
                    'Incline Barbell Press',
                    'Low-to-High Cable Fly',
                    'Incline Push-ups'
                ]
            },

            'push_ups': {
                'name': 'Push-ups',
                'primary_muscles': ['chest', 'triceps', 'front_delts'],
                'type': 'compound',
                'equipment': ['bodyweight'],
                'instructions': [
                    'Start in plank position, hands shoulder-width apart',
                    'Keep body in straight line from head to heels',
                    'Lower chest toward floor',
                    'Push back up to starting position',
                    'Maintain core engagement throughout'
                ],
                'form_cues': [
                    'Don\'t let hips sag or pike up',
                    'Elbows at 45 degree angle',
                    'Full lockout at top',
                    'Chest touches floor at bottom'
                ],
                'alternatives': [
                    'Knee Push-ups',
                    'Incline Push-ups',
                    'Diamond Push-ups',
                    'Wide Push-ups'
                ]
            },

            # BACK EXERCISES
            'barbell_row': {
                'name': 'Barbell Row',
                'primary_muscles': ['lats', 'rhomboids', 'rear_delts', 'biceps'],
                'type': 'compound',
                'equipment': ['barbell'],
                'instructions': [
                    'Stand with feet shoulder-width apart',
                    'Hinge at hips, back flat, chest up',
                    'Grip bar slightly wider than shoulder width',
                    'Pull bar to lower chest/upper abs',
                    'Squeeze shoulder blades at top',
                    'Lower with control'
                ],
                'form_cues': [
                    'Keep back flat, don\'t round',
                    'Lead with elbows',
                    'Don\'t use momentum',
                    'Torso angle ~45 degrees'
                ],
                'alternatives': [
                    'Dumbbell Row',
                    'Cable Row',
                    'T-Bar Row',
                    'Chest Supported Row'
                ]
            },

            'pull_ups': {
                'name': 'Pull-ups',
                'primary_muscles': ['lats', 'biceps', 'rear_delts'],
                'type': 'compound',
                'equipment': ['pull_up_bar'],
                'instructions': [
                    'Grip bar slightly wider than shoulder width',
                    'Hang with arms fully extended',
                    'Pull yourself up until chin clears bar',
                    'Lower with control to full extension',
                    'Avoid swinging or kipping'
                ],
                'form_cues': [
                    'Initiate with lats, not arms',
                    'Keep core engaged',
                    'Shoulders down and back',
                    'Full range of motion'
                ],
                'alternatives': [
                    'Lat Pulldown',
                    'Assisted Pull-ups',
                    'Negative Pull-ups',
                    'Inverted Rows'
                ]
            },

            'lat_pulldown': {
                'name': 'Lat Pulldown',
                'primary_muscles': ['lats', 'biceps', 'rear_delts'],
                'type': 'compound',
                'equipment': ['cable_machine'],
                'instructions': [
                    'Sit with thighs secured under pads',
                    'Grip bar wider than shoulder width',
                    'Pull bar down to upper chest',
                    'Squeeze lats at bottom',
                    'Control the weight back up'
                ],
                'form_cues': [
                    'Don\'t lean back excessively',
                    'Pull elbows down and back',
                    'Keep chest up',
                    'Full stretch at top'
                ],
                'alternatives': [
                    'Pull-ups',
                    'Close Grip Pulldown',
                    'Straight Arm Pulldown'
                ]
            },

            # LEG EXERCISES
            'squat': {
                'name': 'Squat',
                'primary_muscles': ['quads', 'glutes', 'hamstrings', 'core'],
                'type': 'compound',
                'equipment': ['barbell', 'squat_rack'],
                'instructions': [
                    'Position bar on upper back (high bar) or rear delts (low bar)',
                    'Unrack and step back, feet shoulder-width apart',
                    'Brace core and initiate by pushing hips back',
                    'Descend until hip crease below knee',
                    'Drive through feet to stand',
                    'Lock out hips and knees at top'
                ],
                'form_cues': [
                    'Keep chest up and back flat',
                    'Knees track over toes',
                    'Weight in mid-foot/heels',
                    'Don\'t let knees cave in',
                    'Breathe and brace each rep'
                ],
                'alternatives': [
                    'Goblet Squat',
                    'Front Squat',
                    'Leg Press',
                    'Bulgarian Split Squat',
                    'Box Squat'
                ]
            },

            'deadlift': {
                'name': 'Deadlift',
                'primary_muscles': ['hamstrings', 'glutes', 'lower_back', 'traps'],
                'type': 'compound',
                'equipment': ['barbell'],
                'instructions': [
                    'Stand with feet hip-width, bar over mid-foot',
                    'Hinge and grip bar just outside legs',
                    'Drop hips, chest up, back flat',
                    'Drive through floor, keeping bar close',
                    'Lock out hips and knees together',
                    'Reverse the movement to lower'
                ],
                'form_cues': [
                    'Bar stays close to body entire lift',
                    'Don\'t round lower back',
                    'Push floor away with legs',
                    'Lock out by squeezing glutes',
                    'Don\'t hyperextend at top'
                ],
                'alternatives': [
                    'Romanian Deadlift',
                    'Trap Bar Deadlift',
                    'Sumo Deadlift',
                    'Hip Thrust'
                ]
            },

            'romanian_deadlift': {
                'name': 'Romanian Deadlift',
                'primary_muscles': ['hamstrings', 'glutes', 'lower_back'],
                'type': 'compound',
                'equipment': ['barbell', 'dumbbells'],
                'instructions': [
                    'Stand with feet hip-width, holding bar',
                    'Push hips back while keeping knees slightly bent',
                    'Lower bar along thighs until hamstring stretch',
                    'Keep back flat throughout',
                    'Drive hips forward to return to start'
                ],
                'form_cues': [
                    'Hinge at hips, not waist',
                    'Bar stays close to legs',
                    'Feel stretch in hamstrings',
                    'Don\'t round back',
                    'Squeeze glutes at top'
                ],
                'alternatives': [
                    'Stiff Leg Deadlift',
                    'Single Leg RDL',
                    'Good Morning',
                    'Cable Pull Through'
                ]
            },

            'leg_press': {
                'name': 'Leg Press',
                'primary_muscles': ['quads', 'glutes', 'hamstrings'],
                'type': 'compound',
                'equipment': ['leg_press_machine'],
                'instructions': [
                    'Sit in machine with back flat against pad',
                    'Place feet shoulder-width on platform',
                    'Release safety and lower weight',
                    'Lower until knees at 90 degrees',
                    'Press through feet to extend legs',
                    'Don\'t lock knees completely'
                ],
                'form_cues': [
                    'Keep lower back pressed into pad',
                    'Don\'t let knees cave in',
                    'Control the negative',
                    'Full range of motion'
                ],
                'alternatives': [
                    'Squat',
                    'Hack Squat',
                    'Bulgarian Split Squat'
                ]
            },

            # SHOULDER EXERCISES
            'overhead_press': {
                'name': 'Overhead Press',
                'primary_muscles': ['front_delts', 'side_delts', 'triceps'],
                'type': 'compound',
                'equipment': ['barbell'],
                'instructions': [
                    'Grip bar just outside shoulder width',
                    'Start with bar at shoulder level',
                    'Brace core and press bar overhead',
                    'Lock out arms at top',
                    'Lower bar with control to shoulders'
                ],
                'form_cues': [
                    'Keep core tight, don\'t lean back',
                    'Press bar in straight line',
                    'Move head back slightly as bar passes',
                    'Full lockout at top'
                ],
                'alternatives': [
                    'Dumbbell Shoulder Press',
                    'Arnold Press',
                    'Machine Shoulder Press',
                    'Landmine Press'
                ]
            },

            'lateral_raise': {
                'name': 'Lateral Raise',
                'primary_muscles': ['side_delts'],
                'type': 'isolation',
                'equipment': ['dumbbells'],
                'instructions': [
                    'Stand with dumbbells at sides',
                    'Slight bend in elbows',
                    'Raise arms out to sides until shoulder height',
                    'Pause briefly at top',
                    'Lower with control'
                ],
                'form_cues': [
                    'Lead with elbows, not hands',
                    'Don\'t swing or use momentum',
                    'Slight forward lean okay',
                    'Pinkies up at top optional'
                ],
                'alternatives': [
                    'Cable Lateral Raise',
                    'Machine Lateral Raise',
                    'Leaning Lateral Raise'
                ]
            },

            # ARM EXERCISES
            'bicep_curl': {
                'name': 'Bicep Curl',
                'primary_muscles': ['biceps'],
                'type': 'isolation',
                'equipment': ['dumbbells', 'barbell'],
                'instructions': [
                    'Stand with arms at sides, palms forward',
                    'Keep elbows at sides throughout',
                    'Curl weight up toward shoulders',
                    'Squeeze biceps at top',
                    'Lower with control'
                ],
                'form_cues': [
                    'Don\'t swing body',
                    'Keep elbows stationary',
                    'Full range of motion',
                    'Control the negative'
                ],
                'alternatives': [
                    'Hammer Curl',
                    'Preacher Curl',
                    'Cable Curl',
                    'Incline Curl'
                ]
            },

            'tricep_pushdown': {
                'name': 'Tricep Pushdown',
                'primary_muscles': ['triceps'],
                'type': 'isolation',
                'equipment': ['cable_machine'],
                'instructions': [
                    'Stand facing cable machine',
                    'Grip rope or bar attachment',
                    'Keep elbows at sides',
                    'Push down until arms fully extended',
                    'Squeeze triceps at bottom',
                    'Control the return'
                ],
                'form_cues': [
                    'Don\'t let elbows flare',
                    'Keep torso upright',
                    'Full extension at bottom',
                    'Don\'t use momentum'
                ],
                'alternatives': [
                    'Skull Crushers',
                    'Overhead Extension',
                    'Dips',
                    'Close Grip Bench'
                ]
            },

            # CORE EXERCISES
            'plank': {
                'name': 'Plank',
                'primary_muscles': ['core', 'shoulders'],
                'type': 'core',
                'equipment': ['bodyweight'],
                'instructions': [
                    'Start in push-up position on forearms',
                    'Keep body in straight line',
                    'Engage core and glutes',
                    'Hold position for prescribed time',
                    'Breathe normally throughout'
                ],
                'form_cues': [
                    'Don\'t let hips sag or pike',
                    'Keep neck neutral',
                    'Squeeze everything tight',
                    'Quality over duration'
                ],
                'alternatives': [
                    'Side Plank',
                    'Dead Bug',
                    'Bird Dog',
                    'Hollow Hold'
                ]
            },

            'face_pulls': {
                'name': 'Face Pulls',
                'primary_muscles': ['rear_delts', 'rhomboids', 'external_rotators'],
                'type': 'isolation',
                'equipment': ['cable_machine', 'rope'],
                'instructions': [
                    'Set cable at face height',
                    'Grip rope with thumbs pointing back',
                    'Pull toward face, separating hands',
                    'Externally rotate at end of movement',
                    'Squeeze shoulder blades together',
                    'Control return'
                ],
                'form_cues': [
                    'Lead with elbows high',
                    'Pull apart, not just back',
                    'Keep chest up',
                    'Don\'t lean back excessively'
                ],
                'alternatives': [
                    'Reverse Fly',
                    'Band Pull Aparts',
                    'Rear Delt Fly Machine'
                ]
            },

            'calf_raises': {
                'name': 'Calf Raises',
                'primary_muscles': ['calves'],
                'type': 'isolation',
                'equipment': ['calf_machine', 'dumbbells'],
                'instructions': [
                    'Position balls of feet on edge',
                    'Lower heels for full stretch',
                    'Push up onto toes as high as possible',
                    'Pause and squeeze at top',
                    'Lower with control'
                ],
                'form_cues': [
                    'Full range of motion',
                    'Don\'t bounce at bottom',
                    'Pause at top',
                    'Straight knees for gastrocnemius'
                ],
                'alternatives': [
                    'Seated Calf Raise',
                    'Donkey Calf Raise',
                    'Single Leg Calf Raise'
                ]
            },

            'leg_curl': {
                'name': 'Leg Curl',
                'primary_muscles': ['hamstrings'],
                'type': 'isolation',
                'equipment': ['leg_curl_machine'],
                'instructions': [
                    'Lie face down or sit in machine',
                    'Position pad above heels',
                    'Curl legs toward glutes',
                    'Squeeze hamstrings at top',
                    'Lower with control'
                ],
                'form_cues': [
                    'Don\'t lift hips off pad',
                    'Full range of motion',
                    'Control the negative',
                    'Point toes for extra contraction'
                ],
                'alternatives': [
                    'Nordic Curl',
                    'Swiss Ball Curl',
                    'Slider Curl',
                    'Romanian Deadlift'
                ]
            }
        }
