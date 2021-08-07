from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_DEBUG'] = True
app.config['MAIL_USERNAME'] = 'lees82880@gmail.com'
app.config['MAIL_PASSWORD'] = 'lees959595'
app.config['MAIL_DEFAULT_SENDER'] = 'lees82880@gmail.com'  # Who is gonna send ur email
app.config['MAIL_MAX_EMAILS'] = 5
app.config['MAIL_SUPPRESS_SEND'] = False
app.config['MAIL_ASCII_ATTACHMENTS'] = False

mail = Mail(app)


@app.route('/')
def index():
    msg = Message('Hello', recipients=['jilof73039@697av.com'])
    msg.body = 'Hello test'
    # Use Body for simpler messages and body for more complicated messages
    mail.send(msg)

    return "Message has been send"


if __name__ == '__main__':
    app.run()
