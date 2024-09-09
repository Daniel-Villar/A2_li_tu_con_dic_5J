print("Ejemplo de tuplas")
canciones=("Te amo","Si tu me quisieras"," Amor eterno")
print(canciones)
y = list(canciones)#crea una vaiable para cambiar la tupla canciones a lista/list es una funcion que cambia la tupla a lista
print(y)
y[1] = "cry for me"#Agrega un elemento a la lista(remplazo/cambio la unidad 1)
x = tuple(y)#cambia la lista a tupla 
print(x)