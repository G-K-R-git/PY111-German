def calculate_paths(shape: (int, int), point: (int, int)) -> int:
    """
    Given field with size rows*cols count available paths from (0, 0) to point

    :param shape: tuple of rows and cols (each from 1 to rows/cols)
    :param point: desired point for horse
    :return: count of paths from (1, 1) to (point[0], point[1]) (numerating from 0, so (0, 0) - left bottom tile)
    """
    paths_cost = [[0 for _ in range(shape[0])] for _ in range(shape[1])]
    paths_cost[0][0] = 1
    # print(paths_cost)
    turns = [(-2, 1), (2, 1), (-1, 2), (1, 2)]
    height = 0
    positions = [(0, 0)]
    new_pos = []
    while height != point[1]:
        for position in positions:
            x = position[0]
            y = position[1]
            for turn in turns:
                x += turn[0]
                y += turn[1]
                if x < 0 or x > shape[0]-1 or y > shape[1]-1:
                    x -= turn[0]
                    y -= turn[1]
                    pass
                else:
                    new_pos.append((x, y))
                    print(x, y, position, positions, height)
                    paths_cost[y][x] += 2*paths_cost[position[1]][position[0]]
                    x -= turn[0]
                    y -= turn[1]
        positions = set(new_pos)
        new_pos = []
        height += 1
    return paths_cost[point[1]][point[0]]


if __name__ == '__main__':
    # shape = (8, 8)
    print('Result ', calculate_paths((9, 9), (8, 8)))
