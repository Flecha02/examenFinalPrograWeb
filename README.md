#Sistema de Control de Productos y Piezas

Proyecto Full-Stack desarrollado con **Django REST Framework** (Backend) y **React + Vite** (Frontend) para la gestión y asignación de piezas a productos.

---

##Estructura del Proyecto

```text
EXAMEN_FINAL_PROYECTO/
├── backend/                # API REST con Django y SQLite
│   ├── api/                # Modelos, Serializadores, Vistas y URLs
│   ├── config/             # Configuración principal del proyecto Django
│   ├── .env                # Variables de entorno (No incluido en Git)
│   └── manage.py
├── frontend/               # Interfaz de usuario con React + Vite
│   ├── src/
│   └── .env                # Variables de entorno del cliente (No incluido en Git)
├── .gitignore
└── README.md
```

---

##Requisitos Previos

Asegúrate de tener instalado en tu sistema:
* **Python** (3.10 o superior)
* **Node.js** (18.x o superior) y **npm**
* **Git**

---

##Instalación y Configuración

### 1. Clonar el repositorio
```bash
git clone <URL_DE_TU_REPOSITORIO>
cd <NOMBRE_DE_LA_CARPETA_DEL_PROYECTO>
```

---

### 2. Configuración del Backend (Django REST Framework)

1. **Entrar a la carpeta del backend:**
   ```bash
   cd backend
   ```

2. **Crear y activar el entorno virtual:**
   * **Windows (PowerShell/CMD):**
     ```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```
   * **Mac / Linux:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Instalar las dependencias:**
   ```bash
   pip install django djangorestframework django-cors-headers python-decouple
   ```

4. **Configurar las variables de entorno:**
   Crea un archivo llamado `.env` dentro de la carpeta `backend/` (al mismo nivel que `manage.py`) y agrega:
   ```env
   DEBUG=True
   SECRET_KEY=django-insecure-clave-secreta-local-12345
   DATABASE_URL=sqlite:///db.sqlite3
   ```

5. **Ejecutar las migraciones de la base de datos (SQLite):**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Iniciar el servidor de desarrollo:**
   ```bash
   python manage.py runserver
   ```
   > El backend estará corriendo en: `http://127.0.0.1:8000/`

---

### 3. Configuración del Frontend (React + Vite)

Abre una **nueva terminal** (manteniendo el backend encendido) y sigue estos pasos:

1. **Entrar a la carpeta del frontend:**
   ```bash
   cd frontend
   ```

2. **Instalar los paquetes de Node:**
   ```bash
   npm install
   ```

3. **Configurar las variables de entorno:**
   Crea un archivo llamado `.env` dentro de la carpeta `frontend/` y agrega:
   ```env
   VITE_API_URL=http://127.0.0.1:8000/api
   ```

4. **Iniciar la aplicación React:**
   ```bash
   npm run dev
   ```
   > El frontend estará disponible en: `http://localhost:5173/`

---

##Endpoints Principales de la API

| Recurso | Método | Endpoint | Descripción |
| :--- | :--- | :--- | :--- |
| **Productos** | `GET`, `POST` | `/api/productos/` | Listar o crear productos |
| **Productos (ID)** | `GET`, `PUT`, `DELETE` | `/api/productos/{id}/` | Ver, actualizar o eliminar producto |
| **Piezas** | `GET`, `POST` | `/api/piezas/` | Listar o crear piezas |
| **Piezas (ID)** | `GET`, `PUT`, `DELETE` | `/api/piezas/{id}/` | Ver, actualizar o eliminar pieza |
| **Asignaciones** | `GET`, `POST` | `/api/asignaciones/` | Asignar piezas a un producto |
| **Asignaciones (ID)** | `GET`, `PUT`, `DELETE` | `/api/asignaciones/{id}/` | Gestionar asignación específica |

---

##Modelo de Base de Datos

* **`producto`**: Almacena los productos principales (`productoID`, `nombre`, `descripcion`, `precio`, `fechaMod`, `activo`).
* **`pieza`**: Catálogo de piezas disponibles (`piezaID`, `nombre`, `descripcion`, `material`, `esOriginal`, `fechaMod`, `activo`).
* **`asiganacionPieza`**: Tabla intermedia que relaciona productos y piezas con su respectiva cantidad (`asignacionPiezaID`, `cantidad`, `piezaID`, `productoID`, `fechaMod`, `activo`).