import timing_graph

class TimingGraphBuilder:
    def __init__(self):
        self.tg = timing_graph.TimingGraph()

    def build(self, circuit_graph):
        for name, node in circuit_graph.nodes.items():
            self.tg.add_node(name, type=node.type, delay=node.delay)

        for src, dst_list in circuit_graph.edges.items():
            for dst in dst_list:
                self.tg.add_edge(src, dst)

        self.tg.add_node("SOURCE", type="SOURCE", delay=0.0)
        self.tg.add_node("TERMINAL", type="TERMINAL", delay=0.0)

        for inp in circuit_graph.inputs:
            self.tg.add_edge("SOURCE", inp)

        for outp in circuit_graph.outputs:
            self.tg.add_edge(outp, "TERMINAL")

        self.tg.startpoints = ["SOURCE"] + circuit_graph.inputs
        self.tg.endpoints = circuit_graph.outputs + ["TERMINAL"]

        return self.tg
