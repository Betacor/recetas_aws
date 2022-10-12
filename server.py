from flask_app import app

#Importar controlador
from flask_app.controllers import users_controller, recipes_controller #<-igual al nombre de archivo en controllers

#Ejecutamos variable app
if __name__=="__main__":
    app.run(debug=True)
