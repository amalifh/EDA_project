import topological_sort as topo
import timing
import aiger
import critical_path

<<<<<<< HEAD:old_stuff/STA_generator.py
file = "sqrt.aig"
clk = 5
=======

filename = "./benchmarks/arithmetic/sqrt.aig"
clk = 10116
>>>>>>> fa202273d7c022339a89b3b134bbfd83859a9f39:STA_generator.py
parser = aiger.CircuitParser()
graph = parser.processing_aig(file)

toposort = topo.toposort_Kahn(graph)
arrivals = timing.arrival_time(graph, toposort)
requireds = timing.required_time(graph, toposort, clk)
slack = timing.slack(requireds, arrivals)
critical_path, critical_path_delay = critical_path.critical_path(graph, arrivals)

if __name__ == "__main__":
    print("===============STA===============")
    print(f"Total nodes: {len(graph.nodes)}")
    print(f"Total inputs: {len(graph.inputs)}")
    print(f"Total outputs: {len(graph.outputs)}")
    print(f"Worst slack {min(slack.values())} for node {min(slack, key=slack.get)}")
    print(f"Best slack: {max(slack.values())} for node {max(slack, key=slack.get)}")
<<<<<<< HEAD:old_stuff/STA_generator.py
    print(f"Critical path delay: {critical_path_delay}")
=======
    #print(f"Critical path {'->'.join(map(str, critical_path))}")
    print(f"Critical path delay: {critical_path_delay}")
"""    for name,node in graph.nodes.items():
        if not node.predecessors:
            test += 1
    print(test)"""

>>>>>>> fa202273d7c022339a89b3b134bbfd83859a9f39:STA_generator.py
