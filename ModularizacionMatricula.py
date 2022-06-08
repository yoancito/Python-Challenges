"""
Se tiene el proceso de matrícula en una institución educativa, se conoce el estudiante y los cursos que puede matricular, 
se requiere verificar que el estudiante está activo y si es así poder matricular un curso, cambiar un curso por otro o el 
día y hora en que lo sirven, cancelar un curso e inactivarse el sistema. 
Se requiere realizar el proceso de abstracción y modularización del problema, codificación en Python y prueba de funcionalidad básica.
"""
class StudentRegistration:
    def __init__(self, id_user, name, age, status):
        self.id_user = id_user
        self.name = name
        self.age = age
        self.status = status

    def printStudent(self):
        print("Id = {self.id_user}")
        print("Nombre = {self.name}")
        print("Edad (años) = {self.age}")
        print("Estado = {self.status}")

    def getName(self):
        return self.name
    def getStatus(self):
        return self.status

class Courses:
    def __init__(self, iddegree, pregrade, coursesprogram, schedule, activestatus):
        self.iddegree = iddegree
        self.pregrade = pregrade
        self.coursesprogram = coursesprogram
        self.schedule = schedule
        self.activestatus = activestatus

    def printCourse(self):
        print(f"ID Carrera = {self.iddegree}")
        print(f"pregrado = {self.pregrade}")
        print(f"Cursos del programa = {self.coursesprogram}")
        print(f"horario = {self.schedule}")
        print(f"Estado del curso = {self.activestatus}")

    def courseStatus(self,fuckingStatus):
        self.fuckingStatus = fuckingStatus
        if self.fuckingStatus.getStatus() == "Activo":
            print("Estudiante activo")
        elif self.fuckingStatus.getsgetStatus() == "Inactivo":
            print("Estudiante Inactivo")
        else:
            print("Error ingresa Activo/Inactivo")

    def cambiarCurso(self, newCurso, oldCurso):
        self.newCurso = newCurso
        self.oldCurso = oldCurso
        for x in range(len(coursesprogram)):
            if coursesprogram[x] == self.oldCurso:
                coursesprogram[x] = newCurso
        print(f"Se cambiara el curso de '{oldCurso}' por '{newCurso}'")
        print(f"Cursos del programa actualizado :{coursesprogram}")

    def cancelarCurso(self, cursoCancelado, Cnombre):
        self.cursoCancelado = cursoCancelado
        self.Cnombre = Cnombre
        print(f"El estudiante {self.Cnombre.getNombre()} ha cancelado el curso {self.cursoCancelado}")

matricula = Matricula(6666666, "Joan", 66, "Calle 00 # 00 - 00", "+57 3001235678", "joan@joan", "Activo")
matricula.printStudent()
coursesprogram = (["POO", "FISICA 1"])
curso = Courses("AAA000", "Ingenieria de Sistemas", coursesprogram, "22:00", "Activo")
curso.printCourse()
curso.activo(matricula)
curso.cambiarCurso("POO", "Dibujo 1")
curso.cancelarCurso("FISICA 1", matricula)
