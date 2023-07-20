from flask import Flask, render_template, request, url_for, redirect
from flask import session as login_session
import datetime
import time
app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'

@app.route('/', methods=['GET' , 'POST']) # What methods are needed?
def home():
	if request.method == 'POST':
		try:
			login_session['age'] = int(request.form['age'])
			login_session['author'] = request.form['author']
			current_time = datetime.datetime.now()
			curr_time_hour = time.strftime("%H:%M:%S", time.localtime())
			subtime = f'{current_time.day}/{current_time.month}/{current_time.year} at {curr_time_hour} In GMT +2'
			login_session['quotes'] = {request.form['quote'] : subtime}
			
			return redirect(url_for('thanks')) 
		except:
			return redirect(url_for('error'))
	return render_template('home.html')


@app.route('/error')
def error():

	return render_template('error.html')


@app.route('/display')
def display():

	return render_template('display.html', age=login_session['age'] , author=login_session['author'] , quotes=login_session['quotes'])


@app.route('/thanks')
def thanks():

	return render_template('thanks.html')


if __name__ == '__main__':
	app.run(debug=True)