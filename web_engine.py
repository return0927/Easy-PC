from flask import Flask
import easy_pc

_name = easy_pc.settings.get("global", "server_name")
_host = easy_pc.settings.get("web", "")

app = Flask(_name)


@app.route("/")
@app.route("/<path:path>")
def root(path):
    return "Working!"


app.run()
