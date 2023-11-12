import os

from dotenv import load_dotenv
from bottle import jinja2_template, route, run, static_file, default_app

dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path)

IMG_FILEPATH = os.getenv("IMG_FILEPATH", "")


@route(path=f"/{IMG_FILEPATH}/<file_path:path>", method="GET")
def response_image(file_path=""):
    return static_file(file_path, root=f"./{IMG_FILEPATH}")


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
    return jinja2_template("index.html", title="image index", target_dir=target_dir, filenames=files)


if __name__ == "__main__":
    run(host="localhost", port=18000, reloader=True)

app = default_app()
