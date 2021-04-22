from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey
import numpy as np
import json

serviceUsername = "apikey-v2-1i2kicj0k7odnjyrmo4u3qczrt8s9q5auipv2mlgf4br"
servicePassword = "ccd7aca2d4ca6de9c4b87c40f99f0d3e"
serviceURL = "https://apikey-v2-1i2kicj0k7odnjyrmo4u3qczrt8s9q5auipv2mlgf4br:ccd7aca2d4ca6de9c4b87c40f99f0d3e@c6a4d803-08cb-4b54-931c-a273030fe7bb-bluemix.cloudantnosqldb.appdomain.cloud"

client = Cloudant(serviceUsername, servicePassword, url=serviceURL)
client.connect()

databaseName = "databasedemo"
myDatabaseDemo = client.create_database(databaseName)
if myDatabaseDemo.exists():
    print("'{0}' successfully created.\n".format(databaseName))

sampleData = [
    [1, "one", "boiling", 100],
    [2, "two", "hot", 40],
    [3, "three", "warm", 20],
    [4, "four", "cold", 10],
    [5, "five", "freezing", 0]
]

document = np.array(sampleData)

# Crear documentos utilizando los datos de ejemplo.
# Examinar cada fila de la matriz para el documento en sampleData:
# Recuperar los campos de cada fila.
number = document[:, 0].tolist()
name = document[:, 1].tolist()
description = document[:, 2].tolist()
temperature = document[:, 3].tolist()

# Crear un documento JSON que represente todos
# los datos de la fila.
jsonDocument = {
    "numberField": number,
    "nameField": name,
    "descriptionField": description,
    "temperatureField": temperature}
# Crear un documento utilizando la API de la base de datos.
newDocument = myDatabaseDemo.create_document(jsonDocument)
# Comprobar que el documento existe en la base de datos.
if newDocument.exists():
    print("Document '{0}' successfully created.".format(number))
