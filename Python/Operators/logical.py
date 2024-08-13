#there are three logical operations -and,or,not
#these operators returns boolean values

'''        AND                     OR                           NOT
      C1    C2     R           C1      C2      R           C      R

      F     F      F           F       F       F           F      T
      F     T      F           F       T       T           T      F
      T     F      F           T       F       T
      T     T      T           T       T       T  '''

#Example
a,b,c=10,20,30
print(a==b and b==c)  #false
print(a==b or b==c)   #false
print(not a==c)      #true


#example
a,b,c=10,20,10
print(a==c and not a==b or not a*2==c-10 or not a<b and b+10==c)   #true

a,b,c=10,20,10
print(a!=c or not a**2==b*10 or not a>=c and not b*3==c)           #true

a,b,c=10,20,10
print(a==b and not b!=c or not a**4<=a/4 or not b<=3)              #true