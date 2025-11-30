# Personal Trainer Agent

**Version:** 1.0.0
**Type:** Claude Skill
**Architecture:** Simple Skill

An intelligent personal trainer that creates customized workout plans, tracks fitness progress, provides exercise guidance, and adapts training programs based on your goals and performance.

---

## Overview

The Personal Trainer Agent transforms Claude into your dedicated fitness coach. It automates the process of creating personalized workout programs, provides exercise guidance, and helps you track your progress toward your fitness goals.

### Key Features

- **Personalized Workout Plans**: Custom programs based on your goals, experience, and equipment
- **Exercise Library**: Comprehensive database of exercises with form cues
- **Progress Tracking**: Monitor improvements and identify plateaus
- **Adaptive Programming**: Workouts that evolve with your progress
- **Nutrition Guidance**: Basic nutritional recommendations for your goals
- **Rest & Recovery**: Smart scheduling of rest days and deloads

---

## Installation

### For Claude Code Users

The skill activates automatically. Simply start a conversation about fitness:

```
"Create a workout plan for me"
"I want to build muscle"
"Design a training program"
"Help me get fit"
```

### Manual Installation

```bash
cd personal-trainer-agent
pip install -r requirements.txt
```

---

## Usage

### Creating a Workout Plan

Tell Claude about:
1. Your fitness goal (build muscle, lose fat, get stronger)
2. Your experience level (beginner, intermediate, advanced)
3. Available equipment (gym, home, bodyweight)
4. Days per week you can train
5. Any injuries or limitations

**Example:**
```
"I'm a beginner looking to build muscle. I have access to a full gym
and can train 4 days per week. I have no injuries."
```

### Tracking Progress

```
"Log my workout today"
"Track my bench press progress"
"How am I doing this month?"
```

### Getting Exercise Help

```
"How do I do a proper squat?"
"What's a good alternative to pull-ups?"
"Recommend exercises for my chest"
```

---

## Supported Goals

| Goal | Description |
|------|-------------|
| **Muscle Building** | Hypertrophy-focused programs |
| **Weight Loss** | Fat loss with muscle preservation |
| **Strength Gain** | Powerlifting-style training |
| **Endurance** | Cardiovascular and muscular endurance |
| **General Fitness** | Balanced overall fitness |
| **Sport-Specific** | Training for specific sports |

---

## Training Splits Available

| Days/Week | Recommended Split |
|-----------|-------------------|
| 2 days | Full Body |
| 3 days | Full Body or Push/Pull/Legs |
| 4 days | Upper/Lower |
| 5 days | Upper/Lower/Push/Pull/Legs |
| 6 days | Push/Pull/Legs x2 |

---

## Example Workout Plan

### Beginner Full Body (3 days/week)

**Day A:**
| Exercise | Sets | Reps |
|----------|------|------|
| Goblet Squat | 3 | 10-12 |
| Dumbbell Bench Press | 3 | 10-12 |
| Dumbbell Row | 3 | 10-12 |
| Dumbbell RDL | 3 | 10-12 |
| Plank | 3 | 30s |

**Day B:**
| Exercise | Sets | Reps |
|----------|------|------|
| Dumbbell Lunges | 3 | 10/leg |
| Overhead Press | 3 | 10-12 |
| Lat Pulldown | 3 | 10-12 |
| Leg Curl | 3 | 12-15 |
| Dead Bug | 3 | 10/side |

---

## Project Structure

```
personal-trainer-agent/
├── .claude-plugin/
│   └── marketplace.json    # Skill configuration
├── scripts/
│   ├── main.py            # Main orchestrator
│   ├── workout_generator.py
│   ├── exercise_library.py
│   └── progress_tracker.py
├── references/
│   └── exercise_database.yaml
├── SKILL.md               # Comprehensive skill instructions
├── README.md              # This file
└── requirements.txt       # Python dependencies
```

---

## Configuration

### Environment Variables (Optional)

```bash
# Custom data directory
export TRAINER_DATA_DIR=~/.personal-trainer

# Default measurement system
export TRAINER_UNITS=imperial  # or "metric"
```

---

## Quality Standards

Every generated workout includes:

- ✅ Appropriate for stated experience level
- ✅ Progressive overload progression
- ✅ Balanced muscle development
- ✅ Proper rest/recovery scheduling
- ✅ Clear exercise instructions
- ✅ Form cues and safety tips

---

## Troubleshooting

### "I don't know what exercises to choose"

The agent will recommend exercises based on:
- Your available equipment
- Your experience level
- Your specific goals
- Any limitations you mention

### "I hit a plateau"

Tell Claude and it will:
- Suggest a deload week
- Modify rep ranges
- Substitute exercises
- Adjust volume/intensity

### "I got injured"

- Stop the aggravating exercise immediately
- Inform Claude about the injury
- Get exercises modified to work around it
- Always consult a medical professional for serious injuries

---

## Contributing

Contributions welcome! Areas for improvement:
- Additional exercise variations
- Sport-specific programs
- Nutrition plan integration
- Progress visualization

---

## License

MIT License - See LICENSE file for details

---

## Acknowledgments

- Created with Agent-Skill-Creator
- Based on evidence-based training principles
- Follows established strength and conditioning guidelines

---

**Created by:** Haulbrook
**Powered by:** Claude + Agent-Skill-Creator
**Last Updated:** 2024
