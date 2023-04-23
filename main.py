from flask import *
# from flask_ngrok import run_with_ngrok
app = Flask(__name__)
# run_with_ngrok(app)  # Start ngrok when app is run

@app.route('/')
def first():
    return render_template('index.html')


@app.route('/login',methods=['POST'])
def login():
    uname=request.form['unmae']
    email=request.form['email']
    password=request.form['password']
    if email=='test@gmail.com' and password=='admin':
        return render_template('admin.html',data=email)
    else:
        return 'login failed'




if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(debug=True)
