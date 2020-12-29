from typing import Union, Sequence


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

    :param stairway: list of ints, where each int is a cost of appropriate step
    :return: minimal cost of getting to the top
    """
    print(stairway)
    min_cost = [stairway[0], stairway[1]]
    for i in range(2, len(stairway)):
        min_cost.append(stairway[i] + min(min_cost[i-2], min_cost[i-1]))
    print('List of min costs: ', min_cost)
    return min_cost[-1]
