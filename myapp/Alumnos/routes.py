from flask import Blueprint

alumnos=Blueprint('alumnos',__name__)

@alumnos.route('/getalumnos',methods=['GET'])
def getalumnos():
    return {'key':'Alumnos'}