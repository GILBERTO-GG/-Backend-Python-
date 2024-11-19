<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Proyecto Ecommerce con Django</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            background-color: #f9f9f9;
            color: #333;
        }
        .container {
            max-width: 800px;
            margin: 20px auto;
            background: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }
        h1, h2, h3 {
            color: #0056b3;
        }
        ul {
            margin: 10px 0;
            padding-left: 20px;
        }
        code {
            background: #eef;
            padding: 2px 4px;
            border-radius: 4px;
        }
        pre {
            background: #f4f4f4;
            padding: 10px;
            border-radius: 4px;
            overflow-x: auto;
        }
        a {
            color: #0056b3;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Proyecto Ecommerce con Django</h1>

        <h2>Resumen</h2>
        <p>Este proyecto es una aplicación de Ecommerce rica en funcionalidades construida con Django. Permite gestionar productos físicos y digitales, incluyendo opciones para listar, crear, actualizar y eliminar elementos. Está diseñado con escalabilidad y modularidad en mente, ofreciendo una base sólida para desarrollos futuros e integraciones.</p>

        <h2>Características</h2>

        <h3>Gestión de Productos</h3>
        <ul>
            <li>Operaciones CRUD: Crear, Leer, Actualizar y Eliminar productos.</li>
            <li>Soporte para productos digitales y físicos con campos compartidos y únicos.</li>
            <li>Campos personalizables:
                <ul>
                    <li>Título</li>
                    <li>Descripción</li>
                    <li>Precio</li>
                    <li>Información del vendedor</li>
                    <li>Color</li>
                    <li>Dimensiones</li>
                </ul>
            </li>
            <li>Gestión de slugs: Genera automáticamente slugs únicos para URLs amigables con SEO.</li>
        </ul>

        <h3>Autenticación de Usuarios</h3>
        <ul>
            <li>Protección de inicio de sesión: Vistas sensibles aseguradas con decoradores <code>login_required</code> y mixins.</li>
            <li>Vistas personalizadas: Interfaces adaptadas para usuarios autenticados que gestionan sus productos.</li>
        </ul>

        <h3>Búsqueda y Filtrado</h3>
        <p>Funcionalidad de búsqueda poderosa que aprovecha el ORM de Django y <code>Q</code> para consultar múltiples campos.</p>

        <h3>Estructura Modular</h3>
        <ul>
            <li><code>products</code>: Funcionalidades principales de productos.</li>
            <li><code>MyEcommerceApp</code>: Utilidades generales de Ecommerce.</li>
            <li><code>api</code>: Endpoints de API REST para integración.</li>
        </ul>

        <h3>Validación y Señales</h3>
        <ul>
            <li>Valida títulos de productos contra una lista de palabras bloqueadas.</li>
            <li>Usa señales de Django (<code>pre_save</code>) para garantizar la consistencia de datos.</li>
        </ul>

        <h2>Tecnologías y Dependencias</h2>
        <ul>
            <li><strong>Django 4.1.4:</strong> Framework web principal.</li>
            <li><strong>Django REST Framework:</strong> Desarrollo de API.</li>
            <li><strong>Redis & Celery:</strong> Para tareas asincrónicas.</li>
            <li><strong>Gunicorn:</strong> Servidor WSGI para producción.</li>
            <li><strong>Whitenoise:</strong> Manejo eficiente de archivos estáticos.</li>
            <li><strong>SQLite:</strong> Base de datos predeterminada, adaptable a PostgreSQL.</li>
            <li><strong>Herramientas de calidad de código:</strong> Flake8, Isort, Black.</li>
        </ul>

        <h2>Instalación</h2>
        <ol>
            <li>Clona el repositorio:
                <pre>git clone &lt;repository-url&gt;</pre>
            </li>
            <li>Navega al directorio del proyecto:
                <pre>cd Ecommerce</pre>
            </li>
            <li>Crea un entorno virtual y actívalo:
                <pre>python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate</pre>
            </li>
            <li>Instala las dependencias:
                <pre>pip install -r requirements.txt</pre>
            </li>
            <li>Aplica las migraciones:
                <pre>python manage.py migrate</pre>
            </li>
            <li>Inicia el servidor de desarrollo:
                <pre>python manage.py runserver</pre>
            </li>
        </ol>

        <h2>Uso</h2>
        <h3>Panel de Administración</h3>
        <p>Accede al panel de administración de Django en <code>http://localhost:8000/admin</code> para gestionar usuarios y productos.</p>

        <h3>Vistas Públicas</h3>
        <ul>
            <li>Listar productos: <code>/products/</code></li>
            <li>Detalles de un producto: <code>/products/&lt;product-id&gt;</code></li>
        </ul>

        <h3>Vistas Autenticadas</h3>
        <p>Requieren inicio de sesión para crear, editar o eliminar productos.</p>

        <h2>Estructura del Proyecto</h2>
        <pre>
Ecommerce/
|-- MyEcommerceApp/          # Funcionalidad principal de ecommerce
|-- products/                # Gestión de productos
|-- api/                     # Endpoints de API
|-- templates/               # Plantillas HTML
|-- static/                  # Archivos estáticos (CSS, JS, Imágenes)
|-- db.sqlite3               # Base de datos SQLite (por defecto)
|-- manage.py                # Utilidad CLI de Django
|-- requirements.txt         # Dependencias del proyecto
        </pre>

        <h2>Futuras Mejoras</h2>
        <ul>
            <li>Agregar registro de usuarios y gestión de perfiles.</li>
            <li>Implementar pasarelas de pago (Stripe, PayPal).</li>
            <li>Mejorar el frontend con frameworks modernos de JavaScript.</li>
            <li>Soporte para carga de imágenes en los listados de productos.</li>
        </ul>

        <h2>Licencia</h2>
        <p>Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.</p>

        <h2>Agradecimientos</h2>
        <p>Agradecimientos especiales a la comunidad de Django y a los autores de las dependencias utilizadas en este proyecto.</p>
    </div>
</body>
</html>

