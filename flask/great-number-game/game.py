from crypt import methods
from flask import Flask,render_template, redirect, request, session, Markup
import random
app = Flask(__name__)
app.secret_key = 'greatnumgame'

@app.route('/')
def guess_game():
  guess = random.randint(0,100)
  if 'guess' not in session:
    session['guess'] = guess
  return render_template('index.html')

@app.route('/guess', methods=['POST'])
def check_input():
  input_value = request.form.get('guess_input')
  input_value = int(input_value)
  random_guess = session['guess']
  box_color = ''
  box_text = ''
  reset_button = ''
  if input_value == random_guess:
    box_color = 'green'
    box_text = 'wow you guessed it right'
    reset_button = Markup('<a href="/"><button type="submit" class="btn btn-primary subbut" value="Submit">Try Again</button><a>')
    session.clear()

    return render_template('index.html', box_color=box_color, box_text=box_text, reset_button=reset_button)
  if input_value > random_guess:
    box_color = 'red'
    box_text = 'too High'
    return render_template('index.html', box_color=box_color, box_text=box_text, reset_button=reset_button)

  if input_value < random_guess:
    box_color = 'blue'
    box_text = 'too Low'
    return render_template('index.html', box_color=box_color, box_text=box_text)






if __name__ == '__main__':
  app.run(debug=True, port=5000)
