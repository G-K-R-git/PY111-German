from tabulate import tabulate


def calculate_paths(shape: (int, int), point: (int, int)) -> int:
    """
    Given field with size rows*cols count available paths from (0, 0) to point

    :param shape: tuple of rows and cols (each from 1 to rows/cols)
    :param point: desired point for horse
    :return: count of paths from (1, 1) to (point[0], point[1]) (numerating from 0, so (0, 0) - left bottom tile)
    """
    paths_cost = [[0 for _ in range(shape[1])] for _ in range(shape[0])]
    paths_cost[0][0] = 1
    turns = [(-2, 1), (2, 1), (-1, 2), (1, 2)]  # Массив возможных ходов (исключает ходы "вниз")
    height = 0  # Текущий "уровень"
    positions = [(0, 0)]
    new_pos = []
    while height < point[0]:
        for position in positions:
            x, y = position
            for turn in turns:
                x += turn[0]
                y += turn[1]
                if 0 <= x <= shape[1]-1 and y <= shape[0]-1:
                    paths_cost[y][x] += 2*paths_cost[position[1]][position[0]]
                    x, y = position
                else:
                    x, y = position
        for pos in range(shape[1]):
            if paths_cost[height+1][pos]:
                new_pos.append((pos, height+1))
        positions = set(new_pos)
        new_pos = []
        height += 1
    plot_costs(paths_cost)
    return paths_cost[point[0]][point[1]]


def plot_costs(field):
    to_show = []
    for i in range(1, len(field)+1):
        to_show.append(field[-i])
    print(tabulate(to_show, tablefmt="grid", showindex=[j for j in range(len(field), 0, -1)]))


if __name__ == '__main__':
    print('Result ', calculate_paths((8, 8), (7, 7)))
    print('Result ', calculate_paths((9, 9), (8, 8)))
    print("Result ", calculate_paths((17, 12), (16, 9)))
    print("Result ", calculate_paths((12, 10), (11, 9)))
