# server.py
# Math tools web application
# Author: Sébastien Combéfis
# Version: February 3, 2016

import os
from bottle import route, run, post, request
import utils

@route('/')
def home():
    return '''<h1>Application Web</h1><br />
           <a href= https://boiling-beach-99041.herokuapp.com/fact>Factorial</a><br />
           <a href= https://boiling-beach-99041.herokuapp.com/roots>Roots</a><br />
           <a href= https://boiling-beach-99041.herokuapp.com/integrate>Integrate</a><br /><br />
           <b>END</b>
           '''

@route('/fact')
def factroute():
    return '''
           <form action= '/fact/result' method= 'post'>
               factorial:
               <input type= 'text' name= 'factorial' /><br /><br />
               <input type= 'submit' value= 'Calulate factorial' /><br /><br />
           </form>
           <a href= https://boiling-beach-99041.herokuapp.com>Home</a>
           '''

@post('/fact/result')
def postfact():
    numinput= int(request.forms.get('factorial'))
    fact= utils.fact(numinput)
    return '''
           the results: {}<br /><br />
           <a href= https://boiling-beach-99041.herokuapp.com>Home</a>
           '''.format(fact)

@route('/roots')
def rootsroute():
    return '''
           <form action= '/roots/result' method= 'post'>
               function to solve: <br />
               f(x)= <input type= 'text' name= 'roots-a' /><b> X² </b><input type= 'text' name= 'roots-b' /><b> X </b><input type= 'text' name= 'roots-c' /><br /><br />
               <input type= 'submit' value= 'Calculate root(s)'>
           </form><br /><br />
           <a href= https://boiling-beach-99041.herokuapp.com>Home</a>
           '''

@post('/roots/result')
def postroots():
    rootsa= int(request.forms.get('roots-a'))
    rootsb= int(request.forms.get('roots-b'))
    rootsc= int(request.forms.get('roots-c'))
    roots= utils.roots(rootsa, rootsb, rootsc)
    return '''
           the results: {}<br /><br />
           <a href= https://boiling-beach-99041.herokuapp.com>Home</a>
           '''.format(str(roots))

@route('/integrate')
def integrateroute():
    return '''
           <form action= '/integrate/result' method= 'post'><br /><br />
               function to integrate: <br />
               <input type= 'text' name= 'function'><br /><br />
               from <input type= 'text' name= 'lower'> to <input type= 'text' name= 'upper'><br /><br />
               <input type= 'submit' value= 'integrate!'>
           </form><br /><br />
           <a href= https://boiling-beach-99041.herokuapp.com>Home</a>
           '''

@post('/integrate/result')
def postintegrate():
    function= request.forms.get('function')
    lower= int(request.forms.get('lower'))
    upper= int(request.forms.get('upper'))
    integrate= round(utils.integrate(function, lower, upper), 2)
    return '''
           the results: {}<br /><br />
           <a href= https://boiling-beach-99041.herokuapp.com>Home</a>
           '''.format(integrate)

run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
