#11, 3, 5

#11 boxes max 3 and needs to be split 5 way

boxes = 13
max_height = 3

numOfStacks =0

def splitDivide(quantity, maxHeight):
    if quantity > maxHeight:
      a = quantity // 2
      b = quantity % 2 + a
      print(a,b)
      return a, b



if boxes > max_height:
    a,b = splitDivide(boxes, max_height)
    if a > max_height:
        aa, bb = splitDivide(a, max_height)
        if aa > max_height:
            aaa, bbb = splitDivide(aa, max_height)
            if aaa > max_height:
                pass
            else:
                numOfStacks+=1
            if bbb > max_height:
                pass
            else:
                numOfStacks+=1
        else:
            numOfStacks+=1
        if bb > max_height:
            aaa, bbb = splitDivide(bb, max_height)
            if aaa > max_height:
                pass
            else:
                numOfStacks+=1
            if bbb > max_height:
                pass
            else:
                numOfStacks+=1
        else:
            numOfStacks+=1
    else:
        numOfStacks+=1
    if b > max_height:
        cc, dd = splitDivide(b, max_height)
        if cc > max_height:
            ccc, ddd = splitDivide(cc, max_height)
            if ccc > max_height:
                pass
            else:
                numOfStacks+=1
            if ddd > max_height:
                pass
            else:
                numOfStacks+=1
        else:
            numOfStacks+=1
        if dd > max_height:
            ccc, ddd = splitDivide(dd, max_height)
            if ccc > max_height:
                pass
            else:
                numOfStacks += 1
            if ddd > max_height:
                pass
            else:
                numOfStacks += 1
        else:
            numOfStacks+=1
    else:
        numOfStacks+=1


print(numOfStacks)