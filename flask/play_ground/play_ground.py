from flask import Flask, render_template

app = Flask(__name__, template_folder='./templates')

@app.route('/')
def welcome():
  return 'welcome to playground'

@app.route('/play')
def play():
  return render_template('index.html', box="hi from box", times=3)

@app.route('/play/<int:times>')
def play_times(times):
  return render_template('index.html', box="hi from box", times=times)

@app.route('/play/<int:times>/<color>')
def play_with_color(times, color):
  return render_template('index.html', color=color, times=times)
if __name__=='__main__':
  app.run(debug=True)