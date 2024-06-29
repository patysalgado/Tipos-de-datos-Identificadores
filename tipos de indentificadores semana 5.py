# Programa de gestión de un registro de estudiantes
# Este programa permite agregar estudiantes, listar estudiantes y calcular la edad promedio.

class Estudiante:
    """
    Clase que representa a un estudiante.
    """
    def __init__(self, nombre: str, edad: int, matriculado: bool):
        self.nombre = nombre
        self.edad = edad
        self.matriculado = matriculado

def agregar_estudiante(registro: list, nombre: str, edad: int, matriculado: bool):
    """
    Agrega un estudiante al registro.

    :param registro: La lista que contiene el registro de estudiantes.
    :param nombre: El nombre del estudiante.
    :param edad: La edad del estudiante.
    :param matriculado: Estado de matrícula del estudiante.
    """
    nuevo_estudiante = Estudiante(nombre, edad, matriculado)
    registro.append(nuevo_estudiante)
    print(f"Estudiante {nombre} agregado exitosamente.")

def listar_estudiantes(registro: list):
    """
    Lista todos los estudiantes en el registro.

    :param registro: La lista que contiene el registro de estudiantes.
    """
    print("Lista de estudiantes:")
    for estudiante in registro:
        estado_matricula = "Matriculado" if estudiante.matriculado else "No matriculado"
        print(f"Nombre: {estudiante.nombre}, Edad: {estudiante.edad}, Estado: {estado_matricula}")

def calcular_edad_promedio(registro: list) -> float:
    """
    Calcula la edad promedio de los estudiantes en el registro.

    :param registro: La lista que contiene el registro de estudiantes.
    :return: La edad promedio de los estudiantes.
    """
    if not registro:
        return 0.0
    total_edades = sum(estudiante.edad for estudiante in registro)
    promedio = total_edades / len(registro)
    return promedio

def main():
    # Registro de estudiantes
    registro_estudiantes = []

    # Agregar algunos estudiantes al registro
    agregar_estudiante(registro_estudiantes, "Juan Pérez", 20, True)
    agregar_estudiante(registro_estudiantes, "María López", 22, False)
    agregar_estudiante(registro_estudiantes, "Carlos Ruiz", 19, True)

    # Listar estudiantes
    listar_estudiantes(registro_estudiantes)

    # Calcular y mostrar la edad promedio
    edad_promedio = calcular_edad_promedio(registro_estudiantes)
    print(f"La edad promedio de los estudiantes es: {edad_promedio:.2f} años")

if __name__ == "__main__":
    main()
