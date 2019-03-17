import networkx as net


# Jeh, Glen and Widom, Jennifer (2001) SimRank: A Measure of Structural-Context Similarity. Figure 1
def create_graph1():
    graph = net.DiGraph()

    graph.add_node('Univ')
    graph.add_node('ProfA')
    graph.add_node('ProfB')
    graph.add_node('StudA')
    graph.add_node('StudB')

    graph.add_edge('Univ', 'ProfA')
    graph.add_edge('Univ', 'ProfB')
    graph.add_edge('ProfA', 'StudA')
    graph.add_edge('ProfB', 'StudB')
    graph.add_edge('StudA', 'Univ')
    graph.add_edge('StudB', 'ProfB')

    return graph


def create_graph2():
    graph = net.DiGraph()

    graph.add_node('A')
    graph.add_node('B')
    graph.add_node('sugar')
    graph.add_node('frosting')
    graph.add_node('eggs')
    graph.add_node('flour')

    graph.add_edge('A', 'sugar')
    graph.add_edge('A', 'frosting')
    graph.add_edge('A', 'eggs')
    graph.add_edge('B', 'frosting')
    graph.add_edge('B', 'eggs')
    graph.add_edge('B', 'flour')

    return graph
