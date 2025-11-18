import init
#aig M I L O A
#aig 24746 128 0 64 24618

class CircuitParser:
    def __init__(self):
        self.graph = init.CircuitGraph()
    

    def parcing_process(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
            first_line = lines[0]

        for raw_line in lines:
            line = raw_line.strip()
            if not line or first_line:
                continue