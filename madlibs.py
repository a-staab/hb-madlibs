from random import choice

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Save hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)


@app.route('/game')
def show_madlib_form():
    """Gets user's answer whether they would like to play a
    game and, depending whether yes or no, directs them to a goodbye page or the
    game.
    """

    answer = request.args.get("game-choice")

    if answer == "No":
        return render_template("goodbye.html")
    else:
        return render_template("game.html")


@app.route('/madlib')
def show_madlib():
    """Displays the madlib with the words the user input via the form"""

    mad_name = request.args.get("person")
    mad_color = request.args.get("color")
    mad_noun = request.args.get("noun")
    mad_planet = request.args.get("planet")
    mad_adverb = request.args.get("adverb")
    mad_adjectives = request.args.getlist("adjectives")

    return render_template("madlib.html",
                           person=mad_name,
                           color=mad_color,
                           noun=mad_noun,
                           planet=mad_planet,
                           adverb=mad_adverb,
                           adjectives=mad_adjectives,
                           )


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
