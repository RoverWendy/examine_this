import org.apache.spark.graphx._

//CONSTRUCT A BASIC GRAPH
val babysFirstVertices = sc.makeRDD(Array((1L, "Ann"), (2L, "Bill"),
  (3L, "Charles"), (4L, "Diane"), (5L, "Went to the gym this am")))

val babysFirstEdges = sc.makeRDD(Array(Edge(1L, 2L, "is-friends-with"),
  Edge(2L, 3L, "is-friends-with"), Edge(3L, 4L, "is-friends-with"),
  Edge(4L, 5L, "likes-status"), Edge(3L, 5L, "wrote-status")))

val babysFirstGraph = Graph(babysFirstVertices, babysFirstEdges)
babysFirstGraph.vertices.collect
babysFirstGraph.edges.collect
//triplets join vertices and edges based on vertex ID
//native storage keeps edge and vertex separate
babysFirstGraph.triplets.collect
// get all triplets taht involve is-friends-with relation
// and includes people with names that have the letter a
babysFirstGraph.mapTriplets(t => (t.attr, t.attr=="is-friends-with" &&
  t.srcAttr.toLowerCase.contains("a"))).triplets.collect
// compute the out-degree for each vertex
// outputs index, out-degree
babysFirstGraph.aggregateMessages[Int](_.sendToSrc(1), _ + _).collect


// MOST FREQUENTLY CITED PAPER
// create graph
val graph = GraphLoader.edgeListFile(sc, "cit-HepTh.txt")
//get id of document that's most frequently cited
graph.inDegrees.reduce((a,b) => if (a._2 > b._2) a else b)

// EXPLORATION:
// look at 10:
graph.vertices.take(10)


// MOST INFLUENTIAL PAPER (according to pageRank centrality)
val pr = graph.pageRank(0.001).vertices
pr.reduce((a,b) => if (a._2 > b._2) a else b)

//CONSTRUCT A BASIC GRAPH
