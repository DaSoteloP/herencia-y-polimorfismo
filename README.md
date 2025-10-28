# Ejemplo de Herencia y Polimorfismo en Python 🐾

Este proyecto ejemplifica los conceptos de **herencia** y **polimorfismo** utilizando una jerarquía de clases que representan diferentes tipos de animales.

### Herencia
Permite crear nuevas clases basadas en una clase existente.  


### Polimorfismo
Permite que los objetos de diferentes clases respondan de manera distinta al mismo método.  


## Estructura de Clases

- **`Animal`**
  - Clase base.
  - Atributos: `especie`, `edad`.
  - Métodos:
    - `hablar()` y `moverse()` → definidos pero sin implementación (se sobrescriben en las subclases).
    - `describeme()` → imprime el tipo de animal.

- **`perro` y `gato`**
  - Heredan de `Animal`.
  - Atributo adicional: `dueño`.
  - Métodos sobrescritos:
    - `hablar()`, `moverse()`, `casa()`.

- **`Vaca`**
  - Hereda de `Animal`.
  - Sobrescribe `hablar()` y `moverse()`.

- **`abeja`**
  - Hereda de `Animal`.
  - Sobrescribe `hablar()`, `moverse()` y agrega `picar()`.

- **`Pez`**
  - Hereda de `Animal`.
  - Sobrescribe `hablar()` y `moverse()`.

Ejemplo de Uso

```python
mi_perro = perro('mamífero', 10, 'Javi')
mi_vaca = Vaca('mamífero', 6)
esa_abeja = abeja('insecto', 1)
gatito = gato('mamífero', 4, 'Martha')

mi_perro.describeme()  # Soy un animal del tipo perro
mi_perro.hablar()      # guau
mi_vaca.hablar()       # moo
esa_abeja.picar()      # atacar
gatito.casa()          # vivo con mi dueñ@: Martha
