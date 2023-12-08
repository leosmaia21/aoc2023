file = "teste"
file = "data"

file = open(file)

firstLine = file.readline().strip()
file.readline()

data = {}
for line in file:
  line = line.split("=")
  data[line[0].strip()] = line[1].strip().replace(" ", "")[1:-1].split(",")

firstLine = firstLine.strip()
next = "RGT"
ret = 0
i = 0
while next != "ZZZ":
  i %= len(firstLine)
  c = firstLine[i]
  if c == "R":
    next = data[next][1]
  elif c == "L":
    next = data[next][0]
  ret+=1
  i+=1

print(ret)

