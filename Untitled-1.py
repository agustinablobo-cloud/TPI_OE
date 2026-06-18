def cargar_csv(csv):

    empleados = []

    try:

        with open(csv, "r") as archivo:

            lineas = archivo.readlines()

            for i in range(1, len(lineas)):

                linea = lineas[i].strip()
                datos = linea.split(",")

                empleado = {
                    "legajo": int(datos[0]),
                    "nombre": datos[1],
                    "diasdisponibles": int(datos[2])
                }

                empleados.append(empleado)

    except FileNotFoundError:
        print("Error: No se encontro el archivo")

    except ValueError as e:
        print(f"Error en los datos: {e}")

    except IndexError:
        print("Error: Faltan columnas en el CSV")

    

    return empleados


def ingresar_legajo(empleados):

    while True:
        try:

            legajo = input("Ingresa su legajo: ")

            if legajo == "":
                raise ValueError("Error: el legajo no puede estar vacio")
            
            if not legajo.isdigit():
                raise ValueError("Error: debe ingresar un numero entero")
            
            legajo_a_cargar = int(legajo)

            if legajo_a_cargar <= 0:
                raise ValueError("Error: el legajo debe ser mayor a 0")
            

            existe = False

            for empleado in empleados:
                if empleado["legajo"] == legajo_a_cargar:
                    existe = True
                    break
            
            if not existe:
                raise ValueError("Error: el legajo no existe")
            
            return legajo_a_cargar


        except ValueError as e:
            print(e)
            