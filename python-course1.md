---
marp: true
author: Christian Bueno

---

# Logical Operators y Comparison Operators en Python
---

# Introducción

- En esta presentación, aprenderemos sobre los operadores lógicos y de comparación en Python.
- Estos operadores son esenciales para realizar comparaciones y tomar decisiones en nuestros programas.
- Dominar estos operadores te permitirá escribir código más eficiente y efectivo.

---
# Operadores de Comparación

- Los operadores de comparación se usan para comparar dos valores.
- Devuelven un valor booleano: True o False.

---
# Operadores de Comparación (Lista)

- `==` : Igual a
```    
5 == 5  # True
```
- `!=` : Diferente de
```
5 != 3  # True
```
- `>` : Mayor que

```
5 > 3  # True
```

---
Operadores de Comparación

- `<` : Menor que
```
3 < 5  # True
```
- `>=` : Mayor o igual que
```
5 >= 5  # True
```
- `<=` : Menor o igual que
```
3 <= 5  # True
```

---
# Ejemplos de Operadores de Comparación

```
a = 10
b = 20

print(a == b)  # False
print(a != b)  # True
print(a > b)   # False
print(a < b)   # True
print(a >= b)  # False
print(a <= b)  # True
```

---
# Operadores Lógicos

- Los operadores lógicos se usan para combinar declaraciones condicionales.
- Devuelven un valor booleano: True o False.

---
# Operadores Lógicos (Lista)

- `and` : Devuelve True si ambas declaraciones son verdaderas.
```
(5 > 3) and (8 > 5)  # True
```
- `or` : Devuelve True si una de las declaraciones es verdadera.
```
(5 > 3) or (8 < 5)  # True
```
- `not` : Invierte el resultado, devuelve False si el resultado es verdadero.
```
not(5 > 3)  # False
```

---
# Ejemplos de Operadores Lógicos
```
x = True
y = False

print(x and y)  # False
print(x or y)   # True
print(not x)    # False
```

---
# Combinando Operadores

- Puedes combinar operadores de comparación y lógicos para crear expresiones más complejas.

---
# Ejemplo de Combinación
```
a = 5
b = 10
c = 15

# Usando operadores de comparación y lógicos juntos
print((a < b) and (b < c))  # True
print((a > b) or (b < c))   # True
print(not (a == 5))         # False
```

---
# Ejercicio Práctico
- Escribe una función en Python que reciba dos números y devuelva True si ambos son positivos y mayores que 10, de lo contrario, False.
```
def check_numbers(x, y):
    return (x > 10) and (y > 10)

print(check_numbers(12, 15))  # True
print(check_numbers(5, 20))   # False
```

---
# Conclusión
- Resumen de los operadores lógicos y de comparación.
- Importancia de estos operadores en la programación.
- Invitación a practicar más y a experimentar con diferentes combinaciones.

---
# Preguntas
- Espacio para responder preguntas y aclarar dudas.

---
# Agradecimiento
- Gracias por su atención.
- chris@christianbueno.work
- @christianbueno.1
- wa.me/593990288710