# Proyecto Django con Telethon para Telegram Bot
## Estructura del Proyecto
- telegram_web/: Contiene la configuración global del proyecto.
 - settings.py: Configuración principal de Django.
 - urls.py: Define las rutas para las vistas principales del proyecto.
 - asgi.py y wsgi.py: Para ASGI y WSGI respectivamente.
 - manage.py: Script de administración de Django.

- botapp/: Esta es la aplicación principal.
 - forms.py: Formularios usados para la autenticación.
 - views.py: Lógica detrás de cada página.
 - models.py: Definiciones de modelos (si son necesarias).
 - urls.py: Define las rutas específicas.
 - templates/: Plantillas HTML.

- media/: Carpeta para los archivos subidos por los usuarios.
## Funcionalidades
- Autenticación de usuarios.
- Envío de comandos y consultas a un bot de Telegram.
- Recepción y visualización de respuestas del bot.
- Visualización de imágenes de perfil devueltas por el bot.
## Requisitos
- Python 3.x
- Django 4.x
- Telethon
## Instalación
1. Clonar el repositorio:
 git clone https://github.com/grmns/bot_telegram.git
 cd bot_telegram
2. Crear un entorno virtual:
 python -m venv venv
 source venv/bin/activate # En Windows: venv\Scripts\activate
3. Instalar las dependencias:
 pip install -r requirements.txt
4. Configurar la base de datos (si es necesario):
 python manage.py migrate
5. Ejecutar el servidor de desarrollo:
 python manage.py runserver
6. Configurar Telethon: Asegúrate de configurar las credenciales de API de Telegram en
settings.py.
## Uso
1. Inicia sesión o regístrate en la página.
2. Ingresa un DNI en el formulario para enviar un comando al bot de Telegram.
3. El bot procesará la solicitud y la respuesta aparecerá en la página de resultados.
## Contribuciones
Si deseas contribuir a este proyecto, puedes hacerlo mediante un pull request o reportando
problemas.
## Licencia
Este proyecto está bajo la licencia MIT.