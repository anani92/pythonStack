from flask import Flask, session, render_template, request, redirect
import random
import datetime


app = Flask(__name__)
app.secret_key = 'getgold'


@app.route('/')
def play():
  if 'gold' not in session:
    session['gold'] = 1
  if 'activity_log' not in session:
    print('we found nothing')
    session['activity_log'] = []

  activity_log = session['activity_log']
  gold_count = session['gold']
  return render_template('index.html', activity_log=activity_log, gold=gold_count)

@app.route('/process_money', methods=['POST'])
def process_money():
  luck = random.randrange(1,3)

  if request.form['mine'] == 'farming':
    gold_val = random.randint(1,9)
    if luck == 1:
      session['gold'] += gold_val
      date_time = datetime.datetime.now()
      timestamp = date_time.strftime('%B %d %y %U:%M %p')
      event_log = f' you won {str(gold_val)} from farming! {str(timestamp)}'
      session['activity_log'].append(event_log)
    elif luck == 2:
      session['gold'] -= gold_val
      date_time = datetime.datetime.now()
      timestamp = date_time.strftime('%B %d %y %U:%M %p')
      event_log = f'<p class="text text-danger"> you lost {str(gold_val)} from farming ({str(timestamp)})</p>'
      session['activity_log'].append(event_log)


  elif request.form["mine"] == "caving":
    gold_val = random.randint(5,11)
    if luck == 1:
      session['gold'] += gold_val
      date_time = datetime.datetime.now()
      timestamp = date_time.strftime('%B %d %y %U: %M %p')
      event_log = f'<p class="text text-danger"> You won {str(gold_val)} from caving ({str(timestamp)})</p>'
      session['activity_log'].append(event_log)
    elif luck == 2:
      session['gold'] -= gold_val
      date_time = datetime.datetime.now()
      timestamp = date_time.strftime('%B %d %y %U: %M %p')
      event_log = f'<p class="text text-danger"> You lost {str(gold_val)} from caving ({str(timestamp)})</p>'
      session['activity_log'].append(event_log)

  elif request.form['mine'] == 'looting':
    gold_val = random.randint(2,6)
    if luck == 1:
      session['gold'] += gold_val
      date_time = datetime.datetime.now()
      timestamp = date_time.strftime('%B %d %y %U: %M %p')
      event_log = f'<p class="text text-success"> You won {str(gold_val)} from looting ({str(timestamp)})</p>'
      session['activity_log'].append(event_log)
    if luck == 2:
      session['gold'] -= gold_val
      date_time = datetime.datetime.now()
      timestamp = date_time.strftime('%B %d %y %U: %M %p')
      event_log = f'<p class="text text-danger"> You lost {str(gold_val)}, looting today was costly ({str(timestamp)})</p>'
      session['activity_log'].append(event_log)

  elif request.form['mine'] == 'casino-play':
    gold_val = random.randint(10, 100)
    if luck == 1:
      session['gold'] += gold_val
      date_time = datetime.datetime.now()
      timestamp = date_time.strftime('%B %d %y %U: %M %p')
      event_log = f'<p class="text text-success"> You won {str(gold_val)} from casino ({str(timestamp)})</p>'
      session['activity_log'].append(event_log)
    if luck == 2:
      session['gold'] -= gold_val
      date_time = datetime.datetime.now()
      timestamp = date_time.strftime('%B %d %y %U: %M %p')
      event_log = f'<p class="text text-danger"> You lost {str(gold_val)} from casino ({str(timestamp)})</p>'
      session['activity_log'].append(event_log)

  return redirect('/')


@app.route('/restart')
def restart():
  session.clear()
  return redirect('/')


if __name__ == '__main__':
  app.run(debug=True)