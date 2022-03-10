
# Instalacion del recurso RESTframework
```bash
pip install djangorestframework
```
------------------------------- 

```bash
pip install markdown
```
------------------------------

```bash
pip install django-filter
``` 
------------------------------
```bash
pip install Pyllow
```
------------------------------
```bash
pip install django-cors-headers
```
------------------------------
```bash
pip install djangorestframework-simplejwt
```
------------------------------

## agregar libreria a INSTALLED_APPS en settings
```bash
'rest_framework',
'rest_framework.authtoken',
'corsheaders',
```

------------------------------

## Para ocultar credenciales 
```bash
pip install python-dotenv
```

<!-- En settings para el funcionamiento: -->
```bash
from dotenv import load_dotenv
import os
load_dotenv()
```
## Agregar a MIDDLEWARE en settings
```bash
'corsheaders.middleware.CorsMiddleware',
```
## Agregar en settings
```bash
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
]
```

 #203462
