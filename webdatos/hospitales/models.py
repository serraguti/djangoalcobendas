from django.db import models
import oracledb

# Create your models here.
class Departamento:
    def __init__(self):
        self.id = 0
        self.nombre = ""
        self.localidad = ""

class Empleado:
    def __init__(self):
        self.idEmpleado = 0
        self.apellido = ""
        self.oficio = ""
        self.salario = 0

class ServiceDepartamentos:
    def __init__(self):
        self.connection = oracledb.connect(user="system", password="oracle"
                                           , dsn = "localhost/freepdb1")
    
    def getDepartamentos(self):
        sql = "select * from DEPT"
        cursor = self.connection.cursor()
        cursor.execute(sql)
        listaDepartamentos = []
        for row in cursor:
            dept = Departamento()
            dept.id = row[0]
            dept.nombre = row[1]
            dept.localidad = row[2]
            listaDepartamentos.append(dept)
        cursor.close()
        return listaDepartamentos
    
    def insertarDepartamento(self, id, nombre, loc):
        sql = "insert into DEPT values (:id, :nom, :loc)"
        cursor = self.connection.cursor()
        cursor.execute(sql, (id, nombre, loc,))
        self.connection.commit()
        cursor.close()  
        
    def updateDepartamento(self, id, nombre, localidad):
        sql = "update DEPT set DNOMBRE=:nom, LOC=:loc where DEPT_NO=:id"
        cursor = self.connection.cursor()
        cursor.execute(sql, (nombre, localidad, id,))
        self.connection.commit()
        cursor.close()
    
    #Vamos a crear un metodo para buscar un departamento por su ID
    def buscarDepartamento(self, id):
        sql = "select * from DEPT where DEPT_NO=:id"
        cursor = self.connection.cursor()
        cursor.execute(sql, (id,))
        row = cursor.fetchone()
        dept = Departamento()
        dept.id = row[0]
        dept.nombre = row[1]
        dept.localidad = row[2]
        cursor.close()
        return dept
    
    def deleteDepartamento(self, id):
        sql = "delete from DEPT where DEPT_NO=:id"
        cursor = self.connection.cursor()
        cursor.execute(sql, (id,))
        self.connection.commit()
        cursor.close()
        
    def buscarEmpleadosDepartamento(self, iddept):
        sql = "select EMP_NO, APELLIDO, OFICIO, SALARIO from EMP where DEPT_NO=:iddept"
        cursor = self.connection.cursor()
        cursor.execute(sql, (iddept, ))
        listaEmpleados = []
        for row in cursor:
            emp = Empleado()
            emp.idEmpleado = row[0]
            emp.apellido = row[1]
            emp.oficio = row[2]
            emp.salario = row[3]
            listaEmpleados.append(emp)
        cursor.close()
        return listaEmpleados
    
    def buscarEmpleadosSalario(self, salario):
        sql = "select EMP_NO, APELLIDO, OFICIO, SALARIO from EMP where SALARIO>=:sal"
        cursor = self.connection.cursor()
        cursor.execute(sql, (salario, ))
        listaEmpleados = []
        for row in cursor:
            emp = Empleado()
            emp.idEmpleado = row[0]
            emp.apellido = row[1]
            emp.oficio = row[2]
            emp.salario = row[3]
            listaEmpleados.append(emp)
        cursor.close()
        return listaEmpleados
