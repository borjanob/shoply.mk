from flask import Flask, render_template, request,redirect
from datetime import datetime
from flask_mail import Mail, Message

app = Flask(__name__)

mail = Mail()
mail.init_app(app)

username = ''
password = ''
sender = ''
reciever = ''


app.config['MAIL_SERVER'] = 'smtp.mail.yahoo.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = username
app.config['MAIL_PASSWORD'] = password
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False


def send_email(email: str,name:str = 'Unknown', phone: int = None, message: str = 'No message',
             subject: str = 'Web app idea') -> bool:
    
    msg = Message(
        sender= sender,
        body=message,
        recipients=[reciever],
        subject='Test poraka'
    )

    try:
        mail.send(msg)
        print('Message sent!')
        return True
    except Exception as e:
        print(e)
        print('Mail not sent')
        return False


@app.route('/', methods = ['POST','GET'])
def index():

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        number = request.form['phone']
        message = request.form['message']
        is_sent = send_email(email,name,number,message)
        print(is_sent)



    return render_template('mk_index.html')


if __name__ == '__main__':
    app.run(debug=True)