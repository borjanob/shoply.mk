from flask import Flask, render_template, request,redirect
from datetime import datetime
from flask_mail import Mail, Message
import os
#from dotenv import load_dotenv

# TODO: ADD CHOOSE ME BUTTON TO PACKET CARDS
# TODO: ADD POPLAKI/POFALBI
# TODO: ADD USER TESTIMONIALS

app = Flask(__name__)


username = os.environ.get('MAIL_USERNAME')
password = os.environ.get('MAIL_PASSWORD')
sender = os.environ.get('MAIL_USERNAME')
reciever = os.environ.get('MAIL_USERNAME')


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = username
app.config['MAIL_PASSWORD'] = password
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail()
mail.init_app(app)


def send_email(email: str,name:str = 'Unknown', phone: int = None, message: str = 'No message',
             subject: str = 'Web app idea') -> bool:
    
    msg = Message(
        sender= 'obednikovskiborjan@gmail.com',
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