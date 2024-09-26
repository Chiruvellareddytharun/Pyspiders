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


       14.casefold :               string.casefold( )
              ex:
                 print("ADD".lower())                        #add
                 print("ADD".casefold())                     #add


       15.title :                  string.title( )
              ex:
                 print("tharun is a waste guy".title())          #Tharun Is A Waste Guy.


       16.istitle :                string.istitle( ) -> bool
              ex:
                 print("tharun is a alone boy".istitle())        #true


       17.capitalize :             string.capitalize( )
              ex:
                 print("tharun is a alone boy".capitalize())     #Tharun is a alone boy


       18.isalpha :                string.isalpha( ) -> bool
              ex: 
                 print("12aa".isalpha())                        #false
                 print("aa".isalpha())                          #true


       19.isalnum :                string.isalnum( ) -> bool
              ex: 
                 print("123abc".isalnum())                      #true
                 print("abc".isalnum())                         #true
                 print("12@aab".isalnum())                      #false 


       20.isdecimal :             string.isdecimal( ) -> bool
              ex:
                 number='123'


       21.isdigit :               string.isdigt( ) -> bool
              ex:
                 print("is digit with number",num.isdigit())                    #true
                 print("is digit with fraction",fraction.isdigit())             #false
                 print("is digit with superscript",superscript.isdigit())       #true
                 print("is digit with string",string.isdigit())                 #false


       22.isnumeric :             string.isnumeric( ) -> bool
              ex:
                 print("is numeric with number",num.isnumeric())                   #true
                 print("is numeric with fraction",fraction.isnumeric())            #true
                 print("is numeric with superscript",superscript.isnumeric())      #true
                 print("is numeric with string",string.isnumeric())                #false


       23.isspace :               string.isspace( ) -> bool
              ex:
                 print("  ".isspace())                       #true
                 print(" a".isspace())                       #false
                 print("".isspace())                         #false


       24.strip :                 string.strip( )
           - remove space from first & last of string.
              ex:
                 print("  abc abc  ".strip())                     #abc abc  
                 print("abc  abc  abc   ".strip())                #abc abc abc
                 print("  abc abc abc".strip())                   #abc abc abc


       25.lstrip :  
              ex:
                 print("  abc abc  ".lstrip())                    #abc abc  
                 print("abc  abc  abc   ".lstrip())               #abc abc abc
                 print("  abc abc abc".lstrip())                  #abc abc abc


       26.rstrip :
              ex:
                 print("  abc abc  ".rstrip())                    #    abc abc        
                 print("abc  abc  abc   ".rstrip())               #abc abc abc
                 print("  abc abc abc".rstrip())                  #   abc abc abc


       27.count :
          - no. of occurance of a char in string.
              ex:
                 s = "hello abc"
                 print(s.count('l'))                               #2
                 print(s.count('z'))                               #0


       28.zfill :
           - to fill zeros with string.
              ex:
                 print(len(s))                            #9
                 print(s.zfill(20))                       #00000000000hello abc


       29.ljust :
              ex:
                 s="hello"
                 print(s.ljust(10,'_'))                   #hello_ _ _ _ _


       30.rjust :
              ex:
                 s="hello"
                 print(s.rjust(10,'_'))                    #_ _ _ _ _hello 
                 print(s.rjust(5,'_'))                     #  hello 
                 print(s.rjust(11))                        #                hello


       31.center :
              ex:
                 print(s.center(11,'_'))                  #_ _ _hello_ _ _
                 print(s.center(11))                      #      hello   


       32.isascii :              string.isascii( ) -> bool
           - checks whether all char in string have ascii value.
             ex:
                s="hello"
                print(s.isascii())                        #true
                s1="hello "
                print(s1.isascii())                       #false


       33.isprintable :             string.isprintable( ) -> bool
              ex:
                 print("hello".isprintable())             #true
                 print("hello \n \t".isprintable())       #false


       34.isidentifiers :           string.isidentifier( ) -> bool     
              ex: 
                 print('abc1'.isidentifier())                   #true
                 print('123abc'.isidentifier())                 #false
                 print('ab@c'.isidentifier())                   #false
                 print('abc_bbb'.isidentifier())                #true


       35.iskeyword :              string.iskeyword( ) -> bool
              ex:
                 import keyword
                 print("keyword .......")
                 print(keyword.iskeyword('def'))                #true 
                 print(keyword.iskeyword('abc'))                #false          
 
       
       36.swapcase :
              ex:
                 print("hello".swapcase())                      #hello          
'''