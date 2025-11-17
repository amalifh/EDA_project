import init
class CircuitParser:
    def __init__(self):
        self.graph = init.CircuitGraph()
    
    def parsing_process(self, filename):
        #the parser will go through my file, line by line
        #it is to create new nodes, and also create output node
        with open(filename, 'r') as file:
            lines = file.readlines()

        for raw_line in lines:
            line = raw_line.strip()
            if not line or line.startswith('#'):
                continue

            if line.startswith("INPUT"):
                name = line.split()[1]
                node = self.graph.add_or_create_node(name, type="INPUT")
                node.delay = init.GATE_DELAYS.get("INPUT")
                self.graph.inputs.append(name)
                continue
            #choosing this structure to avoid nestes if's :P
            if line.startswith("OUTPUT"):
                name = line.split()[1]
                node = self.graph.add_or_create_node(name, type="OUTPUT")
                #node.delay = init.GATE_DELAYS.get("OUTPUT")
                self.graph.outputs.append(name)
                continue
            
            #now if it is not an input or output
            #knowing gates are defined n1 = AND(a,b)
            if "=" in line: #might change, don't want the extra if sentences
                left, right = line.split("=")
                name = left.strip()
                gate_info = right.strip()
                type = gate_info[:gate_info.index("(")]
                inside_info = gate_info[gate_info.index("(")+1 : gate_info.index(")")]
                inputs = [s.strip() for s in inside_info.split(',')]

                gate_node = self.graph.add_or_create_node(name, type)
                gate_node.type = type
                gate_node.delay = init.GATE_DELAYS.get(type)
                

            #now I have to connect the edges, so graphs henger sammen
                for input in inputs:
                    pred = self.graph.add_or_create_node(input)
                    gate_node.predecessors.append(pred.name)
                    pred.successors.append(gate_node.name)

                continue
            raise ValueError(f"The format of {line} is unknown")
            
        return self.graph

parser = CircuitParser()
graph = parser.parsing_process("simple_circuit.txt")
node = graph.nodes.get("n2")
print(node.delay)
"""print(graph.inputs)
print(graph.outputs)
print(node.successor)
print(node)
"""
    



