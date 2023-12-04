quantity = [1, 1, 1, 1, 1, 1]
win_card = [4, 2, 2, 1, 0, 0]

N = len(quantity)
for i in range(0, N):
  for j in range(i + 1, i + win_card[i] + 1):
    quantity[j] += quantity[i]

  print(quantity)
print(sum(quantity))






