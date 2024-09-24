'''STRING - strings are combined values and enclosed with single qoutes(' ') (or)
            double quotes(" ") (or) triple quotes(''' ''').      '''


'''PROPERTIES :
       1.strings are immutable.
       2.strings supports both positive and negative indexing.
       3.string supports slicing.
       4.strings are ordered collection.
       5.strings supports duplicate values.
       6.strings supports both range and iterables.    
         
       ex:
            1.s="python"
              s[0] = 'a'                #type error :we cant update or add the value.it is immutable.


            2.s="python"
            print(s[4])                 # o
            print(s[-3])                # h


            3.s="python"
            print(s[:1000])              #python
            print(s[::-1])               #nohtyp


            4.s="python"
            print(s)                     #python 


            5.s="ssaa"
            print(s)                     #ssaa             '''

'''LOOPING OF STRING :
       - String supports both for loop in range and iterable methods.    
          #Range :
                  s="python"
                  for i in range(len(s)):
                  print(s[i] , end=" ")                       #python

                  for i in range(len(s)-1,-1,-1):
                  print(s[i] , end=" ")                       #nohtyp


          #iterable :
                  s="python"
                  for i in s:
                  print(i,end=" ")                            #python

                  for i in s[::-1]:
                  print(i,end=" ")                            #nohtyp                 '''


'''BUILT-IN METHODS :
       1.upper :                string.upper( ) -> string
              ex:
                 s1='lucky'
                 res=s1.upper()
                 print(res)                                #LUCKY


       2.isupper :              string.isupper( ) -> bool 
              ex:
                 print(s1.isupper())                      #false
                 print(res.isupper())                     #true 


       3.lower :                string.lower( ) -> string
              ex:
                 s1='LUCKY'
                 res=s1.lower()
                 print(res)                                #lucky


       4.islower :              string.islower( ) -> bool
              ex:
                 print(s1.islower())                       #false
                 print(res.islower())                      #true


       5.index :                 string.index(value,start,stop) -> int
              ex:
                 s='python'
                 res=s.index('o',1,5)
                 print(res)                                   #4


       6.find :                   string.find(value) -> int
              ex:
                 s='python'
                 res=s.find('s')
                 print(res)                                  #-1


       7.rfind :                 string.rfind(value) -> int
              ex:
                 s='abbbba'
                 print(s.rfind('a'))                         #5


       8.rindex :                 string.rindex(value) -> int
              ex:
                 s='abbbba'
                 print(s.rindex('a'))                        #5
                 print(s.rindex('z'))                        #value error


       9.split :                   string.split( )
              ex:
                 s='abababa'
                 print(s.split('b'))                         #['a','a','a','a']
                 print(s.split('b',2))                       #['a','a','aba']
                 s='hellohi!'
                 print(s.split())                            #['hello','hi!']


       10.rsplit :                string.rsplit( )
              ex:
                 s='abababa'
                 res=s.rsplit('b'10)                       #                                    

'''