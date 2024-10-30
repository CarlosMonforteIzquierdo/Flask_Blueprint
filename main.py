from flask import Flask
from blueprints.helloworld.helloworld import hello_world_bp
from blueprints.calculator.calculator import calculator_bp

app = Flask(__name__)
app.register_blueprint(hello_world_bp)
app.register_blueprint(calculator_bp, url_prefix="/calculator")


if __name__ == '__main__':
    app.run(debug=True)