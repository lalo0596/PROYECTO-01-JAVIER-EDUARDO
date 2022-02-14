from pickle import TRUE
from unicodedata import category
from lifestore_file import lifestore_searches, lifestore_sales, lifestore_products
"""
La info de LifeStore_file:

lifestore_searches = [id_search, id product]
lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
lifestore_products = [id_product, n ame, price, category, stock]
"""
"""
login
credenciales:
usuario:
    lalo96
contraseña:
    dudu96


"""
def login():
    usuarioAccedio = False
    intentos = 0
    mensajeBienvenida = 'Bienvenida al sistema\nAccede con tus credenciiales'
    print(mensajeBienvenida)

    while not usuarioAccedio:
        usuario = input('usuario: ')
        contraseña = input('contraseña: ')
        intentos += 1
        if usuario == 'lalo96' and contraseña == 'dudu96':
            usuarioAccedio = True
            print('Hola de nuevo')
        else:
            if usuario == 'lalo96':
                print('Te equivocaste en la contraseña')
            else:
                print(f'El usuario: "{usuario}" no esta registrado')
        print('tienes', 3- intentos, 'intentos restantes ')
        #print(f'tienes {3- intentos}  intentos restantes ')  --> es para reducir una linea de codigo 
        if intentos == 3:
            exit()


def punto_1():

    prod_vistas = {}
    for busqueda in lifestore_searches:
        prod_id = busqueda[0]
        busq_id= busqueda[1]

        if busq_id not in prod_vistas.keys():
            prod_vistas[busq_id] = []
            prod_vistas[busq_id].append(busqueda)

        for key in prod_vistas.keys():
            print(key)
            print(prod_vistas[key])

    category_ids = {}
    for venta in lifestore_sales:
        id_venta = venta[1]
        if id_venta not in category_ids.keys():
            category_ids[id_venta] = []
            category_ids[id_venta].append(id_venta)

    resultado_por_cateria = ()
    for category, venta_id_lista in category_ids.items():
        prod_busq = []
        busq = 0
        ventas = 0
        for venta_id in venta_id_lista:
            if venta_id not in prod_vistas.keys():
                continue
            ventas_busqueda = prod_vistas[venta_id] 
            sale = lifestore_sales[venta_id][1]
            total_sales = len(venta_id)

            prod_busq += ventas_busqueda
        prod_vistas = sum(prod_vistas) / len(prod_vistas)

        resultado_por_cateria[category] = {
            'prod_busq' : prod_busq,
            'ventas' : ventas,
        }
    print(resultado_por_cateria)




def punto_2():
   #hacer el analisis de reviews por ategoria tambien la de ventas 
    prod_reviews = {}
    for sale in lifestore_sales:
        #prod y reviews de venta 
        prod_id = sale[1]
        review = sale[2]
        #categorizar por id 
        if prod_id not in prod_reviews.keys():
            prod_reviews[prod_id] = []
        prod_reviews[prod_id].append(review)

    
    id_rev_prom = {}
    for id, reviews in prod_reviews.items(): 
        rev_prom = sum(reviews) / len(reviews)
        rev_prom = int(rev_prom*100)/100
        id_rev_prom[id] = [rev_prom, len(reviews)]
#para orrdenar siempre esmas 
    dicc_en_lista = []
    for id, lista in id_rev_prom.items():
        
        rev_prom = lista[0]
        cant = lista[1]
        sub = [id, rev_prom, cant]
        dicc_en_lista.append(sub)

    def seg_elemento(sub):
        return sub[1]

    
    
    dicc_en_lista = sorted(dicc_en_lista, key=seg_elemento, reverse=True)
    """ dicc_en_lista = sorted(dicc_en_lista, key=lambda lista:lista[2], reverse=True) """

    for sublista in dicc_en_lista:
        print(sublista)
    print('\nTop 5 productos con las mejores reseñas\n')
    for sublista in dicc_en_lista[:5]:
        id, rev, num = sublista
        indice_lsp = id - 1
        prod = lifestore_products[indice_lsp]
        nombre = prod[1]
        nombre = nombre.split(' ')
        nombre = ' '.join(nombre[:4])
        
        print(f'El producto "{nombre}":\n\trev_prom: {rev}, num de ventas: {num}')
    print('\nTop  5 productos con las peores reseñas\n')    
    for sublista in dicc_en_lista[-5:]:
        id, rev, num = sublista
        indice_lsp = id - 1
        prod = lifestore_products[indice_lsp]
        nombre = prod[1]
        nombre = nombre.split(' ')
        nombre = ' '.join(nombre[:4])
        
        print(f'El producto "{nombre}":\n\trev_prom: {rev}, num de ventas: {num}')






def punto_3():
    id_fecha = [ [sale[0], sale[3]] for sale in lifestore_sales if sale[4] == 0 ]
    # Para categorizar usamos un diccionario
    categorizacion_meses = {}

    for par in id_fecha:
        # Tengo ID y Mes
        id = par[0]
        _, mes, _ = par[1].split('/')
        # Si el mes aun no existe como llave, la creamos
        if mes not in categorizacion_meses.keys():
            categorizacion_meses[mes] = []
        categorizacion_meses[mes].append(id)

    # mes : [ids de venta]

    # for key in categorizacion_meses.keys():
    #     print(key)
    #     print(categorizacion_meses[key])

    # crear dic
    mes_info = {}
    for mes, ids_venta in categorizacion_meses.items():
        lista_mes = ids_venta
        suma_venta = 0
        for id_venta in lista_mes:
            indice = id_venta - 1
            info_venta = lifestore_sales[indice]
            id_product = info_venta[1]
            info_prod = lifestore_products[id_product-1]
            precio = info_prod[2]
            suma_venta += precio
        print(mes, suma_venta, f'ventas totales: {len(lista_mes)}')
        mes_info[mes] = [suma_venta, len(lista_mes)]

    mes_ganancia_ventas = []
    for mes, datos in mes_info.items():
        ganancias, ventas = datos
        sub = [mes, ganancias, ventas]
        mes_ganancia_ventas.append(sub)

    ord_mes = sorted(mes_ganancia_ventas)
    ord_gancia = sorted(mes_ganancia_ventas, key=lambda x:x[1], reverse=True)
    ord_ventas = sorted(mes_ganancia_ventas, key=lambda x:x[2], reverse=True)

    print(ord_ventas)

    id_ventas = []
    for prod in lifestore_products:
        id_prod = prod[0]
        sub = [id_prod, 0]
        id_ventas.append(sub)

    for sale in lifestore_sales:
        id_prod = sale[1]
        indice = id_prod - 1
        if sale[-1] == 1:
            continue
        id_ventas[indice][1] += 1

    print(id_ventas)


def menu():
    login()
    while True:
        print("inicio del proyecto")
        print("\t1: Producto más vendido y productos rezagados")
        print("\t2: productos por reseñas en el servicio")
        print("\t3: promedio mensual,anual y meses con mas demanda")
        print("\t0: Salir")
        seleccion = input('> ')
        if seleccion == '1':
            punto_1()
            print('\n') 
        elif seleccion == '2':
            punto_2()
            print('\n') 
        elif seleccion == '3':
            punto_3()
            print('\n')        
        elif seleccion == '0':
            exit()
        else:
            print('Opcion invalida, solamente son los numeros que aparecen, proximamente nuevas opciones')
menu()

   