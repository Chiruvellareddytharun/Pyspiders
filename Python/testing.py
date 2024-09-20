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
n=int(input("n: "))
s1={int(input(f"val {x}: "))   for x in range(1,n+1)}
print(s1) 