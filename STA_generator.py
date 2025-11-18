import topological_sort as topo
import init
import timing
import circuit_parser as cp
import aiger


filename = "./benchmarks/arithmetic/sqrt.aig"
clk = 7
parser = aiger.CircuitParser()
graph = parser.processing_aig(filename)


#toposort = topo.toposort_Kahn(graph)
#arrivals = timing.arrival_time(graph, toposort)
#requireds = timing.required_time(graph, toposort, clk)
#slack = timing.slack(requireds, arrivals)
#critical_path, critical_path_delay = timing.critical_path(graph, arrivals)



if __name__ == "__main__":
    analysis = {}
    analysis["Inputs"] = graph.inputs
    analysis["Outputs"] = graph.outputs
    #analysis["Sorted topological order"] = toposort
   # analysis["Time slacks"] = slack
   # analysis["Critical path"] = critical_path
    #analysis["Total delay of critical path"] = critical_path_delay
    #print(graph.inputs)
    print(graph.outputs)


    for name,node in graph.nodes.items():
        print(name, node.predecessors, node.successors)
        

"""    for element in a nalysis.items():
        print(element)"""
"""    pos = {node: i for i, node in enumerate(toposort)}
    for name, node in graph.nodes.items():
        for (pred, inv) in node.predecessors:
            if pos[pred] > pos[name]:
                print("Error")"""