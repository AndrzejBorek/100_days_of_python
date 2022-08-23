import random as r

scores = []

for i in range(0,20):
    scores.append(r.randint(1,100))
print(scores)
highestResult = 0

for i in range (0,len(scores)-1):
    if scores[i] > highestResult:
        highestResult = scores[i]

print(f"Highest result is {highestResult}")
