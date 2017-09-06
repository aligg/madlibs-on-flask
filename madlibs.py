"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)


@app.route('/game/<player>')
def show_madlib_form(player):
    """Gets users response if they're up for a game"""

    answer = request.args.get("gameable")


    compliment = choice(AWESOMENESS)

    if answer == 'no':
        return render_template("goodbye.html",
                                person=player)
    else:
        return render_template("game.html",
                                person=player,
                                compliment=compliment)



@app.route('/madlib/<player>')
def show_madlib(player):
    """Displays the libbed result"""

    color = request.args.get("color")
    aperson = request.args.get("aperson")
    noun = request.args.get("noun")
    adjective = request.args.get("adjective")
    animals = request.args.getlist("animals")

    animal_choice = choice(animals)


    return render_template("madlib.html",
                            person=player,
                            color=color,
                            noun=noun,
                            adjective=adjective,
                            aperson=aperson,
                            animals=animal_choice)





if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
