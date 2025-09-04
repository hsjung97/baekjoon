year = int(input())

result = 0
if (year % 400 == 0) or (year % 4 ==0 and year % 100 !=0):
    result = 1
    print(f"{result}")
else:
    result = 0
    print(f"{result}")