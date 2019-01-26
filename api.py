from flask import Flask
from src.visualizer import Visualizer
from flask import request
from flask import send_file
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)


@app.route('/')
def get_graph():
    try:
        fx = repr(request.args.get('fx'))[1:-1]
        fy = repr(request.args.get('fy'))[1:-1]
        skip = request.args.get('skip')
        bounds = list(map(int, request.args.get('bounds').split(",")))
        v = Visualizer(f_x=str(fx), f_y=str(fy))
        plt = v.plot_color(skip=float(skip), bound=bounds)
        plt.savefig("vector_field.png")
        plt.gcf().clear()
        return send_file("./vector_field.png")
    except Exception as e:
        return send_file("./img/error.jpg")


@app.route("/divcurl")
def div_curl():
    try:
        fx = repr(request.args.get('fx'))[1:-1]
        fy = repr(request.args.get('fy'))[1:-1]
        x = float(request.args.get('x'))
        y = float(request.args.get('y'))
        v = Visualizer(f_x=str(fx), f_y=str(fy))
        div = v.div(x, y)
        curl = v.curl(x, y)
        return "Divergence: {}<br>Curl: {}".format(str(div), str(curl))
    except:
        return "Error: Check your equations"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
