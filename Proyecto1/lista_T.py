class lista_T: #Creamos la clase Humano
    def __init__(self, correlativo, token, lexema, tipo, fila,columna): #Definimos el parámetro edad y nombre
        self.correlativo = correlativo
        self.token =token
        self.lexema= lexema
        self.tipo=tipo
        self.fila=fila
        self.columna=columna # Definimos que el atributo nombre, sera el nombre asig

    def __repr__(self):
        return str(self.__dict__)