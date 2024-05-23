from flask import Flask, render_template
from admin.admin import admin

app = Flask(__name__)
app.register_blueprint(admin)


@app.route('/')
def index():
    return render_template('index.html', status='main Page')


if __name__ == '__main__':
    app.run(debug=True)
