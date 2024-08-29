         #grading system
'''a = int(input("enter the a:"))
b = int(input("enter the b:"))
c = int(input("enter the c:"))
z =((a+b+c)/300)*100
print(z)
if  a>=1 and a<100 and b>=1 and b<100 and c>=1 and c<100:
    if a>90:
        print("a grade")
    elif b>80:
        print("b grade")
    elif c>70:
        print("c grade")
    else:
        print("fail")
else:
    print("Invalid number") '''



           #loan eligibility
'''a = int(input("enter the a:"))

if a>=740 and a<=900:
    b = int(input("enter the b:"))
    if b>300000  and b<400000:
        print("u r eligible of loan 100000")
    elif  b>=400000 :
        print("u r eligible of loan of 200000")
    else: 
        print("u r not eligible of loan")     
else:
    print("u r not eligible")  '''      


    #election eligibility
'''gen = input("enter the gender \nmale\tfemale\tother\noption:").lower()
if gen in ['male','female','other']:
    age = float(input("enter the age:"))
    if gen in ['male','other']:
        if age>=18 and age<=65:
            print("u r eligible to vote")
        else:
            print("not eligible to vote")
    else:
        if age>=21 and age<=45: 
            print("u r eligible to vote")
        else:
            print("not eligible to vote")    
else:
    print("invalid gender")      ''' 

                    #(or)

'''gen = input("enter the gender\nmale\tfemale\tother\noption:")
if gen in ['male','female','other']:
   age = float(input("enter the age:"))
   name = input("name:")
   if((gen in ['male','other']) and (age in range(18,66))) or (gen == 'female' and (age in range(21,46))):
           print(f"{name} is eligible to vote")
   else:
           print(f"{name} is not eligible to vote")
else:
   print(f"{gen} is an invalid gender")   '''                                                                   


         #sample calculator
'''operator = input("enter the operation\n +\t-\t*\t/\noperation:")
if operator in ['+','-','*','/']:
    a = float(input("enter the a:"))
    b = float(input("enter the b:"))
    if operator =='+':
        print(a+b)
    elif operator =='-':
        print(a-b)
    elif operator =='*':
        print(a*b)
    else:
        print(a/b)            

else:
    print("invalid operator") '''



#Write a program that checks if a number is within the range of 10 to 50 (inclusive) and if it's divisible by 3, print "The number is within the range and divisible by 3".
'''a = int(input(" enter the a : "))
if  a>=10 and a<=50 :
    if a%3==0 :
        print("number is within the range and divisible by 3")
    else:
        print("number is  within the range and  not divisible by 3")

else:
    print("it is not in the range") '''


         #rainbow
'''color = input("enter the color: ")
rainbow =["violet","indigo","blue","green","yellow","orange","red"]
if color in rainbow :
    if color == "violet":
        print("violet is first color in rainbow")
    elif color == "indigo":
        print("indigo is second color in rainbow")    
    elif color == "blue":
        print("blue is thrid color in rainbow")
    elif color =="green":
        print("green is fourth color in rainbow")
    elif color =="yellow":
        print("yellow is fiveth color in rainbow")
    elif color =="orange":
        print("orange is sixth color in rainbow")
    else:
        print("red is seventh color in rainbow")                   
else:
    print("it is not a color in rainbow")     ''' 


     # greater of four numbers
'''a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))
d = int(input("d:"))
if(a>b):
    if(a>c):
        if(a>d):
            print(a)
        else:
            print(d)
    else:
        if(c>d):
            print(c)
        else:
            print(d)
else:
    if(b>c):
        if(b>d):
            print(b)
        else:
            print(d)
    else:
        if(c>d):
            print(c)
        else:
            print(d) '''



