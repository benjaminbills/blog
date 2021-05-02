from flask import render_template, request, redirect, url_for, flash
from . import main
from ..requests import get_quote
from flask_login import login_required, current_user
from .. import db
from .forms import BlogForm, CommentForm
from ..models import Blog, Comment
import markdown2


@main.route("/")
def index():
    """
    View root page function that returns the index page and its data
    """
    quote = get_quote()
    blogs = Blog.query.filter_by()
    return render_template("index.html", blogs=blogs, quote=quote)


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


@main.route("/blog/<int:id>")
def single_blog(id):
    blog = Blog.query.get(id)
    if blog is None:
        abort(404)
    format_blog = markdown2.markdown(
        blog.blog_content, extras=["code-friendly", "fenced-code-blocks"]
    )
    return render_template("blog.html", format_blog=format_blog)


@main.route("/comment/new/<int:blog_id>", methods=["GET", "POST"])
@login_required
def new_comment(blog_id):
    form = CommentForm()
    blog = Blog.query.get(blog_id)
    if form.validate_on_submit():
        description = form.description.data
        new_comment = Comment(
            description=description,
            user_id=current_user._get_current_object().id,
            blog_id=blog_id,
        )
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for(".new_comment", blog_id=blog_id))
    all_comments = Comment.query.filter_by(blog_id=blog_id).all()
    return render_template("comments.html", form=form, comment=all_comments, blog=blog)


@main.route("/comment/delete/<int:id>/<int:blog_id>")
def delete_comment(id, blog_id):
    comment = Comment.query.filter_by(id=id).first()
    db.session.delete(comment)
    db.session.commit()
    return redirect(url_for(".new_comment", blog_id=blog_id))
