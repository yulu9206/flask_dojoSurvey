from flask import Flask, request, redirect, render_template  # Import Flask to allow us to create our app.
app = Flask(__name__)    # Global variable __name__ tells Flask whether or not we are running the file
                         # directly, or importing it as a module.
@app.route('/')          # The "@" symbol designates a "decorator" which attaches the following
                         # function to the '/' route. This means that whenever we send a request to
                         # localhost:5000/ we will run the following "hello_world" function.
def index():       
  return render_template('index.html') # Return 'Hello World!' to the response.

@app.route('/info', methods = ['POST'])
def info():
	name = request.form['name']
	location = request.form['location']
	language = request.form['language']
	comment = request.form['comment']
	return	render_template('info.html', name = name, location = location, language = language, comment = comment)
app.run(debug=True) 
