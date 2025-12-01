class CircuitParser:
    def parse(self, filename):
        entries = []
        with open(filename) as f:
            for raw in f:
                line = raw.strip()
                if not line or line.startswith("#"):
                    continue
                
                if line.startswith("INPUT"):
                    entries.append({"type": "INPUT", "name": line.split()[1]})
                    continue
                
                if line.startswith("OUTPUT"):
                    entries.append({"type": "OUTPUT", "name": line.split()[1]})
                    continue
                
                if "=" in line:
                    left, right = line.split("=")
                    name = left.strip()
                    gate = right[:right.index("(")].strip()
                    inside = right[right.index("(")+1 : right.index(")")]
                    inputs = [s.strip() for s in inside.split(",")]
                    entries.append({"type": "GATE",
                                    "name": name,
                                    "gate": gate,
                                    "inputs": inputs})
                    continue

                raise ValueError(f"Invalid format: {line}")
                
        return entries