from room import Room
from player import Player
from world import World
from collections import deque
import random
from ast import literal_eval
import time
# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
#map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
#map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)


inverse = {'n':'s', 's':'n', 'e':'w', 'w':'e'}
# room_points = '_to '.join(inverse).split()
connections = {}
endpoints = set()
# # IF INVERSE, APPEND INVERSE PREV DIR
def populate_connections(r):
    feats = [i for i in [r.n_to, r.s_to, r.e_to, r.w_to] if i]
    if r.id in connections:
        return
    connections[r.id] = {}
    if r.n_to:
        connections[r.id]['n'] = r.n_to.id
    if r.s_to:
        connections[r.id]['s'] = r.s_to.id
    if r.e_to:
        connections[r.id]['e'] = r.e_to.id
    if r.w_to:
        connections[r.id]['w'] = r.w_to.id
    for i in feats:
        populate_connections(i)
    if len(feats) == 1:
        endpoints.add(r.id)
        return
visited = set()
def traverse(p):
    breaks = []
    s = [(None, p)]
    last_break = 000
    path = []
    while s!=[]:
        d, p = s.pop()
        path.append((d, p))
        if p in endpoints or len([i for i in connections[p].values() if i not in visited])==0 :
            i = -1
            visited.add(p)
            if len([i for i in connections[breaks[-1]].values() if i not in visited])>1:
                last_break = breaks[-1]
            else:
                last_break = breaks.pop()
            while p != last_break:
                d = inverse[path[i][0]]
                p = connections[p][d]
                path.append((d, p))
                i-=1
        
        else:
            exits = [(d, point)for d, point in connections[p].items()]
            s += exits
            visited.add(p)
            if len(exits)>2:
                breaks.append(p)
        
        print(breaks)
        print(path)
        print(len(visited))
        time.sleep(2)
    return path
populate_connections(player.current_room)

print(endpoints)
print(connections)
print(traverse(000))
# Fill this out with directions to walk
# traversal_path = ['n', 'n']
#traversal_path = [d for d,_ in path]

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

# for move in traversal_path:
#     player.travel(move)
#     visited_rooms.add(player.current_room)

# if len(visited_rooms) == len(room_graph):
#     print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
# else:
#     print("TESTS FAILED: INCOMPLETE TRAVERSAL")
#     print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#         player.current_room.get_exits()
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")


# ------------------------------------------------------------------------------------
# Wouldn't work

# def find_closest_endpoint(p, visited):
#     queue = deque([[p]])
#     shortest = None
#     while shortest == None:
#         path = queue.pop()
#         cur_p = path[-1]
#         if (cur_p in endpoints and cur_p not in visited) or len([i for i in connections[cur_p].values() if i.id not in visited])==0:
#             shortest = path
#         for c in connections[cur_p].values():
#             queue.appendleft(path + [c.id])
#     return shortest
# # two seperate functions bc of loops
# def find_closest_undiscovered(p, visited):
#     queue = deque([[p]])
#     shortest = None
#     while shortest == None:
#         path = queue.pop()
#         cur_p = path[-1]
#         if len([i for i in connections[cur_p].values() if i not in visited])>0 and cur_p!=p:
#             shortest = path
#         for c in connections[cur_p].values():
#             queue.appendleft(path + [c.id])
#     return shortest

# def traverse(start):
#     visited = [start]
#     path = [start]
#     while len(visited)<len(connections):
#         path += find_closest_endpoint(path[-1], visited)[1:]
#         for i in path:
#             if i not in visited:
#                 visited.append(i)
#         path += find_closest_undiscovered(path[-1], visited)[1:]
#         print(len(visited))
#     # path += find_closest_endpoint(path[-1], visited)[1:]
#     # for i in path:
#     #     visited.add(i)
#     # path += find_closest_undiscovered(path[-1], visited)[1:]
#     return path, visited
# #print(connections[475])
# print(connections)
# print(traverse(000))

# def id_to_directions(path):
#     directions = []
#     for i, p in enumerate(path):