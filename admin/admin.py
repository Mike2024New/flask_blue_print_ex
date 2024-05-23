from flask import Blueprint, render_template, redirect, url_for

admin = Blueprint("admin", __name__, url_prefix='/admin', template_folder="templates", static_folder="admin.static")


@admin.route('/')
def admin_login():
    return render_template("admin/index.html", status="Administrator")


@admin.route('/logout')
def logout():
    return redirect(url_for('index'))
