# yapf: disable
BENCH_PRESS    = 'Bench Press'
DEADLIFT       = 'Deadlift'
SQUAT          = 'Squat'
OVERHEAD_PRESS = 'Overhead Press'

CURRENT_DATA = {
    BENCH_PRESS:    (65,   5),  # (weight_in_kg, reps)
    SQUAT:          (105,  5),
    DEADLIFT:       (105,  5),
    OVERHEAD_PRESS: (37.5, 5),
}
# yapf: enable

EXERCISE_PER_DAY = [OVERHEAD_PRESS, DEADLIFT, BENCH_PRESS, SQUAT]

SETS_PER_WEEK = [
    [(0.65, 5), (0.75, 5), (0.85, 5)],
    [(0.70, 3), (0.80, 3), (0.90, 3)],
    [(0.75, 5), (0.85, 3), (0.95, 1)],
]

SUPPLEMENTARY_PERCENT = 0.60
SUPPLEMENTARY_REPS = 10
