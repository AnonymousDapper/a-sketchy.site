# The MIT License (MIT)

# Copyright (c) 2023 AnonymousDapper


import json
import os

from quart import Quart, render_template, url_for

app = Quart(__name__, static_folder="../static", template_folder="../templates")


def dir_last_updated(folder):
    return str(
        max(os.path.getmtime(os.path.join(root_path, f)) for root_path, _, files in os.walk(folder) for f in files)
    )


@app.context_processor
def template_utils():
    def get_static_url_cachebust(filename: str):
        return f"{url_for('static', filename=filename)}?u={dir_last_updated('static')}"

    return dict(static_url=get_static_url_cachebust)


def render_svelte(component, title=None, extra_data=None):
    return render_template(
        "svelte.html",
        component=component,
        title=title,
        extra_data=json.dumps(extra_data),
    )


@app.route("/")
async def root():
    return await render_template("index.html")


@app.route("/svelte/<string:component>/", defaults={"name": "null"})
@app.route("/svelte/<string:component>/<string:name>/")
async def blog(component: str, name: str):
    return await render_svelte(component, component.title(), {"name": name})


@app.errorhandler(404)
async def page_not_found(e):
    return await render_template("errors/404.html"), 404


def _serve():
    app.run()


def _serve_dev():
    app.run(debug=True, use_reloader=True, host="localhost")


if __name__ == "__main__":
    _serve_dev()
