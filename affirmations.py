pip install flask-ask
import logging
import random
from random import randint
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)

@ask.launch

def affirmations():
  WELCOME = (render_template('welcome_1'), render_template('welcome_2'), render_template('welcome_3'))
  welcome = random.choice(WELCOME)
  @ask.intent(YesIntent)
  def operation_distraction():
    if choice == (welcome_1):
#not sure answer function will return specific joke
      def toddler_joke():
      JOKES = (render_template('joke_1'), render_template('joke_2), render_template('joke_3'), render_template('joke_4'))
      joke = random.choice(JOKES)
      return question(joke)
      @ask.intent("JokeIntent")
      def joke_answer():
        if choice == (joke_1):
          return statement(answer_1)
        if choice == (joke_2):
          return statement(answer_2)
        if choice == (joke_3):
          return statement(answer_3)
        if choice == (joke_4):
          return statement(answer_4)
        if choice == (joke_5):
          return statement(answer_5)
# welcome_2 = song.     
    elif choice == (welcome_2)
	def sad_song():

    elif choice == (welcome_3)
      def simon_says():
        SIMON = (render_template(simon_1), render_template(simon_2), render_template(simon_3), render_template(simon_4)
        simon = random.choice(SIMON)
        return statement(simon)
        <break time="7s"/>
        return statement(simon)
        <break time="7s"/>
        return statement(simon)
        <break time="7s"/>
        return statment(render_template(good_job))




