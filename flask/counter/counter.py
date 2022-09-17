from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key = 'secret key'


@app.route('/')

def counter():
  if 'times' not in session:
    session['times'] = 0
  else:
    session['times'] += 1
  return render_template('index.html', times = session['times'])

@app.route('/count', methods=['POST'])
def count():
  if request.form['alter'] == 'add':
    session['times'] += 1
  elif request.form['alter'] == 'reset':
    session['times'] = 0
  return redirect('/')


@app.route('/destroy_session')
def destroy_session():
  session.clear()
  return redirect('/')


if __name__ == '__main__':
  app.run(debug=True)