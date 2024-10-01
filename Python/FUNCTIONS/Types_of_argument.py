'''TYPES OF ARGUMENTS :
       1.POSITIONAL ARGUMENT.
       2.DEFAULT ARGUMENT.
       3.KEYWORD ARGUMENT.
       4.ARBITARY VAIRABLE.
       5.ARBITARY KEYWORD.        

NOTE: ARGUMENT :  varaibles passed inside function defination are called argument.'''


'''1.POSITIONAL ARGUMENT :
      - in positional argument ,during function call the number of argument
        passed must be equal to no. of argument defined.

        ex:
           def fun(a,b):
             print(a,b)
           fun(10,20)                           #10 20 
           fun(10)                              #type error
           fun(10,20,30)                        #type error


   2.DEFAULT ARGUMENT :
      - during function defination on argument with default value will be defined.
      - during function passing values to this arguments and can be skipped.
      - if passed default values are overridden.

      ex:
         def fun(a,b=0):
            print(a,b)

         fun(10,20)                   # 10 20
         fun(10)                      # 10 0
         fun(10,20,30)                #type error:fun() takes from 1 to 2 positional arguments 
                                                  but 3 were given.   


   3.KEYWORD ARGUMENT :
      - during function call values are passed along with its key.

      ex:
         def fun(a,b,c):
            print(a,b,c)  

         fun(c=30,a=10,b=20)              #10 20 30
         fun(10,c=30,b=20)                #10 20 30
         fun(10,c=30,b=20,a=10)           #type error:got multiple values for a.
         fun(b=20,a=10,30)                #type error:positional argument follows keyword argument.


NOTE:  In positional default and keyword argument number of values passed must be equals to number of arguments defined.

   4.ARBITARY VARIABLE :
     - during function definition a variable with a '*' prefixed to it will be defined 
       this argument is called arbitary variable argument.
     - this variable can receive 0 to n no. of values and packs all the the values in the form of tuple.

     ex:
        def fun(*arg)
            print(arg,type(arg))

        fun(10,20,30,40)              #(10,20,30,40)   <class tuple>
        fun()                         #()  <class tuple>
        fun(10,3.5,'don')             #(10,3.5,'don')  <class tuple>     
'''