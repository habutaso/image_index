import os

from dotenv import load_dotenv
from bottle import jinja2_template, route, run, static_file

dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path)

IMG_FILEPATH = os.getenv("IMG_FILEPATH", "")


@route(path=f"/{IMG_FILEPATH}/<file_path:path>", method="GET")
def response_image(file_path=""):
    return static_file(file_path, root="./images")


@route("/views/pure/<filepath:re:.*\.css>")
def css(filepath):
    return static_file(filepath, root="views/pure")


@route(path="/", method="GET")
def index():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    target_dir = f"{IMG_FILEPATH}/"
    files = os.listdir(target_dir)
    # Latest order
    files.sort(key=lambda x: os.path.getmtime(root_dir + "/" + target_dir + x), reverse=True)
    print(files)
    return jinja2_template("index.html", title="test", target_dir=target_dir, filenames=files)


run(host="localhost", port=18000, reloader=True)
