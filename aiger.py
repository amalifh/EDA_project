import init
#aig M I L O A
#aig 24746 128 0 64 24618

class CircuitParser:
    def __init__(self):
        self.graph = init.CircuitGraph()
    
    def read_varint(self, f_binary):
        value = 0
        shift = 0

        while True:
            byte = f_binary.read(1)
            if not byte:
                raise EOFError("EOF while reading varint")
            
            byte = byte[0]
            value |= (byte & 0x7F) << shift
            if(byte & 0x80) == 0:
                break
            shift += 7

        return value
    
#Header, latches, outputs, gates
    def processing_aig(self, filename):
        with open(filename, 'rb') as file:
            first_line = file.readline()
            header = first_line.decode("ascii").strip().split()
            if header[0] != "aig":
                raise ValueError("The file is not binary AIG")
            
            aig, M, I, L, O, A = header
            M, I, L, O, A = map(int, (M, I, L, O, A))

            #latches = []
            #for i in range(L):
             #   latches.append(int(file.readline().strip()))

            outputs = []
            for i in range(O):
                outputs.append(int(file.readline().strip()))

            and_gates = []
            for i in range(A):
                output_literal = 2*(I+L+i+1)
                dA = self.read_varint(file)
                dB = self.read_varint(file)
                A = output_literal + dA
                B = A + dB
                and_gates.append((output_literal, A, B))
    

        for i in range(I):
            lit_input = 2*(i+1)
            node = self.graph.add_or_create_node(lit_input, "INPUT")
            node.delay = init.GATE_DELAYS.get("INPUT")
            self.graph.inputs.append(node.name)
        
        for lit in outputs: #output is a pointer 
            base = lit & ~1
            inversion = lit & 1

            base_node = self.graph.add_or_create_node(base)
            out_name = f"OUT_{base}"
            

        for out_lit, A, B in and_gates:

            gate = self.graph.add_or_create_node(out_lit, "AND")
            gate.delay = init.GATE_DELAYS.get("AND")

            A_base = A & ~1
            A_inv = A & 1
            node_A = self.graph.add_or_create_node(A_base)

            B_base = B & ~1
            B_inv = B & 1
            node_B = self.graph.add_or_create_node(B_base)
            
            gate.predecessors.append((A_base, A_inv))
            gate.predecessors.append((B_base, B_inv))
            node_A.successors.append(out_lit)
            node_B.successors.append(out_lit)
        return self.graph            