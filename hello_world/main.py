from sanic import Sanic
from sanic.response import json
from sanic.response import text
from sanic import Blueprint
from counter import counter_bp

app = Sanic()
app.blueprint(counter_bp)

@app.route("/")
async def test(request):
    return text("OK")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

