def SN_slidingWindow(self, win_size):
	#Algorithm2 -sliding window
	#input: sliding window size(winSize)
	#create all candidate pairs and forward each to phase 2 of cocktail mod1/2
	bdSize = len(self.sorted_list)
	totalSlides = bdSize - winSize
	
	for i in range(0, TotalSlides):
		ids = self.sorted_list[i:i+win_size]
		self.pairRecords_slide(ids)
