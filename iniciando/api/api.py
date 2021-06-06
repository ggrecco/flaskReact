import time
from flask import Flask
from flask.globals import request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:123456@localhost:5432/testepy"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# cria tabela de usuario
class UserModel(db.Model):
    __tablename__ = 'user'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    password = db.Column(db.String())
        
    def __init__(self, name, password):
        self.name = name
        self.password = password
    
    def __repr__(self):
        return f"<User {self.name}>"


@app.route('/user')
def get_users():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            users = UserModel(name=data['name'])
            db.session.add(users)
            db.session.commit()
            return {"message": f"user {users.name} was find in database"}
        else:
            return {"error": "The request payload is not in JSON format"}
    
    elif request.method == 'GET':
        users = UserModel.query.all()
        results = [{
            "name": user.name,
            "password": user.password,
        } for user in users]
        return {"count": len(results), "user": results}
        
@app.route('/ola')
def get_current_time():
    return {'ola': 'Olá Mundo!!'}