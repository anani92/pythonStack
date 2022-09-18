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


@app.route('/<int:x>/<int:y>/<color_x>/<color_y>')
def board_with_colors(x, y,color_x, color_y):
  return render_template('index.html', x=int(x/2), y=int(y/2), color_x = color_x, color_y = color_y)

if __name__ == '__main__':
  app.run(debug=True)