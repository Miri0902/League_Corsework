numbers = []
for i in range(5):
    numbers.append(int(input("number")))

x = numbers[0]
for i in range(1,5):
    if x<numbers[i]:
        x = numbers[i]

print(x)



number= 0
while(number < 100):
  number = number + 5
  print(number)

def my_function(x,y):
    result2 = x
    result1= 0
    for i in range(0,result2-y,y):
        result2 = result2-y
        result1 = result1 + 1
    return result1,result2
