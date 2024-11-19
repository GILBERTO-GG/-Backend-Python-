# 🛒 Ecommerce Django Project

## 📝 Descripción General
Este proyecto es una aplicación de Ecommerce rica en funcionalidades, construida con **Django**. Proporciona herramientas para gestionar productos físicos y digitales, incluyendo la creación, edición, eliminación y visualización de artículos. Está diseñado con escalabilidad y modularidad en mente, siendo una base sólida para futuros desarrollos e integraciones.

---

## 🚀 Características

### 🛍️ Gestión de Productos
- **Operaciones CRUD:** Crear, Leer, Actualizar y Eliminar productos.
- **Soporte para productos digitales y físicos:** Tipos de productos flexibles con campos compartidos y únicos.
- **Campos personalizables:** 
  - Título
  - Descripción
  - Precio
  - Información del vendedor
  - Color
  - Dimensiones
- **Gestión de Slugs:** Genera slugs únicos automáticamente para URLs amigables con SEO.

### 🔑 Autenticación de Usuarios
- Protección de vistas sensibles con decoradores `login_required` y mixins.
- Vistas personalizadas para que los usuarios autenticados gestionen sus productos.

### 🔍 Búsqueda y Filtrado
- Funcionalidad de búsqueda avanzada utilizando el ORM de Django y consultas con `Q` para múltiples campos.

### 🏗️ Estructura Modular
- `products`: Funcionalidades principales de productos.
- `MyEcommerceApp`: Utilidades generales del Ecommerce.
- `api`: Endpoints REST API para integración.

---

## 🛠️ Tecnologías y Dependencias
- **Django 4.1.4:** Framework principal.
- **Django REST Framework:** Desarrollo de APIs.
- **SQLite:** Base de datos predeterminada, adaptable a PostgreSQL.
- **Herramientas de Calidad de Código:** Flake8, Isort, Black.

---

## 📦 Instalación

1. Clona el repositorio:
    ```bash
    git clone <repository-url>
    ```

2. Navega al directorio del proyecto:
    ```bash
    cd Ecommerce
    ```

3. Crea un entorno virtual y actívalo:
    ```bash
    python -m venv env
    source env/bin/activate  # En Windows: env\Scripts\activate
    ```

4. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

5. Aplica las migraciones:
    ```bash
    python manage.py migrate
    ```

6. Inicia el servidor de desarrollo:
    ```bash
    python manage.py runserver
    ```


---

## 💡 Mejoras Futuras
- Añadir registro y gestión de perfiles de usuario.
- Implementar pasarelas de pago (e.g., Stripe, PayPal).
- Enriquecer el frontend con frameworks modernos de JavaScript.
- Soporte para subir imágenes y mejorar las listas de productos.

---

## 📜 Licencia
Este proyecto está licenciado bajo la licencia **MIT**. Consulta el archivo `LICENSE` para más detalles.

---

© 2024 - Proyecto Ecommerce con Django

