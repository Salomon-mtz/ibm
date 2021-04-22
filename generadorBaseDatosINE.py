
from random import randrange
import random

mujeres= ['MARIA', 'ROCIO', 'JESSICA', 'NOEMI', 'PAULA', 'FATIMA', 'ANTONIA','LAURA', 'SONIA','LUCIA']
hombres= ['JUAN','PEDRO', 'JOSE', 'ANTONIO', 'AGUSTIN',
'PABLO', 'ALEJANDRO','RICARDO', 'JAVIER', 'MANUEL', 'LUIS','PACO', 'JAIME', 'RAFAEL']

def Estado():
  Estado = [
	'DF'
  ]
  return Estado[randrange(0, len(Estado))]

def Nombre():
    Nombre = ['Juan','Pedro', 'Maria', 'Rocio', 'Jose', 'Antonio', 'Agustin',
          'Pablo', 'Alejandro', 'Jessica', 'Noemi', 'Paula', 'Fatima',
          'Antonia', 'Ricardo', 'Javier', 'Manuel', 'Luis', 'Laura', 'Sonia',
          'Paco', 'Lucia', 'Jaime', 'Rafael']
    return Nombre[randrange(0,len(Nombre))].upper()
 
def Apellidos_P():
    Apellidos_P = ['Gomez','Troncoso', 'Fernandez', 'Castaño', 'Morales', 'Alcedo',
            'Parodi','Torres', 'Aguilar', 'Sauco', 'Mangano', 'Ruiz', 'Aragon',
          'Candon', 'Acosta', 'Cabeza', 'Soto', 'Ezequiel', 'Pericacho', 'Rodriguez']
    return Apellidos_P[randrange(0,len(Apellidos_P))].upper()

def Apellidos_M():
    Apellidos_M = ['Gomez','Troncoso', 'Fernandez', 'Castaño', 'Morales', 'Alcedo',
            'Parodi','Torres', 'Aguilar', 'Sauco', 'Mangano', 'Ruiz', 'Aragon',
          'Candon', 'Acosta', 'Cabeza', 'Soto', 'Ezequiel', 'Pericacho', 'Rodriguez']
    return Apellidos_M[randrange(0,len(Apellidos_M))].upper()

def Fecha():
  dia=random.randint(0o1, 31)
  mes=random.randint(0o1, 12)
  anio=random.randint(0o1, 99)
  if mes == 2:
    if dia>=28:
      dia=28
      if mes == 4:
        if dia==31:
          dia=30
          if mes == 6:
            if dia==31:
              dia=30
              if mes == 9:
                if dia==31:
                  dia=30
                if mes == 11:
                  if dia==31:
                    dia=30

  if(mes >= 0 and mes <=9):
    mes = "0"+str(mes)

  if(dia >= 0 and dia <=9):
    dia = "0" + str(dia)
  return (str(anio)+str(mes)+str(dia))


def Genero(nombre):
  for i in range(len(hombres)):
    if(nombre == hombres[i]):
      return "M"
    else:
      None
  for i in range(len(mujeres)):
    if(nombre == mujeres[i]):
      return "F"
    else:
      None

def curp(nombre, apellidoP, apellidoM, genero, fecha, estado):
  name= [nombre]
  consonantes=["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P","Q", "R", "S", "T", "V", "X", "Y", "Z"]
  for j in range(1, len(nombre)):
    for i in range(len(consonantes)):
      if(name[0][j] == consonantes[i]):
        internaNombre = consonantes[i]
        break
    else:
        continue
    break

  for i in range (1):
    letraNombre= name[i][i]
  
  apellidoPaterno = [apellidoP]
  for i in range(1):
    letrasApellidoP= apellidoPaterno[i][i]+ apellidoPaterno[i][i+1]

  for j in range(2, len(apellidoP)):
    for i in range(len(consonantes)):
      if(apellidoPaterno[0][j] == consonantes[i]):
        internaApellidoPaterno = consonantes[i]
        break
    else:
        continue
    break
  
  apellidoMaterno = [apellidoM]
  for i in range(1):
    letrasApellidoM= apellidoMaterno[i][i]

  for j in range(1, len(apellidoM)):
    for i in range(len(consonantes)):
      if(apellidoMaterno[0][j] == consonantes[i]):
        internaApellidoMaterno = consonantes[i]
        break
    else:
      continue
    break

  generoCurp = genero
  fechaCurp = fecha 
  estadoCurp = estado
  homoclave = ["A", "0"]
  h=homoclave[randrange(0,len(homoclave))]
  verificador = str(randrange(0,10))
  return(str(letrasApellidoP) + str(letrasApellidoM) + str(letraNombre) + str(fechaCurp) + str(generoCurp) + str(estadoCurp) + str(internaNombre)) + str(internaApellidoPaterno) + str(internaApellidoMaterno)+ str(h) + str(verificador)
  
def claveElector(nombre, apellidoP, apellidoM, genero, fecha, estado):
  consonantes=["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P","Q", "R", "S", "T", "V", "X", "Y", "Z"]
  name= [nombre]
  apellidoPaterno = [apellidoP]
  apellidoMaterno = [apellidoM]
  
  for j in range(1, len(nombre)):
    for i in range(len(consonantes)):
      if(name[0][j] == consonantes[i]):
        internaNombre = consonantes[i]
        break
    else:
        continue
    break

  for i in range (1):
    letraNombre= name[i][i]

  componenteNombre= str(letraNombre)+str(internaNombre)

  for i in range(1):
      letraApellidoP= apellidoPaterno[i][i]

  for j in range(1, len(apellidoP)):  
    for i in range(len(consonantes)):
      if(apellidoPaterno[0][j] == consonantes[i]):
        internaApellidoPaterno = consonantes[i]
        break
    else:
        continue
    break
  
  componenteApellidoP = str(letraApellidoP) + str(internaApellidoPaterno)
  
  for i in range(1):
    letrasApellidoM= apellidoMaterno[i][i]

  for j in range(1, len(apellidoM)):
    for i in range(len(consonantes)):
      if(apellidoMaterno[0][j] == consonantes[i]):
        internaApellidoMaterno = consonantes[i]
        break
    else:
        continue
    break
  
  componenteApellidoM = str(letrasApellidoM) + str(internaApellidoMaterno)
  
  fechaINE = fecha
  generoINE= genero
  claveEstado = "09"
  verificador = str(randrange(1,10)) + "00"
  
  return (componenteApellidoP + componenteApellidoM + componenteNombre + fechaINE + claveEstado + generoINE + verificador) 
  
def Domicilio():
  delegaciones=["Magdalena Contreras", "Cuajimalpa"]
  return delegaciones[randrange(0,len(delegaciones))].upper()

def generarPersona():
  nom = Nombre()
  apellidoP= Apellidos_P()
  apellidoM = Apellidos_M()
  fechaNac = Fecha()
  generoPersona = Genero(nom)
  estadoPersona= Estado()
  domicilio = Domicilio()
  Curp = curp(nom, apellidoP, apellidoM, generoPersona, fechaNac, estadoPersona)
  claveElectoral = claveElector(nom, apellidoP, apellidoM, generoPersona, fechaNac, estadoPersona)
  Persona=[nom, apellidoP, apellidoM, Curp, domicilio, claveElectoral]
  return(Persona)

def generarBaseDatos(numDePersonas):
  baseDeDatos = []
  for i in range(numDePersonas):
    persona=generarPersona()
    baseDeDatos.append(persona)
  return baseDeDatos

