---

marp: true
author: Christian Bueno
paginate: true
backgroundColor: #212529
# color: #e9ecef
style: |
    section.lead h1 {
        text-align: center
    }
    section.img--transparent img {
        background-color: transparent;
    }
    div.myslide {
        display: flex;
    }
    div.col {
        flex: 1;
    }
    section h1 {
        color: #468faf;
    }
    section {
        color: #BDDEE8;
    }
    
# header: 'chris@christianbueno.work'
# footer: 'wa.me/593990288710'

---
<!-- _class: lead -->
# Decoradores en Python

---
# ¿Qué es un Decorador?

- Un decorador es una función que toma otra función y extiende su comportamiento sin modificarla explícitamente.
- Son una forma poderosa y flexible para modificar la funcionalidad de las funciones y métodos.

---
# ¿Por qué usar Decoradores?

- **Reutilización de código**: Puedes aplicar la misma funcionalidad a múltiples funciones.
- **Separación de preocupaciones**: Puedes mantener la lógica de la función separada de aspectos transversales como la validación, registro, etc.

---

# Sintaxis de un Decorador

```python
def decorador(func):
    def wrapper(*args, **kwargs):
        # Aquí puedes añadir código antes de llamar a la función original
        result = func(*args, **kwargs)
        # Aquí puedes añadir código después de llamar a la función original
        return result
    return wrapper
```

---

# Aplicación de un Decorador

```python
@decorador
def mi_funcion():
    pass
```

- El símbolo `@` se usa para aplicar un decorador a una función.
- Equivale a `mi_funcion = decorador(mi_funcion)`.

---

# Ejemplo de Decorador: `succ`

```python
def succ(function):
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs) + 1
    return wrapper
```

- Este decorador toma una función y le añade 1 al resultado.

---

# Uso del Decorador `succ`

```python
@succ
def add(x, y):
    return x + y

print(add(1, 2))  # Output: 4
```

- Aquí, `add` es una función que suma dos números.
- Al aplicar el decorador `@succ`, el resultado de `add` se incrementa en 1.

---

# Explicación del Ejemplo

- La función `succ` toma `add` como argumento.
- `wrapper` llama a `add` con los mismos argumentos y añade 1 al resultado.
- `add(1, 2)` originalmente devuelve 3, pero con el decorador `@succ`, devuelve 4.

---

# Beneficios de los Decoradores

- **Modularidad**: Puedes añadir funcionalidad a las funciones sin modificar su código.
- **Reusabilidad**: El mismo decorador puede aplicarse a múltiples funciones.

---

# Conclusión

- Los decoradores son una herramienta poderosa en Python para extender la funcionalidad de las funciones.
- Pueden hacer tu código más limpio y modular.

---

# Preguntas

- ¿Tienes alguna pregunta sobre decoradores en Python?

---

# Agradecimiento

- Gracias por tu atención.

---
# Contactos
<!-- _class: img--transparent -->
<div class="myslide">
<div class="col">

![w:64](https://api.iconify.design/mdi:linkedin.svg?color=%23ffffff)
linkedin.com/in/christianbueno1

![w:64 ](https://api.iconify.design/material-symbols:mail-outline.svg?color=%23ffffff)
chris@christianbueno.work

![w:64](https://api.iconify.design/mdi:instagram.svg?color=%23ffffff)
@christianbueno.1
</div>
<div class="col">

![w:64](https://api.iconify.design/ic:baseline-whatsapp.svg?color=%23ffffff)
wa.me/593990288710

![w:64](https://api.iconify.design/mdi:github.svg?color=%23ffffff)
github.com/christianbueno1

![w:64](https://api.iconify.design/tabler:world-www.svg?color=%23ffffff)
christianbueno.work/
</div>
</div>