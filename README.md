<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ecommerce Django Project</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            background-color: #f4f4f9;
            color: #333;
            margin: 0;
            padding: 20px;
        }
        h1, h2, h3 {
            color: #2c3e50;
        }
        h1 {
            border-bottom: 2px solid #3498db;
            padding-bottom: 10px;
        }
        ul {
            padding-left: 20px;
        }
        code {
            background-color: #f8f8f8;
            padding: 2px 4px;
            font-size: 90%;
            color: #c0392b;
            border-radius: 4px;
        }
        pre {
            background: #f8f8f8;
            padding: 10px;
            border-left: 3px solid #3498db;
            overflow-x: auto;
        }
        .highlight {
            background: #ecf0f1;
            padding: 10px;
            border-radius: 5px;
        }
        .footer {
            margin-top: 30px;
            font-size: 0.9em;
            color: #7f8c8d;
        }
    </style>
</head>
<body>

    <h1>Ecommerce Django Project</h1>

    <h2>Descripción General</h2>
    <p>
        Este proyecto es una aplicación de Ecommerce rica en funcionalidades, construida con Django. Proporciona herramientas 
        para gestionar productos físicos y digitales, incluyendo la creación, edición, eliminación y visualización de artículos. 
        Está diseñado con escalabilidad y modularidad en mente, siendo una base sólida para futuros desarrollos e integraciones.
    </p>

    <h2>Características</h2>
    <h3>Gestión de Productos</h3>
    <ul>
        <li><strong>Operaciones CRUD:</strong> Crear, Leer, Actualizar y Eliminar productos.</li>
        <li><strong>Soporte para productos digitales y físicos:</strong> Tipos de productos flexibles con campos compartidos y únicos.</li>
        <li><strong>Campos personalizables:</strong> Detalles como:
            <ul>
                <li>Título</li>
                <li>Descripción</li>
                <li>Precio</li>
                <li>Información del vendedor</li>
                <li>Color</li>
                <li>Dimensiones</li>
            </ul>
        </li>
        <li><strong>Gestión de Slugs:</strong> Genera slugs únicos automáticamente para URLs amigables con SEO.</li>
    </ul>

    <h3>Autenticación de Usuarios</h3>
    <ul>
        <li>Protección de vistas sensibles con decoradores <code>login_required</code> y mixins.</li>
        <li>Vistas personalizadas para que los usuarios autenticados gestionen sus productos.</li>
    </ul>

    <h3>Búsqueda y Filtrado</h3>
    <ul>
        <li>Funcionalidad de búsqueda avanzada utilizando el ORM de Django y consultas con <code>Q</code> para múltiples campos.</li>
    </ul>

    <h3>Estructura Modular</h3>
    <ul>
        <li><code>products</code>: Funcionalidades principales de productos.</li>
        <li><code>MyEcommerceApp</code>: Utilidades generales del Ecommerce.</li>
        <li><code>api</code>: Endpoints REST API para integración.</li>
    </ul>

    <h3>Validación y Señales</h3>
    <ul>
        <li>Valida títulos de productos contra una lista de palabras bloqueadas.</li>
        <li>Usa señales de Django (<code>pre_save</code>) para garantizar consistencia en los datos.</li>
    </ul>

    <h2>Tecnologías y Dependencias</h2>
    <ul>
        <li><strong>Django 4.1.4:</strong> Framework principal.</li>
        <li><strong>Django REST Framework:</strong> Desarrollo de APIs.</li>
        <li><strong>Redis & Celery:</strong> Tareas en cola y operaciones asíncronas.</li>
        <li><strong>Gunicorn:</strong> Servidor WSGI para producción.</li>
        <li><strong>Whitenoise:</strong> Sirve archivos estáticos en producción.</li>
        <li><strong>SQLite:</strong> Base de datos predeterminada, adaptable a PostgreSQL.</li>
        <li><strong>Herramientas de Calidad de Código:</strong> Flake8, Isort, Black.</li>
    </ul>

    <h2>Instalación</h2>
    <div class="highlight">
        <pre><code>git clone &lt;repository-url&gt;
cd Ecommerce
python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver</code></pre>
    </div>

    <h2>Estructura del Proyecto</h2>
    <pre>
Ecommerce/
├── MyEcommerceApp/          # Funcionalidad principal de ecommerce
├── products/                # Gestión de productos
├── api/                     # Endpoints API
├── templates/               # Plantillas HTML
├── static/                  # Archivos estáticos (CSS, JS, Imágenes)
├── db.sqlite3               # Base de datos SQLite
├── manage.py                # Utilidad de línea de comandos de Django
├── requirements.txt         # Dependencias del proyecto
    </pre>

    <h2>Mejoras Futuras</h2>
    <ul>
        <li>Añadir registro y gestión de perfiles de usuario.</li>
        <li>Implementar pasarelas de pago (e.g., Stripe, PayPal).</li>
        <li>Enriquecer el frontend con frameworks modernos de JavaScript.</li>
        <li>Soporte para subir imágenes y mejorar las listas de productos.</li>
    </ul>

    <h2>Licencia</h2>
    <p>Este proyecto está licenciado bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.</p>

    <h2>Agradecimientos</h2>
    <p>Agradecimientos especiales a la comunidad de Django y los autores de las dependencias utilizadas en este proyecto.</p>

    <div class="footer">
        <p>&copy; 2024 - Proyecto Ecommerce con Django</p>
    </div>

</body>
</html>

