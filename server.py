# server.py
# Math tools web application
# Author: Sébastien Combéfis
# Version: February 3, 2016

import os
from bottle import route, run, post
import utils

@route('/')
def home():
    return '''<h1>Application Web</h1>
           <a href= https://boiling-beach-99041.herokuapp.com/fact>Factorial</a>
           <a href= https://boiling-beach-99041.herokuapp.com/roots>Roots</a>
           <a href= https://boiling-beach-99041.herokuapp.com/integrate>Integrate</a>
           <b>END</b>
           '''

@route('/fact')
def factroute():
    return '''
           <form action= '/fact/result' method= 'post'>
               factorial:
               <input type= 'text' name= 'factorial' />
               <input type= 'submit' value= 'Calulate factorial' />
           </form>
           '''

@post('/fact/result')
def postfact():
    numinput= request.forms.get('factorial')
    fact= utils.fact(numinput)
    return '''
           the results {}
           '''.format(fact)

run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
