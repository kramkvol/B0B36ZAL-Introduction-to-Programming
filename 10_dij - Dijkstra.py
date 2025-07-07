class Vertex:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.edges = [] # Список ребер, соединенных с этой вершиной
        self.minDistance = float('inf') # Минимальное расстояние от начальной вершины
        self.previousVertex = None # Ссылка на предыдущую вершину в кратчайшем пути
 
class Edge:
    def __init__(self, source, target, weight):
        self.source = source # ID начальной вершины ребра
        self.target = target # ID конечной вершины ребра
        self.weight = weight # Вес (стоимость) ребра
 
class Dijkstra:
    def __init__(self):
        self.vertexes = [] # Список всех вершин графа
         
    def createGraph(self, vertexes, edgesToVertexes):
        self.vertexes = vertexes
        for vertex in self.vertexes:
            vertex.edges = [edge for edge in edgesToVertexes if edge.source == vertex.id or (edge.target == vertex.id and not self.isDirected)]
             
    def isDirected(self, edge):
        # Проверяем, является ли ребро направленным, сравнивая с уже существующими рёбрами
        for vertex in self.vertexes:
            for existing_edge in vertex.edges:
                if existing_edge.source == edge.target and existing_edge.target == edge.source:
                    return True
        return False
 
    def getVertexes(self):
        # Возвращаем список вершин, которые имеют ребра      
 
        connected_vertexes = []
        for vertex in self.vertexes:
            if vertex.edges:  # Проверяем, есть ли у вершины ребра
                connected_vertexes.append(vertex)
        return connected_vertexes
 
    def computePath(self, startVertexId):
         
        # Инициализируем пути для стартовой вершины
        startVertex = self.vertexById(startVertexId)
        startVertex.minDistance = 0
        unvisited = set(self.vertexes)
 
        while unvisited:
            currentVertex = self.getVertexWithMinDistance(unvisited)
            unvisited.remove(currentVertex)
            self.updateDistances(currentVertex, unvisited)
 
    def getVertexWithMinDistance(self, unvisited):
 
        # Находим вершину с минимальным расстоянием из непосещенных
        return min(unvisited, key=lambda vertex: vertex.minDistance)
 
    def updateDistances(self, currentVertex, unvisited):
 
        # Обновляем расстояния для всех соседних вершин
        for edge in currentVertex.edges:
            targetVertex = self.vertexById(edge.target if edge.source == currentVertex.id else edge.source)
            if targetVertex in unvisited:
                newDistance = currentVertex.minDistance + edge.weight
                if newDistance < targetVertex.minDistance:
                    targetVertex.minDistance = newDistance
                    targetVertex.previousVertex = currentVertex
 
    def getShortestPathTo(self, targetVertexId):
        # Возвращает кратчайший путь к заданной вершине
        path = []
        currentVertex = self.vertexById(targetVertexId)
        while currentVertex is not None:
            path.insert(0, currentVertex)
            currentVertex = currentVertex.previousVertex
        return path
 
    def resetDijkstra(self):
        # Сброс всех значений минимальных расстояний и предыдущих вершин
        for vertex in self.vertexes:
            vertex.minDistance = float('inf')
            vertex.previousVertex = None
 
    def vertexById(self, vertexId):
        # Возвращает вершину по ее ID
        for vertex in self.vertexes:
            if vertex.id == vertexId:
                return vertex
        return None
     
if __name__ == '__main__':
    vertexes = [
    Vertex(0, 'Redville'),
    Vertex(1, 'Blueville'),
    Vertex(2, 'Greenville'),
    Vertex(3, 'Orangeville'),
    Vertex(4, 'Purpleville')
    ]
 
 
    edges = [
        Edge(0, 1, 5),
        Edge(0, 2, 10),
        Edge(0, 3, 8),
        Edge(1, 0, 5),
        Edge(1, 2, 3),
        Edge(1, 4, 7),
        Edge(2, 0, 10),
        Edge(2, 1, 3),
        Edge(3, 0, 8),
        Edge(3, 4, 2),
        Edge(4, 1, 7),
        Edge(4, 3, 2)
    ]
    #New Dijkstra created
    dijkstra = Dijkstra()
    #Graph created
    dijkstra.createGraph(vertexes,edges)
    #Getting all vertexes
    dijkstraVertexes = dijkstra.getVertexes()
    #Computing min distance for each vertex in graph
    for vertexToCompute in dijkstraVertexes:
        dijkstra.computePath(vertexToCompute.id)
        print('Printing min distance from vertex:'+str(vertexToCompute.name))
        #Print minDitance from current vertex to each other
        for vertex in dijkstraVertexes:
            print('Min distance to:'+str(vertex.name)+' is: '+str(vertex.minDistance))
        #Reset Dijkstra between counting
        dijkstra.resetDijkstra()
    #Distance with path
    for vertexToCompute in dijkstraVertexes:
        dijkstra.computePath(vertexToCompute.id)
        print('Printing min distance from vertex:'+str(vertexToCompute.name))
        #Print minDitance and path from current vertex to each other
        for vertex in dijkstraVertexes:
            print('Min distance to:'+str(vertex.name)+' is: '+str(vertex.minDistance))
            print('Path is:',end=" ")
            #Get shortest path to target vertex
            path = dijkstra.getShortestPathTo(vertex.id)
            for vertexInPath in path:
                print(str(vertexInPath.name),end=" ")
            print()
        #Reset Dijkstra between counting
        dijkstra.resetDijkstra()