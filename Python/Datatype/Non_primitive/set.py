'''SET - group of elements seperated by ',' and enclosed within '{ }' is called set.
        syntax:
               set={V1,V2,.......,Vn}
            ex:
               s1={10,3.5,'lucky',500,true}
               print(s1)                     #{true,3.5,10,500,'lucky'}
               print(type(s1))               # set 
               print(len(s1))                # 5             '''
            

'''    #PROPERTIES OF SET :
        1.set can be homogeneous or heterogeneous.
        2.set does not support duplicate elements or values.
        3.set are unordered collection.
        4.sets does not support indexing.
        5.set does not support slicing.
        6.sets are mutable collection.
        7.sets supports int,float,complex,string,boolean,tuple as its elements.
             #unhashable type : 'set','list','dictionary'.              '''


'''        #LOOPING OF SET :  
               - we can't use while loop and for loop range method.
               - we can only for i in iterable.
                 s1={10,3.5,true}
                 for i in s1:
                 print(i,end=" ")                #10  true   3.5      '''


''' BUILT IN FUNCTIONS : 
       1.clear :                set.clear( ) -> none
                ex:
                   s1={10,20,30,40}
                   print(s1)                #{40,10,20,30}
                   s1.clear()
                   print(s1)                #set( )
                   
        2.copy :                set.copy( ) -> set 
                ex: 
                   s1={10,20,30,40}
                   print(s1)                 #{40,10,20,30}
                   s2=s1.copy()
                   print(s2)                 #{40,10,20,30}
                
        3.add:                  set.add(value) -> none
                ex:
                   s1={10,20,30,40}
                   print(s1)
                   s1.add(100)                #{40,10,100,20,30}
                   s1.add(10)                 #it is a duplicate value
                   print(s1)
                                                
                                                                             
        4.pop:                   set.pop( ) -> any
                ex:
                   s1={10,20,30,40}
                   c1=s1.pop()          
                   print(s1,c1)                   #{10,20,30} 40
                   s2=set()                       #key error='pop from an empty set'
                                    
                                                     
        5.remove:                set.remove(value) -> none 
                ex:
                   s1={10,20,30,40}
                   s1.remove(20)                   #{40,10,30}
                   s1.remove(1000)                 #key error : 1000
                   print(s1)                     
                     
                       
        6.discard:               set.discard(value) -> none
                ex:
                   s1={10,20,30,40}
                   s1=discard(20)                  #{40,10,30}
                   s1=discard(1000)                #{40,10,30}
                   print(s1)
                

               s1={1,2,3,4,5,10,100}
               s2={10,20,30,40,50,100,4}
               s3={100,200,300,400,500,1,4}             
        7.union:                 set.union(*set) -> set
              ex:
                 res1=s1.union(s2)
                 print(res1)                       #{1,2,3,4,5,10,100,20,30,40,50}
                 res2=s1.union(s2,s3)
                 print(res2)                       #{1,2,3,4,5,10,100,20,30,40,50,200,300,400,500}


        8.update:                set.update(*set) -> none 
              ex:
                 print(s1)                       #{1, 2, 3, 4, 5, 100, 10}
                 s1.update(s2)
                 print(s1)                       #{1, 2, 3, 4, 5, 100, 40, 10, 50, 20, 30}


        9.intersection:          set.intersection(*set) -> set
              ex: 
                 res=s1.intersection(s2)
                 print(s2)                       #{10, 100, 4}


        10.intersection_update:              set.intersection_update(*set) -> none
              ex:
                 print(s1)                           #{1, 2, 3, 4, 5, 100, 10}
                 s1.intersection_update(s2)
                 print(s1)                           #{10, 100, 4}


        11.difference:                        set.difference(*set) -> set
              ex:
                 res=s1.difference(s2)
                 print(res)                          #{1, 2, 3, 5}


        12.difference_update:                 set.difference_update(*set) -> none 
              ex:
                 print(s1)                         #{1, 2, 3, 4, 5, 100, 10}
                 s1.difference_update(s2)
                 print(s1)                         #{1, 2, 3, 5}   


        13.symmetric_difference:              set.symmetric_difference(set) -> set
              ex:
                 res=s1.symmetric_difference(s2) 
                 print(res)                             #{1, 2, 3, 5, 20, 30, 40, 50}


        14.symmetric_difference_update:           set.symmetric_difference_update(set) -> none
              ex:
                 print(s1)                              #{1, 2, 3, 4, 5, 100, 10} 
                 s1.symmetric_difference_update(s2)
                 print(s1)                              #{1, 2, 3, 5, 20, 30, 40, 50}  


        15.issubset:                    set.issubject(set) -> bool
              ex: 
                 print(s2.issubset(s1))                 #true
                 print(s3.issubset(s1))                 #false


        16.issuperset:                   set.issuperset(set) -> bool
              ex: 
              print(s1.issuperset(s2))                    #true
              print(s1.issuperset(s3))                    #false


        17.isdisjoint:                    set.isdisjoint(set) -> bool 
              ex: 
                 s1={1,2,3,4,5}
                 s2={10,20,30,40}
                 s3={100,200,300,3}
                 print(s1.isdisjoint(s2))              #true
                 print(s1.isdisjoint(s3))              #false  
                '''


'''SET CONCATINATION & REPEATITION :
          S1={1,2,3,4}
          S2={10,20,30}
          S3=S1+S2
          print(s3)                                #type error
          s4=s1*3
          print(s4)                                #type error        '''


'''SET COMPREHENSION :
       Syntax:
              set={value    for loop     if condition}
         ex:
            s1={x  for x in range(1,11)}
            print(s1)                                #{1,2,3,4,5,6,7,8,9,10}

            n=int(input("n: "))                                            #n: 3
            s1={int(input(f"val {x}: "))   for x in range(1,n+1)}           val 1: 2                                                       
            print(s1)                                                       val 2: 4
                                                                            val 3: 7                                                          
                                                                            {2, 4, 7}  '''




