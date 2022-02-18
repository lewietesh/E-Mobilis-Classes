# sending a simple email tutorial
from flask import Flask
from flask_mail import Mail,Message
# the message class encapsulates an email message
# mail class manages the email-messaging requirements


app = Flask(__name__)


# configuration of mail

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT']= 465
app.config['MAIL_USERNAME'] = 'lewismutembei001@gmail.com'
app.config['MAIL_PASSWORD'] = 'Lewis668@'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['DEBUG'] =True
app.config['TESTING'] =False
app.config['MAIL_MAX_EMAILS'] = None
app.config['MAIL_ASCII_ATTACHMENTS'] = False

mail = Mail(app)

# message object mapped to a particular url
@app.route('/')
def index():
    msg = Message(
        'Did I just send you an email',
        sender= 'lewismutembei001@gmail.com',
        recipients = ['teshlewie668@gmail.com']
    )
    mail.send(msg)
    return "Hurray I just sent someone an email"

if __name__ == "__main__":
    app.run()
