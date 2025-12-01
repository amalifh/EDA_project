import timing_graph as tg

def critical_paths(graph : tg.TimingGraph, arrivals):
    max_time = 0
    max_output = None
    total_delay = 0
    for name in graph.endpoints:
        arr_time = arrivals[name]
        if arr_time > max_time:
            max_output = name
            max_time = arr_time
    path = [max_output]
    current_node = graph.nodes.get(max_output)

    while current_node.predecessors:
        max_pred = None
        curr_max_time = 0

        for name in current_node.predecessors:
            time = arrivals[name]
            if time > curr_max_time:
                curr_max_time = time
                max_pred = name

        if max_pred is None:
            break
        current_node = graph.nodes.get(max_pred)
        path.append(max_pred)

    for node in path:
        n = graph.nodes.get(node)
        total_delay += n.delay
    return list(reversed(path)), total_delay

def critical_path(graph: tg.TimingGraph, arrivals):
    # Step 1: Find endpoint with maximum arrival time
    max_output = max(graph.endpoints, key=lambda n: arrivals[n])
    path = [max_output]
    current = max_output

    # Step 2: Backtrack
    while graph.nodes[current].predecessors:
        preds = graph.nodes[current].predecessors

        # pick predecessor whose arrival + its edge_delay = arrival[current]
        def pred_score(p):
            edge = graph.edges.get((p, current), 0)  # net delay if present
            return arrivals[p] + edge

        current = max(preds, key=pred_score)
        path.append(current)

    path.reverse()

    # Step 3: critical path delay = arrivals[max_output]
    total_delay = arrivals[max_output]
    return path, total_delay