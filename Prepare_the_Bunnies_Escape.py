from collections import deque

def memodict(f):
    class memodict(dict):
        def __missing__(self, key):
            res = self[key] = f(key)
            return res
    return memodict().__getitem__

@memodict
def adjancencies((maze, point)):
    neighbors = (
        (point[0] - 1, point[1]),
        (point[0], point[1] - 1),
        (point[0], point[1] + 1),
        (point[0] + 1, point[1])
    )
    return [p for p in neighbors if 0 <= p[0] < maze[0] \
            and 0 <= p[1] < maze[1]]

def removable(maze, i, j):
    """Determine if the node is passable when the wall is removed."""
    counter = 0
    for p in adjancencies(((len(maze), len(maze[0])), (i, j))):
        if not maze[p[0]][p[1]]:
            if counter > 0:
                return True
            counter += 1
    return False

def answer(maze):

    dimensions = (len(maze), len(maze[0]))

    passable_walls = set()
    for i in xrange(dimensions[0]):
        for j in xrange(dimensions[1]):
            if maze[i][j] == 1 and removable(maze, i, j):
                passable_walls.add((i, j))

    if not passable_walls:
        return len(maze) + len(maze[0]) - 1

    # for row in maze:
    #     print row
    # print

    res = float('inf')

    for wall in passable_walls:
        maze[wall[0]][wall[1]] = 0
        # for row in maze:
        #     print row
        # print wall
        path_mat = [[float('inf')] * dimensions[1] for _ in xrange(dimensions[0])]
        path_mat[0][0] = 1
        visited = set([])
        q = deque()
        q.append((0, 0))
        while q:
            current = q.popleft()
            current_val = path_mat[current[0]][current[1]]
            visited.add(current)
            # if wall == (0, 1):
            #     print 'the path', current
            #     for row in path_mat:
            #         print row
            #     print

            if current == (len(maze)-1, len(maze[0])-1):
                break

            for p in adjancencies((dimensions, current)):
                if maze[p[0]][p[1]] == 0:
                    temp_val = path_mat[current[0]][current[1]] + 1
                    if temp_val < path_mat[p[0]][p[1]]:
                        path_mat[p[0]][p[1]] = temp_val
                    if p not in visited and p not in q:
                        q.append(p)

            # least_neighbor = []
            # for p in adjancencies((dimensions, current)):
            #     # if current == (5, 5) and wall == (0, 1):
            #     #     print p, path_mat[p[0]][p[1]], p_add_val, current_val
            #     # if current == (4, 5) and wall == (0, 1):
            #     #     print p, path_mat[p[0]][p[1]], p_add_val, current_val
            #     if p not in visited:
            #         p_add_val = 1 if maze[p[0]][p[1]] == 0 else 400
            #         path_mat[p[0]][p[1]] = min(path_mat[p[0]][p[1]], current_val + p_add_val)
            #         if len(least_neighbor) == 0 or path_mat[least_neighbor[0][0]][least_neighbor[0][1]] > path_mat[p[0]][p[1]]:
            #             least_neighbor.append(p)
            # for neighbor in least_neighbor:
            #     if p not in q:
            #         q.append(neighbor)
            # if wall == (0, 1):
            #     for row in path_mat:
            #         print row
            #     print current
        maze[wall[0]][wall[1]] = 1
        res = min(res, path_mat[-1][-1])
    #return path_mat[-1][-1] if path_mat[-1][-1] < 400 else path_mat[-1][-1] - 399
    return res

print answer([[0], [0]]) == 2
print answer([[0,1], [1,0], [1,0]]) == 4
print answer([[0, 0], [0, 0]]) == 3
print answer([[0, 1], [0, 0]]) == 3
print answer([[0, 1], [1, 0]]) == 3
print answer([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]) == 7
print answer([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]) == 11

bmaze = [
[0, 0, 0, 0, 0, 0], 
[1, 1, 1, 1, 1, 0], 
[0, 0, 0, 0, 0, 0], 
[0, 1, 1, 1, 1, 1], 
[0, 1, 1, 1, 1, 1], 
[0, 0, 0, 0, 0, 0]
]
print answer(bmaze) == 11

amaze = [
[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], 
[0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], 
[1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], 
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
print answer(amaze) == 61

cmaze = [
    [0, 1, 0, 0, 0, 0, 0, 0, ],
    [1, 1, 1, 1, 1, 1, 1, 0, ],
    [1, 1, 1, 0, 0, 0, 1, 0, ],
    [0, 0, 0, 0, 1, 0, 1, 0, ],
    [0, 1, 0, 0, 1, 0, 1, 0, ],
    [0, 1, 0, 0, 1, 0, 0, 0, ],
    [0, 1, 1, 1, 1, 1, 1, 1, ],
    [0, 0, 0, 0, 0, 0, 0, 0, ],
]
print answer(cmaze) == 35
