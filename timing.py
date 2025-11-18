import init
import circuit_parser as cp
import topological_sort as t

def arrival_time(graph : init.CircuitGraph, topological_order):
    arrivals = {name : 0.0 for name in graph.nodes}

    for name in topological_order:
        node = graph.nodes.get(name)

        if node.type == "INPUT":
            continue

        max_time = 0.0
        for pred, inv in node.predecessors:
            a_time = arrivals.get(pred)
            if a_time > max_time:
                max_time = a_time
        arrivals[name] = max_time + node.delay

    return arrivals


def required_time(graph : init.CircuitGraph, topological_order, clock_period):
    required = {name : float('inf') for name in graph.nodes}

    for _, node_name, _ in graph.outputs:
        required[node_name] = clock_period

    for name in reversed(topological_order):
        node = graph.nodes.get(name)
        
        min_time = float('inf')
        for succ in node.successors:
            req_time = required[succ] - node.delay
            min_time = min(req_time, min_time)

        if node.successors:
            required[name] = min_time
    return required


def slack(required, arrival):
    slack = {}
    for name in required:
        slack[name] = required[name] - arrival[name]
    return slack


def critical_path(graph : init.CircuitGraph, arrivals):
    max_time = -1
    max_output = None
    total_delay = 0
    for _, node_name, _ in graph.outputs:
        arr_time = arrivals[node_name]
        if arr_time > max_time:
            max_output = node_name
            max_time = arr_time
        
    path = [max_output]
    current_node = graph.nodes.get(max_output)

    while current_node.predecessors:
        max_pred = None
        curr_max_time = -1

        for pred_name, _ in current_node.predecessors:
            time = arrivals[pred_name]
            if time > curr_max_time:
                curr_max_time = time
                max_pred = pred_name

        if max_pred is None:
            break
        
        path.append(max_pred)
        current_node = graph.nodes.get(max_pred)
    path.reverse()
    total_delay = sum(graph.nodes[n].delay for n in path)
    return path, total_delay
"""
parser = cp.CircuitParser()
graph = parser.parsing_process("simple_circuit.txt")
topo = t.toposort_Kahn(graph)
arrivals = arrival_time(graph, topo)
print(critical_path(graph, arrivals))"""
    



        

