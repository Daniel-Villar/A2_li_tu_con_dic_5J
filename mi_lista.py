print("Ejemplo de listas")
arcoiris=["verde", "Azul","Morado"]
print(arcoiris)
longitud=len(arcoiris)
print(longitud)
print("elementos que contiene la lista arcoiris",longitud)
print(f"elementos que contiene la lista arcoiris v2 {longitud}")
print ("accediendo a un elemento de la lista ")
print (arcoiris[1])#imprime un elemento de arcoiris (se indica el de la posicion numero 1)
print (f"elemento en la posicion 0 es {arcoiris[0]}")
print (f"El primer color del arcoiris es:",arcoiris[0])
print ("agregar a un elemento de la lista ")
arcoiris.append("rosa")#agrega un elemento a la lista de arcoiris
print(arcoiris)
print ("Listar los elementos de la lista ciclo for")
for villar in arcoiris:
    print(villar)