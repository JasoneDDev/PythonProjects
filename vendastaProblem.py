#11, 3, 5

#11 boxes max 3 and needs to be split 5 way

boxes = 13
max_height = 3

numOfStacks = 0


def splitDivide(quantity, maxHeight):
    global numOfStacks
    if quantity > maxHeight:
      a = quantity // 2
      b = quantity % 2 + a
      if a <= maxHeight:
          numOfStacks += 1
      else:
          splitDivide(a, max_height)
      if b <= maxHeight:
          numOfStacks += 1
      else:
          splitDivide(b, max_height)
      print(a,b)
      return a, b
    return numOfStacks


splitDivide(boxes, max_height)
print(numOfStacks)