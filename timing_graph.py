import init

class TimingGraph:
    def __init__(self):
        self.nodes = {}
        self.edges = {}
        self.rev_edges = {}

        self.startpoints = []
        self.endpoints = []

    def add_node(self, name, type=None, delay=0.0):
        if name not in self.nodes:
            self.nodes[name] = init.Node(name, type, delay)
        else:
            if type is not None:
                self.nodes[name].type = type
            if delay is not None:
                self.nodes[name].delay = delay
        return self.nodes[name]

    def add_edge(self, src, dst):
        self.edges.setdefault(src, []).append(dst)
        self.rev_edges.setdefault(dst, []).append(src)

        self.nodes[src].successors.append(dst)
        self.nodes[dst].predecessors.append(src)
