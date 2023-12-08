
file = "data"
file = "teste"


seeds = []
data = []
with open(file) as f:
  i = -1
  for indexLine, line in enumerate(f):
    line = line.strip()
    if indexLine == 0: seeds = [int(x) for x in line.split(":")[1].split()]
    else:
      if not len(line): continue
      elif len(line)!=0 and line[0].isalpha():
        i+=1
        data.append([])
      elif line[0].isdigit():
        data[i].append([int(x) for x in line.split()])

oldSeeds = seeds
min = 9223372036854775807
for groupIndex in (range(0, len(oldSeeds), 2)):
  start = oldSeeds[groupIndex]
  range_ = oldSeeds[groupIndex + 1]

  for seed in (range(start, start + range_)):
    for block in data:
      for line in block:
          if seed >= line[1] and seed < line[1] + line[2]:
            seed = seed - line[1] + line[0]
            break
    if seed < min:
      min = seed
print(min)




