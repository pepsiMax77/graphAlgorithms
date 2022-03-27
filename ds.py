
###################### data structures #######################################

class Graph:
	def __init__(self):
		self.E = []
		self.V = []
		self.adj = {}

	def addV(self,*V):
		for v in V:
			self.V.append(v)
			self.adj[v] = []

	def addE(self,u,v):
		self.E.append((u,v))
		self.adj[u].append(v)


	def Adj(self,v):
		return self.adj[v]


######################### directed graph algorithms ################################

def BFS(G,s):
	colors = {v: 'white' for v in G.V}
	pi = {v:None for v in G.V}
	d = {v:None for v in G.V}

	stack = []

	colors[s] = 'gray'
	d[s] = 0

	stack.insert(0,s)

	while len(stack):
		curr = stack[0]
		stack = stack[1:]
		for u in G.Adj(curr):
			if colors[u] == 'white':
				stack.append(u)
				colors[u] = 'gray'
				d[u] = d[curr] + 1
				pi[u] = curr

		colors[curr] = 'black'

	return colors,pi,d

def DFS_visit(G,v,colors,pi,top):	
	colors[v] = 'gray'
	for u in G.Adj(v):
		if colors[u] == 'white':
			DFS_visit(G,u,colors,pi,top)
			pi[u] = v

	colors[v] = 'black'
	top.append(v)

def isDAGv(G,v,colors,pi):	
	colors[v] = 'gray'

	for u in G.Adj(v):
		if colors[u] == 'gray':
			return False
		if colors[u] == 'white':
			isDAGv(G,u,colors,pi)
			pi[u] = v

	colors[v] = 'black'
	return True

def DFS(G):
	colors = {v: 'white' for v in G.V}
	pi = {v:None for v in G.V}
	top = []
	

	for v in G.V:
		if colors[v] == 'white':
			DFS_visit(G,v,colors,pi,top)

	return colors,pi,top[::-1]

def isDAG(G):
	DAG = True
	colors = {v: 'white' for v in G.V}
	pi = {v:None for v in G.V}

	for v in G.V:
		if colors[v] == 'white':
			DAG = DAG and isDAGv(G,v,colors,pi)

	return DAG


########################## test driver program #########################


if __name__ == "__main__":

	g = Graph()


	g.addV(1,2,3,4)
	g.addE(1,2)
	g.addE(3,4)
	g.addE(2,3)
	# g.addE(6,1)

	print((DFS(g)[2]))



