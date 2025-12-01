class Node:
    def __init__(self, name, type, delay = 0.0):
        self.name = name
        self.type = type
        self.delay = delay

        self.predecessors = []
        self.successors = []

    def __repr__(self):
        return (f'Node({self.name}, type = {self.type}, delay = {self.delay})')
    
class CircuitGraph:
    def __init__(self):
        self.nodes = {}
        self.edges = {}
    
        self.inputs = []
        self.outputs = []
    
    def add_node(self, name, type = None, delay = 0.0):
        
        self.nodes[name] = Node(name, type, delay)
        return self.nodes[name]

    def add_edge(self, source, destination):
        if source not in self.edges:
            self.edges[source] = []
            
        self.edges[source].append(destination)

        self.nodes[source].successors.append(destination)
        self.nodes[destination].predecessors.append(source)

GATE_DELAYS = {
    "INPUT": 0.0,
    "OUTPUT": 0.0,
    "AND": 1.0,
    "OR": 1.0,
    "NOT": 0.5,
    "NAND": 1.2,
    "NOR": 1.2,
    "XOR": 1.5,
    "BUF": 0.0
}