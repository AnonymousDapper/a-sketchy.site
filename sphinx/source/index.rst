
API Reference
==============

A wise man once said:

    fuck off, mate
    
.. code-block:: python
    
    from quart import Quart, render_template

    app = Quart(__name__, static_folder="../static", template_folder="../templates")


    @app.route("/")
    async def root():
        return await render_template("page.html", stylesheets=["fonts.css", "pico/pico.css"], title="Hello, This is a Test")


    def _serve():
        app.run()


    if __name__ == "__main__":
        app.run(debug=True, use_reloader=True)
