'''TUPLE - group of elements seperated by ',' and enclosed between pair of "( )"
        syntax:
               var=(V1,V2, .........Vn) (OR) var=V1,V2,........Vn
         - storing a single value in tuple. we should give a ',' like this var=(val1,)
         - ( ) -> empty tuple  [default value]   


    note :
         - bool( ) is used to check whether the value stored in a variable is default or non-default.  '''


''' #PROPERTIES:
        1.tuple supports homogeneous and heterogeneous collection.
        2.tuple is an ordered collection. 
        3.tuple supports the positive  and negative indexing.
        4.tuple supports duplicate elements or values.
        5.tuples are immutable collection.
        6.tuple supports slicing.

        ex:
          5.t1=(10,34,54,73)
            t1[2]="rose"
            print(t1)                    #type error

          6.t1(10,20,30,40,50)
            print(t1[1:4])             #(20,30,40)   '''


''' #BUILT-IN-FUNCTIONS :

       1.COUNT:         count( ) -> none
              - gives the no. of occurence of the element
              ex:
                 t1=(10,20,10,10)
                 c=t1.count(10)
                 print(c)                               # 3

        2.INDEX:         index(value,start,stop) -> int
              ex:
                 t1=(10,20,30)
                 c = t1.index(10)
                 print(c)                               # 0    '''


''' #TUPLE CONCATINATION &REPETATION :
          t1=(1,2,3,4)
          t2=(10,20)
          t3=t1+t2
          print(t3)                         #{1,2,3,4,10,20} 
          t4=t1*2
          print(t4)                         #{1,2,3,4,1,2,3,4}          '''


''' #TUPLE COMPREHENSION :
            - in python tuople comprehension is not possible. if u try to archive python 
              returns generate object and the expression is called generator expression.
           
           ex: 
              t1=(x  for i in range(1,6))
              print(t1)                           #<generator object<genexpr> at0x00001090>     '''


'''FETCHING OF ELEMENTS IN THE TUPLE :
        - USING FOR LOOP IN RANGE:
          l1=(10,20,30,40,50)
          for i in range(len(l1)):
              print(l1[i],end=" ")           #10 20 30 40 50


        - USING FOR LOOP IN ITERABLE:
          L1=(10,20,30,40,50)
          for i in l1:
              print(i,end=" ")               #10 20 30 40 50


        - USING WHILE LOOP:
          l1=(10,20,30,40,50)
          i=0
          while i<len(l1):
               print(l1[i] ,end=" ")
          i+=1                              #10  20 30 40 50                
        '''