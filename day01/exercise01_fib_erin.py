## Fibonacci sequence
## X_[i] = X_[i-1] + X_[i-2], where X_1 = 1, X_2 = 1
## 1,1,2,3,5,8,....

## Write a for loop, while loop, or function (or all three!) to create a
## list of the first 10 numbers of the fibonacci sequence




fibonacci = []
for i in range(1,11):
    if i==1 or i==2: fibonacci.append(1)
    else: fibonacci.append(sum([fibonacci[i-2], fibonacci[i-3]]))

fibonacci = [1,1]
for i in range(2,11):
    fibonacci[i].append(fibonacci[i-1] + fibonacci[i-2])

fibonacci = []
while len(fibonacci)<10:
    if len(fibonacci)<2: fibonacci.append(1)
    else: fibonacci.append(sum(fibonacci[-2:]))


def findn(n):
    fibonacci = []
    while len(fibonacci)<n:
        if len(fibonacci)<2: fibonacci.append(1)
        else: fibonacci.append(sum(fibonacci[-2:]))
    return fibonacci