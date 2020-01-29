# Jeff Austin
import sys
import random
import time

# find shortest path between start and end
def BFS(G, start, end):
  Q = []
  # path = []
  previous = {}
  path = []
  if G[start[0]][start[1]][1] == False:   # if the starting point in the graph is empty
    return -1
  if start == (0,0) and end == (0,0):
    path.append((0,0))
    return path
  G[start[0]][start[1]] = (True, True)  # start.visited = True
  Q.append((start[0], start[1])) # add start vertex (tuple passed in) to the queue.
  # path.append((start[0], start[1]))
  while Q != []:
    vertex = Q.pop(0)  # remove the first element of the queue. (FIFO Queue) (dequeue)
    h = vertex[0]      # the vertex is a tuple
    v = vertex[1]
    l1 = h
    l2 = v
    if h != len(G) - 1:
      l1 = h + 1    # if the horizontal component is not equal to the length of G
    if v != len(G[vertex[0]]) - 1:
      l2 = v + 1    # if the vertical component is not equal to the length of the vth array in G
    # l1 = last index 1
    # l2 = last index 2 (indices to check in for loop)
    for i in range(h, l1 + 1):
      for j in range(v, l2 + 1):
        if G[i][j][0] == False and G[i][j][1] == True and is_adjacent_to((i, j), (vertex[0], vertex[1])) == True:  # if it has not been visited and is not empty 
          G[i][j] = (True, G[i][j][1])
          Q.append((i, j)) # enqueue
          previous[(i, j)] = (h, v)
          # path.append((i, j))
          if i == end[0] and j == end[1]:
            path = [(i, j)]
            k = 0
            while path[k] != (start[0], start[1]):
              path.append(previous[path[k]])
              k = k + 1
            path.reverse()
            return path
  return -1

def is_adjacent_to(v, u):
  if abs((v[0] + v[1]) - (u[0] + u[1])) == 1:
    return True
  return False

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
      else:                             # Of the form (Visited, IsDot)
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

    if i >= 0 and i < 10:
      print("   ", end = '')
    if i >= 10 and i < 100:
      print("  ", end = '')
    elif i >= 100 and i < 1000:
      print(" ", end = '')
    print("| ", end='')
    for j in range(len(G[i])):
      if G[i][j][1] == False:
        print("#   ", end='')
      else:
        print(".   ", end='')
    print()
    i = i - 1
  print("     ", end='')
  for k in range(0, len(G[0])):
    if k == len(G[0]) - 1:
      print("---", end='')
    else:
      print("----", end='')
  print()
  print("      ", end='')

  for k in range(0, len(G[0])):
    print(k, end = '')
    if k >= 0 and k < 10:
      print("   ", end = '')
    if k >= 10 and k < 100:
      print("  ", end = '')
    elif k >= 100 and k < 1000:
      print(" ", end = '')
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
  path = BFS(G, start, end)
  if path == -1:
    print("No such path exists.")
    return
  print("\npath:")
  for i in range(len(path)):
    print(path[i])
  print(flush = True)
  return

if __name__ == '__main__':
  main()
