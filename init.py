class Node:
    def __init__(self, name, type, delay = 0.0):
        self.name = name
        self.type = type
        self.delay = delay
        
        self.predecessors = []
        self.successors = []

    def __repr__(self):
        return (f'Node({self.name}, type = {self.type})')
    
class CircuitGraph:
    def __init__(self):
        self.nodes = {}
        self.inputs = []
        self.outputs = []
    
    def add_or_create_node(self, name, type = None):
        if name not in self.nodes:
            self.nodes[name] = Node(name, type)
        return self.nodes[name]
    
GATE_DELAYS = {
    "INPUT": 0.0,
    "OUTPUT": 0.0,
    "AND": 1.0,
    "OR": 1.0,
    "NOT": 0.5,
    "NAND": 1.2,
    "NOR": 1.2,
    "XOR": 1.5
}
