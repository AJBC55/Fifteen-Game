#
# DO NOT FORGET TO ADD COMMENTS!!!
#


from ast import Set


class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def peek(self):
        return self.items[0]
        
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    
    
    
class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
        self.color = 'white'

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        vert = Vertex(key)
        
        self.vertList.update({vert.getId(): vert})
        self.numVertices + 1 

    def getVertex(self,n):
        try:
            x =self.vertList[n]
            return x
        except:
            return False
        
        
        
        
        

    def __contains__(self,n):
        return n in self.vertList.values()

    def addEdge(self,f,t,weight=0):
        self.vertList[f].addNeighbor(t, weight)
      
        

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())
    
    def breadth_first_search(self, s):
        q = Queue()
        seen = []
        seen.append(s)
        for i in self.getVertex(s).getConnections():
            
            q.enqueue(self.vertList[i])
            if i not in seen:
                seen.append(i)
        s = q.dequeue()
        for connects in s.getConnections():
                if connects not in seen:
                    q.enqueue(self.vertList[connects])
                    seen.append(connects)
        while not q.isEmpty():
                y = q.dequeue()
                for ex in  y.getConnections():
                        if ex not in seen: 
                            seen.append(ex)   
        return seen
                
            
            
    
    def depth_first_search(self):
        stack = Stack()
        seen = set()
        keys = list(self.vertList.keys())
        for key in keys:
            seen.add(key)
            for i in self.vertList[key].getConnections():
                stack.push(i)
            while not stack.is_empty():
                seen.add(stack.pop())
        return list(seen)
            
        
        
            
        

    
    def DFS(self, vid, path):
        pass

if __name__ == '__main__':

    g = Graph()
 
    for i in range(6):
        g.addVertex(i)
    
        
    g.addEdge(0,1)
    g.addEdge(0,5)
    g.addEdge(1,2)
    g.addEdge(2,3)
    g.addEdge(3,4)
    g.addEdge(3,5)
    g.addEdge(4,0)
    g.addEdge(5,4)
    g.addEdge(5,2)

    for v in g:
        print(v)
        
    assert (g.getVertex(0) in g) == True
    assert (g.getVertex(6) in g) == False
        
    print(g.getVertex(0))
    assert str(g.getVertex(0)) == '0 connectedTo: [1, 5]'

    print(g.getVertex(5))
    assert str(g.getVertex(5)) == '5 connectedTo: [4, 2]'

    path = g.breadth_first_search(0)
    print('BFS traversal by discovery time (preordering): ', path)
    assert path == [0, 1, 5, 2, 4, 3]
    
    path = g.depth_first_search()
    print('DFS traversal by discovery time (preordering): ', path)
    assert path == [0, 1, 2, 3, 4, 5]


