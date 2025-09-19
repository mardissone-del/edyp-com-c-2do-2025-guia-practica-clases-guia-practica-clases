# Ejercicio 2: Modelar una computadora
# 
# En este archivo debes crear la clase Computadora siguiendo las consignas del README.
# Recordá:
# - Definir atributos relevantes en el constructor (__init__), con valores por defecto.
# - Implementar el método __str__ para mostrar la informacion esencial.
# - Instanciar al menos 3 computadoras con distintos valores.
# - Llevar la cuenta de computadoras creadas (usar variable de clase).
# - Implementar al menos 2 metodos de los sugeridos (updateOS, PM, addRAM, getCapacity).
# - Crear otra clase para un componente (ej: Disco, RAM, etc.) con su propio __init__, __str__ y al menos un metodo.
# 
# ¡No olvides probar todos los metodos y comentar tu criterio para los valores

class Computadora():
    lista_compus=[]
    modelos_disp=['air','pro']
    marcas_disp=['mac','samsung']
    
    def __init__(self, id:str, modelo:str, marca:str):
        self.validar_id(id)
        self.set_modelo(modelo)
        self.set_marca(marca)
    
        
    def __str__(self):
        return f'La computadora de id: {self.id} es de modelo: {self.modelo} y marca: {self.marca}'
    '''visualizo todos los atributos de un objeto'''
    
    #repr para cuando no quiero imprimir en cad ainstancia sino la lista completa d eobjetos y esta en *lista, dict etc)
    
    def __eq__(self,other):
        if not isinstance(other, Computadora):
            return NotImplemented
        return self.id==other.id
    '''estblaezco que el id debe ser unico para cada computadora entonces cuando quiera comparar me compara el valor'''
    
    def validar_cadena(self, cadena: str):
        if not isinstance(cadena,str):
            raise TypeError('Debe ser una cadena')
        if len(cadena)==0:
            raise ValueError('No debe estar vacio')
    
    def get_id(self):
        return self.id
    
    def get_marca(self):
        return self.marca
    
    def get_modelo(self):
        return self.modelo
    
    def validar_id(self,id):
        self.validar_cadena(id) #asi cada vez que cambio el id me valida que sea sr y no este vacio
        id=id.lower()
        if id in Computadora.lista_compus:
            raise ValueError('Ese id ya esta ingresado')
        self.id=id
        Computadora.lista_compus.append(id)
    
    def set_id(self, nuevo_id:str):
        self.validar_cadena(nuevo_id) #asi cada vez que cambio el id me valida que sea sr y no este vacio
        nuevo_id=nuevo_id.lower()
        if nuevo_id in Computadora.lista_compus:
            raise ValueError('Ese id ya esta ingresado')
        Computadora.lista_compus.remove(self.id)
        self.id=nuevo_id
        Computadora.lista_compus.append(nuevo_id)
        
    def set_modelo(self, nuevo_modelo:str):
        nuevo_modelo=nuevo_modelo.lower()
        self.validar_cadena(nuevo_modelo)
        if nuevo_modelo not in Computadora.modelos_disp:
            raise ValueError('Ese modelo no se encuentra dentro de los disponibles') 
        self.modelo=nuevo_modelo
        
    def set_marca(self, nueva_marca:str):
        nueva_marca=nueva_marca.lower()
        self.validar_cadena(nueva_marca)
        if nueva_marca not in Computadora.marcas_disp:
            raise ValueError('Esa marca no se encuentra dentro de las disponibles') 
        self.marca=nueva_marca    
            
            
    #funcionales, mi idea es, si el id esta en lista compus entonces la puedo vender, sino no.
    
def vender(id):
    if id not in Computadora.lista_compus:
        raise ValueError('El id de esa computadora ya fue vendido')
    Computadora.lista_compus.remove(id)
    print('Venta completada con exito') 
    
def mostrar_lista_compus():
    if not Computadora.lista_compus:
        for i,v in enumerate(Computadora.lista_compus,1):
            print(i,v)
    else:
        print('No hay compus para vender')
    
def menu():
    numeros=int(input('Para cara ver la lista de computadoras disponibles escribe 1\n Para comprar una computadora escribe 2\n Para salir del menu escribe 3'))
    while numeros!=3:
        if numeros==1:
            mostrar_lista_compus()
            numeros=int(input('Para cara ver la lista de computadoras disponibles escribe 1\n Para comprar una computadora escribe 2\n Para salir del menu escribe 3'))
        if numeros==2:
            try:
                id_comprar=str(input('Ingrese el id de la computadora a comprar: '))
                if id_comprar not in Computadora.lista_compus:
                    print('El id de esa computadora ya fue vendido')
                Computadora.lista_compus.remove(id_comprar)
                print('Venta completada con exito')
            except ValueError as e:
                print('Hubo un error')
                numeros=int(input('Para cara ver la lista de computadoras disponibles escribe 1\n Para comprar una computadora escribe 2\n Para salir del menu escribe 3'))
            
                
        
if __name__=='__main__':
    '''para que si creo herencias, que solo me corra esto si es esta clase'''
    try:
        c1=Computadora('A2','pro','mac')
        print(c1)
        c2=Computadora('A3','air','samsung')
        print(c2)
        c3=Computadora('A4','air','mac')
        print(c3)
        #c4=Computadora(3,'pro','mac')
        #print(c4)
        #c5=Computadora('A3','aires','samsung')
        #print(c5)
        c4=Computadora('ee','air','4')
        print(c4)
        '''siempre imprimir todo par chequear que me devuelve'''
    except TypeError as e:
        print('El error es 1: ', e)
        '''sacar todos los errores e imprimirlos, y dsp exception'''
    except ValueError as e:
        print('El error es 2: ', e)
    except Exception as e:
        print('El error es 3: ', e)
    #vender compu
    
    if 'A2'.lower() not in Computadora.lista_compus:
        print('El id de esa computadora no existe')
    else: 
        Computadora.lista_compus.remove('A2'.lower())
        print('Venta completada con exito')

    
    
    
    