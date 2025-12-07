lista_estudiantes = [
    {
        "nombre": "Jose Ludeña",
        "edad": 22,
        "promedio": 18.5
    },
    {
        "nombre": "David Vargas",
        "edad": 25,
        "promedio": 15.0
    },
    {
        "nombre": "Lionel Messi",
        "edad": 21,
        "promedio": 19.2
    }
]

def agregar_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ").strip()
    
    while True:
        try:
            edad = int(input("Ingrese la edad del estudiante: "))
            if edad <= 0:
                print("La edad debe ser un número positivo.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Ingrese un número entero para la edad.")
    
    while True:
        try:
            promedio = float(input("Ingrese el promedio del estudiante: "))
            if not (0.0 <= promedio <= 20.0):
                print("El promedio debe estar entre 0.0 y 20.0.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Ingrese un número real para el promedio.")

    estudiante = {
        "nombre": nombre,
        "edad": edad,
        "promedio": promedio
    }
    lista_estudiantes.append(estudiante)
    print(f"Estudiante '{nombre}' agregado exitosamente.")

def mostrar_estudiantes():
    if not lista_estudiantes:
        print("No hay estudiantes registrados.")
        return
    
    print("\nLista de Estudiantes")
    for i, est in enumerate(lista_estudiantes, 1):
        print(f"{i}. Nombre: {est['nombre']}, Edad: {est['edad']}, Promedio: {est['promedio']:.2f}")

def mostrar_mejor_promedio():
    if not lista_estudiantes:
        print("No hay estudiantes para calcular el mejor promedio.")
        return
    
    mejor_estudiante = max(lista_estudiantes, key=lambda est: est['promedio'])
    
    print("\nEstudiante con Mejor Promedio")
    print(f"Nombre: {mejor_estudiante['nombre']}")
    print(f"Edad: {mejor_estudiante['edad']}")
    print(f"Promedio: {mejor_estudiante['promedio']:.2f}")

def buscar_por_nombre():
    nombre_buscado = input("Ingrese el nombre del estudiante a buscar: ").strip()
    encontrados = [est for est in lista_estudiantes if nombre_buscado.lower() in est['nombre'].lower()]
    
    if encontrados:
        print(f"\nEstudiantes Encontrados ({len(encontrados)})")
        for est in encontrados:
            print(f"Nombre: {est['nombre']}, Edad: {est['edad']}, Promedio: {est['promedio']:.2f}")
    else:
        print(f"No se encontró ningún estudiante con el nombre '{nombre_buscado}'.")

def eliminar_por_nombre():
    global lista_estudiantes 

    nombre_eliminar = input("Ingrese el nombre del estudiante a eliminar (coincidencia exacta): ").strip()
    
    estudiantes_antes = len(lista_estudiantes)
    
    lista_estudiantes = [est for est in lista_estudiantes if est['nombre'] != nombre_eliminar]
    
    if len(lista_estudiantes) < estudiantes_antes:
        print(f"Estudiante '{nombre_eliminar}' eliminado exitosamente.")
    else:
        print(f"No se encontró un estudiante con el nombre '{nombre_eliminar}' para eliminar.")

def menu_principal():
    while True:
        print("\nRegistro de Estudiantes")
        print("1. Agregar estudiante")
        print("2. Mostrar estudiantes")
        print("3. Mostrar estudiante con mejor promedio")
        print("4. Buscar por nombre")
        print("5. Eliminar por nombre")
        print("6. Salir")
        
        opcion = input("Seleccione una opción (1-6): ")
        
        if opcion == '1':
            agregar_estudiante()
        elif opcion == '2':
            mostrar_estudiantes()
        elif opcion == '3':
            mostrar_mejor_promedio()
        elif opcion == '4':
            buscar_por_nombre()
        elif opcion == '5':
            eliminar_por_nombre()
        elif opcion == '6':
            print("Saliendo del programa. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

menu_principal()