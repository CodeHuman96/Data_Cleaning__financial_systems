def compare_rules(t1, t2, rule_set, insignificantList):
	###Algorithm 11
	###input record pair t1,t2 
	###output matching record pair t1, t2
	
	
	y_j = compute_vector_pattern(t1, t2)
	
	for insig in insignificantList:
		y_j[insig] = 0
	
	if check_rules(y_j, rule_set)
		classifier(t1,t2)
	return 

def check_rules(y_j, rule_set)
		for rule in rule_set:
			res =True
			for i in range(0,TOTAL_ATTRIBUTES):
				if rule[i] == 1:
					if rule[i] != y_j[i]:
						res = False
			if res:
				return True
			return False
