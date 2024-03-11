# cse30
# pa5
# test modules graph.py, fifteen.py, and game.py

if __name__ == '__main__':

    score1 = 0
    score2 = 0
    score3 = 0

# test module graph.py and class Graph
    total1 = 10
    module1 = 'graph.py'
    classname1 = 'Graph'

#1
    try:
        from graph import Graph
        print(f'module {module1} and class {classname1} are implemented +1/1')
        score1 += 1
    except:
        print(f'module {module1} or class {classname1} is not implemented +0/{total1}')
    else:
#2
        try:
            g = Graph()
            print('contructor is implemented +1/1')
            score1 += 1
        except:
            print('constructor is not implemented +0/1')
#3        
        try:
            for i in range(6):
                g.addVertex(i)
            print('addVertex is implemented +1/1')
            score1 += 1
        except:
            print('addVertex is not implemented +0/1')
#4
        try:
            g.addEdge(0,1)
            g.addEdge(0,5)
            g.addEdge(1,2)
            g.addEdge(2,3)
            g.addEdge(3,4)
            g.addEdge(3,5)
            g.addEdge(4,0)
            g.addEdge(5,4)
            g.addEdge(5,2)
            print('addEdge is implemented +1/1')
            score1 += 1
        except:
            print('addEdge is not implemented +0/1')      
#5
        try:
            assert (g.getVertex(0) in g) == True
            assert (g.getVertex(6) in g) == False
            print('getVertex is implemented +1/1')
            score1 += 1
        except:
            print('getVertex is not implemented +0/1')
#6
        try:
            assert str(g.getVertex(0)) == '0 connectedTo: [1, 5]'
            assert str(g.getVertex(5)) == '5 connectedTo: [4, 2]'
            print(f'class {classname1} is implemented correctly +1/1')
            score1 += 1
        except:
            print(f'class {classname1} is not implemented correctly +0/1')
#7
        try:
            path = g.breadth_first_search(0)
            assert path == [0, 1, 5, 2, 4, 3]
            print('BFS is implemented +2/2')
            score1 += 2
        except:
            print('BFS is not implemented +0/2')
#8
        try:
            path = g.depth_first_search()
            assert path == [0, 1, 2, 3, 4, 5]
            print('DFS is implemented +2/2')
            score1 += 2
        except:
            print('DFS is not implemented +0/2')
    
# output results       
    print(f'{module1}: total {score1} points out of {total1}\n')
    
# test module fifteen.py and class Fifteen
    total2 = 20
    module2 = 'fifteen.py'
    classname2 = 'Fifteen'
#1
    try:
        from fifteen import Fifteen
        print(f'module {module2} and class {classname2} are implemented +1/1')
        score2 += 1
    except:
        print(f'module {module2} or class {classname2} is not implemented +0/{total2}')
    else:
#2
        try:
            game = Fifteen()
            print('constructor is implemented +2/2')
            score2 += 2
        except:
            print('costructor is not implemented +0/2')
#3
        try:
            assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
            print('str is implemented +2/2')
            score2 += 2
        except:
            print('str is not implemented +0/2')
#4
        try:
            assert game.is_valid_move(15) == True
            assert game.is_valid_move(12) == True
            assert game.is_valid_move(14) == False
            assert game.is_valid_move(11) == False
            print('is_valid_move is implemented +2/2')
            score2 += 2
        except:
            print('is_valid_move is not implemented +0/2')
#5
        try:
            game.update(15)
            assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14    15 \n'
            game.update(15)
            assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
            print('update is implemented +2/2')
            score2 += 2
        except:
            print('update is not implemented +0/2')
#6
        try:
            assert game.is_solved() == True
            print('is_solved is implemented +2/2')
            score2 += 2
        except:
            print('is_solved is not implemented +0/2')
#7
        try:
            game.shuffle()
            assert str(game) != ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
            print('shuffle is implemented +4/4')
            score2 += 4
        except:
            print('shuffle is not implemented +0/4')
#8
        try:
            game = Fifteen()
            game.update(15)
            game.update(11)
            game.update(12)
            game.update(15)
            assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 12 15 \n13 14 11    \n'
            assert game.is_solved() == False
            game.update(15)
            game.update(12)
            game.update(11)
            game.update(15)
            assert game.is_solved() == True
            print(f'class {classname2} is implemented correctly +5/5')
            score2 += 5
        except:
            print(f'class {classname2} is not implemented correctly +0/5')
#9
        try:
            game = Fifteen()
            assert game.is_solved() == True
            game.shuffle()
            assert game.is_solved() == False
            game.solve()
            assert game.is_solved() == True
            game.update(15)
            game.update(11)
            game.update(12)
            game.update(15)
            assert game.is_solved() == False
            game.solve()
            assert game.is_solved() == True
            print('extra credit method solve is implemented +10/10')
            score2 += 10
        except:
            print('extra credit method solve is not implemented +0/10')
    
# output results       
    print(f'{module2}: total {score2} points out of {total2}\n')

# test module game.py
    total3 = 10
    module3 = 'game.py'
    
# output results
    try:
        f = open('tmp', 'r')
        score = int(f.read())
        assert 0 <= score <= total3
        if score == total3:
            print(f'{module3} output is correct +{score}/{total3}')
        else:
            print(f'{module3} output is partially correct +{score}/{total3}')
        score3 += score
    except Exception:
        print(f'output is incorrect +0/{total3}')
    
    print(f'{module3}: total {score3} points out of {total3}\n')

    score = score1 + score2 + score3
    with open('tmp', 'w') as f:
        f.write(str(score))    
