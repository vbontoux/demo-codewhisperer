# create single page website with flask and python showing a lottery
from flask import Flask, render_template
import random
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

# create the index.html content with css
@app.route('/lucky_number')
def lucky_number():
    lucky_number = random.randint(1, 10)
    return render_template('lucky_number.html', lucky_number=lucky_number)

# create a function that returns html code as a string with light blue background
@app.route('/about_me')
def about_me():
    return render_template('about_me.html')

if __name__ == '__main__':
    app.run(debug=True)

