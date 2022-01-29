import random
from flask import *
app=Flask(__name__)
@app.route('/error',methods=['GET','POST'])
def error():
	urlget=request.url
	urlget=urlget.split('?')
	if request.method=='GET':
		try:
			with open('user.txt','a') as f:
				f.write(urlget[1]+'\n')
			d=random.randint(1000,10000)
			return render_template('index.html',d=d)
		except Exception as e:
			try:
				open('user.txt','x')
			except:
				pass
			print(str(e))
			return redirect(url_for('login'))

	else:
		return redirect(url_for('login'))
@app.route('/',methods=['GET'])
def home():

    return render_template("m.html")
if __name__=='__main__':
	app.run(debug=True)