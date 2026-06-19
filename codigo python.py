import csv

def cargar_empleados():
    ruta = __file__.replace("codigo python.py", "empleado.csv")
    with open(ruta, mode='r', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        return {f['legajo']:{'nombre': f['nombre'],'dias': int(f['dias'])} for f in lector}

empleado = cargar_empleados()
estado = "inicio"
formulario = {}
#-------------------------------------------- DESARROLLO DEL PROGRAMA --------------------------------------------
print("🤖 VacacionesBot 🤖 - Sistema de Gestión de Solicitudes de Vacaciones ✈️ - Departamento de Recursos Humanos 💼\n\n")
print("¡Hola! 👋\n")

while True:
    if estado == "inicio":
        solicitud = input("Ingrese SOLICITAR para pedir días de vacaciones 📩 \nIngrese SALIR para terminar 🚪🏃🏻‍♀️")
        solicitud = solicitud.lower()

        if solicitud == "solicitar":
            estado = "legajo"
            print()
        elif solicitud == "salir":
            print("👋 Gracias por usar el sistema 👋")
            break
        else:
            print("🚫 Ingrese una opción válida: SOLICITAR o SALIR 🚫")

    elif estado == "legajo":
        legajo = input("Por favor, ingrese su número de legajo 🗂️: ")
        print()

        if legajo in empleado:
            formulario["legajo"] = legajo
            nombre = empleado[legajo]["nombre"]
            print(f"¡Hola, {nombre}! 👋😊")
            estado = "dias"
        else:
            print("ERROR ❗. Legajo no encontrado 🤔 Ingréselo nuevamente 🔍")

    elif estado == "dias":
        try:
            dias = int(input("¿Cuántos días de vacaciones desea solicitar? 📅 "))

            if dias <= 0:
                print("Error ❗. Debe ingresar una cantidad de días mayor a 0 🔢")
            
            else:
                formulario["dias"] = dias
                estado = "verificar"
                print()
        except ValueError:
            print("ERROR ❗. Ingrese solo numeros 🔢")

    elif estado == "verificar":
        legajo = formulario["legajo"]
        solicitud_dias = formulario["dias"]
        dias_disponibles = empleado[legajo]["dias"]

        if solicitud_dias <= dias_disponibles:
            empleado[legajo]["dias"] -= solicitud_dias
            resto_dias = empleado[legajo]["dias"]
            print(f"Estado de solicitud APROBADA ✅. Le quedan {resto_dias} dias de vacaciones\n")
        else:
            print(f"Estado de solicitud RECHAZADA ❌. Solo le quedan {dias_disponibles} dias de vacaciones disponibles\n")

        estado = "inicio"
        formulario = {}
        print("Escribí SOLICITAR 📝 para hacer otra solicitud o SALIR 🚪")