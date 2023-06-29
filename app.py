from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)

@app.route("/")
# Generates form and prompts user for different words for madlib
def madlibs(): 
    words = story.prompts
    return render_template("index.html", words=words)

@app.route("/story")
# Returns story result with words that user has provided
def get_story():
    text = story.generate(request.args)
    return render_template("story.html", text=text)