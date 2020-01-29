# Jeff Austin
import sys
import random
import time

# find shortest path between start and end
def BFS(G, start, end):
  path_length = 0 # at the start node the path grade is zero.
  Q = []
  previous = {}
  if G[start[0]][start[1]][1] == False:   # if the starting point in the graph is impassable
    return -1
  if start == (0,0) and end == (0,0):
    return path_length
  G[start[0]][start[1]] = (True, True)  # start.visited = True
  Q.append((start[0], start[1])) # add start vertex (tuple passed in) to the queue.
  # path.append((start[0], start[1]))
  while Q != []:
    vertex = Q.pop(0)  # remove the first element of the queue. (FIFO Queue) (dequeue)
    x = vertex[0]      # the vertex is a tuple
    y = vertex[1]
    h = len(G) - 1
    w = len(G[0]) - 1
    path_length = path_length + 1

    if x - 1 >= 0 and x - 1 <= h:
      if G[x - 1][y][0] == False and G[x - 1][y][1] == True: # if it has not been visited and is not empty
        G[x - 1][y] = (True, G[x - 1][y][1])
        Q.append((x - 1, y)) # enqueue
        previous[(x - 1, y)] = (x, y)
        # path.append((i, j))
        if x - 1 == end[0] and y == end[1]:
          '''
          path = [(x - 1, y)]
          k = 0
          while path[k] != (start[0], start[1]):
            path.append(previous[path[k]])
            k = k + 1
          return len(path) - 1
          '''
          return path_length

    if y - 1 >= 0 and y - 1 <= w:
      if G[x][y - 1][0] == False and G[x][y - 1][1] == True: # if it has not been visited and is not empty
        G[x][y - 1] = (True, G[x][y - 1][1])
        Q.append((x, y - 1)) # enqueue
        previous[(x, y - 1)] = (x, y)
        # path.append((i, j))
        if x == end[0] and y - 1 == end[1]:
          '''
          path = [(x, y - 1)]
          k = 0
          while path[k] != (start[0], start[1]):
            path.append(previous[path[k]])
            k = k + 1
          return len(path) - 1
          '''
          return path_length

    if x + 1 >= 0 and x + 1 <= h:
      if G[x + 1][y][0] == False and G[x + 1][y][1] == True: # if it has not been visited and is not empty
        G[x + 1][y] = (True, G[x + 1][y][1])
        Q.append((x + 1, y)) # enqueue
        previous[(x + 1, y)] = (x, y)
        # path.append((i, j))
        if x + 1 == end[0] and y == end[1]:
          '''
          path = [(x + 1, y)]
          k = 0
          while path[k] != (start[0], start[1]):
            path.append(previous[path[k]])
            k = k + 1
          return len(path) - 1
          '''
          return path_length

    if y + 1 >= 0 and y + 1 <= w:
      if G[x][y + 1][0] == False and G[x][y + 1][1] == True: # if it has not been visited and is not empty
        G[x][y + 1] = (True, G[x][y + 1][1])
        Q.append((x, y + 1)) # enqueue
        previous[(x, y + 1)] = (x, y)
        # path.append((i, j))
        if x == end[0] and y + 1 == end[1]:
          '''
          path = [(x, y + 1)]
          k = 0
          while path[k] != (start[0], start[1]):
            path.append(previous[path[k]])
            k = k + 1
          return len(path) - 1
          '''
          return path_length

  return -1

def is_adjacent_to(v, u):
  if abs((v[0] + v[1]) - (u[0] + u[1])) == 1:
    return True;
  return False;

# generate graph --retangular grid. start: (0, 0) end: (h-1, w-1)
def gen_graph(height, width):
  #We COULD randomize the size but we are just going to let the user generate it for now.
  random.seed()
  #w = random.randint(0, 5)
  h = height
  w = width
  Graph = []
  l = 0
  for l in range(h):
    Graph.append([])
  for i in range(0, h):
    for j in range(0, w):
      a = random.randint(0,2)
      if a == 1 or a == 2:
        Graph[i].append((False, True))
      else:                             # Of the form (Visited, IsNotEmpty)
        Graph[i].append((False, False))
  return Graph

def print_formatted_graph(G):
  if G == []:
    print("[]")
    return
  i = len(G) - 1
  print("Graph layout:\n")
  while i >= 0:
    print(i, end='')
    print("| ", end='')
    for j in range(len(G[i])):
      if G[i][j][1] == False:
        print("# ", end='')
      else:
        print(". ", end='')
    print()
    i = i - 1
  print("   ", end='')
  for k in range(0, len(G[0])):
    print("--", end='')
  print()
  print("   ", end='')
  for k in range(0, len(G[0])):
    print(k, end='')
    print(" ", end='')
  print()
  print()
  print("# => impassable object")
  print(". => passable object")

#Program usage format: Usage format: `python3 BFS_cells.py height width starty startx endy endx`
def main():
  if len(sys.argv) < 7:
    print("Error. Not enough arguments")
    print("Usage format: `python3 BFS_cells.py height width starty startx endy endx`");
    return
  G = gen_graph(int(sys.argv[1]), int(sys.argv[2]))
  start = (int(sys.argv[3]), int(sys.argv[4]))
  end = (int(sys.argv[5]), int(sys.argv[6]))

  G[0][0] = (False, True)   # ensure that the start and end points are `nonempty`
  G[int(sys.argv[5])][int(sys.argv[6])] = (False, True) # ensure that the start and end points are `nonempty`
  print()
  print_formatted_graph(G)
  path_length = BFS(G, start, end)
  if path_length == -1:
    print("No such path exists.")
    return
  print("\npath length:", end='')
  print(path_length)
  return

if __name__ == '__main__':
  main()
