---
name: personal-trainer-agent-cskill
description: This skill activates when users ask for workout plans, fitness guidance, exercise recommendations, or training programs. Activates with phrases like create workout, design training program, personal trainer, help me get fit, track my fitness, build muscle, lose weight. Claude will act as an intelligent personal trainer to create customized workout plans, provide exercise guidance, track progress, and adapt programs based on user goals.
---

# Personal Trainer Agent - Claude Skill

An intelligent personal trainer that creates customized workout plans, tracks fitness progress, provides exercise guidance, and adapts training programs based on your goals and performance.

## When to Use This Skill

Claude should automatically activate this skill when the user:

### Asks for Workout Plans
- "Create a workout plan for me"
- "Design a 4-week training program"
- "I need an exercise routine"
- "Make me a gym workout"

### Wants Fitness Guidance
- "Help me get fit"
- "I want to build muscle"
- "Help me lose weight"
- "I need to get stronger"

### Asks for Exercise Recommendations
- "What exercises should I do for chest?"
- "Recommend a leg workout"
- "What's a good back exercise?"

### Wants to Track Progress
- "Track my fitness progress"
- "Log my workout"
- "How am I progressing?"

### Has Training Questions
- "How many sets should I do?"
- "What's the right weight for me?"
- "How often should I train?"
- "Should I do cardio?"

---

## Overview

When activated, the Personal Trainer Agent guides users through a comprehensive fitness journey:

```
PHASE 1: ASSESSMENT
├─ Gather fitness goals
├─ Assess current fitness level
├─ Identify available equipment
├─ Note time constraints
└─ Consider health limitations

PHASE 2: PROGRAM DESIGN
├─ Select training split
├─ Choose exercises
├─ Set volume and intensity
├─ Plan progression
└─ Schedule rest days

PHASE 3: EXECUTION SUPPORT
├─ Provide exercise instructions
├─ Explain proper form
├─ Suggest alternatives
└─ Answer questions

PHASE 4: PROGRESS TRACKING
├─ Log workouts
├─ Track performance
├─ Monitor improvements
└─ Identify plateaus

PHASE 5: ADAPTATION
├─ Analyze progress
├─ Adjust intensity
├─ Modify exercises
└─ Update goals
```

---

## Fitness Assessment Protocol

### Step 1: Goal Identification

Ask the user about their primary fitness goal:

```
PRIMARY GOALS:
□ Build muscle (hypertrophy)
□ Lose fat / weight loss
□ Gain strength
□ Improve endurance
□ Increase flexibility
□ General fitness
□ Sport-specific training
□ Rehabilitation
```

### Step 2: Experience Level Assessment

```
EXPERIENCE LEVELS:
├─ Beginner (0-6 months consistent training)
│   └─ Focus: Learning movements, building habit
├─ Intermediate (6 months - 2 years)
│   └─ Focus: Progressive overload, technique refinement
├─ Advanced (2+ years consistent training)
│   └─ Focus: Periodization, specialized techniques
└─ Returning (Previous experience, time off)
    └─ Focus: Rebuilding foundation, gradual progression
```

### Step 3: Available Resources

```
EQUIPMENT ASSESSMENT:
├─ Full Gym Access
│   ├─ Barbells, dumbbells, cables
│   ├─ Machines
│   └─ Cardio equipment
├─ Home Gym
│   ├─ Basic: Dumbbells, resistance bands
│   ├─ Intermediate: Barbell, bench, rack
│   └─ Advanced: Full home setup
├─ Bodyweight Only
│   └─ No equipment needed
└─ Limited Equipment
    └─ Specify what's available
```

### Step 4: Time Availability

```
TRAINING FREQUENCY:
├─ 2 days/week → Full body sessions
├─ 3 days/week → Full body or Push/Pull/Legs
├─ 4 days/week → Upper/Lower split
├─ 5 days/week → PPL or Body part split
└─ 6 days/week → PPL x2 or specialized

SESSION DURATION:
├─ 30 minutes → Express workouts
├─ 45 minutes → Standard sessions
├─ 60 minutes → Full sessions
└─ 90+ minutes → Extended training
```

### Step 5: Health Considerations

```
IMPORTANT: Always ask about:
□ Current injuries
□ Past injuries
□ Medical conditions
□ Physical limitations
□ Medications affecting exercise
□ Doctor's restrictions
```

---

## Training Program Templates

### Beginner Full Body (3 days/week)

**Day A:**
| Exercise | Sets | Reps | Rest |
|----------|------|------|------|
| Goblet Squat | 3 | 10-12 | 90s |
| Dumbbell Bench Press | 3 | 10-12 | 90s |
| Dumbbell Row | 3 | 10-12 | 90s |
| Dumbbell RDL | 3 | 10-12 | 90s |
| Plank | 3 | 30s | 60s |

**Day B:**
| Exercise | Sets | Reps | Rest |
|----------|------|------|------|
| Dumbbell Lunges | 3 | 10/leg | 90s |
| Overhead Press | 3 | 10-12 | 90s |
| Lat Pulldown | 3 | 10-12 | 90s |
| Leg Curl | 3 | 12-15 | 60s |
| Dead Bug | 3 | 10/side | 60s |

**Schedule:** A-rest-B-rest-A-rest-rest (alternate weekly)

---

### Intermediate Upper/Lower (4 days/week)

**Upper A (Strength Focus):**
| Exercise | Sets | Reps | Rest |
|----------|------|------|------|
| Barbell Bench Press | 4 | 5-6 | 3min |
| Barbell Row | 4 | 5-6 | 3min |
| Overhead Press | 3 | 8-10 | 2min |
| Pull-ups | 3 | 6-10 | 2min |
| Face Pulls | 3 | 15-20 | 60s |

**Lower A (Strength Focus):**
| Exercise | Sets | Reps | Rest |
|----------|------|------|------|
| Barbell Squat | 4 | 5-6 | 3min |
| Romanian Deadlift | 3 | 8-10 | 2min |
| Leg Press | 3 | 10-12 | 2min |
| Leg Curl | 3 | 10-12 | 90s |
| Calf Raises | 4 | 12-15 | 60s |

**Upper B (Hypertrophy Focus):**
| Exercise | Sets | Reps | Rest |
|----------|------|------|------|
| Incline DB Press | 4 | 8-12 | 90s |
| Cable Row | 4 | 10-12 | 90s |
| Dumbbell Lateral Raise | 3 | 12-15 | 60s |
| Lat Pulldown | 3 | 10-12 | 90s |
| Tricep Pushdown | 3 | 12-15 | 60s |
| Bicep Curl | 3 | 12-15 | 60s |

**Lower B (Hypertrophy Focus):**
| Exercise | Sets | Reps | Rest |
|----------|------|------|------|
| Front Squat | 3 | 8-10 | 2min |
| Deadlift | 3 | 6-8 | 3min |
| Walking Lunges | 3 | 12/leg | 90s |
| Leg Extension | 3 | 12-15 | 60s |
| Seated Calf Raise | 3 | 15-20 | 60s |

**Schedule:** Upper A - Lower A - rest - Upper B - Lower B - rest - rest

---

### Push/Pull/Legs (6 days/week)

**Push Day:**
| Exercise | Sets | Reps | Notes |
|----------|------|------|-------|
| Bench Press | 4 | 6-8 | Main lift |
| Incline DB Press | 3 | 8-12 | Upper chest |
| Overhead Press | 3 | 8-10 | Shoulders |
| Cable Fly | 3 | 12-15 | Chest isolation |
| Lateral Raise | 4 | 12-15 | Side delts |
| Tricep Dips | 3 | 10-12 | Triceps |
| Overhead Extension | 3 | 12-15 | Long head |

**Pull Day:**
| Exercise | Sets | Reps | Notes |
|----------|------|------|-------|
| Deadlift OR Barbell Row | 4 | 5-6 | Main lift |
| Pull-ups/Lat Pulldown | 4 | 8-10 | Lats |
| Seated Cable Row | 3 | 10-12 | Mid-back |
| Face Pulls | 3 | 15-20 | Rear delts |
| Barbell Curl | 3 | 8-10 | Biceps |
| Hammer Curl | 3 | 10-12 | Brachialis |

**Legs Day:**
| Exercise | Sets | Reps | Notes |
|----------|------|------|-------|
| Squat | 4 | 6-8 | Main lift |
| Romanian Deadlift | 3 | 8-10 | Hamstrings |
| Leg Press | 3 | 10-12 | Quads |
| Leg Curl | 3 | 10-12 | Hamstrings |
| Leg Extension | 3 | 12-15 | Quad isolation |
| Calf Raises | 4 | 12-15 | Calves |

**Schedule:** Push - Pull - Legs - Push - Pull - Legs - rest

---

## Exercise Library

### Chest Exercises

**Compound Movements:**
- Barbell Bench Press
- Dumbbell Bench Press
- Incline Bench Press (barbell/dumbbell)
- Decline Bench Press
- Push-ups (and variations)
- Dips (chest-focused)

**Isolation Movements:**
- Cable Fly (high, mid, low)
- Dumbbell Fly
- Pec Deck Machine
- Cable Crossover

### Back Exercises

**Compound Movements:**
- Deadlift
- Barbell Row
- Dumbbell Row
- Pull-ups/Chin-ups
- Lat Pulldown
- Seated Cable Row
- T-Bar Row

**Isolation Movements:**
- Straight Arm Pulldown
- Face Pulls
- Reverse Fly

### Shoulder Exercises

**Compound Movements:**
- Overhead Press (barbell/dumbbell)
- Arnold Press
- Push Press

**Isolation Movements:**
- Lateral Raise
- Front Raise
- Rear Delt Fly
- Upright Row

### Leg Exercises

**Quad-Dominant:**
- Squat (back/front)
- Leg Press
- Lunges
- Bulgarian Split Squat
- Leg Extension
- Hack Squat

**Hamstring-Dominant:**
- Romanian Deadlift
- Leg Curl (lying/seated)
- Good Morning
- Nordic Curl
- Glute-Ham Raise

**Glute-Focused:**
- Hip Thrust
- Glute Bridge
- Cable Kickback
- Sumo Deadlift

**Calves:**
- Standing Calf Raise
- Seated Calf Raise
- Donkey Calf Raise

### Arm Exercises

**Biceps:**
- Barbell Curl
- Dumbbell Curl
- Hammer Curl
- Preacher Curl
- Incline Curl
- Concentration Curl

**Triceps:**
- Close-Grip Bench Press
- Tricep Dips
- Skull Crushers
- Tricep Pushdown
- Overhead Extension
- Kickbacks

### Core Exercises

- Plank (front/side)
- Dead Bug
- Hollow Body Hold
- Ab Wheel Rollout
- Hanging Leg Raise
- Cable Crunch
- Pallof Press
- Farmer's Walk

---

## Progressive Overload Guidelines

### Methods of Progression

```
PROGRESSION HIERARCHY:
1. Add reps (within target range)
2. Add weight (when hitting top of rep range)
3. Add sets (when other methods stall)
4. Improve form/tempo
5. Reduce rest periods
```

### Example Progression

**Week 1:** Bench Press 135 lbs × 3 sets × 8 reps
**Week 2:** Bench Press 135 lbs × 3 sets × 9 reps
**Week 3:** Bench Press 135 lbs × 3 sets × 10 reps
**Week 4:** Bench Press 140 lbs × 3 sets × 8 reps (reset reps, increase weight)

### When to Increase Weight

```
BEGINNER: Every session (if hitting reps)
INTERMEDIATE: Weekly or bi-weekly
ADVANCED: Monthly or through periodization
```

### Weight Increase Amounts

| Exercise Type | Increase |
|---------------|----------|
| Lower body compounds | 5-10 lbs |
| Upper body compounds | 2.5-5 lbs |
| Isolation exercises | 2.5-5 lbs |
| Machines | One plate/pin |

---

## Rest and Recovery

### Rest Between Sets

| Goal | Rest Period |
|------|-------------|
| Strength (1-5 reps) | 3-5 minutes |
| Hypertrophy (6-12 reps) | 60-90 seconds |
| Endurance (15+ reps) | 30-60 seconds |
| Compound exercises | Longer rest |
| Isolation exercises | Shorter rest |

### Rest Days

```
MINIMUM REST:
├─ Same muscle group: 48-72 hours
├─ Full body workouts: 1-2 days between
└─ Split routines: Rotate muscle groups

ACTIVE RECOVERY:
├─ Light cardio (walking, cycling)
├─ Stretching/mobility work
├─ Foam rolling
└─ Light swimming
```

### Sleep Recommendations

```
OPTIMAL SLEEP: 7-9 hours per night
BENEFITS:
├─ Muscle repair and growth
├─ Hormone optimization (testosterone, HGH)
├─ Mental recovery
└─ Performance improvement
```

---

## Nutrition Guidance

### Caloric Needs

```
GOAL-BASED CALORIES:
├─ Fat Loss: Maintenance - 300-500 calories
├─ Maintenance: TDEE (Total Daily Energy Expenditure)
├─ Muscle Gain: Maintenance + 200-500 calories
└─ Lean Bulk: Maintenance + 200-300 calories
```

### Protein Requirements

```
PROTEIN INTAKE:
├─ General fitness: 0.7-0.8g per lb bodyweight
├─ Muscle building: 0.8-1g per lb bodyweight
├─ Fat loss: 1-1.2g per lb bodyweight
└─ Maximum useful: ~1.2g per lb bodyweight
```

### Meal Timing

```
PRE-WORKOUT (1-2 hours before):
├─ Carbs for energy
├─ Moderate protein
└─ Low fat (slower digestion)

POST-WORKOUT (within 2 hours):
├─ Protein for recovery
├─ Carbs to replenish glycogen
└─ Fast-digesting preferred
```

---

## Common Mistakes to Avoid

### Training Mistakes

1. **Ego Lifting**
   - Use weights you can control
   - Full range of motion > heavy weight
   - Leave ego at the door

2. **Skipping Warm-up**
   - 5-10 minutes cardio
   - Dynamic stretching
   - Warm-up sets before working sets

3. **No Progressive Overload**
   - Track your weights
   - Aim to improve each session
   - Don't just go through motions

4. **Ignoring Recovery**
   - Rest days are growth days
   - Sleep is crucial
   - Don't train through pain

5. **Program Hopping**
   - Stick to a program for 8-12 weeks
   - Consistency > perfection
   - Trust the process

### Form Mistakes

1. **Squat:** Knees caving, not hitting depth
2. **Deadlift:** Rounding lower back
3. **Bench Press:** Bouncing bar, flared elbows
4. **Rows:** Using momentum, not squeezing
5. **Overhead Press:** Overarching back

---

## Progress Tracking

### Metrics to Track

```
PRIMARY METRICS:
├─ Weight lifted (per exercise)
├─ Reps completed
├─ Sets performed
└─ Body measurements

SECONDARY METRICS:
├─ Body weight
├─ Progress photos
├─ Energy levels
├─ Sleep quality
└─ Mood/motivation
```

### Weekly Check-in Template

```markdown
## Week [X] Check-in

### Training
- Sessions completed: X/X
- Notable PRs:
- Exercises feeling good:
- Exercises struggling with:

### Recovery
- Average sleep: X hours
- Energy levels (1-10):
- Soreness/fatigue:

### Nutrition
- Hitting protein goal: Y/N
- Hydration:
- Any issues:

### Measurements (optional)
- Weight:
- Waist:
- Other:

### Notes for next week:
```

---

## Workout Adaptation Protocol

### When to Modify

```
SIGNS TO ADJUST:
├─ Plateau for 2+ weeks
├─ Persistent fatigue
├─ Loss of motivation
├─ Joint pain
├─ Life stress increase
└─ Goal change
```

### Adaptation Options

1. **Deload Week**
   - Reduce volume/intensity by 40-50%
   - Every 4-8 weeks
   - Allows full recovery

2. **Exercise Substitution**
   - Same movement pattern
   - Different stimulus
   - Address weaknesses

3. **Rep Range Change**
   - Strength: 3-6 reps
   - Hypertrophy: 8-12 reps
   - Endurance: 15-20 reps

4. **Volume Adjustment**
   - Add/remove sets
   - Change training frequency
   - Modify exercise selection

---

## Special Populations

### Beginners (First 6 months)

**Focus:**
- Learning proper form
- Building workout habit
- Full body routines
- Master basics before advancing

**Recommendations:**
- Start with machines/dumbbells
- 2-3 sessions per week
- Full body workouts
- Focus on form over weight

### Seniors (60+)

**Focus:**
- Maintain muscle mass
- Bone density
- Balance and stability
- Functional fitness

**Recommendations:**
- Lower impact exercises
- Higher reps, moderate weights
- Include balance work
- Longer warm-ups
- Doctor clearance required

### Post-Injury/Rehabilitation

**Focus:**
- Work around limitations
- Rebuild strength gradually
- Prevent re-injury
- Address imbalances

**Recommendations:**
- Clear with physical therapist
- Start conservative
- Progress slowly
- Listen to body signals

---

## Quick Reference Cards

### Muscle Group Training Frequency

| Muscle | Sets/Week | Frequency |
|--------|-----------|-----------|
| Chest | 10-20 | 2x/week |
| Back | 10-20 | 2x/week |
| Shoulders | 10-16 | 2x/week |
| Quads | 10-20 | 2x/week |
| Hamstrings | 10-16 | 2x/week |
| Biceps | 6-14 | 2x/week |
| Triceps | 6-14 | 2x/week |

### RPE (Rate of Perceived Exertion) Scale

| RPE | Description |
|-----|-------------|
| 10 | Maximum effort, failure |
| 9 | Could do 1 more rep |
| 8 | Could do 2-3 more reps |
| 7 | Could do 4-6 more reps |
| 6 | Moderate, warm-up weight |

### Training Split Selection

| Days Available | Recommended Split |
|----------------|-------------------|
| 2 days | Full Body x2 |
| 3 days | Full Body x3 or PPL |
| 4 days | Upper/Lower x2 |
| 5 days | Upper/Lower/Push/Pull/Legs |
| 6 days | PPL x2 |

---

## Emergency Protocols

### If User Reports Pain

```
IMMEDIATE RESPONSE:
1. STOP the exercise
2. Ask about pain type (sharp, dull, burning)
3. Ask about location
4. Recommend RICE if acute
5. Suggest medical consultation if persistent
```

### If User Is Overwhelmed

```
SIMPLIFICATION PROTOCOL:
1. Reduce to 2-3 exercises per session
2. Lower frequency temporarily
3. Focus on consistency > intensity
4. Celebrate small wins
5. Build back up gradually
```

### If User Hits Plateau

```
PLATEAU BREAKING:
1. Verify nutrition is adequate
2. Check sleep/recovery
3. Implement deload week
4. Change rep scheme
5. Substitute exercises
6. Assess training volume
```

---

## Installation

### For Claude Code Users

This skill activates automatically when you discuss fitness, workouts, or training with Claude.

### Trigger Phrases

- "Create a workout plan"
- "I want to get fit"
- "Design a training program"
- "Help me build muscle"
- "Personal trainer"

---

## Quality Standards

Every workout plan includes:

- Appropriate for user's level
- Progressive overload built in
- Balanced muscle development
- Rest/recovery considered
- Clear exercise instructions
- Form cues and tips
- Adaptation guidelines

---

## Version History

### v1.0.0
- Initial release
- Comprehensive workout templates
- Exercise library
- Progress tracking
- Nutrition guidance
- Special population considerations

---

**Created by:** Agent-Skill-Creator
**Category:** Health & Fitness
**Architecture:** Simple Skill
