

# # Jeh, Glen and Widom, Jennifer (2001) SimRank: A Measure of Structural-Context Similarity. Equation (1)
# graph = any directed graph
# c = a constant between 0 and 1
def basic_sim_rank(graph, c):
    m = initialize_matrix(graph)

    for i in range(1, 5):
        for node_a in graph.nodes():
            if node_a == 'Univ':
                k = 100
            for node_b in graph.nodes():
                # print(i,node_a,node_b, m[node_a])
                similarity = get_similarity(c, graph, m, node_a, node_b)
                m[node_a][node_b] = similarity
                m[node_b][node_a] = similarity

    return m

def jaccard_similarity(graph):
    m = initialize_matrix(graph)

    for node1 in graph.nodes():
        m[node1] = {}
        for node2 in graph.nodes():
            n1_neighbors = get_all_neighbors(graph, node1)
            n2_neighbors = get_all_neighbors(graph, node2)
            common_neighbors = n1_neighbors.intersection(n2_neighbors)
            m[node1][node2] = len(common_neighbors) / (len(n1_neighbors.union(n2_neighbors)))

    return m

def get_similarity(C, graph, similarities, node1, node2):
    if node1 == node2:
        return 1
    normalizer = graph.in_degree(node1) * graph.in_degree(node2)
    if normalizer == 0:
        c = 0
    else:
        c = C / normalizer
    sum = 0
    for p1 in graph.predecessors(node1):
        for p2 in graph.predecessors(node2):
            sum = sum + similarities[p1][p2]
    return c * sum

def print_table(graph, sims):
    print("\n\t\t\t", end='')
    for node_a in graph.nodes():
        print(node_a, '\t', end='')
    print()
    for node_a in graph.nodes():
        print(node_a,'\t\t',end='')
        for node_b in graph.nodes():
            print(round(float(sims[node_a][node_b]),3), '\t', end='')
        print()



def initialize_matrix(graph):
    m = {}
    for node1 in graph.nodes():
        m[node1] = {}
        for node2 in graph.nodes():
            if node1 == node2:
                m[node1][node2] = 1
            else:
                m[node1][node2] = 0
    return m


def get_all_neighbors(graph, node):
    neighbors = set()
    in_neighbors = graph.predecessors(node)
    out_neighbors = graph.neighbors(node)

    for i in in_neighbors:
        neighbors.add(i)

    for i in out_neighbors:
        neighbors.add(i)

    return neighbors
