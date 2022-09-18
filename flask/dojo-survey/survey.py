from distutils.log import debug
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/result', methods=['POST'])
def create_user():
  print('*' * 30)
  print('user info recieved')
  print(request.form)
  name = request.form['name']
  comment = request.form['comment']
  language = request.form['language']
  location = request.form['location']
  email = request.form['email']
  return render_template('show.html', name=name, comment=comment, language=language, location=location, user_email=email)



if __name__ == '__main__':
  app.run(debug=True)

