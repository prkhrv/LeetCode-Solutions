def minMoves(arr):
  count1 = 0
  dis = 0 
  for num in arr:
      if num ==1:
          count1+=1
      if num==0:
          dis+=count1
          
  count0 = len(arr) - count1
  rev_dis = count1 * count0 - dis
  return min(dis, rev_dis)
