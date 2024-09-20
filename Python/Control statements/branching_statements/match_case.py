           #calculator
'''a = int(input("a:"))
b = int(input("b:"))
opp =input("enter the operation:")
match opp:
    case '+':
        print(a+b) 
    case '-':
        print(a-b)
    case '*':
        print(a*b)
    case '/':
        print(a/b)      
    case _:
        print("not a operation") '''

    
                  # (or)
             #using while loop
'''while True:
    a = int(input("a:"))
    b = int(input("b:"))
    opp =input("enter the operation:")
    match opp:
        case '+':
           print(a+b) 
        case '-':
           print(a-b)
        case '*':
           print(a*b)
        case '/':
           print(a/b) 
        case 'cancle':
           break         
        case _:
           print("not a operation") '''

                 #pizza

'''val =input("enter the topin: ")
baseprice =100
match val:
      case "onion":
            print(baseprice+100)
      case "paneer":
            print(baseprice+100)
      case "cheese":
            print(baseprice+100)
      case _:
            print("no topin")    '''


                  