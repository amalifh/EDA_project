import init


def arrival_time(graph : init.CircuitGraph, topological_order):
    arrivals = {name : 0.0 for name in graph.nodes}

    for name in topological_order:
        node = graph.nodes.get(name)

        if node.type == "INPUT":
            continue

        max_time = 0.0
        for pred in node.predecessors:
            a_time = arrivals.get(pred)
            if a_time > max_time:
                max_time = a_time
        arrivals[name] = max_time + node.delay

    return arrivals

def required_time(graph : init.CircuitGraph, topological_order, clock_period):
    required = {name : float('inf') for name in graph.nodes}

    for name in graph.outputs:
        required[name] = clock_period

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
    max_time = 0
    max_pred = 0
    path = []
    for name in graph.outputs:
        arr_time = arrivals[name]
        if arr_time > max_time:
            max_output = name
            max_time = arr_time
    
    node = graph.nodes.get(max_output)
    for pred in node.predecessors:
        pred_time = arrivals.get(pred)



        

