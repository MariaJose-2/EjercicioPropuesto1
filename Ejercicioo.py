#importamos libreria para la fecha y la tome directamente del sistema (dia/mes/año)(hora,segundos) del módulo 'datetime'
from datetime import datetime

# Define una clase llamada 'InventarioEquipos'
class InventarioEquipos:
    #Metodo 'init' constructor de la clase
    def __init__(self):
        # Inicializa un diccionario vacio para almacenar la inormacion de los equipos
        self.equipos = {}
        # Inicializa una lista vacía para almacenar las novedades de los equipos
        self.novedades = []

    #Metodo para agregar un nuevo equipo al inventario
    #pasa de ser una funcion a ser un metodo ya que esta dentro de una clase y opera en la instancia actual de la clase InventarioEquipos como self
    def agregarEquipo(self):
        #Solicita al usuario ingresar el ID del equipo
        equipoId = input("Ingrese el ID del equipo: ")
        #Solicita al usuario ingresar el numero del ambiente al que pertenece el equipo
        nAmbiente = int(input("Ingrese el numero del ambiente al que pertenece: "))
        #Solicita al usuario ingresar si el equipo tiene cargador (si/no) y convierte la respuesta a minusculas mediante el .lower
        disCargador = input("¿Tiene cargador? si/no: ").lower()
        #Solicita al usuario ingresar si el equipo tiene mouse (si/no) y convierte la respuesta a minusculas mediante el .lower
        disMouse = input("¿Tiene mouse? si/no: ").lower()
        #Almacena la informacion del equipo en el diccionario 'equipos'
        self.equipos[equipoId] = {"cargador": disCargador, "mouse": disMouse, "ambiente": nAmbiente}
        #Imprime un mensaje indicando que el equipo ha sido agregado
        print("Equipo agregado")

    #Metodo para agregar una novedad a un equipo existente
    def agregarNovedad(self):
        #Solicita al usuario ingresar el ID del equipo al que desea agregar la novedad
        equipoId = input("Ingrese el ID del equipo al que desea agregar una novedad: ")
        #Verifica si el equipo existe en el inventario
        if equipoId in self.equipos:
            #Solicita al usuario ingresar la descripcion de la novedad
            descripcion = input("Ingrese la descripcion de la novedad: ")
            #Agrega la novedad a la lista 'novedades' con informacion sobre el equipo, la fecha y la descripcion
            self.novedades.append({"equipo ID": equipoId, "fecha": str(datetime.now()), "descripcion": descripcion})
            #Imprime un mensaje indicando que la novedad ha sido agregada
            print("Novedad agregada")
        else:
            #Imprime un mensaje indicando que el equipo no fue encontrado en la lista
            print("Equipo no encontrado en la lista")

    #Metodo para buscar y mostrar la informacion de un equipo en el inventario
    def buscarEquipo(self):
        #Solicita al usuario ingresar el ID del equipo que desea buscar
        equipoId = input("Ingrese el ID del equipo que desea buscar: ")
        #Verifica si el equipo existe en el inventario
        if equipoId in self.equipos:
            # Muestra la información del equipo
            print(self.equipos[equipoId])
        else:
            #En caso de que el equipo no este en el inventario imprime un mensaje indicando que el equipo no fue encontrado
            print("Equipo no encontrado")

    #Metodo para mostrar los reportes de novedades de un equipo especifico
    def mostrarReporte(self):
        #Solicita al usuario ingresar el ID del equipo para ver los reportes
        equipoId = input("Ingrese el ID del equipo para ver los reportes: ")
        #Imprime el encabezado del reporte
        print(f"Reportes del equipo con ID {equipoId}:")
        #Itera sobre la lista de novedades
        for reporte in self.novedades:
            #Verifica si el ID del equipo en el reporte coincide con el ID ingresado por el usuario
            if reporte["equipo ID"] == equipoId:
                #Muestra la fecha y la descripcion de la novedad
                print(f"Fecha: {reporte['fecha']}")
                print(f"Descripcion: {reporte['descripcion']}")
            else:
                #Si el equipo esta en la lista pero no presenta novedades o simplemente no esta en la lista imprime un mensaje indicando que el equipo no esta en la lista de agregados o no presenta novedades
                print("El equipo no esta en la lista de agregados o no presenta novedades")

    #Metodo para modificar el estado de un equipo en el inventario
    def modificarEquipo(self):
        #Solicita al usuario ingresar el ID del equipo a modificar
        equipoId = input("Ingrese el ID del equipo a modificar: ")
        #Solicita al usuario ingresar el nuevo estado del equipo
        nuevoEstado = input("Ingrese el nuevo estado: ")
        #Verifica si el equipo existe en el inventario
        if equipoId in self.equipos:
            #Modifica el estado del equipo en el diccionario 'equipos'
            self.equipos[equipoId]['estado'] = nuevoEstado
            #Imprime un mensaje indicando que el estado del equipo ha sido modificado
            print(f"Se modifico el estado del equipo con ID {equipoId} a {nuevoEstado}")
        else:
            #Imprime un mensaje indicando que no existe un equipo con el ID que ingreso el usuario 
            print(f"No existe un equipo con ID {equipoId}")

    #Metodo para eliminar un equipo del inventario
    def eliminarEquipo(self):
        #Solicita al usuario ingresar el ID del equipo a eliminar
        equipoId = input("Ingrese el ID del equipo a eliminar: ")
        #Verifica si el equipo existe en el inventario
        if equipoId in self.equipos:
            #Elimina el equipo del diccionario 'equipos'
            del self.equipos[equipoId]
            #Imprime un mensaje indicando que el equipo ha sido eliminado
            print(f"Se eliminó el equipo con ID {equipoId}")
        else:
            #De lo contrario imprime un mensaje indicando que no existe un equipo con el ID ingresado
            print(f"No existe un equipo con ID {equipoId}")

    #Metodo para mostrar la lista completa de equipos en el inventario
    def mostrarEquipos(self):
        #Imprime un encabezado indicando que se mostrara la lista de equipos
        print("\nLista de equipos:")
        #Itera sobre el diccionario 'equipos' y muestra la informacion de cada equipo que esta en la lista
        for equipoId, equipoInfo in self.equipos.items():
            print(f"Equipo ID: {equipoId}")
            print(f"Cargador: {equipoInfo['cargador']}")
            print(f"Mouse: {equipoInfo['mouse']}")
            print()

#Crea una instancia de la clase 'InventarioEquipos' con el nombre de 'inventario'
inventario = InventarioEquipos()

#Bucle principal del programa
while True:
    #Imprime el menu de opciones para el usuario
    print("\nOpciones")
    print("1. Agregar equipo")
    print("2. Agregar novedad")
    print("3. Buscar equipo")
    print("4. Mostrar novedades de un equipo")
    print("5. Modificar equipo")
    print("6. Eliminar equipo")
    print("7. Mostrar lista de equipos")
    print("8. Salir")

    #Solicita al usuario seleccionar una opcion del menu
    opcion = input("Seleccione una opcion: ")

    #Evalua la opcion seleccionada por el usuario y realiza la accion correspondiente
    if opcion == '1':
        #llama la instancia 'inventario' y el nombre del metodo 'agregarEquipo'
        inventario.agregarEquipo()
    elif opcion == '2':
        inventario.agregarNovedad()
    elif opcion == '3':
        inventario.buscarEquipo()
    elif opcion == '4':
        inventario.mostrarReporte()
    elif opcion == '5':
        inventario.modificarEquipo()
    elif opcion == '6':
        inventario.eliminarEquipo()
    elif opcion == '7':
        inventario.mostrarEquipos()
    elif opcion == '8':
        #Imprime un mensaje indicando que el usuario salio del programa y sale del bucle
        print("Salio del programa")
        break #termina el programa
    else:
        #Imprime un mensaje indicando que la opcion seleccionada no es valida
        print("Opcion no valida, elija una opcion valida")
        
#Maria Jose Perez
#Nataly Stefani Montaña
