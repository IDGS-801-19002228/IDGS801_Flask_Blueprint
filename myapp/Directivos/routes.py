from flask import Blueprint

directivos=Blueprint('directivos',__name__)

@directivos.route('/getdirectivos',methods=['GET'])
def getdirectivos():
    return {'key':'Directivos'}