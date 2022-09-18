from flask import Flask

app = Flask(__name__)

@app.route('/')

def hello_world():
  return 'hello world!'

@app.route('/dojo')
def dojo():
  return 'Dojo!'

@app.route('/say/<name>')
def say_hi(name):
  return f'Hi {name}!'



@app.route('/repeat/<int:num>/hello')
def hello(num):
  return 'hello ' * num

@app.route('/repeat/<int:num>/bye')
def bye(num):
  return 'bye ' * num

@app.route('/repeat/<int:num>/dogs')
def dogs(num):
  return 'dogs ' * num
@app.route('/<badRequest>')
def handle_bad_request(badRequest):
  return 'Sorry! No response. try again '
if __name__ == '__main__':
  app.run(debug=True)
