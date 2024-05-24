from flask import Blueprint, render_template
from config import blue_prints

contacts = Blueprint("contacts", __name__, url_prefix='/contacts', template_folder="templates", static_folder="static")


@contacts.route('/')
def contacts_read():
    return render_template("contacts/index.html", status="Contacts", blue_prints=blue_prints)
