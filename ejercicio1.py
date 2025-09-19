# Este archivo corresponde al Ejercicio 1 de la guia practica sobre Clases.
# Aqui deberas implementar la clase Camion y resolver los puntos a, b, c, d y f segun las consignas



    
    #def __eq__(self, other): ###B
        #if not isinstance(other, Camion): #si el objeto a comparar es de la misma clase que camion va al return ()
           # return False #si no son de la misma clase ni se gasta porque es al pepe
       # return (self.patente == other.patente and #me compara cada valor en vez del id
               # self.marca == other.marca and
               # self.carga == other.carga and
               # self.anio == other.anio)
class Camion:
    patentes_usadas = {} #creo esta variable para poder identificar si esa patente fue usada onno
    marcas_disp=['volskwagen','fiat','bmw']
    def __init__(self, patente, marca, carga, anio):
        self.validar_patente(patente)
        self.validar_marca(marca)
        self.carga= self.validar_int(carga)
        self.anio = self.validar_int(anio)
        
         
    def __str__(self):
        return f"Camión: #{self.patente} \nCarga: {self.carga} \nMarca: {self.marca} \nAnio: {self.anio}"
    
    def validar_str(self,cadena):
        if not isinstance(cadena,str):
             raise TypeError('Debe ser un string')
        if len(cadena)==0:
            raise ValueError('La cadena no debe estar vacia')
        else:
            return cadena
        
    def validar_patente(self,patente):
        patente= self.validar_str(patente)
        patente=patente.strip().upper()
        if len(patente)!=7:
            raise ValueError('La patente debe estar conformada por dos letras, tres numeros y luego dos letras')
        if patente in Camion.patentes_usadas: #raiseo un error si la patente ya fue usada
                raise ValueError(f"La patente {patente} ya está registrada.")
        else:
            self.patente=patente
            #despues de crear la instancia, uso registrar patente
    
    def validar_marca(self,marca):
        marca=self.validar_str(marca)
        marca=marca.lower()
        if marca not in Camion.marcas_disp:
            raise ValueError('La marca no esta dentro de las disponibles')
        else:
            self.marca=marca
       
    def validar_int(self,numero):   
        if not isinstance(numero,int):
            raise TypeError('Debe ser un numero')
        elif numero is None:
            raise ValueError('No debe estar vacia')
        else:
            return numero
            
  
    def __eq__(self, other): ###c
        if not isinstance(other, Camion): #si el objeto a comparar es de la misma clase que camion va al return ()
            return False #si no son de la misma clase ni se gasta porque es al pepe
        return (self.patente == other.patente) #igual que el b solo que solo me compara la patente
    
    def get_patente(self):
        return self.patente
    
    def get_marca(self):
        return self.marca
    
    def get_carga(self):
        return self.carga
    
    def get_anio(self):
        return self.anio
    
    def set_carga(self, nueva_carga):
        nueva_carga=self.validar_int(Camion,nueva_carga)
        
    
def modificar_carga(patente,nueva_carga):
    patente= Camion.validar_str(Camion,patente)
    patente=patente.strip().upper()
    if len(patente)!=7:
        raise ValueError('La patente debe estar conformada por dos letras, tres numeros y luego dos letras')
    if patente in Camion.patentes_usadas:
        Camion.set_carga(Camion,nueva_carga)
        Camion.patentes_usadas[patente].carga=nueva_carga
        print('Se ha cambiado la carga con exito')
              
    else:
        raise ValueError('La patente ingresada no se encuentra registrada')  
        
def render_camiones():
    camiones_ordenados=(sorted(Camion.patentes_usadas.values(),key=lambda obj: obj.anio)) #agarra cada objeto y se fija el anio
    for obj in camiones_ordenados:
        print(f"{obj.patente} {obj.marca} {obj.carga} {obj.anio}")
              


def max_marca():
    conteo = {}
    for obj in Camion.patentes_usadas.values():
        marca = obj.marca #mira cada marca de los objetos
        conteo[marca] = conteo.get(marca, 0) + 1
    tupla_max=max(conteo.items(), key=lambda x: x[1]) #x es una de las tuplas del dict conteo, x[1] es la posicion donde esta al cantidad
    print(f'La marca mas utilizada es: {tupla_max[0]}')
    

def menu(Camiones):
    while True:
        try:
            numero=int(input('1 Registrar un nuevo camion \n2 Modificar la carga de un camion \n3 Mostrar la lista de camiones registrados \n4 Mostrar la marca que mas fue registrada \n5 Cerrar el programa \n Ingrese el numero deseado: '))
        except ValueError:
            print('Debe ingresar un numero dentro de los mostrados')
            continue
        if numero ==1:
            try:
                patente=str(input('Ingrese la patente: '))
                marca=str(input('Ingrese la marca: '))
                carga=int(input('Ingrese la carga: '))
                anio=int(input('Ingrese el anio: '))
                Ingreso=Camion(patente,marca,carga,anio)
                Camiones.append(Ingreso)
            
            except ValueError:
                print('Ingrese datos correctos')
            continue
        elif numero==2:
            try:
                patente_carga = input("Ingrese la patente del camión a editar la carga: ")
                encontrado = False
                for camion in Camiones:
                    if camion.patente == patente_carga:
                        nuevo_valor = int(input("Ingrese la nueva carga: "))
                        camion.carga = nuevo_valor #aca en realidad deberia usar un setter
                        encontrado = True
                        print("Carga actualizada correctamente")
                    break
                if not encontrado:
                    print("La patente no está cargada, registre un nuevo camión")
                else:
                    print("La patente no está registrada, primero registre el camión")    
            except ValueError:
                print('Los valores ingresados no son correctos')
            continue
            
        elif numero==3:
            ordenados = sorted(Camiones, key=lambda c: c.anio)
            print(ordenados)
        elif numero==4:
                #la logica es que pase por toda la lista y que vaya contando cuantas son = (agarra 1, compara y agrega al contador, y dsp pasa a la siguiente que es distinta a la primera y asi hasta termianr.)
            conteo = {}
            for c in Camiones:
                if c.marca in conteo:
                    conteo[c.marca] += 1
                else:
                    conteo[c.marca] = 1
            max_marca = max(conteo, key=conteo.get)
            print(f'La marca mas registrada es: {max_marca}')
            continue
        elif numero==5:
            print('Chau')
            break
        else:
            print('Debe ingresar un numero dentro de los mostrados')
            continue



if __name__ == "__main__":
    #registar camiones
    try:
        c1=Camion('ab131cd','fiat',500 ,2003)
        Camion.patentes_usadas[c1.patente]=c1
        print('Camion c1 creado con exito')
        
        c2=Camion('aa131cd','Bmw',300, 2005)
        Camion.patentes_usadas[c2.patente]=c2
        print('Camion c2 creado con exito')
        
        c3=Camion('as131cd','volskwagen',100 ,1999)
        Camion.patentes_usadas[c3.patente]=c3
        print('Camion c3 creado con exito')
        
        c4=Camion('aa131dd','Bmw',5, 2025)
        Camion.patentes_usadas[c4.patente]=c4
        print('Camion c4 creado con exito')
        
        
    except TypeError as e:
        print('El error es: ', e)
        '''sacar todos los errores e imprimirlos, y dsp exception'''
    except ValueError as e:
        print('El error es: ', e)
    except Exception as e:
        print('El error es: ', e)
        
    #modificar carga
    try:
        patente='ab131cd'
        nueva_carga= 22
        modificar_carga(patente,nueva_carga)
        print(c1)
    except ValueError as e:
        print('El error es: ', e)   
    except ValueError as e:
        print('El error es: ', e)
    except Exception as e:
        print('El error es: ', e)     
    #camiones registrados
    render_camiones()
    #max marca
    max_marca()
      
    
    
    
# a. Indica que devuelven las siguientes expresiones. Analizalo con tus companeros y luego ejecuta las instrucciones en la maquina para comprobar tu respuesta.
#furgon1 = Camion("ABC123", "Mercedes", 1000 ,2020)
#furgon2 = furgon1
#furgon3 = Camion("DEF456", "Volvo", 2000, 2021)
#furgon4 = Camion("ABC123", "Mercedes", 1000,2020)

#print(furgon1 == furgon2) #true
#print(furgon1 is furgon2) #true, son el mismo objeto
#print(furgon3 == furgon4) #false proque compara identidad de almacenamiento
#print(furgon3 is furgon4) #false porque auneuqe tengan mismos valore son distintos objetos
#print(furgon1 == furgon4) # False proque compara identidad de almacenamiento al no haber definido --eq--

#b. Modifica el codigo dado para que la comparacion de dos objetos de la clase Camion devuelva True cuando todos sus atributos sean iguales.

# para responder esto defino --eq-- esto hace que cuando uso == no me compara la identidad de memoria sino el contenido. 

#c. Que atributo hace unico a nuestros objetos? Identifica el atributo que hace unico al objeto Camion y modifica el codigo para que la comparacion de dos objetos de la clase Camion devuelva True cuando ese atributo sea igual.

# la patente hace unico a los objetos 

#d. Si dos personas tienen el mismo DNI, entonces... Son la misma persona! ¿Como evitaris asignar el mismo DNI a dos personas distintas? Siguiendo esta analogia, adapta el codigo anterior para el caso de los camiones.

#creo patentes usadas y evito que pongan 

#f. Crea un pequeno menu que te permita:

#1. Registrar un nuevo camion.
#1. Modificar la carga de un camion.
#1. Mostrar por terminal la lista de camiones registrados, del mas antiguo al mas moderno.
#1. Mostrar por terminal la marca que maa veces fue registrada.

def menu(Camiones):
    while True:
        try:
            numero=int(input('1 Registrar un nuevo camion \n2 Modificar la carga de un camion \n3 Mostrar la lista de camiones registrados \n4 Mostrar la marca que mas fue registrada \n5 Cerrar el programa \n Ingrese el numero deseado: '))
        except ValueError:
            print('Debe ingresar un numero dentro de los mostrados')
            continue
        if numero ==1:
            try:
                patente=str(input('Ingrese la patente: '))
                marca=str(input('Ingrese la marca: '))
                carga=int(input('Ingrese la carga: '))
                anio=int(input('Ingrese el anio: '))
                Ingreso=Camion(patente,marca,carga,anio)
                Camiones.append(Ingreso)
            
            except ValueError:
                print('Ingrese datos correctos')
            continue
        elif numero==2:
            try:
                patente_carga = input("Ingrese la patente del camión a editar la carga: ")
                encontrado = False
                for camion in Camiones:
                    if camion.patente == patente_carga:
                        nuevo_valor = int(input("Ingrese la nueva carga: "))
                        camion.carga = nuevo_valor #aca en realidad deberia usar un setter
                        encontrado = True
                        print("Carga actualizada correctamente")
                    break
                if not encontrado:
                    print("La patente no está cargada, registre un nuevo camión")
                else:
                    print("La patente no está registrada, primero registre el camión")    
            except ValueError:
                print('Los valores ingresados no son correctos')
            continue
            
        elif numero==3:
            ordenados = sorted(Camiones, key=lambda c: c.anio)
            print(ordenados)
        elif numero==4:
                #la logica es que pase por toda la lista y que vaya contando cuantas son = (agarra 1, compara y agrega al contador, y dsp pasa a la siguiente que es distinta a la primera y asi hasta termianr.)
            conteo = {}
            for c in Camiones:
                if c.marca in conteo:
                    conteo[c.marca] += 1
                else:
                    conteo[c.marca] = 1
            max_marca = max(conteo, key=conteo.get)
            print(f'La marca mas registrada es: {max_marca}')
            continue
        elif numero==5:
            print('Chau')
            break
        else:
            print('Debe ingresar un numero dentro de los mostrados')
            continue



