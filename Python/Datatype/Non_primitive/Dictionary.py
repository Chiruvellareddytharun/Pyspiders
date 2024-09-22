'''DICTIONARIES - group of keys and values,seperated by ',' and enclosed with '{ }' is known as dictionaries.
         syntax:
                d={key1:values1,key2:value2,.......keyn:valuen}    '''


'''PROPERTIES :
        1.dictionary is a mutable collection.
        2.dictionary does not support indexing.
        3.dictionary does not support slicing.  
        4.dictionary is an ordered collection.
        5.dictionary supports nested values.
        6.values can be int,float,complex,string,list,tuple and dictionary.
        7.keys can be only integer,float,string,complex,boolean and tuple.
        8.keys can't be duplicate and values can be duplicate. 
        ex:
           
        '''


'''BUILT-IN-METHODS :
      1.KEYS :               dict.keys( )
          ex:
             d1={1:10,2:20,3:30}
             for i in d1:
             print(i,end=" ")                     # 1 2 3
             print( )
             res1=d1.keys( )
             print(res1)                          #dict_keys([1,2,3])
             for i in d1.keys():
             print(i,end=" ")                      # 1 2 3  
             print( ) 


       2.values :             dict.values( )
           ex:
              d1={1:10,2:20,3:30}
              res2=d1.values()
              print(res2)                           #dict_values([10,20,30])
              for i in d1.values():
              print(i, end=" ")
              print( )                               # 10 20 30


       3.items :                 dict.items( )
           ex: 
              d1={1:10,2:20,3:30}
              res3=d1.items()                     
              print(res3)                               #dict_items([(1,10),(2,20),(3,30)]) 
              for i in d1.items():
              print(i,end=" ")                          #(1,10),(2,20),(3,30) 


       4.copy :                   dict.copy( ) -> dict
           ex:
              print(d1)                                #{1:10,2:20,3:30}
              d2 = d1.copy( )                    
              print(d2)                                #{1:10,2:20,3:30}   


       5.clear :                  dict.clear( ) -> none 
           ex: 
              d1.clear()
              print(d1)             #{ }


       6.pop :                    dict.pop(key) -> any  
           ex: 
              c1=d1.pop(2)
              print(c1)             #20
              print(d1)             #{1:10,3:30}
              c2=d1.pop()           #type error
              d2={ }
              d2.pop(1)             #key error : 1


       7.pop_items :               dict.popitem( ) -> tuple
           ex:
              t1=d1.popitem()
              print(t1)                   #{3:30} 
              print(d1)                   #{1:10,2:20}
              d2={ }
              d2.popitem()                #{key error:'popitem(): dictionary is empty'}  


       8.update :                    dict.update(dict) -> none
           ex:
              d1.update({1:100,4:40})
              print(d1)                    #{1:100,2:20,3:30,4:40}


       9.setdefault :                   dict.setdefault(key:value) -> value 
           ex:
              c1=d1.setdefault(1,200)
              c2=d1.setdefault(4,40)
              print(c1,c2)                       #10 40
              print(d1)                          #{1: 10, 2: 20, 3: 30, 4: 40}


       10.get( ) :                     dict.get(key,default) -> any
           ex: 
              c = d1.get(1)
              print(c)                                #10
              c1 = d1.get(5,"key does not exist")
              print(c1)                               #key does not exist


       11.fromkeys( ):                  dict.fromkey(iterable,value) -> dict
           ex: 
              d1={}.fromkeys()
              print(d1)                      #{1: None, 2: None, 3: None}   
              d2={}.fromkeys('abcd')  
              print(d2)                      #{'a': None, 'b': None, 'c': None, 'd': None}    '''


'''DICTIONARY CONCATINATION & REPEATITION :
          d1 ={1:10,2:20,3:30}
          d2 ={4:500}
          d3=d1+d2                        #type error
          d4=d1*2                         #type error             '''  


'''DICT COMPREHENSION :                           dict={key:value   for loop     if condition}
     n =int(input("n: "))
     d1 = {x:x**2  for x in range(1,n+1)}
     print(d1)                            #n=2  {1;1,2:4}

     ZIP USING :
                first =['virat','sachin','vamsi','kapil']
                last =['kohil','tendulkar','krishna','dev']
                d1={x:y for x,y in zip(first,last)}
                print(d1)                         #{'virat':'kohli','sachin':'tendulkar','vamsi':'krishna','kapil':'dev'}    
 '''