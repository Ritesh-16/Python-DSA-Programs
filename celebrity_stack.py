L = [
  [1, 1, 0, 1],
  [1, 0, 0, 1],
  [0, 0, 0, 1],
  [0, 0, 0, 0]
]

def find_the_celeb(L):
  stack = Stack()
  for i in range(len(L)):
    stack.push(i)

  while stack.size() >= 2:
    r = stack.pop()
    p = stack.pop()

    #this means r does not know p
    if L[r][p]==0:
      # so p is not a celebrity
      stack.push(r)
    else:
      # if r knows p that means r is not celebrity
      stack.push(p)
    
  celeb = stack.pop()

  for i in range(len(L)):
    if i!= celeb:
      if L[i][celeb] == 0 or L[celeb][i] == 1:
        print("There is no Celebrity")
        return
  print("The Celebrity is", celeb)
  return