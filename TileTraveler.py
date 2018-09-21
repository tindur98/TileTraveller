#Mér fannst léttara að gera verkefnið án function en það er vissulega flottari kóði að nota function
#Kóðinn með fucntion er mun skiljanlegri, kóðinn þar kemur ekki allur í klessu.
#Ég t.d gat alltaf kallað í skipunina direction í stað þess að þurfa að skrifa hana aftur og aftur.











# beginner = [1,1]


# while True:
#     #direction = input("Direction: ")
#     x = False
    
#     if beginner == [1,1]:
#         print("You can travel: (N)orth.")
#         direction = input("Direction: ")
#         direction = direction.lower()
#         direction_info = ["s","n","e","w"]
#         while True:
            
                
#             if direction in direction_info:
#                 if direction == "n":
#                     beginner = [1,2]
#                     break
                    
                    
#                 else:
#                     print ("Not a valid direction!")
#                     direction = input("Direction: ")
#                     direction = direction.lower()
            
            

#     if beginner == [1,2]:
#         print ("You can travel: (N)orth or (E)ast or (S)outh.")
#         direction = input("Direction: ")
#         direction = direction.lower()
#         direction_info = ["s","n","e","w"]
#         while True:
        
#             if direction in direction_info:
                
                
#                 if direction == "s":
#                     beginner = [1,1]
                
#                     break
#                 elif direction == "e":
#                     beginner = [2,2]
#                     break
#                 elif direction == "n":
#                     beginner = [1,3]
#                     break

                
#                 else:
#                     print ("Not a valid direction!")
#                     direction = input("Direction: ")
#                     direction = direction.lower()
                    

#     if beginner == [1,3]:
#         print ("You can travel: (E)ast or (S)outh.")
#         direction = input("Direction: ")
#         direction = direction.lower()
#         direction_info = ["s","n","e","w"]
#         while True:
            
        
#             if direction in direction_info:
#                 if direction == "e":
#                     beginner = [2,3]
                
#                     break
#                 elif direction == "s":
#                     beginner = [1,2]
#                     break
                
#                 else:
                    
#                     print ("Not a valid direction!")
#                     direction = input("Direction: ")
#                     direction = direction.lower()
                    


#     if beginner == [2,2]:
#         print ("You can travel: (S)outh or (W)est.")
#         direction = input("Direction: ")
#         direction = direction.lower()
#         direction_info = ["s","n","e","w"]
#         while True:
        
#             if direction in direction_info:
#                 if direction == "w":
#                     beginner = [1,2]
                
#                     break
#                 elif direction == "s":
#                     beginner = [2,1]
#                     break
                
#                 else:
#                     print ("Not a valid direction!")
#                     direction = input("Direction: ")
#                     direction = direction.lower()
                    

#     if beginner == [2,1]:
#         print ("You can travel: (N)orth.")
#         direction = input("Direction: ")
#         direction = direction.lower()
#         direction_info = ["s","n","e","w"]
#         while True:
        
#             if direction in direction_info:
#                 if direction == "n":
#                     beginner = [2,2]
                
#                     break
                
                
#                 else:
#                     print ("Not a valid direction!")
#                     direction = input("Direction: ")
#                     direction = direction.lower()
                   


#     if beginner == [2,3]:
#         print ("You can travel: (E)ast or (W)est.")
#         direction = input("Direction: ")
#         direction = direction.lower()
#         direction_info = ["s","n","e","w"]
#         while True:
        
#             if direction in direction_info:
#                 if direction == "w":
#                     beginner = [1,3]
                
#                     break
#                 elif direction == "e":
#                     beginner = [3,3]
#                     break
                
#                 else:
#                     print ("Not a valid direction!")
#                     direction = input("Direction: ")
#                     direction = direction.lower()
                   


#     if beginner == [3,3]:
#         print ("You can travel: (S)outh or (W)est.")
#         direction = input("Direction: ")
#         direction = direction.lower()
#         direction_info = ["s","n","e","w"]
#         while True:
        
#             if direction in direction_info:
#                 if direction == "w":
#                     beginner = [2,3]
                
#                     break
#                 elif direction == "s":
#                     beginner = [3,2]
#                     break
                
#                 else:
#                     print ("Not a valid direction!")
#                     direction = input("Direction: ")
#                     direction = direction.lower()
                    

    
#     if beginner == [3,2]:
#         print ("You can travel: (N)orth or (S)outh.")
#         direction = input("Direction: ")
#         direction = direction.lower()
#         x = False
#         direction_info = ["s","n","e","w"]
#         while True:
        
#             if direction in direction_info:
#                 if direction == "n":
#                     beginner = [3,3]
                
#                     break
#                 elif direction == "s":
#                     beginner = [3,1]
#                     print ("Victory!")
#                     x = True
#                     break
                
#                 else:
#                     print ("Not a valid direction!")
#                     direction = input("Direction: ")
#                     direction = direction.lower()
                    
#     if x == True:
#         break
                    


def direction():
    direction = str(input("Direction: "))
    direction = direction.lower()
    direction_info = ["s","n","e","w"]
    return direction, direction_info
    

def error(direction):
    print ("Not a valid direction!")
    direction = input("Direction: ")
    direction = direction.lower()
    return direction




def dalkur1(direction):
    
    while True:
        if beginner == [1,1]:
            print("You can travel: (N)orth.")
        
            direction, direction_info = direction()
        while True:
                
            if direction in direction_info:
                if direction == "n":
                    return [1,2]
                   
                    
                    
                else:
                    direction = error(direction)
                   

        
def dalkur2(direction):

    while True:
        if beginner == [1,2]:
            print("You can travel: (N)orth or (E)ast or (S)outh.")
        
            direction, direction_info = direction()

        while True:
                
            if direction in direction_info:
                if direction == "s":
                    return [1,1]
                elif direction == "e":
                    return [2,2]
                elif direction == "n":
                    return [1,3]
                    
                    
                else:
                    direction = error(direction)

def dalkur3(direction):

    while True:
        if beginner == [1,3]:
            print("You can travel: (E)ast or (S)outh.")
        
            direction, direction_info = direction()
        
        while True:
                
            if direction in direction_info:
                if direction == "s":
                    return [1,2]
                elif direction == "e":
                    return [2,3]       
                else:
                    direction = error(direction)



def dalkur4(direction):

    while True:
        if beginner == [2,2]:
            print("You can travel: (S)outh or (W)est.")
        
            direction, direction_info = direction()
        
        while True:
                
            if direction in direction_info:
                if direction == "w":
                    return [1,2]
                elif direction == "s":
                    return [2,1]    
                else:
                    direction = error(direction)
        


def dalkur5(direction):

    while True:
        if beginner == [2,1]:
            print("You can travel: (N)orth.")
        
            direction, direction_info = direction()
        
        while True:
                
            if direction in direction_info:
                if direction == "n":
                    return [2,2]   
                else:
                    direction = error(direction)




def dalkur6(direction):

    while True:
        if beginner == [2,3]:
            print("You can travel: (E)ast or (W)est.")
        
            direction, direction_info = direction()
         
        while True:
                
            if direction in direction_info:
                if direction == "w":
                    return [1,3]
                elif direction == "e":
                    return [3,3]    
                else:
                    direction = error(direction)


def dalkur7(direction):

    while True:
        if beginner == [3,3]:
            print("You can travel: (S)outh or (W)est.")
        
            direction, direction_info = direction()
        
        while True:
                
            if direction in direction_info:
                if direction == "w":
                    return [2,3]
                elif direction == "s":
                    return [3,2]    
                else:
                    direction = error(direction)


def victory(direction):
    if beginner == [3,1]:
        print("Victory!")
        x = True


def dalkur8(direction):

    while True:
        if beginner == [3,2]:
            print("You can travel: (N)orth or (S)outh.")
        
            direction, direction_info = direction()
          
        while True:
                
            if direction in direction_info:
                if direction == "n":
                    return [3,3]
                elif direction == "s":
                    return [3,1]    
                else:
                    direction = error(direction)


beginner = [1,1]
while True:
    x = False
    
    if beginner == [1,1]:
        beginner = dalkur1(direction)
    
    if beginner == [1,2]:
        beginner = dalkur2(direction)
    if beginner == [1,3]:
        beginner = dalkur3(direction)

    if beginner == [2,2]:
        beginner = dalkur4(direction)

    if beginner == [2,1]:
        beginner = dalkur5(direction)
    if beginner == [2,3]:
        beginner = dalkur6(direction)

    if beginner == [3,3]:
        beginner = dalkur7(direction)

    if beginner == [3,2]:
        beginner = dalkur8(direction)

    if beginner == [3,1]:
        beginner = victory(direction)
        break




















































    

    

                    

    
    

    

        
            
    
    


        
            
    
    

