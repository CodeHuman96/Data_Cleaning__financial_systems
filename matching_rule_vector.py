for k in mCollectionVecPatter.keys():
	y_j = eval(k)
	mFrequrency = uFrequency =0.0
	minU =0.0
	
	mFrequrency = mCollectionVecPatter[k]
	if k in uCollectionVecPattern.keys():
		uFrequency = 0.0
	else:
		uFrequency =0.0
		
	if uFrequency == 0:
		minu = 0.0
		
	if (mFrequrency - uFrequency) <= 0:
		continue
	if float(math.log(mFrequrency-uFrequency)/math.log(totalPairs)) >= t1 and minu <= t2:
		for insig in insignificantList:
			y_j[insig] = 0
		total_1 = 0
		for i in range(TOTAL_ATTRIBUTES):
			if y_j[i] == 1:
				total_1 +=1
		temp = (y_j,total_1)
		x.append(temp)
		if y_j not in Z:
			Z.append(y_j)
return Z
