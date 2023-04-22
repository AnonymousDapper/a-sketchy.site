# The MIT License (MIT)

# Copyright (c) 2023 AnonymousDapper


from quart import Quart, request, render_template

import os  

app = Quart(__name__, static_folder="../static", template_folder="../templates")

def dir_last_updated(folder):
    return str(max(os.path.getmtime(os.path.join(root_path, f))
                    for root_path, _, files in os.walk(folder)
                    for f in files))

def render_svelte(component, title=None, extra_data=None):
    return render_template('svelte_template.html', component=component, title=title, extra_data=extra_data, last_updated=dir_last_updated('static'))


@app.route("/")
async def root():
    return await render_template("index.html")


@app.route("/svelte/<string:component>")
async def blog(component: str):
    return await render_svelte(component, component.title()) 

@app.errorhandler(404)
async def page_not_found(e):
    return await render_template("errors/404.html"), 404

def _serve():
    app.run()

def _serve_dev():
    app.run(debug=True, use_reloader=True, host="localhost")


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True, host="localhost")
