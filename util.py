import config
from typing import Union, Tuple, List

Number = Union[int, float]


def get_training_max(weight: Number, rep: Number) -> float:
    one_rm = weight * 36.0 / (37.0 - float(rep))
    return one_rm * 0.9


def print_bar(msg: str, num_bar: int = 20):
    bar = '-' * num_bar
    print(bar, msg, bar)


def print_exercise(exercise: str, sets: List[Tuple[int, float]]):
    training_max = get_training_max(*config.current_data[exercise])
    print(exercise)
    for percent, reps in sets:
        print('\t{:8.2f}kg, {} reps'.format(training_max * percent, reps))


def print_week(week: int):
    sets = config.sets_per_week[week - 1]
    for day in config.DAY_A, config.DAY_B:
        print_bar('Week {}, {}'.format(week, day))
        for exercise in config.exercises_per_day[day]:
            print_exercise(exercise, sets)
