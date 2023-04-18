from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages.db'
db = SQLAlchemy(app)


@app.route("/")
def index():
    print(1111111111111)
    return render_template('index.html')


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    message = db.Column(db.String(500), nullable=False)


@app.route('/submit_form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        print("fgcf",message)
        new_message = Message(name=name, email=email, message=message)
        db.session.add(new_message)
        db.session.commit()
        return render_template('index.html')
    else:
        return 'Error'


@app.route('/messages')
def messages():
    messages = Message.query.all()
    return render_template('messages.html', messages=messages)


if __name__ == "__main__":
    app.run(debug=True)

#
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages.db'
# db = SQLAlchemy(app)
#
#
# class Message(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), nullable=False)
#     email = db.Column(db.String(120), nullable=False)
#     message = db.Column(db.String(500), nullable=False)
#
#
# @app.route('/')
# def index():
#     name = "Nurullah"
#     surname = "Kayahan"
#     email = "nrllhkyhn@gmail.com"
#     personal_info = "Yazılım mühendisiyim. Python dili uzmanlık alanım. " \
#                     "Pamukkale Üniversitesi elektrik elektronik mühendisliği öğrencisiyim."
#     return render_template('index.html', name=name, surname=surname, email=email, personal_info=personal_info)
#
#
# @app.route('/submit_form', methods=['POST'])
# def submit_form():
#     if request.method == 'POST':
#         name = request.form['name']
#         email = request.form['email']
#         message = request.form['message']
#         new_message = Message(name=name, email=email, message=message)
#         db.session.add(new_message)
#         db.session.commit()
#         return render_template('thankyou.html')
#     else:
#         return 'Error'
#
#
# @app.route('/thankyou')
# def thankyou():
#     return render_template('thankyou.html')
#
#
# @app.route('/messages')
# def messages():
#     messages = Message.query.all()
#     return render_template('messages.html', messages=messages)
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
