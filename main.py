# Import
from flask import Flask, render_template,request, redirect



app = Flask(__name__)


# Página de contenidos en ejecución
@app.route('/')
def index():
    return render_template('index.html')


# Habilidades dinámicas
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    return render_template('index.html', button_python=button_python)

@app.route('/', methods=['POST'])
def process_feedback():
    if request.method == "POST":
        email = request.form["email"]
        text = request.form["text"]
        button = request.form.get("form_button")
        return render_template("index.html", button = button)

if __name__ == "__main__":
    app.run(debug=True)
