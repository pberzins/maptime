##1st block
#
##import library for connection to PostgreSQL
#import psycopg2
#
##database auth
#username = "ariel"
#password = ""
##limit for queries
#limit = 3
#
##connect to database
#conn = psycopg2.connect("dbname=routing user=" + username + " password= " + password)
#cur = conn.cursor()
#
##find our source
#way_osm_id = 195743190
#cur.execute("SELECT source FROM ways WHERE osm_id = %s", (way_osm_id,))
#source = cur.fetchone()[0]
#print("My source: " + str(source))
#
##2nd block
#
##find our pizza nodes up to limit
#cur.execute("SELECT * FROM osm_nodes WHERE tag_value = 'pizza' limit %s", (limit,))
#osm_ids = []
#for record in cur:
#   osm_ids.append(record[0])
#print("We're going to route to: " + str(len(osm_ids)) + " pizza nodes.")
#
###3rd block
#
##get the closet ways to our pizza nodes
#pizza_sources = []
#for osm_id in osm_ids:
#   cur.execute("SELECT source\
#       FROM ways\
#       ORDER BY ways.the_geom <-> (SELECT the_geom FROM osm_nodes WHERE osm_id = %s limit 10) limit 1;", (osm_id,))
#   pizza_sources.append(cur.fetchone()[0])
#
#print("We've got: " + str(len(pizza_sources)) + " nearest streets. Should be the same number as pizza nodes.")
#
###4th block
##
#for target in pizza_sources:
#   sql = "(select gid, the_geom, agg_cost from (SELECT * FROM pgr_dijkstra('SELECT gid as id, source, target, length as cost FROM ways', " \
#        + str(source) + ", " + str(target) + ", false)) as x, ways where x.edge = ways.gid)"
#   uri = QgsDataSourceUri()
#   uri.setConnection("localhost", "5432", "routing", username, password)
#   uri.setDataSource("", sql, "the_geom", "", "gid")
#   vlayer = iface.addVectorLayer(uri.uri(False), "route " + str(target), "postgres")
##