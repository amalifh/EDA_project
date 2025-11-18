import init

def toposort_Kahn(graph : init.CircuitGraph):
    #first I have to calcute all indegree of each node
    indegree = {name : 0 for name in graph.nodes} #nodes is a dictionary
    queue = []
    ordered = []
    for name, node in graph.nodes.items():
        for successor in node.successors:
            indegree[successor] += 1
    
    #next step: enqueue all nodes of indegree 0
    #I need to check the indegree
    for name, deg in indegree.items():
        if deg == 0 :
            queue.append(name)
    
    
    while queue:
        #now dequeue element at front
        #then I want to decrement indegree of all neigbour nodes
        front = queue.pop(0)
        ordered.append(front)
        node_front = graph.nodes.get(front)

        for succ in node_front.successors:
            indegree[succ] -= 1

            if indegree[succ] == 0:
                queue.append(succ)
        
    return ordered



        

        