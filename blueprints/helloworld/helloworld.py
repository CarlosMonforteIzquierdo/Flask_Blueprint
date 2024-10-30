from flask import Blueprint,  render_template, redirect

hello_world_bp = Blueprint("helloworld", __name__, template_folder="templates")

@hello_world_bp.route("/")
def index():
    return "Hello World!"

@hello_world_bp.route("/hello")
def hello():
    return "Hello World AGAIN!"

@hello_world_bp.route("/hello/<name>")
def hello_name(name):
    return f"Hello {name}"

@hello_world_bp.route("/hello_html")
def hello_html():
    return render_template("helloworld/hello.html")