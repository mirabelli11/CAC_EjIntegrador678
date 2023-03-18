""" Ejercicio 6 - Persona
Crear una clase llamada Persona. 
Sus atributos son: nombre, edad y DNI. 
Construya los siguientes métodos para la clase:
- Un constructor, donde los datos pueden estar vacíos.
- Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
- mostrar(): Muestra los datos de la persona.
- Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.
"""
class Persona:
    """ Clase persona. Atributos: nombre, edad, dni
    Los atribitutos en el constructor pueden venir vacíos"""
    def __init__(self, nombre="", edad=0, dni=""):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni
    # Los setters y getters para cada uno de los atributos

    @property
    def nombre(self):
        """ Getter para el atributo nombre"""
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        """ Setter para el atributo nombre"""
        self.__nombre = nombre

    @property
    def edad(self):
        """ Getter para el atributo edad"""
        return self.__edad

    @edad.setter
    def edad(self, edad):
        """ Setter para el atributo edad"""
        self.__edad = edad

    @property
    def dni(self):
        """ Getter para el atributo dni"""
        return self.__dni

    @dni.setter
    def dni(self, dni):
        """ Setter para el atributo dni"""
        self.__dni = dni

    def mostrar(self):
        """ Muestra los datos completos de la persona"""
        print(f"- Nombre: {self.__nombre}")
        print(f"- Edad  : {self.__edad}")
        print(f"- DNI   : {self.__dni}")

    def es_mayor_de_edad(self):
        """ Devuelve true si la edad de la persona es mayor o igual a 18"""
        return self.__edad >= 18


#""" 7. Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una
#persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es
#opcional. Crear los siguientes métodos para la clase:
#- Un constructor, donde los datos pueden estar vacíos.
# - Los setters y getters para cada uno de los atributos. El atributo no se puede modificar
# directamente, sólo ingresando o retirando dinero.
# - mostrar(): Muestra los datos de la cuenta.
# - ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es
# negativa, no se hará nada.
# - retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números
# rojos.
# """

# """ 8. Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase
# CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase,
# además del titular y la cantidad se debe guardar una bonificación que estará expresada en
# tanto por ciento. Crear los siguientes métodos para la clase:
# - Un constructor.
# - Los setters y getters para el nuevo atributo.
# - En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo
# tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es
# mayor de edad pero menor de 25 años y falso en caso contrario.
# - Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
# - El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la
# cuenta.
# """
# ---------------------------------------------------------------------------------
# ----***** Pruebas
# Instancio una persona con los atributos vacios
# Los completo con los setters y despues los muestro con los getters
p1 = Persona()
p1.dni = 30333555
p1.edad = 40
p1.nombre = "Fulano"
print("--- Persona 1 ---")
print(" * Muestro con los getters")
print(f"Nombre: {p1.nombre} \nEdad: {p1.edad} \nDNI: {p1.dni}")
# Muestro con el método mostrar
print(" * Muestro con mostrar()")
p1.mostrar()
# Uso es_mayor_de_edad
if p1.es_mayor_de_edad():
    print("Es mayor de edad")
else:
    print("Es MENOR de edad")


# p = Persona("Juan", 20, "20202303")
# print(p.edad)
