from flask import Flask, request
from flask import render_template
import svm_test
app=Flask(__name__,static_url_path='/flask')

@app.route('/')
def index():
	print('Hello world!')
	return render_template('/index.html')
@app.route('/dysg.html')
def dysg():
	print("hello")
	return render_template('/dysg.html')
@app.route('/audi.html')
def audi():
	return render_template('/audi.html')
@app.route('/anxi.html')
def anxi():
	return render_template('/anxi.html')
if __name__=="__main__":
	app.run(debug=True)
@app.route('/submit-answer', methods = ['POST'])
def getFormData():
	if request.method == 'POST':
		data = request.form
		svm_test.main(data)
	return render_template('some-template')