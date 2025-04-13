from random import randint
import numpy as np

x = np.zeros((20, 20))

j = 0


def x_matrix():
    for i in range(0, 20):
        j = i
        if i < 5:
            x[i][j + 5] = 1
            if i == 0:
                x[i][j + 1] = 1
            elif i == 4:
                x[i][j - 1] = 1
            else:
                x[i][j + 1] = 1
                x[i][j - 1] = 1
        elif i < 15:
            x[i][j + 5] = 1
            x[i][j - 5] = 1
            if i == 5 or i == 10:
                x[i][j + 1] = 1
            elif i == 9 or i == 14:
                x[i][j - 1] = 1
            else:
                x[i][j + 1] = 1
                x[i][j - 1] = 1
        else:
            x[i][j - 5] = 1
            if i == 15:
                x[i][j + 1] = 1
            elif i == 19:
                x[i][j - 1] = 1
            else:
                x[i][j + 1] = 1
                x[i][j - 1] = 1
    return x


x = x_matrix()
print(x)

d = np.zeros((20, 20))


def dist_matrix():
    for i in range(0, 20):
        for j in range(0, 20):
            rand = randint(50, 201)
            d[i][j] = rand
            d[j][i] = d[i][j]
            d[i][i] = 0
    return d * x


d = dist_matrix()
print(d)

a = np.zeros((20, 20))


def beauty_matrix():
    for i in range(0, 20):
        for j in range(0, 20):
            rand = randint(1, 6)
            a[i][j] = rand
            a[j][i] = a[i][j]
            a[i][i] = 0
    return a * x


a = beauty_matrix()
print("BEAUTY----------\n", a)

b = np.zeros((20, 20))


def roughness_matrix():
    for i in range(0, 20):
        for j in range(0, 20):
            rand = randint(1, 6)
            b[i][j] = rand
            b[j][i] = b[i][j]
            b[i][i] = 0
    return b * x


b = roughness_matrix()
print("ROUGHNESS----------\n", b)

s = np.zeros((20, 20))


def safety_matrix():
    for i in range(0, 20):
        for j in range(0, 20):
            rand = randint(1, 6)
            s[i][j] = rand
            s[j][i] = s[i][j]
            s[i][i] = 0
    return s * x


s = safety_matrix()
print("SAFETY----------\n", s)

l = np.zeros((20, 20))


def slope_matrix():
    for i in range(0, 20):
        for j in range(0, 20):
            rand = randint(1, 6)
            l[i][j] = rand
            l[j][i] = l[i][j]
            l[i][i] = 0
    return l * x


l = slope_matrix()
print("SLOPE----------\n", l)


def find_all_paths(matrix, start, end):
    # Convert matrix to a Python list
    matrix = matrix.tolist()

    # Define matrix dimensions
    size = len(matrix)

    # Initialize path list
    paths = []

    # Backtracking function
    def backtrack(path, current):
        # Add current position to the path
        path.append(current)
        # If current position is the end point, add the path to the list of paths
        if current == end:
            paths.append(path[:])
        else:
            # Get the possible moves for the current node
            moves = [i for i, val in enumerate(matrix[current]) if val != 0]

            # Explore all valid neighboring points
            for move in moves:
                next_row = move

                # Check if the next point is within the matrix bounds
                if (
                        0 <= next_row < size
                        and next_row not in path
                ):
                    # Recursively call backtrack with the updated path and the next point
                    backtrack(path, next_row)

        # Remove the current point from the path to backtrack
        path.pop()

    # Call the backtracking algorithm with the starting point and an empty path
    backtrack([], start)

    return paths


temp_paths = find_all_paths(x, 0, 19)
paths = []
c = 0
for i in range(0, len(temp_paths)):
    if 7 <= len(temp_paths[i]) <= 10:
        paths.append(temp_paths[i])
        # print(paths[c])
        c += 1

sum_dist = np.zeros(len(paths))
sum_a = np.zeros(len(paths))
sum_b = np.zeros(len(paths))
sum_s = np.zeros(len(paths))
sum_l = np.zeros(len(paths))

for i in range(0, len(paths) + 1):
    if i == len(paths):
        break
    print("Path ", i + 1, ":", paths[i])
    for node in paths[i]:
        if node == paths[i][-1]:
            break
        # print("Node ", node, ":", d[node][paths[i][paths[i].index(node) + 1]])
        sum_dist[i] += d[node][paths[i][paths[i].index(node) + 1]]
        sum_a[i] += a[node][paths[i][paths[i].index(node) + 1]]
        sum_b[i] += b[node][paths[i][paths[i].index(node) + 1]]
        sum_s[i] += s[node][paths[i][paths[i].index(node) + 1]]
        sum_l[i] += l[node][paths[i][paths[i].index(node) + 1]]

    print("Sum of distances: ", sum_dist[i])
    print("Sum of beauty: ", sum_a[i])
    print("Sum of roughness: ", sum_b[i])
    print("Sum of safety: ", sum_s[i])
    print("Sum of slope: ", sum_l[i])

import csv

def write_arrays_to_csv(file_name, *arrays):
    with open(file_name, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(zip(*arrays))

write_arrays_to_csv('output.csv', paths, sum_a,sum_s, sum_b, sum_l, sum_dist)
