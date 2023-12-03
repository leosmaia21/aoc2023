import numpy as np
file = "data"
file = "teste"


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

  print(ret)
part1()


def part2():
  ret = 0
  def check(start, end, line):
    top = list(map(lambda x: -1 if x.isdigit() or x=="."else x, data[line-1][start-1:end+2]))
    bottom = list(map(lambda x: -1 if x.isdigit() or x=="." else x,data[line+1][start-1:end+2]))
    right = list(map(lambda x: -1 if x.isdigit() or x=="." else x,data[:,end+1][line:line +1]))
    left = list(map(lambda x: -1 if x.isdigit() or x=="." else x,data[:,start-1][line:line +1]))

    top = [i for i, x in enumerate(top) if x != -1]
    bottom = [i for i, x in enumerate(bottom) if x != -1]
    right = [i for i, x in enumerate(right) if x != -1]
    left = [i for i, x in enumerate(left) if x != -1]
    index = 0
    if len(top) != 0:
      index = [line-1, top[0]]
    elif len(bottom) != 0:
      index = [line+1, bottom[0]]
    elif len(right) != 0:
      index = [end+1, 

    
    return int("".join(data[line][start:end+1])), () if len(top+bottom+right+left) != 0 else 0

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

  print(ret)
    
part2()



