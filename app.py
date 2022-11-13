from flask import Flask, request, render_template, send_from_directory
from loader.views import loader_blueprint
from main.views import main_blueprint
import logging

# logger = logging.basicConfig(
#     filename='flask.log',
#     level=logging.DEBUG
# )

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

app.register_blueprint(loader_blueprint)
app.register_blueprint(main_blueprint)


@app.route("/list")
def page_tag():
    pass


@app.route("/post", methods=["GET", "POST"])
def page_post_form():
    pass


@app.route("/post", methods=["POST"])
def page_post_upload():
    pass


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()
