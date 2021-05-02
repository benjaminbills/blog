from flask import render_template, request, redirect, url_for, flash
from . import main
from ..requests import get_quote
from flask_login import login_required, current_user
from .. import db
from .forms import BlogForm
from ..models import Blog
import markdown2


@main.route("/")
def index():
    """
    View root page function that returns the index page and its data
    """
    quote = get_quote()
    blogs = Blog.query.filter_by()
    if blogs is None:
        abort(404)
    format_blogs = markdown2.markdown(
        blogs.blog_content, extras=["code-friendly", "fenced-code-blocks"]
    )
    return render_template(
        "index.html", blogs=blogs, format_blogs=format_blogs, quote=quote
    )


@main.route("/new_blog", methods=["GET", "POST"])
@login_required
def new_blog():
    form = BlogForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        user_id = current_user._get_current_object().id
        new_blog = Blog(title=title, blog_content=content, user_id=user_id)
        new_blog.save_blog()
        return redirect(url_for(".index"))
    return render_template("new_post.html", post_form=form)
