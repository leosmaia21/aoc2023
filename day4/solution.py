file = "teste"

data = []

with open(file) as f:
  for line in f:
    line = line.strip().split(":")[1].split("|")
    data.append([[int(x) for x in line[0].split()],[int(x) for x in line[1].split()]])

def part1():
  ret = 0
  for g in data:
    # print(g[0], g[1])
    power = -1
    for card in g[1]:
      if card in g[0]: power += 1
    if power != -1: ret += 2**power
  print(ret)

def part2():

  def match(line):
    x = 0
    g = data[line]
    for card in g[1]:
      if card in g[0]: x += 1
    return x

  quantity = [1 for _ in range(len(data))]
  win_card = [match(line) for line in range(len(data))]

  N = len(quantity)
  for i in range(0, N):
    for j in range(i + 1, i + win_card[i] + 1):
      quantity[j] += quantity[i]

  print(sum(quantity))
  # for i, x in enumerate(data):
  #   m = match(i)
  #   for c in range(i+1, i+m+2):
  #     if c < len(data):
  #       ret[c] += ret[i]

part2()
