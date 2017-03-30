import org.apache.spark.graphx._

// Load graphs by binned ears
val patents_1975 = GraphLoader.edgeListFile(sc, "edgelist_1975.txt")
val patents_1980 = GraphLoader.edgeListFile(sc, "edgelist_1980.txt")
val patents_1985 = GraphLoader.edgeListFile(sc, "edgelist_1985.txt")
val patents_1990 = GraphLoader.edgeListFile(sc, "edgelist_1990.txt")
val patents_1995 = GraphLoader.edgeListFile(sc, "edgelist_1995.txt")
val patents_2000 = GraphLoader.edgeListFile(sc, "edgelist_2000.txt")


//MOST CITED PATENTS
patents.inDegrees.reduce((a,b) => if (a._2 > b._2) a else b)
patents_1975.inDegrees.reduce((a,b) => if (a._2 > b._2) a else b)
// (org.apache.spark.graphx.VertexId, Int) = (3760171,80)
patents_1980.inDegrees.reduce((a,b) => if (a._2 > b._2) a else b)
//(org.apache.spark.graphx.VertexId, Int) = (3702886,105)
patents_1985.inDegrees.reduce((a,b) => if (a._2 > b._2) a else b)
//(org.apache.spark.graphx.VertexId, Int) = (4258264,106)
patents_1990.inDegrees.reduce((a,b) => if (a._2 > b._2) a else b)
//(org.apache.spark.graphx.VertexId, Int) = (4723129,195)
patents_1995.inDegrees.reduce((a,b) => if (a._2 > b._2) a else b)
//(org.apache.spark.graphx.VertexId, Int) = (4723129,462)
patents_2000.inDegrees.reduce((a,b) => if (a._2 > b._2) a else b)
//(org.apache.spark.graphx.VertexId, Int) = (4723129,519)



// MOST INFLUENTIAL PAPER (according to pageRank centrality)
val pr_1975 = patents_1975.pageRank(0.001).vertices
pr_1975.reduce((a,b) => if (a._2 > b._2) a else b)
//(3778614,5.246652535201344)

val pr_1980 = patents_1980.pageRank(0.001).vertices
pr_1980.reduce((a,b) => if (a._2 > b._2) a else b)
//(org.apache.spark.graphx.VertexId, Double) = (4054595,7.698000000000007)

val pr_1985 = patents_1985.pageRank(0.001).vertices
pr_1985.reduce((a,b) => if (a._2 > b._2) a else b)
//(org.apache.spark.graphx.VertexId, Double) = (4237224,4.828451410599356)

val pr_1990 = patents_1990.pageRank(0.001).vertices
pr_1990.reduce((a,b) => if (a._2 > b._2) a else b)
//(org.apache.spark.graphx.VertexId, Double) = (4880804,6.308953241804201)

val pr_1995 = patents_1995.pageRank(0.001).vertices
pr_1995.reduce((a,b) => if (a._2 > b._2) a else b)
// (org.apache.spark.graphx.VertexId, Double) = (4683195,16.046935417166022)

val pr_2000 = patents_2000.pageRank(0.001).vertices
pr_2000.reduce((a,b) => if (a._2 > b._2) a else b)
//
