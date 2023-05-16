from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///register.db'
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'registered users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(30), nullable=False, unique=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Registration %r' % self.id


@app.route('/')
def main():
    return render_template("main.html")


@app.route('/registration-form', methods=['POST', 'GET'])
def registrate_page():
    return render_template("singInScreen.js")

def add_registrated_user_data():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        user = User(email=email, username=username, password=password)
        try:
            db.session.add(user)
            db.session.commit()
            return  redirect('/')
        except:
            return "Помилка при реєстрації."
    else:
        return render_template("registration-form.html")


@app.route('/login-form', methods=['POST', 'GET'])
def login_page():
    return render_template("login-form.html")

def log_user_in():
    if request.method == 'POST':
        try:
            if User.objects.get(username=request.form['username']).exist and \
                    User.objects.get(password=request.form['password']).exist:
                return True
            else:
                return False
        except:
            return IOError
    else:
        return render_template("login-form.html")



if __name__ == '__main__':
    app.run(host='localhost', port=5001, debug=True)
with app.app_context():
    db.create_all()
