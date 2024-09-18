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
                '''