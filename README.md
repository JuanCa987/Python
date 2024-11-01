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

