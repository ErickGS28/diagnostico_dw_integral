# CineApp

## Descripción

Aplicación web para gestionar un catálogo de películas. Permite crear, consultar, editar y eliminar películas mediante una interfaz web. También expone una API REST para integración con otros sistemas.

## Tecnologías utilizadas

- Python 3.10
- Django 5.2
- Django REST Framework 3.17
- SQLite (base de datos)
- Bootstrap 5 (estilos vía CDN)

## Funcionalidades

- Listar todas las películas registradas
- Ver el detalle completo de una película
- Crear una nueva película
- Editar una película existente
- Eliminar una película con confirmación
- API REST en `/api/peliculas/` con soporte completo CRUD (GET, POST, PUT, DELETE)

## Campos de la entidad Película

| Campo | Descripción |
|---|---|
| `titulo` | Nombre de la película |
| `director` | Nombre del director |
| `anio` | Año de estreno |
| `genero` | Género cinematográfico |
| `sinopsis` | Descripción de la trama |
| `duracion_minutos` | Duración en minutos |

## Instrucciones para ejecutar el proyecto

### 1. Clonar el repositorio

```bash
git clone https://github.com/<tu-usuario>/cineapp.git
cd cineapp
```

### 2. Crear y activar entorno virtual

```bash
python -m venv venv
```

Windows:
```bash
venv\Scripts\activate
```

macOS/Linux:
```bash
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Aplicar migraciones

```bash
python manage.py migrate
```

### 5. Ejecutar el servidor

```bash
python manage.py runserver
```

Abrir en el navegador: [http://127.0.0.1:8000](http://127.0.0.1:8000)

### 6. API REST

Disponible en: [http://127.0.0.1:8000/api/peliculas/](http://127.0.0.1:8000/api/peliculas/)
