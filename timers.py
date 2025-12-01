import timing_graph as tg

def arrival_time(graph : tg.TimingGraph, topological_order):
    arrivals = {name : 0.0 for name in graph.nodes}
    
    for name in topological_order:
        node = graph.nodes.get(name)

        if node.type == "INPUT":
            continue

        max_time = 0.0
        for pred in node.predecessors:
            a_time = arrivals.get(pred,0.0)
            if a_time > max_time:
                max_time = a_time
        arrivals[name] = max_time + float(node.delay)

    return arrivals

def required_time(graph : tg.TimingGraph, topological_order, clock_period):
    required = {name : float('inf') for name in graph.nodes}

    for name in graph.endpoints:
        required[name] = clock_period

    for name in reversed(topological_order):
        node = graph.nodes.get(name)
        
        min_time = float('inf')
        for succ in node.successors:
            req_time = required[succ] - graph.nodes[succ].delay
            min_time = min(req_time, min_time)

        if node.successors:
            required[name] = min_time
    return required

def slack(required, arrival):
    slack = {}
    for name in required:
        slack[name] = required[name] - arrival[name]
    return slack