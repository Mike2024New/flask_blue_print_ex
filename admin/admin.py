from flask import Blueprint, render_template, redirect, url_for
from config import blue_prints

admin = Blueprint("admin", __name__, url_prefix='/admin', template_folder="templates", static_folder="static")


@admin.route('/')
def admin_login():
    return render_template("admin/index.html", status="Administrator", blue_prints=blue_prints)


@admin.route('/logout')
def logout():
    return redirect(url_for('index'))
