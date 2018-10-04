--Find our source
SELECT source
FROM ways
WHERE osm_id = 195743190;
--source 183593

--Find our pizza place
SELECT *
FROM osm_nodes
WHERE tag_value = 'pizza'
LIMIT 1;
--osm_id 1658397652

--Find the way closest to our pizza place
SELECT source, ST_DISTANCE(ways.the_geom, pizza.the_geom) as distance, *
FROM ways, (SELECT the_geom
			FROM osm_nodes
			WHERE osm_id = 1658397652
			LIMIT 1) as pizza
ORDER BY ways.the_geom <-> pizza.the_geom
LIMIT 10;
--source 52,623

--Find our route
SELECT *
FROM pgr_dijkstra('
	SELECT gid as id, source, target, length as cost
	FROM ways',
	183593, 52623);
--pgrouting query

--Add geometry to our route
SELECT the_geom, *
FROM (SELECT *
	  FROM pgr_dijkstra('SELECT gid as id, source, target, length as cost
						FROM ways', 183593, 52623, false)) as route, ways
WHERE route.edge = ways.gid;
--pgrouting with ways
