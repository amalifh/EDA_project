import EDA_project.init as init

class CircuitParser:
    def __init__(self):
        self.graph = init.CircuitGraph()
    
    def parsing_process(self, filename):
        #the parser will go through my file, line by line
        #it is to create new nodes, and also create output node
        with open(filename, 'r') as file:
            for raw_line in file:
                line = raw_line.strip()
                if not line or line.startswith('#'):
                    continue

                if line.startswith("INPUT"):
                    name = line.split()[1]
                    node = self.graph.add_or_create_node(name, type="INPUT")
                    node.delay = init.GATE_DELAYS["INPUT"]
                    self.graph.inputs.append(name)
                    continue
                #choosing this structure to avoid nestes if's :P
                if line.startswith("OUTPUT"):
                    name = line.split()[1]
                    node = self.graph.add_or_create_node(name, type="OUTPUT")
                    node.delay = init.GATE_DELAYS["OUTPUT"]
                    self.graph.outputs.append(name)
                    


    



