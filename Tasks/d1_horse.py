def calculate_paths(shape: (int, int), point: (int, int)) -> int:
    """
    Given field with size rows*cols count available paths from (0, 0) to point

    :param shape: tuple of rows and cols (each from 1 to rows/cols)
    :param point: desired point for horse
    :return: count of paths from (1, 1) to (point[0], point[1]) (numerating from 0, so (0, 0) - left bottom tile)
    """
    print(shape, point)
    paths_count = 0
    position = [1, 1]
    x = 1
    y = 1
    while y < point[1]:
        for turn in range(4):
            if turn == 0:
                position[0] -= 2
                position[1] += 1
            elif turn == 1:
                position[0] -= 1
                position[1] += 2
            elif turn == 2:
                position[0] += 2
                position[1] += 1
            elif turn == 3:
                position[0] += 1
                position[1] += 2
        if position[0] == point[0] and position[1] == point[1]:
            paths_count += 1
            position = [1, 1]


    return paths_count
