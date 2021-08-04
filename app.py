
from flask import Flask,render_template,request
from flask.globals import request
from flask.helpers import url_for
from werkzeug.utils import redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/Zeliha/Desktop/TodoApp/todo.db'
db = SQLAlchemy(app)
@app.route("/")
def index():
    todos=Todo.query.all() # todos liste icinde sozluk seklinde
    """
    [
        {"id":1,"title":"Deneme1","content":"deneme1 todo","complete"=0}
    ]
    """
    return render_template("index.html",todos=todos)
@app.route("/add",methods=["POST"])
def addTodo():
    title=request.form.get("title")
    content=request.form.get("content")
    newTodo=Todo(title=title,content=content,complete=False)
    db.session.add(newTodo)
    db.session.commit()

    return redirect(url_for("index"))

@app.route("/complete/<string:id>",methods=["GET"])
def completeTodo(id): # db den row u al bir objeye koy
    todo = Todo.query.filter_by(id=id).first()
    if(todo.complete==False):
        todo.complete=True
    else:
        todo.complete=False
    db.session.commit()
    return redirect(url_for("index"))
    # Not: db.session.commit() veritabanında bir degisiklik
    #  yapmıyorsak commit'e gerek yok
@app.route("/delete/<string:id>") 
# index.html'de bir butona basınca bu url e gidiyorsak
# bu fonksiyonu cagir
def deleteTodo(id):
    todo=Todo.query.filter_by(id=id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))
@app.route("/detail/<string:id>")
def detailsTodo(id):
    todo = Todo.query.filter_by(id=id).first()
    return render_template("detail.html",todo=todo)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    content=db.Column(db.Text)
    complete=db.Column(db.Boolean)
    """id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    """


if __name__ == "__main__":
    app.run(debug=True)