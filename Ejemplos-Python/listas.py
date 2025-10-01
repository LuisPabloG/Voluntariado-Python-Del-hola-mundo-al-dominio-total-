frutas = ["manzana", "banana", "pera", "naranja",]
frutas.append("cereza")
print(frutas) # ['manzana', 'banana', 'cereza']


colores = ["rojo", "verde"]
colores.insert(0, "azul")
print(colores) # ['rojo', 'azul', 'verde']

numeros = [1, 2, 3, 2]
numeros.remove(3)
print(numeros) # [1, 3, 2]

letras = ["a", "b", "c"]
elemento_borrado = letras.pop(1)
print(letras) # ['a', 'c']
print(elemento_borrado) # b


valores = [3, 1, 4, 1, 5]
valores.sort()
print(valores) # [1, 1, 3, 4, 5]


items = ["uno", "dos", "tres"]
items.reverse()
print(items) # ['tres', 'dos', 'uno']