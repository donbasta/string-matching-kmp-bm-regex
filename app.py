from flask import Flask, render_template, request, redirect

app = Flask(__name__)
key = None
news = []

@app.route('/', methods=['POST', 'GET'])
def index():

	global key

	if request.method == 'POST':
		key = request.form['keyword']
		print(key)
		return redirect('/')
	else:
		return render_template("index.html", keyword=key)
		

# @app.route('')


if __name__ == "__main__":
	app.run(debug=True)