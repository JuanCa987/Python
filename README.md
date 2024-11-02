# 🚀 Guía para Iniciar un Proyecto en Python

Bienvenido a esta guía para crear y estructurar un proyecto en Python de manera ordenada y profesional. Aquí encontrarás los pasos básicos, desde la configuración de un entorno virtual hasta la organización de archivos esenciales.

---

## 📦 Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:
- **Python 3.8 o superior**
- **pip** para la gestión de paquetes
- **virtualenv** (opcional, pero recomendado)

---

## 📂 Estructura de Carpetas Sugerida

Organizar los archivos es clave para un proyecto mantenible. Aquí tienes una estructura inicial:

```plaintext
mi_proyecto/
├── src/
│   └── main.py
├── tests/
│   └── test_main.py
├── README.md
├── requirements.txt
└── .gitignore
```

- **src/**: Código fuente principal.
- **tests/**: Pruebas unitarias.
- **README.md**: Descripción del proyecto y guía de uso.
- **requirements.txt**: Lista de dependencias.
- **.gitignore**: Archivos que no se deben incluir en Git.

---

## 🌐 Crear y Activar un Entorno Virtual

Un entorno virtual aísla las dependencias de tu proyecto:

1. **Crear el entorno virtual**  
   Ejecuta el siguiente comando para crear el entorno virtual:

   ```bash
   python -m venv venv
   ```

2. **Activar el entorno virtual**  
   - En **Windows**:

     ```bash
     .\venv\Scripts\activate
     ```
   - En **macOS/Linux**:

     ```bash
     source venv/bin/activate
     ```

   Para desactivar el entorno virtual, usa:

   ```bash
   deactivate
   ```

---

## 📥 Instalar Dependencias

Para instalar dependencias desde un archivo `requirements.txt`, usa:

```bash
pip install -r requirements.txt
```

Para añadir nuevas dependencias, instala cada paquete y luego actualiza `requirements.txt`:

```bash
pip freeze > requirements.txt
```

---

## 📄 Configuración de Archivos Esenciales

1. **README.md**  
   Este archivo describe el proyecto, sus funcionalidades, y cómo usarlo.

2. **.gitignore**  
   Especifica los archivos y carpetas a ignorar en el control de versiones. Ejemplo de contenido:

   ```
   venv/
   __pycache__/
   *.pyc
   ```

3. **requirements.txt**  
   Lista de dependencias del proyecto generada con `pip freeze > requirements.txt`.

---

## 📝 Escribe el Código Principal

Crea un archivo `main.py` en la carpeta `src/` con el siguiente código:

```python
# src/main.py

def main():
    print("¡Hola, mundo!")

if __name__ == "__main__":
    main()
```

---

## ▶️ Ejecutar el Proyecto

Para ejecutar el archivo principal, asegúrate de activar el entorno virtual y ejecuta:

```bash
python src/main.py
```

---

## ➕ Crear Pruebas Unitarias (Opcional)

En la carpeta `tests/`, añade pruebas unitarias para verificar que el código funcione correctamente. Por ejemplo:

```python
# tests/test_main.py

from src.main import main

def test_main():
    assert main() is None  # Modifica según tu código
```

Ejecuta las pruebas con `pytest` (si tienes pytest instalado):

```bash
pytest
```

---

## 🚀 Próximos Pasos

1. **Desarrolla funcionalidades adicionales**: Expande el archivo `main.py` o crea nuevos módulos en `src/`.
2. **Documentación**: Mejora este archivo README con detalles sobre las funcionalidades.
3. **Control de versiones**: Usa Git para gestionar versiones y colabora fácilmente.

---
```
Con estos pasos básicos, tu proyecto Python tendrá una estructura profesional y será fácil de escalar y mantener. ¡Disfruta programando! 🚀🐍
 ```

**[!NOTE]**  
>set: es una coleccion de elementos que no pueden repetirse, se aprendio sobre set en el curso de python basico

>[!TIP]
>diccionario: es un tipo de dato que almacena pares clave-valor, se aprendio sobre diccionarios en el curso de python basico

## 🧱 Programación Orientada a Objetos (POO) en Python

La Programación Orientada a Objetos (POO) es un paradigma de programación que permite estructurar el código en "objetos". Cada objeto representa una entidad con características (atributos) y comportamientos (métodos). La POO en Python nos ayuda a escribir código más organizado, modular y fácil de mantener.

### Conceptos Básicos de POO

1. **Clase:** Es el molde o estructura que define las propiedades y comportamientos que tendrán los objetos. En Python, una clase se define con la palabra clave `class`.

2. **Objeto:** Es una instancia de una clase. Cada objeto creado a partir de una clase tendrá los mismos atributos y métodos, pero sus valores pueden variar.

3. **Atributos:** Son las propiedades o datos que se almacenan en cada objeto. Definen el estado de un objeto.

4. **Métodos:** Son las funciones definidas dentro de una clase, que permiten realizar acciones o modificar el estado de un objeto.

5. **Encapsulamiento:** Es la práctica de ocultar los detalles internos de los objetos, permitiendo que solo se acceda a ellos a través de métodos públicos.

6. **Herencia:** Permite crear nuevas clases basadas en clases existentes, reutilizando y extendiendo sus funcionalidades.

7. **Polimorfismo:** Permite utilizar métodos en diferentes clases con el mismo nombre pero con comportamientos específicos.

### Ejemplo Básico de POO en Python

A continuación, se muestra un ejemplo básico de cómo implementar una clase en Python:

```python
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo de instancia
        self.edad = edad

    def hablar(self):
        print("Este animal hace un sonido.")

# Herencia: La clase Perro hereda de la clase Animal
class Perro(Animal):
    def hablar(self):
        print("Guau! Guau!")  # Polimorfismo: redefinimos el método hablar

# Crear una instancia de la clase Perro
mi_perro = Perro("Fido", 3)
print(f"Mi perro se llama {mi_perro.nombre} y tiene {mi_perro.edad} años.")
mi_perro.hablar()  # Llamada al método polimórfico
