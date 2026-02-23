from django.db import models
import oracledb

# Create your models here.
class Departamento:
    def __init__(self):
        self.id = 0
        self.nombre = ""
        self.localidad = ""

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
    
    
