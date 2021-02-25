import config
from typing import Union, Tuple, List

Number = Union[int, float]


def get_training_max(weight: Number, rep: Number) -> float:
    one_rm = weight * 36.0 / (37.0 - float(rep))
    return one_rm * 0.9


def print_exercise(exercise: str, sets: List[Tuple[int, float]]):
    training_max = get_training_max(*config.CURRENT_DATA[exercise])
    for percent, reps in sets:
        print('\t{:8.2f}kg, {} reps'.format(training_max * percent, reps))
    print('\t{:8.2f}kg, {} reps (x5)'.format(training_max *
                                             config.SUPPLEMENTARY_PERCENT, config.SUPPLEMENTARY_REPS))


def print_week(week: int):
    sets = config.SETS_PER_WEEK[week - 1]
    for day in range(4):
        exercise = config.EXERCISE_PER_DAY[day]
        print('Week {}, Day {}: {}'.format(week, day + 1, exercise))
        print_exercise(exercise, sets)
