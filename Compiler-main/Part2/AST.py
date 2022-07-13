from Regex import isID
from pyvis.network import Network


def AST(inputList, fileName):
    x = generateAST(inputList)
    drawAST(x, fileName)


def generateAST(list):
    # base cases
    if len(list) == 1 and isID(list[0]):
        return list
    # recursion
    if '||' in list:
        x = len(list) - list[::-1].index("||") - 1
        first = list[:x]
        second = list[x + 1:]
        firstReady = generateAST(first)
        secondReady = generateAST(second)
        return '||', firstReady, secondReady
    elif '&&' in list:
        x = len(list) - list[::-1].index("&&") - 1
        first = list[:x]
        second = list[x + 1:]
        firstReady = generateAST(first)
        secondReady = generateAST(second)
        return '&&', firstReady, secondReady
    elif '<' in list or '>' in list or '=' in list:
        for x in list[::-1]:
            if x == '<' or x == '>' or x == '=':
                index = len(list) - list[::-1].index(x) - 1
                first = list[:index]
                second = list[index + 1:]
                firstReady = generateAST(first)
                secondReady = generateAST(second)
                return x, firstReady, secondReady
    elif list[0] == '!':
        after = generateAST(list[1:])
        return '!', after


def drawAST(tup, filename):
    AST = Network(height='650px', width='730px', directed=False)
    nodes = []
    AST = drawRecursive(0, 0, AST, nodes, tup)
    for n in AST.nodes:
        n.update({'physics': False})
    AST.save_graph(filename)


def drawRecursive(x_coor, y_coor, graph, dictionary, node, parent=None):
    x = len(dictionary)
    # base case
    if len(node) == 1:
        graph.add_node(n_id=x + 1, x=x_coor, y=y_coor, label=node)
        if parent is not None:
            graph.add_edge(parent, x + 1)
        dictionary.append((node[0], x + 1))
        return graph
    # recursive
    # adding the node
    graph.add_node(n_id=x + 1, x=x_coor, y=y_coor, label=node[0])
    if parent is not None:
        graph.add_edge(parent, x + 1)
    dictionary.append((node[0], x + 1))
    # adding the children
    if len(node) == 3:
        # left branch
        graph = drawRecursive(x_coor - 100, y_coor + 100, graph, dictionary, node[1], x + 1)
        # right branch
        graph = drawRecursive(x_coor + 100, y_coor + 100, graph, dictionary, node[2], x + 1)
        return graph
    elif len(node) == 2:
        graph = drawRecursive(x_coor, y_coor + 100, graph, dictionary, node[1], x + 1)
        return graph


def test1():
    list = ['x', '||', 'y', '&&', '!', 'c', '<', 'a']
    print(generateAST(list))


def test2():
    list = ['x', '||', 'y', '&&', '!', '!', '!', 'c', '<', 'a']
    print(generateAST(list))


def test3():
    list = ['x', '=', 'y', '&&', '!', 'c', '&&', 'a', '<', 'B']
    print(generateAST(list))


def testDraw():
    list = ['x', '||', 'y', '||', '!', 'c', '<', 'a']
    x = generateAST(list)
    drawAST(x, '1.html')


def testDraw2():
    list = ['x', '||', 'y', '&&', '!', '!', '!', 'c', '<', 'a']
    x = generateAST(list)
    drawAST(x, '1.html')


def testDraw3():
    AST(['x', '||', 'y', '&&', '!', 'c', '<', 'a'], "1.html")


def testDraw4():
    AST(['x', '<', 'y', '<', 'a'], "1.html")


def testDraw5():
    AST(['hi', '||', 'y_2'], "1.html")


def testDraw6():
    AST(['x', '<', 'y', '<', 'z', '>', 'm'], "1.html")
