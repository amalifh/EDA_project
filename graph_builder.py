import init
class CircuitBuilder:
    def __init__(self):
        self.graph = init.CircuitGraph()
    
    def builder(self, entries):
        for entry in entries:
            name = entry.get("name")
            type = entry.get("type")
            
            
            if type == 'INPUT':
                delay = init.GATE_DELAYS.get(type)
                self.graph.inputs.append(name)
                self.graph.add_node(name, type, delay)
                continue

            if type == 'OUTPUT':
                delay = init.GATE_DELAYS.get(type)
                self.graph.outputs.append(name)
                self.graph.add_node(name, type, delay)
                continue

            if type == 'GATE':
                gate = entry.get("gate")
                delay = init.GATE_DELAYS.get(gate)
                inputs = entry.get("inputs")
                self.graph.add_node(name, gate, delay)
        
                for pred in inputs:
                    self.graph.add_edge(pred, name)

                continue
            raise ValueError(f"Something went wrong with {entry}.")
        
        return self.graph
    


            