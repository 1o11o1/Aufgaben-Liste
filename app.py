from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Konfiguration der SQLite-Datenbank
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Datenbank-Instanz erstellen
db = SQLAlchemy(app)

# Datenbankmodell für die To-Do Aufgaben
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(100), nullable=False)
    done = db.Column(db.Boolean, default=False)

# Datenbank erstellen (nur einmal notwendig)
with app.app_context():
    db.create_all()

# Startseite, zeigt alle To-Do Aufgaben an
@app.route('/')
def index():
    todos_active = Todo.query.filter_by(done=False).all() # Nur unerledigte Aufgaben
    todos_done = Todo.query.filter_by(done=True).all() # Nur erledigte Aufgaben
    return render_template('index.html', todos_active=todos_active, todos_done=todos_done)

# Route zum Hinzufügen neuer Aufgaben
@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task') # Holt die eingegebene Aufgabe aus dem Formular
    if task:
        new_task = Todo(task=task) # Neue Aufgabe erstellen
        db.session.add(new_task)
        db.session.commit() # Speichern der neuen Aufgabe in der Datenbank
    return redirect(url_for('index')) # Leitet zurück zur Startseite

# Route zum Löschen einer Aufgabe
@app.route('/delete/<int:task_id>')
def delete(task_id):
    task_to_delete = Todo.query.get_or_404(task_id)
    db.session.delete(task_to_delete)
    db.session.commit()
    return redirect(url_for('index')) # Leitet zurück zur Startseite

#Route zum Markieren einer Aufgabe als erledigt/nicht erledigt
@app.route('/toggle/<int:task_id>')
def toggle(task_id):
    task = Todo.query.get_or_404(task_id)
    task.done = not task.done # Status der Aufgabe ändern
    db.session.commit()
    return redirect(url_for('index')) # Leitet zurück zur Startseite 

if __name__ == '__main__':
    app.run(debug=True)