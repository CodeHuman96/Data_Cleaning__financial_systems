del create_blocks(self):
	###algorithm 1
	###input: all sorted records from dataset
	###note: all blocks are non-overlapping windows
	
	blocks_list = []
	nw = NeedlemanWunsch()
	threshold = 1
	i = 0
	while i<len(self.sorted_list)
		record_A = self.sorted_list[i].getCandKey()
		blockSize = 1
		for j in range (i+1, len(self.sorted_list)):
			record_B = self.sorted_list[j].getCandKey()
			sscore = nw.getSimilarity(record_A,record_B)
			if sscore >= threshold:
				blockSize += 1
			else :
				break
			if blockSize > 1:
				ids = self.sorted_list[i:(i+blockSize)]
				blocks_list.append(ids)
			else:
				pass
			i += blockSize
		return blocks_list
