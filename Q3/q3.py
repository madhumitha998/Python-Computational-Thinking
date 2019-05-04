# q3.py
# Name: Madhumitha D/O Suresh Kumar
# Section: G1

#TODO: fill ttsum
# nums is a list of integers (e.g. [3, 0, 1, 0, -1, -2, 0])
# t is the target sum (e.g. 0)
def ttsum(nums, t):
  # your code here
  new_list=[]
  for f in range(0,len(nums)):
    diff=t-nums[f]
    for s in range(f+1,len(nums)):
      if nums[s]==diff:
        new_list.append([f,s])

  for f in range(0,len(nums)):
    diff=t-nums[f]
    for s in range(f+1,len(nums)):
      for l in range (s+1,len(nums)):
        if nums[s]+nums[l]==diff:
          new_list.append([f,s,l])
  return new_list

  


  
