import topological_sort as topo
import init
import timing
import circuit_parser as cp
import networkx as nx

filename = "simple_circuit.txt"
clk = 7
parser = cp.CircuitParser()
graph = parser.parsing_process(filename)

graph_from_ABC = nx. DiGraph(nx.nx_pydot.read_dot("sqrt_optimized.blif"))

toposort = topo.toposort_Kahn(graph_from_ABC)
arrivals = timing.arrival_time(graph, toposort)
requireds = timing.required_time(graph, toposort, clk)
slack = timing.slack(requireds, arrivals)
critical_path, critical_path_delay = timing.critical_path(graph, arrivals)



if __name__ == "__main__":
    analysis = {}
    analysis["Inputs"] = graph.inputs
    analysis["Outputs"] = graph.outputs
    analysis["Sorted topological order"] = toposort
    analysis["Time slacks"] = slack
    analysis["Critical path"] = critical_path
    analysis["Total delay of critical path"] = critical_path_delay
    print(toposort)

"""    for element in analysis.items():
        print(element)"""