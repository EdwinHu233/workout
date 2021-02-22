BENCH_PRESS    = 'Bench Press'
DEADLIFT       = 'Deadlift'
SQUAT          = 'Squat'
OVERHEAD_PRESS = 'Overhead Press'

current_data = {
    BENCH_PRESS:    (60,  5),  # (weight_in_kg, reps)
    SQUAT:          (100, 5),
    DEADLIFT:       (100, 5),
    OVERHEAD_PRESS: (35,  5),
}

DAY_A = "Day A"
DAY_B = "Day B"

exercises_per_day = {
    DAY_A: (BENCH_PRESS,    SQUAT),
    DAY_B: (OVERHEAD_PRESS, DEADLIFT),
}

sets_per_week = [
    [(0.65, 5), (0.75, 5), (0.85, 5)],
    [(0.70, 3), (0.80, 3), (0.90, 3)],
    [(0.75, 5), (0.85, 3), (0.95, 1)],
]
