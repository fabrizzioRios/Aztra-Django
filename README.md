# Aztra Prueba Django - Sistema de Blog y Tareas

[![Django](https://img.shields.io/badge/Django-3.2-brightgreen)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/Django_REST-3.12-blue)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13-blue)](https://www.postgresql.org/)

API Django con Docker Compose para gestión de blog y tareas.

# 📦 Características Principales
- 🏗️ **API REST** completa con Django REST Framework

- ✏️**CRUD** completo para posts de blog y tareas

- 🔍 **Filtrado avanzado** de tareas por estado/proyecto

- 📚 **Documentación API automática** con Swagger

- 🐳 **Configuración Docker** lista para producción

- 🧪 **Pruebas unitarias** y de integración

- ⚡ **Optimizado** para entornos de desarrollo y producción

## 🚀 Requisitos

- Docker 20.10+
- Docker Compose 1.29+
- Python 3.8+ (opcional para desarrollo local)

## 📊 Estructura del Proyecto

```
Aztra_Prueba_Django/
├── app/
│   ├── app/              # Configuración Django
│   ├── blog/             # App de blog
│   ├── tasks/            # App de tareas
│   └── manage.py
├── docker-compose.yml    # Configuración Docker
├── Dockerfile            # Build de la aplicación
└── requirements.txt      # Dependencias Python
```

## 🛠️ Configuración

1. Clona el repositorio:
```bash
git clone git@github.com:fabrizzioRios/Aztra-Django.git

cd Aztra_Prueba_Django
```
# 2. Construir y levantar servicios
```bash
docker compose up -d --build
```
# 3. Aplicar migraciones
```bash
docker-compose run --rm app sh -c "python manage.py makemigrations && python manage.py migrate"
```

# 🌐 Endpoints Disponibles
## 📝 Blog
- `GET /blog/posts/` - Listar posts (paginados)

- `POST /blog/posts/` - Crear nuevo post

- `GET /blog/posts/<id>/` - Detalles de post

- `PATCH /blog/posts/<id>/` - Actualizar post

- `DELETE /blog/posts/<id>/` - Eliminar post

## ✅ Tareas
- `GET /tasks/tareas/?proyecto=<id>&estado=<estado>` - Listar tareas filtradas

- `POST /tasks/tareas/` - Crear nueva tarea

- `PATCH /tasks/tareas/<id>/cambiar-estado/` - Actualizar estado


## 🧪 Ejecución de Tests
```bash
docker-compose run --rm app sh -c "cd /app && python manage.py test blog.tests"
```

## 📌 Notas Adicionales
- 🌍 La API está disponible en http://localhost:8000

- 📄 Documentación interactiva en http://localhost:8000/swagger/

- ⚙️ Panel de administración en http://localhost:8000/admin/

## 🖋️ Autor

**Fabrizzio Ríos** - Software Engineer  

[![GitHub](https://img.shields.io/badge/GitHub-Profile-blue)](https://github.com/fabrizzioRios) [![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue)](https://www.linkedin.com/in/fabrizzio-rios-21b21b240/) 
