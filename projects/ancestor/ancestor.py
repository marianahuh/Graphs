# traverse graph with queue for the shortest path - BFS
class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)

# build graph


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        # if not in in self.vertices,
        if vertex_id not in self.vertices:
            # then add to an empty set
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        # check to pass both vertices
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)


def earliest_ancestor(ancestors, starting_node):
    # initialize graph
    g = Graph()
    # add vertices to each pair
    for pair in ancestors:
        g.add_vertex(pair[0])
        g.add_vertex(pair[1])
        # add edges to each pair in reverse - linking children to up to the parents
        g.add_edge(pair[1], pair[0])
    # implement queue for BFS
    q = Queue()
    q.enqueue([starting_node])
    # keep track of when done
    long_path_length = 1
    # when not found
    earliest_ancestor = -1
    # while still something in the queue
    while q.size() > 0:
        # dq path in the queue
        path = q.dequeue()
        # last vertex in the path becomes current vertex
        vtx = path[-1]
        # if the two paths are the same length, then keep the path of the lowest numeric value
        if (len(path) >= long_path_length and vtx < earliest_ancestor) or (len(path) > long_path_length):
            earliest_ancestor = vtx
            # update longest path to the length of the path
            long_path_length = len(path)
        #
        neighbors = g.vertices[vtx]
        for ancestor in neighbors:
            # make new copy of path
            new_path = list(path)
            # add next ancestor to new path
            new_path.append(ancestor)
            # enqueue new path to queue
            q.enqueue(new_path)
    return earliest_ancestor
