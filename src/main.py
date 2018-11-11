from flask import Flask
import take_function as t
from flask import request
from flask import send_file

app = Flask(__name__)


@app.route('/color')
def get_graph():
    fx = request.args.get('fx')
    fy = request.args.get('fy')
    t.graph_color(fx,fy, skip=2)
    return send_file("./vector_field.jpg")


app.run()
