from flask import render_template, request, redirect, url_for, flash
from . import main
from ..requests import get_quote
from flask_login import login_required, current_user
from .. import db
from .forms import BlogForm


@main.route("/")
def index():
    """
    View root page function that returns the index page and its data
    """
    quote = get_quote()
    return render_template("index.html", quote=quote)


@main.route("/new_blog")
def new_blog():
    form = BlogForm()
    if form.validate_on_submit():
        print("Yes")

    return render_template("new_post.html", post_form=form)
