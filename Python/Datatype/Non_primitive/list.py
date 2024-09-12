''' LIST - group of values seperated by ',' enclosed within "[]" is known as list
    syntax:
          list = [val 1,val2,..........,val n]     
          
          ex:
             l1=[10,2.7,3+4j,true,'lucky']
            # display the list
             print(l1)
            # verifying the type 
              print(l1,type(l1))
            # counting total elements
              print(len(l1)) '''




''' properties:
      1. list can be homogeneous or heterogeneous
      2. list support duplicate elements or values
      3. list is ordered collection
      4. list supports both positive and negative indexing
      5. list supports slicing    syntax:  list[start index, stop index, step index]
      6. list are mutable collection               
       
    ex:
      1. homogenious:
               l1=[1,3,6,99,346]
               l2=[3.4,5.3,6.7,5.1]
         heterogenious:
               l1=[10,2.6,true,'lucky',3+4j]

      2. l1=[10,23,54,10,45]
            print(l1)
     
      3. l1=[10,29,3+4j,'lucky']
            print(l1) 
            
      4. l1=[10,29,3+4j,'lucky']
            print(l1[i])
      
      5. l1=[10,20,30,40,50]
            print(l1[1:4:1])
                               
      6. l1=[10,20,30,40] 
         print(l1)
         l1[0]='lucky'
         print(l1)                   '''



'''looping list:
#using for loop in range
  for i in range(len(l1)):
     print(l1[i],end=" ")
#using for in iterables
  for i in l1:
     print(i ,end=" ")
  print()      
#using while loop
    i=0
    while i<len(l1):
    print(l1[i],end="  ")
    i+=1
#reverse iteration using for loop in range
    for i in range(len(l1)-1,-1,-1)
    print(l1[i],end=" ")                   '''



'''BUILT IN FUNCTIONS:
    - list has 11 built in methods
       syntax:
             list.method( ) 
    
      1.clear:     list.clear() -> none    
           ex:
              l1=[1,2,3,4]
              print(l1)     #[1,2,3,4]
              l1.clear()
              print(l1)     #[]      
      
      
      2.copy:       list.copy() -> list
            ex:
               l1=[1,2,3,4]
               print(l1)       #[1,2,3,4]
               l2=l1.copy()
               print(l2)       #[1,2,3,4]            
                    
                         
      3.count:       list.count(value) -> int
            ex:
               l1=[1,2,3,4,2,2]
               c1=l1.count(10)         #0
               c2=l1.count(2)          #3
               print(c1,c2)

               
      4.append:       list.append(object) -> none
            ex:
               l1=[1,2,3,4,2,2]
               l1.append(1000)
               l1.append([10,20])      
               l1.append('lucky')      
               l1.append()             #type error:list.append() takes exactly one argument
               print(l1)               #[1,2,3,4,2,2,1000,[10,20],'lucky']


      5.extend:       list.extend(iterable) -> none
            ex:
               l1=[1,2,3,4]
               l1.extend([10,20])
               l1.extend('lucky')
               print(l1)                #[1,2,3,4,10,20,'l','u','c','k','y']


      6.insert:        list.insert(index,object) -> none 
            ex: 
               l1=[1,2,3,4]
               l1.insert(1,1000)        #[1,1000,2,3,4] 
               l1.insert(-1,1000)       #[1,2,3,1000,4]
               l1.insert(100,1000)      #[1,2,3,4,1000]
               l1.insert(-100,1000)     #[1000,1,2,3,4]
               print(l1)


      7.pop:           list.pop(index) -> any
            ex: 
               l1=[1,2,3,4,1.4]
               c1=l1.pop(0)       #[2,3,4,1.4] 1                          
               c2=l1.pop()        #[1,2,3,4] 1.4
               l1.pop(100)        #index error = pop index is out of range
               print(l1,c1,c2)

      8.remove:        list.remove(value) -> none
            ex: 
               l1=[1,2,3,4,2]
               l1.remove(2)         #[1,3,4,2]
               l1.remove(100)       #value error
               print(l1) 


      9.index:         list.index(value,start,stop) -> int
            ex: 
               l1=[1,2,3,4,2,1,3,4,4] 
               i1=l1.index(2)             #1 
               i2=l1.index(3,5)           #6 
               i3=l1.index(2,5,8)         #value error:2 is not in the list             
                print(i1,i2,i3)


      10.reverse:       list.reverse() -> none 
            ex:
               l1=[1,2,3,4,5,'19',1.2]
               l1.reverse()
               print(l1)            #[1.2,'19',5,4,3,2,1]


      11.sort:           list.sort() -> none
            ex: 
               l1=[1,5.4,3,87]
               l1.sort()               #[1,3,5.4,87]
               l1.sort(reverse=true)
               print(l1)                #[87,5.4,3,1]


      12.concatination:
            l1=[1,2,3,4]
            l2=[10,20]
            l3=l1+l2 
            print(l3)               #[1,2,3,4,10,20]   


      13.repetation:
            l1=[1,2,3,4]
            l2=l1*3  
            print(l2)               #[1,2,3,4,1,2,3,4,1,2,3,4]             '''