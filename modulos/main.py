"""los modulos son partes de un programa que se encargan de realizar una tarea en particular
los modulos se encuentran en el directorio de la aplicacion"""

#import: se usa para importar modulos
#from: se usa para importar modulos

import mensaje as msg #se puede usar el alias msg para importar el modulo mensaje
msg.saludar()
msg.despedir()

from mensaje import saludar, despedir #se nombran las funciones que se quieren importar
from mensaje import * #se puede usar * para importar todas las funciones de un modulo

saludar()
despedir()

help("modules") #se puede usar help para ver la documentacion de un modulo