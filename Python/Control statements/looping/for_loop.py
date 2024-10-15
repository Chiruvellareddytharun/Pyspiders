#multiplication
'''n = int(input("n:"))
for i in range(1,11):
    print(f"{n}*{i}={n*i}")'''

     #break is using printing numbers
'''for i in range(1,11):
    if i==4:
        break
    print(i)   '''
        
# continue is using  printing the numbers
'''for i in range(1,11):
    if i==5 or i==8:
        continue
    print(i)               '''


#write a prgm to print odd numbers 1 to n
'''n = int(input("n:"))
for i in range(1,n+1):
    if i%2==0:
        pass
    else:
        print(i)   '''

# write a prgm multiples of 5
'''n=int(input("n:"))
for i in range(1,n+1):
    if i%5==0:
        print(i, end=" ")    '''    

#write a prgm to find sum of 1 to n integers
'''n= int(input("n:"))
result = 0
for i in range(1,n+1):
    result+=i
print(result)    '''       


#write a prgm product of 1 to n integers (OR) factorial prgm
'''n = int(input("n:"))
res= 1
for i in range(1,n+1):
    res*=i
print(res)    '''

#write a prgm to find the sum of eve numbers from 1 to n
'''n = int(input("n:"))
res=0
for i in range(1,n+1):
    if i%2==0:
        res+=i
print(res)  '''


#write a prgm to find odd numbers upto n without using %
'''n=int(input("n:"))
res=1
for i in range(1,n+1,2):
    print(i)      '''

#write a prgm to print even numbers two times odd numbers two times upto n
'''n = int(input("n:"))
for i in range(1,n+1):
    if i%2==0:
       for j in range(2):
        print(i,end=" ")
        
    else:
       for k in range(3):    
        print(i,end=" ")    '''   

#print * using for loop
'''n=int(input("n:"))
for i in range(1,n+1):
    print('*') '''



