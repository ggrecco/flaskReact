import time
from flask import Flask

app = Flask(__name__)
app.debug = False

@app.route('/ola')
def get_current_time():
    return {'ola': 'Olá Mundo!!'}
