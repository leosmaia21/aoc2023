

ret = 0
with open("data") as file:
  for line in file:
    first = [x for x in line if x.isdigit()][0]
    last = [x for x in line if x.isdigit()][-1]
    ret += int(first + last)
print(ret)

data = "teste"
data = "data"

ret = 0
numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight",  "nine"]
with open(data) as file:
  for line in file:
    finalline=''
    for i , c in enumerate(line):
      for j, n in enumerate(numbers):
        if line[i:i+len(n)] == n:
          finalline += str(j+1)
      if c.isdigit():
        finalline += c

          
    first = [x for x in finalline if x.isdigit()][0]
    last = [x for x in finalline if x.isdigit()][-1]
    ret += int(first + last)


print(ret)
