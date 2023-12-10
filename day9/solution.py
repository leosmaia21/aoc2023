
file = "teste"
file = "data"

data = []

def checkIfAllZeros(d):
  for x in d:
    if x != 0: return False
  return True

def part1():
  def funcao(l, retList):
    newList = [l[i+1] - l[i] for i in range(len(l)-1)]
    retList.append(newList + [0])
    if checkIfAllZeros(newList):
      return retList
    return funcao(newList, retList)
  final = 0
  with open(file) as f:
    for line in f:
      data.append([int(x) for x in line.strip().split()])


  for line in data:
    ret = funcao(line, [line + [0]])
    prev = 0
    for x in range(len(ret)-1, -1 , -1):
      ret[x][-1] = prev + ret[x][-2]
      prev = ret[x][-1]

    final += ret[0][-1]
  print(final)

# part1()

def part2():
  def funcao(l, retList):
      newList = [l[i+1] - l[i] for i in range(len(l)-1)]
      retList.append([0] + newList)
      if checkIfAllZeros(newList):
        return retList
      return funcao(newList, retList)
  final = 0
  with open(file) as f:
    for line in f:
      data.append([int(x) for x in line.strip().split()])


  for line in data:
    ret = funcao(line, [[0] + line])
    prev = 0
    for x in range(len(ret)-1, -1 , -1):
      ret[x][0] = ret[x][1] - prev
      prev = ret[x][0]
    final += ret[0][0]
  print(final)

part2()
