from flask_mail import Message
from flask import render_template
from . import mail

sender_email = "oneobaben@gmail.com"


def mail_message(subject, template, to):

    email = Message(subject, sender=sender_email, recipients=to)
    email.body = render_template(template + ".txt")
    email.html = render_template(template + ".html")
    mail.send(email)
