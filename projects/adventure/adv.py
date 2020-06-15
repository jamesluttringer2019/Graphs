from room import Room
from player import Player
from world import World
from collections import deque
import random
from ast import literal_eval
# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
#map_file = "maps/test_line.txt"
#map_file = "maps/test_cross.txt"
#map_file = "maps/test_loop.txt"
#map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)


inverse = {'n':'s', 's':'n', 'e':'w', 'w':'e'}

connections = {}
endpoints = set()
visited = set()
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

def find_endpoint(p):
    stack = [[p]]
    while stack != []:
        path = stack.pop()
        cur_p = path[-1]
        visited.add(cur_p)
        if len([i for i in connections[cur_p].values() if i not in visited])==0:
            return path
        for c in [i for i in connections[cur_p].values() if i not in visited]:
            stack.append(path + [c])

def find_closest_undiscovered(p):
    queue = deque([[p]])
    while len(queue)>0:
        path = queue.pop()
        cur_p = path[-1]
        if len([i for i in connections[cur_p].values() if i not in visited])>0:
            return path
        for c in connections[cur_p].values():
            queue.appendleft(path + [c])
    

def traverse(start):
    path = [start]
    while len(visited)<len(connections):
        path += find_closest_undiscovered(path[-1])[1:]
        path += find_endpoint(path[-1])[1:]
    return path

def path_to_dir(path):
    curr = path[0]
    dirs = []
    for i in path[1:]:
        for m,p in connections[curr].items():
            if p == i:
                dirs.append(m)
        curr = i
    return dirs
populate_connections(player.current_room)
traversal_path = path_to_dir(traverse(000))
# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



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
