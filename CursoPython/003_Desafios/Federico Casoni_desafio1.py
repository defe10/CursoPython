
while True:
    num_min = 0
    num_max = 0
    num_usuario = int(input(f"Ingrese 2 números (de uno a la vez): "))
    
    
   
    if num_usuario < num_min:
        num_min = num_usuario
    elif num_usuario > num_max:
        num_max = num_usuario
    
    num_usuario2= int(input(f"Ingrese 1 números (de uno a la vez): "))

    if num_usuario2 < num_min:
        num_min = num_usuario
    elif num_usuario2 > num_max:
        num_max = num_usuario
    
    if num_usuario or num_usuario2 == "@":
        print (num_max, num_min)
  
        
    
    
   


    



