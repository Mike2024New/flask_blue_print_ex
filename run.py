from flask import Flask, render_template
from config import blue_prints

app = Flask(__name__)
if blue_prints['admin']:
    from admin.admin import admin

    app.register_blueprint(admin)
if blue_prints['blog']:
    from blog.blog import blog

    app.register_blueprint(blog)
if blue_prints['contacts']:
    from contacts.contacts import contacts

    app.register_blueprint(contacts)


@app.route('/')
def index():
    return render_template('index.html', status='main Page', blue_prints=blue_prints)


if __name__ == '__main__':
    app.run(debug=True)
