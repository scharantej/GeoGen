
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

class ContactForm(FlaskForm):
    name = StringField('Name')
    email = StringField('Email')
    message = StringField('Message')
    submit = SubmitField('Send')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/solutions')
def solutions():
    return render_template('solutions.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            name = request.form.get('name')
            email = request.form.get('email')
            message = request.form.get('message')
            return render_template('contact.html', name=name, email=email, message=message)
    return render_template('contact.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
