''' USER-DEFINED-FUNCTION :
    syntax:
          def functionname(argument):
            #statement
        ex:
           #defining functions 'neethu' and 'tharun'
            def neethu():
               print("dancing")
            def tharun():
               print("singing")
            print("start")                                    #start
            neethu()        #function call                    #dancing   
            tharun()        #function call                    #singing
            print("end")                                      #end 

NOTE: WE CAN'T CALL FUNCTION BEFORE DEFINING THEM.                        '''


'''FIVE TYPES OF USER-DEFINED-FUNCTIONS :
   1.Function without return without argument.
   2.Function without return with argument.
   3.Function with return without argument.
   4.Function with return with argument.
   5.Recursion.

   ex:
      1.function without return without argument.

        def add_two_numbers():
            a=int(input("a:"))
            b=int(input("b:"))
            c=a+b                                                   o\p:
            print(c)                                                a:4
                                                                    b:3
        add_two_numbers()                                           7


      2.function without return with argument. 

        def add_two_numbers(a,b):        
            c=a+b                                                    o\p:      
            print(c)                                                 a:5
                                                                     b:6
        add_two_numbers(int(input("a:"))),int(input("b:"))           11
        add_two_numbers(10,20)                                       30


      3.function with return without argument.

        def numbers():
           a=int(input("a:"))
           b=int(input("b:"))
           c=a+b
           return c
                                                                    o\p:
        #val=numbers()                                                  a:5
        #print(val)                                                     b:3 
        print(numbers())                                                8


      4.function with return with argument.

        def numbers(a,b):
           return a+b                                            o\p:
        print(numbers(10,34))                                        44
        print(numbers(12.5,6.1))                                     18.6
        print(numbers("python",developers"))                         pythondevelopers
        print(numbers("python",1))                                   #error


        ex:write a function which accepts a parameter and returns a string if the given value is a even number
           or a odd number.

            def check_number(num):
                if num %2==0:
                  return "even"
                else:                                            o\p:
                  return "odd"                                       12
                                                                     even  
            num=int(input("num:"))                                   3 
            print(check_number(num))                                 odd


NOTE: we can write multiple values from a function with ',' seperation
      the function will return the values in the form of tuples. 

      ex:
         def check_numbers(n1,n2,n3):
             return n1,n2,n3
                                                               o\p:    
         print(check_numbers(10,20,30))                            (10,20,30)

      ex:
        1.write a program to write function which accept string as a parameter and return a list of values 
          if the length of a sting is even return list of even numbers from 1 to 50, if the length of a 
          string is odd return list of odd numbers from 51 to 100.

            def string_length(s1):
               if len(s1)%2==0:
                   return[n for n in range(1,51)    if n%2==0]
               else:
                   return[n for n in range(51,100)  if n%2!=0]

            s1=input("enter the string:")
            print(string_length(s1))                '''
