from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')
@app.route('/account')
def account():
    return render_template('account.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/Subscription')
def Subscription():
    return render_template('Subscription.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')


if __name__ == '__main__':
    app.run()
