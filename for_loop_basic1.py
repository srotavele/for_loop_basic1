# Basic
for n in range(0, 150):
    n = n + 1
    print(n)

# Multiples of Five
for n in range(5, 1001, 5):
    print(n)


# Counting, the Dojo Way -
result = []
for i in range(1, 101):
    if i % 5 == 0 and i % 10 == 0:
        result.append("Coding Dojo")
    elif i % 5 == 0:
        result.append("Coding")
    else:
        result.append(str(i))
print(result)


# Whoa. That Sucker's Huge
n = 500000
oddnums = 0
for i in range(1, n+1, 2):
    oddnums += i
print(oddnums)


# Countdown by Fours
for n in range(2018, 0, -4):
    print(n)


# Flexible Counter
lowNum = 5
highNum = 50
mult = 4
for i in range(lowNum, highNum):
    if i % mult == 0:
        print(i)
