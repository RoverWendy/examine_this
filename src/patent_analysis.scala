import org.apache.spark.graphx._

// MOST FREQUENTLY CITED Patent
// create patents
val patents = GraphLoader.edgeListFile(sc, "citations_mini.txt")
//get id of document that's most frequently cited
patents.inDegrees.reduce((a,b) => if (a._2 > b._2) a else b)

// EXPLORATION:
// look at 10:
graph.vertices.take(10)


// MOST INFLUENTIAL PAPER (according to pageRank centrality)
val pr2 = patents.pageRank(0.001).vertices
pr2.reduce((a,b) => if (a._2 > b._2) a else b)
