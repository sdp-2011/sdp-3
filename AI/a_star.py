def aStar(self, graph, current, end):
    openSet = set()	# The set of nodes to be evaluated
    closedSet = set()	# The set of nodes already evaluated

    def retracePath(c):
	def parentgen(c):
	    while c:
		yield c
		c = c.parent
	result = [element for element in parentgen(c)]
	result.reverse()
	return result

    openSet.add(current)
    while openSet:
	current = min(openSet, key=lambda inst:inst.H)[0]
	if current == end:
	    return retracePath(current)
	openSet.remove(current)
	closeSet.add(current)
	for tile in graph[current]:
	    if tile not in closedSet:
		tile.H = (abs(end.x-tile.x)+abs(end.y-tile.y))*10
		openSet.add(tile)
		tile.parent = current
    return []
