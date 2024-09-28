'''MISULLENEOUS FUNCTION :
         - it is a process of giving the alias name to existing function.
         - need to give alias name by assigning the function address the another variable.
         - when a variable assign by the address of function type we can call that function

        Syntax:
                variable=functionname
              
        ex:         
            def function():
               print("i am a funcction")

            function()
            new=function
            print(new)
            print(type(new))
            new() 
'''