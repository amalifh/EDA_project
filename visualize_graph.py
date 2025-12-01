import networkx as nx
import matplotlib.pyplot as plt


def timing_graph_to_nx(tg):
    G = nx.DiGraph()

    # Add nodes with attributes
    for name, node in tg.nodes.items():
        G.add_node(name, type=node.type, delay=node.delay)

    # Add edges
    for src, dst_list in tg.edges.items():
        for dst in dst_list:
            G.add_edge(src, dst)

    return G


def compute_levels(tg, topo):
    level = {name: 0 for name in topo}

    for name in topo:
        for succ in tg.edges.get(name, []):
            level[succ] = max(level[succ], level[name] + 1)

    return level


def level_layout(tg, topo):
    level = compute_levels(tg, topo)

    # group nodes by their level
    levels = {}
    for node, lvl in level.items():
        levels.setdefault(lvl, []).append(node)

    pos = {}
    for lvl, nodes in levels.items():
        for i, node in enumerate(nodes):
            pos[node] = (lvl, -i) 
    return pos


def draw_timing_graph(nx_graph, pos):
    color_map = []
    for n in nx_graph.nodes:
        t = nx_graph.nodes[n]["type"]
        if t == "INPUT":
            color_map.append("lightgreen")
        elif t == "OUTPUT":
            color_map.append("orange")
        elif t == "SOURCE":
            color_map.append("cyan")
        elif t == "TERMINAL":
            color_map.append("magenta")
        else:
            color_map.append("lightblue")

    labels = {n: f"{n}\n({nx_graph.nodes[n]['delay']})" for n in nx_graph.nodes}

    plt.figure(figsize=(12, 6))
    nx.draw(
        nx_graph,
        pos,
        with_labels=True,
        labels=labels,
        node_color=color_map,
        node_size=1500,
        font_size=8,
        arrows=True
    )
    plt.show()
