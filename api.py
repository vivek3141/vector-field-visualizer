from flask import Flask
from src.visualizer import Visualizer
from flask import request
from flask import send_file

app = Flask(__name__)


@app.route('/')
def get_graph():
    fx = request.args.get('fx')
    fy = request.args.get('fy')
    v = Visualizer(f_x=str(fx), f_y=str(fy))
    v.plot_color()
    return send_file("./src/vector_field.jpg")


if __name__ == "__main__":
    app.run()
