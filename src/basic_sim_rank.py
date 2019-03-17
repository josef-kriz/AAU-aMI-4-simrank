

# # Jeh, Glen and Widom, Jennifer (2001) SimRank: A Measure of Structural-Context Similarity. Equation (1)
# graph = any directed graph
# c = a constant between 0 and 1
def basic_sim_rank(graph, c):
    m = {}

    for node1 in graph.nodes():
        m[node1] = {}
        for node2 in graph.nodes():
            if node1 == node2:
                m[node1][node2] = 1
            else:
                m[node1][node2] = 0

    for i in range(1, 5):
        for node_a in graph.nodes():
            for node_b in graph.nodes():
                similarity = 1  # magic
                m[node_a][node_b] = similarity
                m[node_b][node_a] = similarity

    return m
