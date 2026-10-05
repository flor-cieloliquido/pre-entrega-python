
productos = [] #[[],[],[]]

while True:
    print("="*30)
    print("\033[92mSistema de gestión de productos\033[0m")
    print("="*30)
    print("\n1. Agregar productos")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")

    opt = input("\nElegí una opción (1-5): ").strip()
    
    if opt == "1":
        print("\n\033[92m---- Agregar producto ----\033[0m")
        while True:
            nombre = input("\nNombre del producto (ingresá 's' para volver al menú principal): ").strip()
            if nombre == "s":
                break
            while nombre == "":
                print("\n\033[91mIngrese un producto válido\033[0m")
                nombre = input ("\nNombre del producto (ingresá 's' para volver al menú principal): ").strip()

            categoria = input("Categoria del producto: ").strip()
            while categoria == "":
                print("\n\033[91mIngrese una categoria válida\033[0m")
                categoria = input ("Categoria del producto: ").strip()

            precio_str = input("Precio del producto (sin centavos): ").strip()
            while not precio_str.isdigit():
                print("\n\033[91mIngrese un precio válido (sin centavos)\033[0m")
                precio_str = input("Precio del producto (sin centavos): ").strip()
            precio = int(precio_str)

            datos = [nombre,categoria,precio]
            productos.append(datos)
            # print(productos)
    
    elif opt == "2":
        print("\n\033[92m---- Lista de productos ----\033[0m")

        if len(productos) == 0:
            print("\n\033[93mTodavia no hay productos cargados\033[0m")
        else:
            for i in range (0,len(productos),1):
                print(f"\nID: {i+1}\n- Nombre: {productos[i][0]}\n- Categoría: {productos [i][1]}\n- Precio: ${productos [i][2]}")

    elif opt == "3":
        print("\n\033[92m---- Buscar producto ----\033[0m")
        if len(productos) == 0:
            print("\n\033[93mTodavia no hay productos cargados\033[0m")
        else:
            busqueda = input("\nIngrese producto a buscar: ").strip().lower()
            while busqueda == "":
                print("\n\033[91mIngrese un nombre de producto válido\033[0m")
                busqueda = input("\nIngrese producto a buscar: ").strip().lower()

            encontrado = 0
            for i in range (len(productos)):
                if busqueda in productos[i][0].lower():
                    print(f"\nProducto encontrado\nID: {i+1}\n- Nombre: {productos[i][0]}\n- Categoría: {productos [i][1]}\n- Precio: ${productos [i][2]}")
                    encontrado += 1
            if encontrado == 0:
                print("\n\033[91mNo se encontró ningun resultado\033[0m")
            else:
                print(f"\nProductos econtrados: {encontrado}")

    elif opt == "4":
        print("\n\033[92m---- Eliminar producto ----\033[0m")
        if len(productos) == 0:
                    print("\n\033[93mTodavia no hay productos cargados\033[0m")
        else:
            for i in range (len(productos)):
                print(f"\nID: {i+1}\n- Nombre: {productos[i][0]}\n- Categoría: {productos [i][1]}\n- Precio: ${productos [i][2]}")    
            while True:
                id_eliminar = input ("\nIngrese numero de producto a eliminar (o ingrese 's' para salir): ").strip()
                if id_eliminar == 's':
                    break
                if  len(productos) <= 0:
                    print("\033[93mLa lista se encuentra vacía\033[0m")
                    break
                
                while not id_eliminar.isdigit():
                    print("\n\033[91mIngresá un id válido\033[0m")
                    id_eliminar = input ("\nIngrese numero de producto a eliminar: ").strip()
                id_eliminar_int = int(id_eliminar)
                # #aca quiero que no se rompa el programa cuando pongo un id mayor que el n° de items en la lista, sino me da error de index : pop index out of range
                # while id_eliminar_int > len(productos):
                #     print("\n\033[91mIngresá un id válido\033[0m")
                #     id_eliminar = input ("\nIngrese numero válido de producto a eliminar: ").strip()
                posicion = id_eliminar_int - 1
                eliminado = productos.pop(posicion)
                print(f"\n\033[91mSe eliminó el producto: {eliminado[0]}\033[0m")

    elif opt == "5":
        print("\n\033[93mGracias por utilizar nuestro sistema!\033[0m")
        break
    else:
        print("\n\033[91mIngrese una opción válida de 1 a 5\033[0m")