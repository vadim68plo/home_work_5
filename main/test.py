from flask import Flask

app = Flask(__name__)

@app.route("/hi/<x>")
def page_index(x):
    return f"Привеt {x}"

app.run(host='0.0.0.0', port=80)