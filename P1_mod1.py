def computeUI(vector_patterns)
	##algorithm 8 
    ##vector_patterns = collection of vector patterns and their respective frequency counts
	##output u_i
	u_i = [0.1]*TOTAL_ATTRIBUTES
	c = {}
	for x in range(0, totalPairs):
		t1 = dataList[random.randint(0, len(dataList)-1)]
		t2 = dataList[random.randint(0, len(dataList)-1)]
		while t1 != t2:
			t2 = dataList[random.randint(0, len(dataList)-1)]
			
		y_j = repr(compute_vector_pattern(t1,t2))
		if y_i in c.keys():
			c[y_j] += 1
		else :
		c[y_j] = 1
	for i in range(TOTAL_ATTRIBUTES):
		counter = 0
		for k in vector_patterns.keys():
			y_j = eval(k)
			if y_j == 0:
				counter += vector_patterns[k]
			
		u_i = countyer/ totalPairs
