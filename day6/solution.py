

file = "teste"
file = "data"

def part1():
  time = []
  distance = []
  with open(file) as f:
      time = [int(x) for x in f.readline().strip().split(":")[1].strip().split()]
      distance = [int(x) for x in f.readline().strip().split(":")[1].strip().split()]


  ret = []
  for race in range(len(time)):
    ret.append(0)
    for t in range(time[race]+1):
      initialTime = time[race]
      timeleft = initialTime - t
      distancetravelled = (initialTime - timeleft) * timeleft
      if distance[race] < distancetravelled: ret[race] += 1 

  r = 1
  for c in ret:
    r *= c
  print(r)


def part2():
  time = []
  distance = []
  with open(file) as f:
      time = [x for x in f.readline().strip().split(":")[1].strip().split()]
      distance = [x for x in f.readline().strip().split(":")[1].strip().split()]


  time = [int("".join(time))]
  distance = [int("".join(distance))]
  ret = []
  for race in range(len(time)):
    ret.append(0)
    for t in range(time[race]+1):
      initialTime = time[race]
      timeleft = initialTime - t
      distancetravelled = (initialTime - timeleft) * timeleft
      if distance[race] < distancetravelled: ret[race] += 1 

  r = 1
  for c in ret:
    r *= c
  print(r)


part2()
