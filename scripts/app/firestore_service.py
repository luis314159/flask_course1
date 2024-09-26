import firebase_admin
import os
from firebase_admin import credentials
from firebase_admin import firestore

#credential = credentials.Certificate("C://luis//flask//scripts//app//clave//flask-436115-373e1bf1bf02.json")
#firebase_admin.initialize_app(credential)
# Establecer la variable de entorno en el código
path= "C://Users//lalmazan//AppData//Roaming//gcloud//application_default_credentials.json"


#path = "C://luis//flask//scripts//app//clave//flask-436115-373e1bf1bf02.json"

#os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = path

# Inicializar la app de Firebase
#cred = credentials.Certificate(os.environ['GOOGLE_APPLICATION_CREDENTIALS'])
#firebase_admin.initialize_app(cred)

#db = firestore.client()


project_id = 'flask-436115'
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
  'projectId': project_id,
})


db = firestore.client()

def get_users():
    return db.collection('users').get()

def get_todos(user_id):
    return db.collection('users')\
    .document(user_id)\
    .collection('todos').get()