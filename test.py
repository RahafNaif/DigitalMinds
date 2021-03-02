import datetime

print("Hello world")
number = 1.0
print(type(number))
x = 2
r = x * 3
print(r)
# name = input("your name:")
# print (name)
#year = int(input("the year :"))
#month = int(input("the month:"))
#day = int(input("the day:"))
#today_date = datetime.datetime.now()
#DateOfBir = datetime.datetime(year,month,day)
#age = today_date - DateOfBir
#yourAge = age.days/365
#print("your age",yourAge)
my_list = ['rahaf','hano']
print(my_list)
student_d = {"name":"rahaf","age":20}
print(student_d['name'])
if number >0 :
   print ("positiv")
else:
   print("not positive")

#nu = int(input("enter number:"))
#if nu % 2==0 :
   print("even")
#else:
   print("odd")


price = float(input("enter the total :"))
#if price <1000 :
   discount = price * (5/100)
   finalTotal = price - discount

#elif price >=1000 and price <=5000 :
   discount = price * (10/100)
   finalTotal = price - discount
#else:
   discount = price * (15/100)
   finalTotal = price - discount

print("discount :",discount)
print("the total price",finalTotal)


PassGrade = ['A','B','C','D']
failed = 'F'

#grade = input("enter grade :")

#if grade.upper() in PassGrade or grade.lower() in PassGrade:
 #  print("congrg..")

#elif grade.upper()==failed or grade.lower()==failed:
   print("good lock next year")
#else :
   print("enter corcet grade")
   
loopList = [1,2,3,4]

for item in loopList:
    print(item)
for number in range(5):
   print(number)

numberr = 10
for item in range(11):
   multi = item * numberr
   print(item,"*",numberr,"=",multi)

dollarlist = []
riyallist = []

for item in range (1,101):
   dollarlist.append(item)

#convretedRate = float(input("enter converted rate:"))
while True:
 if convretedRate >0 and convretedRate <10:
    for item in dollarlist:
       riyalvalue = item * convretedRate
       riyallist.append(riyalvalue)
 else:
    convretedRate = float(input("enter >0and less<10"))
    # print("enter >0 and less <10")

#print(riyallist)

try:
   numb = input("enter number:")
   res = numb/2
   print(res)
except:
   print("there is error")
