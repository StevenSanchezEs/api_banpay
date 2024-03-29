# API Banpay

Esta API te permite realizar operaciones CRUD en /usuarios/, y en base a roles consumir endpoint de Studio Ghibli desde esta misma API.

## Requisitos

- Python 3.8
- Postgresql
- SO Linux

## Configuración del entorno virtual

1.**Clonar el Repositorio:**

> git clone https://github.com/StevenSanchezEs/api_banpay.git

2.**Acceder al Directorio del Proyecto:**

> cd api_banpay

3.**Crear y Activar el Entorno Virtual:**

> python3.8 -m venv venv

> source venv/bin/activate

4.**Instalar Dependencias:**

> pip install -r requirements.txt

5.**Crear archivo .env**
> vim .env

## Configuración de variables de entorno y Base de Datos

6.**Base de datos**

Debes tener una base de datos Postgres creada o crear una, para este ejemplo se creo una base de datos llamada **banpay**, tu puedes elegir el de tu preferencia ya que en el archivo **.env** podras cambiar la configuración de tu base de datos si así lo requieres.

Puedes usar una instancia de Postgres tradicional o un contenedor como se muestra a continuación.
> docker run --name mi-postgres \
           -e POSTGRES_DB=nombre_base_de_datos \
           -e POSTGRES_USER=nombre_usuario \
           -e POSTGRES_PASSWORD=contraseña \
           -p puerto_local:5432 \
           -d postgres


7.**Configurar variables de entorno para producción**

Los datos presentados a continuación son unicamente para representar un ejemplo, tienes que remplazar los valores por tus propias credenciales, el **SECRET KEY** es muy importante que lo cambies por uno generado por herramientas como **secrets** de Python, DEBUG debes cambiarlo a **False** y en **ALLOWED_HOST** por el dominio o ip donde se permitiran las solicitudes.

Ejemplo para definir Variables de entorno en el archivo .env creado previamente:
	
 	#Variables para Configuración Base de Datos
	DB_NAME=banpay
	DB_USER=pruebas
	DB_PASSWORD=MbI6avYvzR2rYKihN5IokQQ-KCYQ
	DB_HOST=monorail.proxy.rlwy.net
	DB_PORT=24621
	
 	#Variables para configuracion de producción
	SECRET_KEY=django-insecure-34hdbp&tde8_+zd2k)q$+u
	ALLOWED_HOSTS='*'
	DEBUG=True

Ejemplo secrets:
```python
import secrets

SECRET_KEY = secrets.token_urlsafe(32)
print(SECRET_KEY)
```

8.**Crear Migraciones y Migrar**

> python manage.py makemigrations

> python manage.py migrate

8.**Crear superuser**

Con este comando podras crear el superusuario el cual es necesario y te permitira consumir el endpoint /usuarios para crear más usuarios y asignar roles.
> python manage.py createsuperuser

## Deploy
Los siguientes datos son un ejemplo para deploy lo unico que se modifica conforme a las necesidades para el deploy es la **IP** o **Dominio** así como el **puerto** y **workers(-w)**.

> gunicorn -w 4 -b 192.168.150.251:8000 banpay.wsgi:application

**Enspoints de la API**

Documentación de la API: 

/api/redoc

GRUD usuarios: 

/api/usuarios

Consultas de recursos Ghibliapi: 

/api/films
/api/people
/api/locations
/api/species
/api/vehicles


**Notas**

Cada solicitud para consumir un endpoint requiere que se pase el token generado previamente en los Headers de la solicitud, por ejemplo:


Key: Authorization

Value: Bearer tutoken3242onoin23o4n32i3on34223oi
