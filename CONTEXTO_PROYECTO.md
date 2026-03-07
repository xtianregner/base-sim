# Contexto del Proyecto Django - My Django App

> **Última sesión:** 6 Marzo 2026  
> **Objetivo:** Crear un sitio web robusto con Django

---

## 📁 Estructura del Proyecto

```
my-django-app/                  👈 Raíz del proyecto (aquí trabajas)
├── .venv/                      # Entorno virtual de Python
├── requirements.txt            # Dependencias del proyecto
├── pytest.ini                  # Configuración de tests
├── README.md                   # Documentación original
├── CONTEXTO_PROYECTO.md        # Este archivo
└── src/                        # Código fuente
    ├── manage.py               # CLI de Django
    ├── conftest.py             # Fixtures de pytest
    ├── myproject/              # Configuración del proyecto
    │   ├── settings.py         # Configuraciones
    │   ├── urls.py             # URLs principales
    │   └── wsgi.py             # Servidor WSGI
    └── myapp/                  # Tu aplicación
        ├── models.py           # Modelos de datos
        ├── views.py            # Vistas (lógica)
        ├── urls.py             # URLs de la app
        ├── admin.py            # Panel de admin
        ├── static/myapp/       # Archivos estáticos
        │   ├── css/style.css
        │   ├── js/main.js
        │   └── images/
        └── templates/myapp/    # Templates HTML
            ├── base.html       # Layout base
            └── index.html      # Página de inicio
```

---

## 🚀 Comandos Esenciales

### Entorno Virtual
```bash
# Activar (cada vez que trabajes)
source .venv/bin/activate

# Desactivar
deactivate

# Verificar si está activo
echo $VIRTUAL_ENV
```

### Servidor de Desarrollo
```bash
# Desde la raíz del proyecto (con venv activo)
python src/manage.py runserver

# El servidor corre en: http://127.0.0.1:8000/
```

### Migraciones (Base de Datos)
```bash
# Aplicar migraciones pendientes
python src/manage.py migrate

# Crear migraciones cuando cambies models.py
python src/manage.py makemigrations

# Crear superusuario para el admin
python src/manage.py createsuperuser
```

### Instalar Dependencias
```bash
pip install -r requirements.txt
```

---

## 🌐 URLs Configuradas

| URL | Vista | Tipo | Descripción |
|-----|-------|------|-------------|
| `/` | `index` | HTML | Página principal |
| `/about/` | `about` | HTML | Página About |
| `/contact/` | `contact` | HTML | Página Contact |
| `/api/data/` | `api_data` | JSON | Endpoint API ejemplo |
| `/admin/` | Django Admin | HTML | Panel de administración |

---

## 📦 Dependencias Instaladas

| Paquete | Uso |
|---------|-----|
| Django | Framework web principal |
| djangorestframework | Crear APIs REST robustas |
| python-dotenv | Variables de entorno (.env) |
| psycopg2-binary | Conexión a PostgreSQL |
| gunicorn | Servidor para producción |

---

## 🔑 Conceptos Clave Aprendidos

### 1. manage.py
- Herramienta CLI de Django
- Ejecuta comandos: runserver, migrate, createsuperuser, shell, test

### 2. conftest.py
- Archivo de pytest para fixtures compartidos
- Se ejecuta automáticamente en los tests

### 3. Entorno Virtual (.venv)
- Aísla las dependencias del proyecto
- Evita conflictos entre proyectos
- Se crea en la raíz del proyecto

### 4. Migraciones
- Django crea tablas en la base de datos automáticamente
- `makemigrations` → genera archivos de migración
- `migrate` → aplica los cambios a la BD

### 5. Django puede servir ambos:
- **Páginas HTML** → Templates renderizados
- **APIs JSON** → Para frontend JS, apps móviles

---

## 📝 Archivos Corregidos en Esta Sesión

### admin.py
```python
# Cambiado de YourModelName a MyModel
from .models import MyModel
admin.site.register(MyModel)
```

### views.py
```python
# Agregadas las vistas: index, about, contact
# index ahora usa template: 'myapp/index.html'
```

### urls.py (myapp)
```python
# Agregada ruta para API
path('api/data/', views.api_data, name='api_data'),
```

---

## 🎯 Próximos Pasos Sugeridos

### Para un sitio web más robusto:

1. **[ ] Aplicar migraciones**
   ```bash
   python src/manage.py migrate
   ```

2. **[ ] Crear superusuario**
   ```bash
   python src/manage.py createsuperuser
   ```

3. **[ ] Agregar template CSS descargado**
   - Reemplazar `static/myapp/css/style.css`
   - Adaptar `templates/myapp/base.html`

4. **[ ] Crear más modelos en models.py**
   - Definir entidades de tu aplicación

5. **[ ] Configurar variables de entorno**
   - Crear archivo `.env` para secrets
   - Usar python-dotenv en settings.py

6. **[ ] Expandir APIs con Django REST Framework**
   - Serializers
   - ViewSets
   - Autenticación

7. **[ ] Agregar autenticación de usuarios**
   - Login/Logout
   - Registro
   - Perfiles

---

## 💡 Tips Recordar

- **Siempre trabaja desde la raíz:** `/Users/user/dhru/my-django-app`
- **Activa el venv antes de trabajar:** `source .venv/bin/activate`
- **El código está en `src/`**, pero los comandos se ejecutan desde la raíz
- **Recarga automática:** Django detecta cambios en el código automáticamente
- **Ignora el warning de migraciones** si solo estás explorando

---

## 🔗 Referencias

- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [pytest-django](https://pytest-django.readthedocs.io/)
