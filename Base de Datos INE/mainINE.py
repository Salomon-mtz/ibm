from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey
import numpy as np
import json
from generadorBaseDatosINE import generarBaseDatos

serviceUsername = "apikey-v2-1i2kicj0k7odnjyrmo4u3qczrt8s9q5auipv2mlgf4br"
servicePassword = "ccd7aca2d4ca6de9c4b87c40f99f0d3e"
serviceURL = "https://apikey-v2-1i2kicj0k7odnjyrmo4u3qczrt8s9q5auipv2mlgf4br:ccd7aca2d4ca6de9c4b87c40f99f0d3e@c6a4d803-08cb-4b54-931c-a273030fe7bb-bluemix.cloudantnosqldb.appdomain.cloud"

client = Cloudant(serviceUsername, servicePassword, url=serviceURL)
client.connect()

databaseName = "databasedemo"
myDatabaseDemo = client.create_database(databaseName)
if myDatabaseDemo.exists():
    print("'{0}' successfully created.\n".format(databaseName))

sampleData = generarBaseDatos(500)

document = np.array(sampleData)

# Crear documentos utilizando los datos de ejemplo.
# Examinar cada fila de la matriz para el documento en sampleData:
# Recuperar los campos de cada fila.
nombre = document[:, 0].tolist()
apellidoP = document[:, 1].tolist()
apellidoM = document[:, 2].tolist()
curp = document[:, 3].tolist()
domicilio = document[:, 4].tolist()
claveElectoral = document[:, 5].tolist()

# Crear un documento JSON que represente todos
# los datos de la fila.
jsonDocument = {
    "nombre": nombre,
    "apellidoP": apellidoP,
    "apellidoM": apellidoM,
    "curp": curp,
    "domicilio": domicilio,
    "claveElectoral": claveElectoral}
# Crear un documento utilizando la API de la base de datos.
newDocument = myDatabaseDemo.create_document(jsonDocument)
# Comprobar que el documento existe en la base de datos.
if newDocument.exists():
    print("Document '{0}' successfully created.".format(nombre))
