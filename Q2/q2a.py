# q2a.py
# Name: Madhumitha D/O Suresh Kumar
# Section: G1

# TODO: fill sv_iterative
# m is a matrix represented by a 2D list of integers. e.g. m = [[3, 0, 2, 18],[-1, 1, 3, 4],[-2, -3, 18, 7]]
# This function returns the Special Value of the matrix passed in.
def sv_iterative(m):
  # your code here
  max_row=len(m)-1
  max_col=len(m[0])-1
  #starts from last num which has no bottom or right sv values
  #goes to next upper row
  for r in range(max_row,-1,-1):
    #fills up sv columns leftward
    for c in range(max_col,-1,-1):
      sv=m[r][c]
      if r!=max_row:
        sv+= m[r+1][c]
      if c!=max_col:
        sv+= m[r][c+1]               
      m[r][c]=sv

  return m[0][0]
