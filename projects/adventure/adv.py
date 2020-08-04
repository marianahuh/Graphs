from room import Room
from player import Player
from world import World
from util import Stack, Queue
import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
# create dict of visited
visited = {}
# create list of paths
path = []
# ability to reverse directions/commands
re_direct = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}
# assign current room visited to exits to move around
visited[player.current_room.id] = player.current_room.get_exits()
# while the number of the visited rooms are less than the number of the given number of rooms
while len(visited) < len(room_graph) - 1:
    # check of the room has not been visited
    if player.current_room.id not in visited:
        # then add to visisted
        visited[player.current_room.id] = player.current_room.get_exits()
        prev_path = path[-1]
        # remove previous path so it will not be re-visited
        visited[player.current_room.id].remove(prev_path)
    # while the number of the current visited room has no other paths/end
    while len(visited[player.current_room.id]) == 0:
        # pop the path to return to the previous path
        prev_path = path.pop()
        # the add back to traversal path
        traversal_path.append(prev_path)
        # then have player move to potential other unvisited paths
        player.travel(prev_path)
    # check for current room exits. get the last room then it will be assigned as next path
    next_path = visited[player.current_room.id].pop(0)
    # add to traversal path as the next path to go
    traversal_path.append(next_path)
    # add to path and show already visited
    path.append(re_direct[next_path])
    # player will continue to travel to other rooms not visited with the re direct dict
    player.travel(next_path)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
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
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
