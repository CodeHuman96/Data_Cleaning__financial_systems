def computeMI(data)
  m = 0.9
  u = 0.1
  p = 0.5
  convergeValue = 0.00001
  for i in data:
    m[i] = m
    u[i] = u
  while m[i+1]-m[i] !=convergeValue 
             and 
        u[i+1]-u[i] !=convergeValue:  
        runEStep(m[i],u[i],p)
return        
        
