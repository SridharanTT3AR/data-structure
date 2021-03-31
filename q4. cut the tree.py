class vertex:
    def __init__(self,data):
        self.data = data
        self.neighbour = list()
        self.value = int(data)
        self.parent = None
        
    def add_neighbour(self,v):
        if v not in self.neighbour:
            self.neighbour.append((v))
            self.neighbour.sort()     
            
class Graph:
    vertices = {}

    def add_vertices(self,vertex):
        if vertex not in self.vertices:
            self.vertices[vertex.data] = vertex
            return True
        else:
            return False
        
    def add_edges(self,u,v):
        if u in self.vertices and v in self.vertices:
            self.vertices[u].add_neighbour(v)
            self.vertices[v].add_neighbour(u)
            self.vertices[v].parent = self.vertices[u]
            
            return True
        else:
            return False
    
    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key , self.vertices[key].neighbour)
    
        
    def dfs(self,visited,node):
        if node not in visited:
            #print(node)
            visited.add(node)
            for sondhakaran in self.vertices[node].neighbour:
                self.dfs(visited,sondhakaran)
                if(self.vertices[sondhakaran].parent==self.vertices[node]):
                    self.vertices[node].value+=self.vertices[sondhakaran].value
    
    
    def get_value(self):
        for node in self.vertices.keys():
            print(node + str(" ") +  str(self.vertices[node].value))
            
    def get_parent(self):
        print("parent")
        for node in self.vertices.keys():
            if (self.vertices[node].parent):
                print(node + str(" ") +  str(self.vertices[node].parent.data))
                
    def solution(self,val):
        min_value = 10**9
        total_sum = self.vertices[str(val)].value
        for node in self.vertices.keys():
            min_value = min(min_value,abs(total_sum - 2*self.vertices[node].value))
  
        return min_value


def cutTheTree(data, edges):
    print(data)
    print(edges)
    g = Graph()
   
    for i in range(len(data)):
        g.add_vertices(vertex(str(data[i])))

    for edge in edges:
        g.add_edges(str(data[edge[0]-1]),str(data[edge[1]-1]))

    g.print_graph()
    g.dfs(set(),str(data[0]))
    #g.get_value()
    #g.get_parent()
    return g.solution(data[0])
