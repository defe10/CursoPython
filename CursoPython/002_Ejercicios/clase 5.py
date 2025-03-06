"""lista = [1,2,3,4,5,6,7,8,9,]

for i in range (0,len(lista)):
    numero = lista[i]
    print (numero)

3.1"""

palabra_usuario = str (input("Ingrese una palabra: "))
lista_vocales = ("a","e","i", "o", "u")
vocales = {"a": 0,"e": 0,"i": 0,"o": 0,"u": 0}

for i in range (0,len(palabra_usuario)):
    caracter = palabra_usuario[i]

    if caracter in lista_vocales:
        vocales[caracter] = vocales[caracter] + 1

for vocal in lista_vocales:
    print(f"{vocal}: {vocales[vocal]}")
        
    
    

   
    
        

