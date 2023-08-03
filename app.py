from flask import Flask, request, render_template
from random import choice
from stories import story 


app = Flask(__name__)

@app.route('/')
def show_promts():
    
    prompts = story.prompts
    return render_template('questions.html', prompts=prompts)

@app.route('/home')
def show_form():
    return render_template('form.html')

@app.route('/story')
def show_story():
    text = story.generate(request.args)

    return render_template('story.html', text=text)