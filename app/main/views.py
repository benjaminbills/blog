from flask import render_template, request, redirect, url_for, flash
from . import main
from ..requests import get_quote
from flask_login import login_required, current_user
from .. import db


@main.route("/")
def index():
    """
    View root page function that returns the index page and its data
    """
    quote = get_quote()
    return render_template("index.html", quote=quote)
