from flask import Blueprint, render_template, request, flash, session
#from digital_asisstent import get_the_answer
from chatgpt2 import CustomChatGPT

views = Blueprint(__name__,"views")


####################################################
# ROUTES za new index.html
@views.route("/")
def index():
    # ovime sam dobila da se sve prethodne flash poruke maknu s prozora
    # prilikom povratka na pocetni prozor za unos
    message = session.pop('_flashes', None)

    # flash funkcija omogućuje generiranje poruka koje se mogu prikazati korisnicima kada se izvrši određena akcija, 
    # poput slanja obrasca ili prijave u sustav. 
    flash("Hi, I'm your personal AI asisstent running with OpenAI API.\n How may i help you?")
    return render_template("index.html",message=message)


@views.route("/chatgptanswer", methods=["POST","GET"])
def greet():
    # ovime dohvaćamo input usera
    # unos varijable u zagradama treba odgovarati 
    # name inputu u html dokumentu (<input type="text" name="name_input">)
    # -> request.form['name_input']
    input_from_user = request.form['pitanje']

    # flash pozdravna poruka 
    flash("This is your input: " + str(input_from_user))

    chatgpt_answer =  CustomChatGPT(str(input_from_user))

    return render_template("answer.html", input_text= input_from_user, odgovor = chatgpt_answer)


