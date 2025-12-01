
import circuit_parser2 as cp
import timers 
import topological_sort as tp
import graph_builder as gb
import timing_builder as tb
import critical_path
import visualize_graph

file1 = "circuit_tests/circuit1.txt"
file2 = "circuit_tests/circuit2.txt"
file3 = "circuit_tests/circuit3.txt"

parser = cp.CircuitParser()
entries =  parser.parse(file2)
builder = gb.CircuitBuilder()
graph = builder.builder(entries)


time_build = tb.TimingGraphBuilder()
t_graph = time_build.build(graph)
sorted = tp.toposort_Kahn(t_graph)


#______________CLK_____________
clk = 8

arrivals = timers.arrival_time(t_graph, sorted)
requireds = timers.required_time(t_graph, sorted, clk)
slacks = timers.slack(requireds, arrivals)

nxgraph = visualize_graph.timing_graph_to_nx(t_graph)

critical_path, delay = critical_path.critical_path(t_graph, arrivals)

pos = visualize_graph.level_layout(t_graph, sorted)

if __name__ == "__main__":
    print("--------------Static Timing Analysis---------------")
    print("______________INFORMATION______________")
    print(f"File used in analysis: {file1}")
    print(f"Inputs of graph: {graph.inputs}")
    print(f"Outputs of graph: {graph.outputs}")
    print(f"Total nodes in graph: {len(graph.nodes)}")
    
    print("______________ACTUAL ANALYSIS______________")
    print(f"Best slack: {max(slacks.values())} for node {max(slacks, key=slacks.get)}")
    print(f"Critical path: {critical_path}")
    print(f"Critical path delay: {delay}")
    visualize_graph.draw_timing_graph(nxgraph,pos)







