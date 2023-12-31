import numpy as np
file = "teste"
file = "data"

def multiplyList(myList):
 
    # Multiply elements one by one
    result = 1
    for x in myList:
        result = result * x
    return result


data = []
with open(file) as f:
  data = [list("." + line.strip() +".") for line in f]
  data.insert(0, list("."*len(data[0])))
  data.insert(len(data), list("."*len(data[0])))
  data = np.array(data)

# print(data)
def part1():
  ret = 0
  def check(start, end, line):
    top = list(filter(lambda x: x.isdigit()==False and x!=".", data[line-1][start-1:end+2]))
    bottom = list(filter(lambda x: x.isdigit()==False and x!=".",data[line+1][start-1:end+2]))
    right = list(filter(lambda x: x.isdigit()==False and x!=".",data[:,end+1][line:line +1]))
    left = list(filter(lambda x: x.isdigit()==False and x!=".",data[:,start-1][line:line +1]))
    return "".join(data[line][start:end+1]) if len(top+bottom+right+left) != 0 else 0

  for linenumber, line in enumerate(data):
    number = False
    start = 0
    for i, c in enumerate(line):
      if c.isdigit() and number == False:
        start = i
        number = True
      elif c.isdigit() ==False and number:
        end = i-1
        number = False
        ret += int(check(start, end, linenumber))

  #print(ret)
# part1()


def part2():
  ret = 0

  #print(data)
  def check(start, end, line):
    top = list(map(lambda x: 1 if x=="*" else 0, data[line-1][start-1:end+2]))
    bottom = list(map(lambda x:1 if x=="*" else 0,data[line+1][start-1:end+2]))
    right = list(map(lambda x:1 if x=="*" else 0, [data[line][end+1]])) #data[:,end+1][line:line +1]))
    left = list(map(lambda x:1 if x =="*" else 0, [data[line][start-1]]))#data[:,start-1][line:line +1]))

    # top = [c * (x + start-1) for x, c in enumerate(top) if c == 1]
    # print(top, bottom, left, right)

    if (sum(top) > 1 or sum(bottom) > 1) and (sum(left) or sum(right)): 
      print("Gotcha")
      exit()
    top = top.index(1) if 1 in top else -1
    bottom = bottom.index(1) if 1 in bottom else -1
    left = left.index(1) if 1 in left else -1
    right = right.index(1) if 1 in right else -1

    index =(-1, -1)

    if (top) != -1:
      index= (top+start-1, line-1)
    elif (bottom) != -1:
      index= (bottom+start-1, line+1)
    elif (left) != -1:
      index= (start -1,line)
    elif (right) != -1:
      index= (end+1, line)
    else:
      index=(-1, -1)

    #print(index)

    if index != (-1, -1):
      print(top, bottom, left, right)
      print(index)
      print(data[index[1]- 1: index[1] + 2, index[0]-1: index[0] + 2])
      print("\n\n")
      return int("".join(data[line][start:end+1])), index
    return 0, (-1, -1)

  final ={}
  for linenumber, line in enumerate(data):
    number = False
    start = 0
    for i, c in enumerate(line):
      if c.isdigit() and number == False:
        start = i
        number = True
      elif c.isdigit() ==False and number:
        end = i-1
        number = False
        value , x= check(start, end, linenumber)
        if not x in final:
          final[x] =[value]
        else:
          final[x].append(value)

  print(final)
  for key, value in final.items():
    if len(value) == 2:
      print(f'{key}:', value)
      ret += value[0] * value[1]
  print(ret)
part2()
