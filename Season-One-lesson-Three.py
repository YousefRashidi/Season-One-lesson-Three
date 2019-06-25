# install and configuring JetBrains PyCharm 2019.1.2 x64 Start write code
print("Hello World")
num = 10
cond = num > 10
print("condition = ", cond)
 # upper lower
 upper = 10
 lower = 80
 # You can change the number for condition

 num = 80
 cond = num > upper and num < lower

 if cond:
     print("the number is between 10 and 100")
     print("anouther line of my code")
     # 4 space recommended
 else:
     print("ELSE")

 print(cond)

 # with input
upper = 10
lower = 80
num = input("Enter number : ")
num = int(num)
cond = num > upper and num < lower

if cond:
    print("the number is between 10 and 100")
    print("anouther line of my code")
    # 4 space recommended
else:
    print("ELSE")

    # new program if
if num > 10:
        print("number is greaterthan10")
else:
        if num > 0:
            print("number is greater than 0")
        else:
            print("lesser than zero")

# elif
if num > 10:
    print("number is greater than 10")
elif num > 0:
    print("number is greater than 0")
elif num > -10:
    print("number is greater than -10")
else:
    print("lesser than -10")
# input final
text = input("say something")
print(text)
if text.isnumeric():
text_new = eval(text)
print(type(text))
print(type(text_new))
if text.isnumeric():
else:
    print(text, "is not numeric")

# press ctrl+q to use documentations
import urllib.request
urllib.request.urlopen()
# loops
i = 1
print(i)
i = i+ 1
print(i)
i = i+ 1
print(i)
i = i+ 1
print(i)
i = i+ 1
print(i)
 # while
 i = 0
 print(i)
 upper = 20
 while i < upper:
     i = i + 1
     print(i)
  # tasks
  start = 0
  upper = 1000000
  # metod 1
  sum_even = 0
  counter = start
  while counter <= upper:
      sum_even += counter
      counter = counter + 2
      print(sum_even)
   # metod 2
   sum_even = 0
   counter = start
   while counter <= upper:
       if counter % 2 == 0:
           sum_even += counter
           counter = counter +1
    print(sum_even)

    # metod 3
    vals = [10, 20, 32, 3445, 2342, 234234234]
    my_sum = 0
    i = 0
    while i < len(vals):
       print(vals[i])
       i += 1
 # print type
 print("hello", "world", "!", sep="-", end="\n\n")
print("hello", "world", "!", sep="   ", end="\n\n")
print("hello", "world", "!", sep="\t", end="\n\n")
# fact test
list = []
n = 100
fact = 1
i = 1
while i <= n:
    fact = fact * i
    i += 1
    print(fact)

   #--------------
   i = 0
   while i< 5:
       lst.append(2 * i)
       i + 1
       print(lst)

#---------
list = [2, 5, 3, 7, 8]
i = 0
while i < len(list):
    list[i] = list[i] * 2
    i += 1
    print(list)
#-----------
tup = (2, 3, 5, 7, 8)
out = []
i = 0
while i < len(tup):
    tmp = tup[i] * 2
    out.append(tmp)
    i += 1
    print(tup)
    print(out)
    







