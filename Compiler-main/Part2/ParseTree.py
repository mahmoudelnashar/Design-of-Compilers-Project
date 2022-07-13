from pyvis.network import Network
import queue as q


def generateParseTree(inputString, fileName, config):
    x_offset = 900
    y_offset = 100
    div = 1.5
    if config:
        x_offset = 1800
        div = 3
    # this function parses the input string and returns 1- state(Acc/Rej)  and generates the tree in the file name
    ParseTree = Network(height='650px', width='800px', directed=False)
    # convert the input string list into a queue
    input = q.Queue()
    for x in inputString:
        input.put(x)

    lexeme = input.get()

    nodeCount = 0
    # initializing the pares stack and tree
    parseStack = [('Exp', nodeCount, 0, 0, x_offset)]
    ParseTree.add_node(n_id=nodeCount, x=0, y=0, label='Exp', color='Red')
    nodeCount += 1
    currentExp = None
    while not input.empty() or len(parseStack) != 0 or (lexeme is not None and currentExp is not None):
        # get the first element of the queue if there isn't an element currently being matched
        if lexeme is None and not input.empty():
            lexeme = input.get()
        # get the top of the parse stack
        if currentExp is None and len(parseStack) != 0:
            currentExp = parseStack.pop()
            x_offset = currentExp[4]

        # parse table
        if currentExp[0] == 'Exp':
            if lexeme == '!' or lexeme == 'id':
                parseStack.append(
                    ('Exp-dash', nodeCount, currentExp[2] + x_offset, currentExp[3] + y_offset, x_offset // div))
                ParseTree.add_node(n_id=nodeCount, x=currentExp[2] + x_offset, y=currentExp[3] + y_offset,
                                   label='Exp-dash')
                ParseTree.add_edge(currentExp[1], nodeCount)
                nodeCount += 1

                parseStack.append(
                    ('Term', nodeCount, currentExp[2] - x_offset, currentExp[3] + y_offset, x_offset // div))
                ParseTree.add_node(n_id=nodeCount, x=currentExp[2] - x_offset, y=currentExp[3] + y_offset, label='Term')
                ParseTree.add_edge(currentExp[1], nodeCount)
                nodeCount += 1
                currentExp = None
            else:
                return 'R'
        elif currentExp[0] == 'Exp-dash':
            if lexeme == '||':
                parseStack.append(
                    ('Exp-dash', nodeCount, currentExp[2] + x_offset, currentExp[3] + y_offset, x_offset // div))
                ParseTree.add_node(n_id=nodeCount, x=currentExp[2] + x_offset, y=currentExp[3] + y_offset,
                                   label='Exp-dash')
                ParseTree.add_edge(currentExp[1], nodeCount)
                nodeCount += 1

                parseStack.append(('Term', nodeCount, currentExp[2], currentExp[3] + y_offset, x_offset // div))
                ParseTree.add_node(n_id=nodeCount, x=currentExp[2], y=currentExp[3] + y_offset, label='Term')
                ParseTree.add_edge(currentExp[1], nodeCount)
                nodeCount += 1

                # parseStack.append(('||', nodeCount, currentExp[2] - x_offset, currentExp[3] + y_offset))
                ParseTree.add_node(n_id=nodeCount, x=currentExp[2] - x_offset, y=currentExp[3] + y_offset, label='||')
                ParseTree.add_edge(currentExp[1], nodeCount)
                nodeCount += 1
                lexeme = None
                currentExp = None

            elif lexeme is None:
                ParseTree.add_node(n_id=nodeCount, x=currentExp[2], y=currentExp[3] + y_offset, label='ε')
                ParseTree.add_edge(currentExp[1], nodeCount)
                nodeCount += 1
                currentExp = None
            else:
                return 'R'

        elif currentExp[0] == 'Term':

            if lexeme == '!' or lexeme == 'id':
                parseStack.append(
                    ('Term-dash', nodeCount, currentExp[2] + x_offset, currentExp[3] + y_offset, x_offset // div))
                ParseTree.add_node(n_id=nodeCount, x=currentExp[2] + x_offset, y=currentExp[3] + y_offset,
                                   label='Term-dash')
                ParseTree.add_edge(currentExp[1], nodeCount)
                nodeCount += 1

                parseStack.append(
                    ('Factor', nodeCount, currentExp[2] - x_offset, currentExp[3] + y_offset, x_offset // div))
                ParseTree.add_node(n_id=nodeCount, x=currentExp[2] - x_offset, y=currentExp[3] + y_offset,
                                   label='Factor')
                ParseTree.add_edge(currentExp[1], nodeCount)
                nodeCount += 1
                currentExp = None
            else:
                return 'R'

        elif currentExp[0] == 'Term-dash':
            if lexeme == '&&':
                parseStack.append(
                    ('Term-dash', nodeCount, currentExp[2] + x_offset, currentExp[3] + y_offset, x_offset // div))
                ParseTree.add_node(n_id=nodeCount, x=currentExp[2] + x_offset, y=currentExp[3] + y_offset,
                                   label='Term-dash')
                ParseTree.add_edge(currentExp[1], nodeCount)
                nodeCount += 1

                parseStack.append(('Factor', nodeCount, currentExp[2], currentExp[3] + y_offset, x_offset // div))
                ParseTree.add_node(n_id=nodeCount, x=currentExp[2], y=currentExp[3] + y_offset, label='Factor')
                ParseTree.add_edge(currentExp[1], nodeCount)
                nodeCount += 1

                # parseStack.append(('&&', nodeCount, currentExp[2] - x_offset, currentExp[3] + y_offset))
                ParseTree.add_node(n_id=nodeCount, x=currentExp[2] - x_offset, y=currentExp[3] + y_offset, label='&&')
                ParseTree.add_edge(currentExp[1], nodeCount)
                nodeCount += 1
                lexeme = None
                currentExp = None

            elif lexeme == '||':
                ParseTree.add_node(n_id=nodeCount, x=currentExp[2], y=currentExp[3] + y_offset, label='ε')
                ParseTree.add_edge(currentExp[1], nodeCount)
                nodeCount += 1
                currentExp = None

            elif lexeme is None:
                ParseTree.add_node(n_id=nodeCount, x=currentExp[2], y=currentExp[3] + y_offset, label='ε')
                ParseTree.add_edge(currentExp[1], nodeCount)
                nodeCount += 1
                currentExp = None
            else:
                return 'R'

        elif currentExp[0] == 'Factor':

            if lexeme == '!' or lexeme == 'id':
                parseStack.append(
                    ('Factor-dash', nodeCount, currentExp[2] + x_offset, currentExp[3] + y_offset, x_offset // div))
                ParseTree.add_node(n_id=nodeCount, x=currentExp[2] + x_offset, y=currentExp[3] + y_offset,
                                   label='Factor-dash')
                ParseTree.add_edge(currentExp[1], nodeCount)
                nodeCount += 1

                parseStack.append(
                    ('Operand', nodeCount, currentExp[2] - x_offset, currentExp[3] + y_offset, x_offset // div))
                ParseTree.add_node(n_id=nodeCount, x=currentExp[2] - x_offset, y=currentExp[3] + y_offset,
                                   label='Operand')
                ParseTree.add_edge(currentExp[1], nodeCount)
                nodeCount += 1
                currentExp = None
            else:
                return 'R'

        elif currentExp[0] == 'Factor-dash':

            if lexeme == '<' or lexeme == '=' or lexeme == '>':
                parseStack.append(
                    ('Factor-dash', nodeCount, currentExp[2] + x_offset, currentExp[3] + y_offset, x_offset // div))
                ParseTree.add_node(n_id=nodeCount, x=currentExp[2] + x_offset, y=currentExp[3] + y_offset,
                                   label='Factor-dash')
                ParseTree.add_edge(currentExp[1], nodeCount)
                nodeCount += 1

                parseStack.append(
                    ('Operand', nodeCount, currentExp[2], currentExp[3] + y_offset, x_offset // div))
                ParseTree.add_node(n_id=nodeCount, x=currentExp[2], y=currentExp[3] + y_offset,
                                   label='Operand')
                ParseTree.add_edge(currentExp[1], nodeCount)
                nodeCount += 1

                parseStack.append(
                    ('Compop', nodeCount, currentExp[2] - x_offset, currentExp[3] + y_offset, x_offset // div))
                ParseTree.add_node(n_id=nodeCount, x=currentExp[2] - x_offset, y=currentExp[3] + y_offset,
                                   label='Compop')
                ParseTree.add_edge(currentExp[1], nodeCount)
                nodeCount += 1

                currentExp = None

            elif lexeme == '||' or lexeme == '&&':
                ParseTree.add_node(n_id=nodeCount, x=currentExp[2], y=currentExp[3] + y_offset, label='ε')
                ParseTree.add_edge(currentExp[1], nodeCount)
                nodeCount += 1
                currentExp = None
            elif lexeme is None:
                ParseTree.add_node(n_id=nodeCount, x=currentExp[2], y=currentExp[3] + y_offset, label='ε')
                ParseTree.add_edge(currentExp[1], nodeCount)
                nodeCount += 1
                currentExp = None
            else:
                return 'R'

        elif currentExp[0] == 'Compop':

            if lexeme == '<':
                ParseTree.add_node(n_id=nodeCount, x=currentExp[2], y=currentExp[3] + y_offset, label='<')
                ParseTree.add_edge(currentExp[1], nodeCount)
                nodeCount += 1
                lexeme = None
                currentExp = None
            elif lexeme == '=':
                ParseTree.add_node(n_id=nodeCount, x=currentExp[2], y=currentExp[3] + y_offset, label='=')
                ParseTree.add_edge(currentExp[1], nodeCount)
                nodeCount += 1
                lexeme = None
                currentExp = None
            elif lexeme == '>':
                ParseTree.add_node(n_id=nodeCount, x=currentExp[2], y=currentExp[3] + y_offset, label='>')
                ParseTree.add_edge(currentExp[1], nodeCount)
                nodeCount += 1
                lexeme = None
                currentExp = None
            else:
                return 'R'
        elif currentExp[0] == 'Operand':

            if lexeme == '!':
                parseStack.append(
                    ('Operand', nodeCount, currentExp[2] + x_offset, currentExp[3] + y_offset, x_offset // div))
                ParseTree.add_node(n_id=nodeCount, x=currentExp[2] + x_offset, y=currentExp[3] + y_offset,
                                   label='Operand')
                ParseTree.add_edge(currentExp[1], nodeCount)
                nodeCount += 1

                # parseStack.append(('!', nodeCount, currentExp[2] - x_offset, currentExp[3] + y_offset))
                ParseTree.add_node(n_id=nodeCount, x=currentExp[2] - x_offset, y=currentExp[3] + y_offset, label='!')
                ParseTree.add_edge(currentExp[1], nodeCount)
                nodeCount += 1
                lexeme = None
                currentExp = None
            elif lexeme == 'id':
                ParseTree.add_node(n_id=nodeCount, x=currentExp[2], y=currentExp[3] + y_offset, label='id')
                ParseTree.add_edge(currentExp[1], nodeCount)
                nodeCount += 1
                lexeme = None
                currentExp = None

    for n in ParseTree.nodes:
        n.update({'physics': False})
    # save the tree and return that the state is accepted
    ParseTree.save_graph(fileName)
    return 'A'


def test1():
    inputList = ['id', '||', 'id', '&&', '!', 'id', '<', 'id']
    x = generateParseTree(inputList, 'ParseTree.html', False)
    print(x)


def test2():
    inputList = ['id', '||', 'id', '&&', 'id', '||', '!', '!', '!', 'id']
    x = generateParseTree(inputList, 'ParseTree1.html', True)
    print(x)


def test3():
    inputList = ['id', '<', 'id', '<', 'id']
    x = generateParseTree(inputList, 'ParseTree1.html', False)
    print(x)
