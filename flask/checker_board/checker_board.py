from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def show_board():
  return render_template('index.html', x=4, y=4)

@app.route('/4')
def show_8_by_4():
  return render_template('index.html', x=4, y=2)

@app.route('/<int:x>/<int:y>')
def board_x_y(x, y):
  return render_template('index.html', x=int(x/2), y=int(y/2))

if __name__ == '__main__':
  app.run(debug=True)