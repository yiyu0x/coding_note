//implement with array
function Graph () {
	this.vertexs = [];
	this.edges = [];

	this.addVertex = function (value) {
		this.vertexs.push(value);
		this.edges[value] = [];
	}
	this.addEdge = function (v1,v2) {
		this.edges[v1].push(v2);
		this.edges[v2].push(v1);
	}

	this.DFS = function (vertex,visited=[]) {
		if ( this.vertexs.indexOf(vertex)!=-1 ) {
			console.log(vertex)
			visited[vertex] = true;
			for (let i=0;i<this.edges[vertex].length;i++) {
				let target = this.edges[vertex][i];
				if ( !visited[target] ) {
					this.DFS(target,visited)
				}
			}
		} else {
			console.log('start vertexs not in graph')
		}

	}
}

var g = new Graph();
g.addVertex("A")
g.addVertex("B")
g.addVertex("C")
g.addVertex("D")
g.addVertex("E")
g.addVertex("F")
g.addVertex("G")
g.addVertex("H")
g.addVertex("I")
g.addVertex("J")
g.addVertex("K")
// console.log(g.vertexs)
g.addEdge("A","B");
g.addEdge("A","C");
g.addEdge("B","D");
g.addEdge("B","E");
g.addEdge("C","F");
g.addEdge("C","G");
g.addEdge("D","H");
g.addEdge("H","E");
g.addEdge("E","I");
g.addEdge("E","J");
g.addEdge("F","K");
g.DFS("A")