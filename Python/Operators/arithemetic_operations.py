       #addition(+)
'''int     + int     --> int 
   int     + float   --> float
   int     + complex --> complex
   float   + complex --> complex   
   complex + complex --> complex    
   int     + string  --> type error
   float   + string  --> type error
   complex + string  --> type error
   string  + string  --> string    '''
'''a = 1+4j
   b ="lucky"
   print(a+b)
   TypeError: unsupported operand type(s) for +: 'complex' and 'str' '''

       #subraction(-)
'''int     - int     --> int
   int     - float   --> float
   int     - complex --> complex
   float   - complex --> complex
   complex - complex --> complex
   if any operand is string -> type error'''
'''a = 7
b =3.5
print(a-b)'''

       #multiplication(*)
'''int     * int     --> int
   int     * float   --> float
   int     * complex --> complex
   float   * complex --> complex
   complex * complex --> complex
   int     * string  --> string
   float   * string  --> type error
   complex * string  --> type error
   string  * string  --> type error '''
# (*) can act as multiplication and str repetition
'''a = 7
b = "lucky"
print(a*b)'''

       #division(/)
'''int     / int     --> float
   int     / float   --> float
   if any operand is complex --> complex 
   if any operand is string  --> type error'''
'''a = 6.8
b = 4+8j
print(a/b)'''

       #modulus(%)
'''int     % int     --> int
   int     % float   --> float
   if any operand is complex or string  --> type error'''
'''a = 3+5j
b = "lucky"
print(a%b)
TypeError: unsupported operand type(s) for %: 'complex' and 'str'''

       #exponentiation(**)
'''int     ** int      --> int 
   int     ** float    --> float/int
   int     ** complex  --> complex
   float   ** complex  --> complex
   complex ** complex  --> complex
   if any operand is string --> type error'''
'''a = 5.9
b = 7
print(a**b)'''

       #floor division(//)
'''int     //  int   --> int
   int     //  float --> float
   if any operand is complex or string --> type error'''
'''a=5.9
b="lucky"
print(a//b)
TypeError: unsupported operand type(s) for //: 'float' and 'str' '''
       