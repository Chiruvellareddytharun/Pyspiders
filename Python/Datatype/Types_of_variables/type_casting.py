 #integer
a = int(input("enter the value a: "))
print(a,type(a))
'''   input       output

      "100"        100
      "10.5"      value error
      "1+3j"      value error
      "don"       value error
        100        100
        10.5       10
        1+2j      type error'''
 
 #float
b = float(input("enter the value b: "))
print(b,type(b))
'''    input       output

       "100"        100.0
       "10.5"        10.5
       "1+2j"      value error
       "don"       value error
        100         100.0
        10.5        10.5
        1+2j      type error   '''

 #complex 
c = complex(input("enter the value c: "))
print(c,type(c))
'''    input        output

       "100"         (100+0j)
       "10.5"        (10.5+0j)
       "1+2j"         1+2j
       "don"          value error
        100           (100+0j) 
        10.5          (10.5+0j)
        (1+2j)        (1+2j)
          j             1j    '''

 #string
 #can connect any type of string
