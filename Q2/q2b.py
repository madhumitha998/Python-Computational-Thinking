# q2b.py
# Name: Madhumitha D/O Suresh Kumar
# Section: G1

# TODO: fill sv_recursive
# m is a matrix represented by a 2D list of integers. e.g. m = [[3, 0, 2, 18],[-1, 1, 3, 4],[-2, -3, 18, 7]]
# This function returns the Special Value of the matrix passed in.
def sv(m,row,col):
  max_row=len(m)-1
  max_col=len(m[0])-1
  if row==max_row and col==max_col:
    return m[max_row][max_col]    
  elif row==max_row:
    return m[row][col]+sv(m,row,col+1)
  elif col==max_col:
    return m[row][col]+sv(m,row+1,col)
  else:
    return m[row][col]+sv(m,row+1,col)+sv(m,row,col+1)

def sv_recursive(m):
  # your code here
  sv_firstcell=sv(m,0,0)
  return sv_firstcell 

