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
        # Acá estoy accediedo al atributo interno. Si accedo self.nombre, paso por las validaciones
        # que tenga el .setter.
        # La mejor práctica es acceder a al atributo interno (__) solo desde getters y setters 
        # y desde cualquier otro lugar acceder a la property y al .setter

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

class Cuenta:
    """ Clase cuenta - Atributos titular del tipo persona y cantidad de tipo float"""
    def __init__(self, titular = Persona(), cantidad = 0.0) :
        if not isinstance(titular, Persona):
            ### isinstance es la forma correcta de determinar el tipo de un dato. 

            raise ValueError("El titular debe ser un objeto persona")
        if titular.nombre == '':
            raise ValueError("El titular debe tener nombre")
        self.__titular = titular
        self.__cantidad = cantidad

    @property
    def titular(self):
        """ Getter para el atributo titular"""
        return self.__titular

    @titular.setter
    def titular(self, titular):
        """ Setter para el atributo titular"""
        self.__titular = titular

    @property
    def cantidad(self):
        """ Getter para el atributo cantidad (Este atributo no tiene setters) """
        return self.__cantidad

    def ingresar(self, cantidad):
        """ Permite el ingreso de una cantidad en pesos que se agrega al saldo
        de la cuenta. Si se ingresan cantidades negativas no tienen efecto"""
        if cantidad > 0:
            self.__cantidad += cantidad

    def retirar(self, cantidad):
        """ Permite el egreso de una cantidad en pesos de se resta del saldo"""
        self.__cantidad -= cantidad

    def mostrar(self):
        """ Muestra los datos completos de la persona"""
        print("-- Datos de la cuenta --")
        print(self.__titular.mostrar())
        print(f"- Saldo  : {self.__cantidad}")

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

class CuentaJoven(Cuenta):
    """ Clase Cuenta Joven. Hereda de la clase Cuenta. Se agrega el atributo
    Bonificación """
    def __init__(self, titular=Persona(), cantidad=0.0, bonificacion=0.0):
        super().__init__(titular, cantidad)
        self.__bonificacion = bonificacion

    @property
    def bonificacion(self):
        """ Getter del atributo bonificación"""
        return self.__bonificacion

    @bonificacion.setter
    def bonificacion(self, bonificacion):
        """ Setter para el atributo bonificación """
        self.__bonificacion = bonificacion

    def es_titular_valido(self):
        """El titular debe ser mayor de edad y menor de 26 años"""
        if self.titular.es_mayor_de_edad() and self.titular.edad <= 26:
            return True
        else:
            return False

    def retirar(self, cantidad):
        """ Permite el egreso de una cantidad en pesos de se resta del saldo
        Solo puede retirar si el titular es válido"""
        if self.es_titular_valido():
            super().retirar(cantidad)

    def mostrar(self):
        """ Muestra los datos completos de la persona"""
        print("-- Cuenta Joven --")
        print(super().mostrar())
        print(f"- Bonificación  : {self.__bonificacion}")

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
# ---------------------------------------------------------------------------------
# Instancio una persona con los atributos inicializados desde el constructor
# Muestro con los getters y con mostrar. Idem mayor de edad

p2 = Persona("Mengano", 20, "40202303")
print("--- Persona 2 ---")
print(" * Muestro con los getters")
print(f"Nombre: {p2.nombre} \nEdad: {p2.edad} \nDNI: {p2.dni}")
# Muestro con el método mostrar
print(" * Muestro con mostrar()")
p2.mostrar()
# Uso es_mayor_de_edad
if p2.es_mayor_de_edad():
    print("Es mayor de edad")
else:
    print("Es MENOR de edad")

# Pruebas de la clase Cuenta usando Persona1
print("\n --- Pruebas con la clase Cuenta ---")
print(" * Instancia con una persona sin nombre")
try:
    psn = Persona()
    c1 = Cuenta(psn)
except ValueError as error:
    print(error)

print("\n * Instancia sin objeto persona")
try:
    c1 = Cuenta("Zutano")
except ValueError as error:
    print(error)

print("\n * Instancia correcta")
try:
    c1 = Cuenta(p1, 1000)
except ValueError as error:
    print(error)

print(c1.mostrar())
print(" * Retiro 500 de la cuenta")
c1.retirar(500)
print(c1.mostrar())
print(" * Retiro 0.5 de la cuenta")
c1.retirar(0.5)
print(c1.mostrar())
print(" * Ingreso 750 de la cuenta")
c1.ingresar(750)
print(c1.mostrar())
print(" * Ingreso -200 de la cuenta")
c1.ingresar(-200)
print(c1.mostrar())

# Pruebas de la clase CuentaJoven usando Persona2

print("\n --- Pruebas con la clase CuentaJoven ---")
print(" * Instancia con una persona de 20 años")
cj1 = CuentaJoven(p2, 1000, 30)
print(f" * Es titular válido: {cj1.es_titular_valido()}")
cj1.retirar(300)
print(" * Retiro 300 y muestro los datos de la cuenta")
print(cj1.mostrar())
print("\n\n --- Pruebas con la clase CuentaJoven ---")
print(" * Instancia con una persona de más de 26 años")
cj2 = CuentaJoven(p1, 1000, 30)
print(f" * Es titular válido: {cj2.es_titular_valido()}")
cj2.retirar(300)
print(" * Retiro 300 y muestro los datos de la cuenta")
print(cj2.mostrar())
