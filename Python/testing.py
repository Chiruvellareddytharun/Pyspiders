# s1={1,2,3,4,5,10,100}
# s2={10,20,30,40,50,100,4}
# s3={100,200,300,400,500,1,4}
# print(s1)
# s1.update(s2)
# print(s1)
# print(s1)
# s1.intersection_update(s2)
# print(s1)
# res=s1.difference(s2)
# print(res)
# print(s1)                         
# s1.difference_update(s2)
# print(s1)  
# res=s1.symmetric_difference(s2) 
# print(res)  
# print(s1)
# s1.symmetric_difference_update(s2)
# print(s1)
# s1={1,2,3,4,5}
# s2={3,5}
# s3={3,100}  
# # print(s2.issubset(s1))
# # print(s3.issubset(s1))    
# print(s1.issuperset(s2))
# print(s1.issuperset(s3)) 
# s1={1,2,3,4,5}
# s2={10,20,30,40}
# s3={100,200,300,3}
# print(s1.isdisjoint(s2))              #
# print(s1.isdisjoint(s3)) 
# n=int(input("n: "))
# s1={int(input(f"val {x}: "))   for x in range(1,n+1)}
# print(s1) 
# d1={1:10,2:20,3:30}
# c1=d1.setdefault(1,200)
# c2=d1.setdefault(4,40)
# print(c1,c2)
# print(d1) 
# d1={1:10,2:20,3:30}
# c = d1.get(3)
# print(c)
# c1 = d1.get(100,"key does not exist")
# print(c1) 
# d1={1:10,2:20,3:30}
# d1={}.fromkeys(d1)
# print(d1)
# d2={}.fromkeys('abcd')  
# print(d2)  
# l1=[1,2,3,4,2]
# print(l1)
# l1.remove(2)
# print(l1)
# l1=[1,2,3,4,2,4,3,8]
# l2=l1.index(4,4,7)
# print(l2)
# l3=l1.pop(l2)
# print(l3)
# print(l1)
# l1=[y  for x in range(1,4)  for y in range(1,4)]
# print(l1)
# a=10
# b=5
# a=a^b
# b=a^b
# a=a^b
# print(a)
s="ababababa"
print(s.rsplit('b',1))
print(s.rsplit('b',2))
l=["hello","hi"]
print(":".join(l))