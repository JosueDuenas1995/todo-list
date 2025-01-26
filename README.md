# Todo List App


Este es un proyecto de una aplicación de lista de tareas (Todo List) construida con Flask y SQLite. La aplicación permite a los usuarios registrarse, iniciar sesión, crear, actualizar y eliminar tareas.


**Asignatura:** Desarrollo de Aplicaciones Web en la Nube
**TSU:** Servicios en la Nube  
**Nombres:** Josue Daniel 
**Apellidos:** Dueñas Bolaños 




## Características


- Registro de usuarios
- Inicio de sesión de usuarios
- Creación de tareas
- Actualización de tareas
- Eliminación de tareas
- Visualización de tareas


## Requisitos


- Python 3.x
- Flask
- Flask-SQLAlchemy
- Werkzeug


## Instalación


1. Clona el repositorio en tu máquina local:


    ```sh
    git clone https://github.com/tu-usuario/todo-list-app.git
    cd todo-list-app
    ```


2. Crea y activa un entorno virtual:


    ```sh
    python -m venv venv
    .\venv\Scripts\activate  # En Windows
    source venv/bin/activate  # En macOS/Linux
    ```


3. Instala las dependencias:


    ```sh
    pip install -r requirements.txt
    ```


4. Configura la base de datos:


    ```sh
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```


## Uso


1. Inicia la aplicación Flask:


    ```sh
    flask run
    ```


2. Abre tu navegador web y navega a `http://127.0.0.1:5000` para ver la aplicación en acción.


## Estructura del Proyecto


todo-list-app/ ├── instance/ │ └── todolist.db ├── todor/ │ ├── init.py │ ├── auth.py │ ├── models.py │ ├── todo.py │ └── templates/ │ ├── base.html │ ├── auth/ │ │ ├── login.html │ │ └── register.html │ ├── todo/ │ │ ├── create.html │ │ ├── index.html │ │ └── update.html ├── run.py ├── requirements.txt └── README.md

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
