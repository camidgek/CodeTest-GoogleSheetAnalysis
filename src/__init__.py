from flask import Flask

from src.routes import my_app

app = Flask(__name__)
app.register_blueprint(my_app)
