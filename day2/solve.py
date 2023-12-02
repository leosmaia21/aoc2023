#!/usr/bin/python3

file = "teste"
file = "data"

ret = 0
with open(file) as f:
  for i, line in enumerate(f):
    data = {'red':0, 'blue':0, 'green':0}
    possible = True
    for round in line.strip().split(":")[1].strip().split(";"):
      for play in [[x.strip() for x in move.strip().split()]  for move in round.strip().split(",")]:
        data[play[1]] = int(play[0])
        if data['red'] > 12 or data['green'] > 13 or data['blue'] > 14:
          possible = False
        
    if possible:
      ret += i+1

print(ret)


ret = 0
final = []
with open(file) as f:
  for i, line in enumerate(f):
    data = {'red':[], 'blue':[], 'green':[]}
    for r, round in enumerate(line.strip().split(":")[1].strip().split(";")):
      for play in [[x.strip() for x in move.strip().split()]  for move in round.strip().split(",")]:
        data[play[1]].append(int(play[0]))
    final.append(max(data['red']) * max(data['blue']) * max(data['green']))

print(sum(final))

