import networkx as net


# Jeh, Glen and Widom, Jennifer (2001) SimRank: A Measure of Structural-Context Similarity. Figure 1
def create_graph1():
    graph = net.DiGraph()

    graph.add_node('StudA')
    graph.add_node('ProfA')
    graph.add_node('Univ')
    graph.add_node('ProfB')
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

    graph.add_node('A', type='user')
    graph.add_node('B', type='user')
    graph.add_node('sugar', type='item')
    graph.add_node('frosting', type='item')
    graph.add_node('eggs', type='item')
    graph.add_node('flour', type='item')

    graph.add_edge('A', 'sugar')
    graph.add_edge('A', 'frosting')
    graph.add_edge('A', 'eggs')
    graph.add_edge('B', 'frosting')
    graph.add_edge('B', 'eggs')
    graph.add_edge('B', 'flour')

    return graph


def create_users_graph(n):
    graph = net.DiGraph()
    with open('../data/reviews') as file:
        for cnt, line in enumerate(file):
            if cnt > n:
                break
            if line.startswith('user: '):
                user, friends = parse_user(line, file)
                graph.add_node(user)
                for f in friends:
                    graph.add_node(f)
                    graph.add_edge(user, f)
                    # graph.add_edge(f, user)
    return graph


def parse_user(line, file):
    name = line.split(':')[1].strip()
    names = file.readline().replace('friends:\t', '').split('\t')
    names[len(names) - 1] = names[len(names) - 1].replace("\n","")
    return name, names
