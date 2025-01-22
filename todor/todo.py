from flask import Blueprint, render_template, redirect, request, url_for, g

# Agregando Validacion
from todor.auth import login_required
from .models import Todo, User
from todor import db

# Creando instancia
bp = Blueprint('todo', __name__, url_prefix='/todo')

# Creando ruta y función
#Accion para listar Tareas
@bp.route('/list')
@login_required
def index():
    todos = Todo.query.all()
    return render_template('todo/index.html', todos = todos)

# Acción para crear listas
@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']

        todo = Todo(g.user.id, title, desc)
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('todo.index'))
    return render_template('todo/create.html')

def get_todo(id):
    todo = Todo.query.get_or_404(id)
    return todo

# Acción para actualizar
@bp.route('/update/<int:id>', methods=('GET', 'POST'))
@login_required
def update(id):
    todo = get_todo(id)

    if request.method == 'POST':
        todo.title = request.form['title']
        todo.desc = request.form['desc']
        todo.state = True if request.form.get('state') == 'on' else False
        db.session.commit()
        return redirect(url_for('todo.index'))
    return render_template('todo/update.html', todo=todo)

# Acción para eliminar
@bp.route('/delete/<int:id>')
@login_required
def delete(id):
    todo = get_todo(id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('todo.index'))

