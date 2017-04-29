''' Created on 31 jan. 2016 
 
@author: Adri ''' #-*-coding:utf8-*- 

import psycopg2
import psycopg2.extras
import sysconfig
import pprint

    
class Alumno():
        
    def __init__(self, id, nombre, tipo, curso, fecha, horas, precio):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.curso = curso
        self.fecha = fecha
        self.horas = horas
        self.precio = precio
        
 
 
    def mostrarAlumno(self):
        return(self.id, self.nombre, self.tipo, self.curso, self.fecha, self.horas, self.precio)


    
class Principal():
    
    
    
    aux = True; 
    print()
    print("Acceso Datos")
    
    conx = None
    try:
        
        conx = psycopg2.connect("dbname=postgres user = openpg password=openpgpwd")
        print("Estableciendo conexion con la base de datos Postgres")
        print()
        cur=conx.cursor()
        print("Conectado ! \n")
        cur.execute('select version()')
        version = cur.fetchone()
        print("version de Postgres \n", version)
        cur.execute("CREATE TABLE alumnos (id integer, nombre varchar, tipo varchar, nombre_curso varchar, fecha_inscripcion varchar, horas_curso varchar, precio integer)")
        
       

        
        #cur.execute("CREATE TABLE alumnos (nombre varchar, tipo varchar, nombre_curso varchar, fecha_inscripcion varchar, horas_curso varchar, precio integer)")
        #Se insertan algunas tuplas en la tabla. La última se inserta de otra forma
            
   
           
        while aux:   
             
            print ("""     
            1.Insertar alumno     
            2.Editar datos de alumnos
            3.Borrar alumnos    
            5.Salir     """)     
            aux=input ("Que quieres hacer?: ")           
            if aux=="1": 
                id=input ("Introduce el id: ") 
                nombre=input ("Introduce el nombre: ")   
                tipo=input ("Introduce el tipo (empleado o cliente): ")
                nombre_curso=input ("Introduce el curso: ") 
                fecha_inscripcion=input ("Introduce la fecha de inscripcion: ")
                horas_curso=input ("Introduce las horas del curso: ")  
                precio=input ("Introduce el precio: ")     
                alumno = Alumno(id, nombre, tipo, nombre_curso, fecha_inscripcion, horas_curso, precio);   
                #cur.execute("INSERT INTO alumnos (nombre, tipo, nombre_curso, fecha_inscripcion, horas_curso, precio) VALUES ("+alumno.nombre+","+alumno.tipo+","+alumno.nombre_curso+","+alumno.fecha_inscripcion+","+alumno.horas_curso+","+alumno.precio+")")
                #cur.execute("INSERT INTO alumnos (nombre, tipo, nombre_curso, fecha_inscripcion, horas_curso, precio) VALUES (%s, %s, %s, %s, %s, %d)",(alumno.nombre,alumno.tipo,alumno.nombre_curso,alumno.fecha_inscripcion,alumno.horas_curso,alumno.precio))
                cur.execute("INSERT INTO alumnos (id, nombre, tipo, nombre_curso, fecha_inscripcion, horas_curso, precio) VALUES (%s, %s, %s, %s, %s, %s, %s)",(alumno.id, alumno.nombre, alumno.tipo, alumno.curso, alumno.fecha, alumno.horas, alumno.precio))
                
                
            elif aux=="2":
                    
                    cur.execute("SELECT * FROM alumnos")
                    tuplas=cur.fetchall()
    
                    print()
                    print("Tabla Alumnos")
                    for row in tuplas:
                        print(row)
                    
                        
                    alumno.id=input("Introduce el identificador del alumno a modificar: ")
                    
                    auxiliar2 = True;
                    while auxiliar2:     
                        print ("""
                        ¿Que quieres modificar?
                        1.Modificar nombre   
                        2.Modificar tipo
                        3.Modificar nombre_curso
                        4.Modificar fecha
                        5.Modificar horas
                        6.Modificar precio
                        7.Salir     """)     
                        auxiliar2=input ("Que quieres hacer?: ")           
                        if auxiliar2=="1":
                            alumno.nombre=input("Nuevo nombre: ")
                            cur.execute("update alumnos SET nombre = %s WHERE Id = %s", (alumno.nombre, alumno.id))
                            cur.execute("SELECT * FROM alumnos")
                            tuplas=cur.fetchall()
            
                            print()
                            print("Tabla Alumnos")
                            for row in tuplas:
                                print(row)
                        if auxiliar2=="2":
                            alumno.tipo=input("Nuevo tipo: ")
                            cur.execute("update alumnos SET tipo = %s WHERE Id = %s", (alumno.tipo, alumno.id))
                            cur.execute("SELECT * FROM alumnos")
                            tuplas=cur.fetchall()
            
                            print()
                            print("Tabla Alumnos")
                            for row in tuplas:
                                print(row)
                        if auxiliar2=="3":
                            alumno.nombre_curso=input("Nuevo nombre del curso: ")
                            cur.execute("update alumnos SET nombre_curso = %s WHERE Id = %s", (alumno.nombre_curso, alumno.id))
                            cur.execute("SELECT * FROM alumnos")
                            tuplas=cur.fetchall()
            
                            print()
                            print("Tabla Alumnos")
                            for row in tuplas:
                                print(row)
                        if auxiliar2=="4":
                            alumno.fecha_inscripcion=input("Nuevo nombre: ")
                            cur.execute("update alumnos SET fecha_inscripcion = %s WHERE Id = %s", (alumno.fecha_inscripcion, alumno.id))
                            cur.execute("SELECT * FROM alumnos")
                            tuplas=cur.fetchall()
            
                            print()
                            print("Tabla Alumnos")
                            for row in tuplas:
                                print(row)
                        if auxiliar2=="5":
                            alumno.horas_curso=input("Nuevo horas del curso: ")
                            cur.execute("update alumnos SET horas_curso = %s WHERE Id = %s", (alumno.horas_curso, alumno.id))
                            cur.execute("SELECT * FROM alumnos")
                            tuplas=cur.fetchall()
            
                            print()
                            print("Tabla Alumnos")
                            for row in tuplas:
                                print(row)
                        if auxiliar2=="6":
                            alumno.precio=input("Nuevo precio: ")
                            cur.execute("update alumnos SET precio = %s WHERE Id = %s", (alumno.precio, alumno.id))
                            cur.execute("SELECT * FROM alumnos")
                            tuplas=cur.fetchall()
            
                            print()
                            print("Tabla Alumnos")
                            for row in tuplas:
                                print(row)
                        elif auxiliar2=="7":                  
                            break;
                        

                            
            elif aux=="3":   
                cur.execute("SELECT * FROM alumnos")
                tuplas=cur.fetchall()
    
                print()
                print("Tabla Alumnos")
                for row in tuplas:
                    print(row)
                        
                alumno.id=input("Introduce el identificador del alumno a eliminar: ")
                    
                cur.execute("DELETE FROM alumnos WHERE id = %s", (alumno.id))
                cur.execute("SELECT * FROM alumnos")
                tuplas=cur.fetchall()
    
                print()
                print("Tabla Alumnos")
                for row in tuplas:
                    print(row)   
                                              
            elif aux=="5":         
                print("Gracias por usar esta aplicación!");         
                break;          
            elif aux !="":            
                print("\n No existe esa opcion")
                
        
       
                    
    except:
        print("No se puede conectar con la base de datos")  
        
        
                  
        