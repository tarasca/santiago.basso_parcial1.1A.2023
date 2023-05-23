import os
import re
import json


#nota: hay funciones alternativas q terminan en guion bajo, muestran informacion en forma de fichas verticales.
def menu()->str:#funcion menu, hace clear y muestra un menu de opciones de vuelve str
    os.system("cls")
    print("1. Cargar datos desde archivo")#desde csv
    print("2. Listar insumos por marca")
    print("3. Listar insumos por marca")
    print("4. Buscar insumo por característica")
    print("5. Listar insumos ordenados")
    print("6. Realizar compras")
    print("7. Guardar en formato JSON")
    print("8. Leer desde formato JSON")
    print("9. Actualizar precios")
    print("10. Salir del programa")
    opt = input("ingresar opcion: ")
    return opt

def carga_csv(path_csv:str)->list:#carga el csv
    print("abriendo csv...")
    with open(path_csv, newline='',encoding='utf8') as File:  
        raw_data = File.readlines()
        raw_array = []
        for i in range(1,len(raw_data)-1):
            single = raw_data[i].split(sep=',')#divido el string por comas
            single[-1] = single[-1].strip('\r\n')
            single[-2] = single[-2].strip('$')
            insumo = {'id':single[0],'nombre':single[1],'marca':single[2],'precio':single[3],'carac':single[4]}#lo hago dict
            raw_array.append(insumo)#apendeo a la lista

    os.system("pause")
    return raw_array

def print_all(array_items:list):#imprime toda la lista
    print(f"|{'id':^2s}|{'nombre':^31s}|{'marca':^30s}|{'precio':^6s}|{'caracteristicas':^100s}|")
    print(f"|--|-------------------------------|------------------------------|------|----------------------------------------------------------------------------------------------------|")
    for item in array_items:
        print_insumo(item)
    os.system("pause")

def print_insumo(item:dict):#imprime cada dict
    print(f"|{item['id']:2s}|{item['nombre']:^31s}|{item['marca']:^30s}|{float(item['precio']):^6.2f}|{item['carac']:^100s}|")

def print_insumo_(item:dict):#imprime cada dict en forma de ficha
    print(f"ID = {item['id']}")
    print(f"NOMBRE = {item['nombre']}")
    print(f"MARCA = {item['marca']}")
    print(f"PRECIO = {item['precio']}")
    print(f"CARACTERISTICAS:\n {item['carac']}")

def print_marcas_cant_(array_items:list):#imprime insumos por marcas en forma de ficha
    print("listado de marcas y sus insumos:")
    print("--------------------------------")
    #print(f"|{'id':^2s}|{'nombre':^31s}|{'marca':^30s}|{'precio':^6s}|{'caracteristicas':^100s}|")
    marcas_set = set()
    for i in range(len(array_items)):
        marcas_set.add(array_items[i]['marca'])
    marcas_list = list(marcas_set)
    for i in range(len(marcas_list)):
        print(f"|marca: {marcas_list[i]}|")
        for j in range(len(array_items)):
            if(marcas_list[i] == array_items[j]['marca']):
                print("___________________________________________________")
                print(f"ID = {array_items[j]['id']}")
                print(f"NOMBRE = {array_items[j]['nombre']}")
                print(f"MARCA = {array_items[j]['marca']}")
                print("---------------------------------------------------")
            else:
                pass
    os.system("pause")

def print_marcas_cant(array_items:list):#imprime insumos por marca en forma de planilla
    print("listado de marcas y sus insumos:")
    print("--------------------------------")
    marcas_set = set()
    for i in range(len(array_items)):
        marcas_set.add(array_items[i]['marca'])
    marcas_list = list(marcas_set)
    for i in range(len(marcas_list)):
        print(f"\n|{'id':^2s}|{'marca':^30s}|{'nombre':^31s}|")
        print(f"|--|------------------------------|-------------------------------|")
        for j in range(len(array_items)):
            if(marcas_list[i] == array_items[j]['marca']):
                print(f"|{array_items[j]['id']:2s}|{array_items[j]['marca']:^30s}|{array_items[j]['nombre']:^31s}|")
            else:
                pass
    os.system("pause")
    
def print_marcas_cant_precio(array_items:list):#imprime insumos por marca y sus respectivos precios
    print("listado de marcas y sus insumos con sus respectivos precios:")
    print("------------------------------------------------------------")
    marcas_set = set()
    for i in range(len(array_items)):
        marcas_set.add(array_items[i]['marca'])
    marcas_list = list(marcas_set)
    for i in range(len(marcas_list)):
        print(f"\n|{'id':^2s}|{'marca':^30s}|{'nombre':^31s}|{'precio':^6s}|")
        print(f"|--|------------------------------|-------------------------------|------|")
        for j in range(len(array_items)):
            if(marcas_list[i] == array_items[j]['marca']):
                print(f"|{array_items[j]['id']:2s}|{array_items[j]['marca']:^30s}|{array_items[j]['nombre']:^31s}|{float(array_items[j]['precio']):^6.2f}|")
            else:
                pass
    os.system("pause")

def search_insumo(array_items:list):#busca insumo segun caracteristica
    print("-submenu buscar insumo-")
    pista = input("ingrese la frase(key-sensitive): ")
    listas = []
    for i in range(len(array_items)):
        coincidencia = {'index':i,'coincidencia':re.findall(pattern=pista,string=array_items[i]['carac'])}
        listas.append(coincidencia)
    for unit in listas:
        if(len(unit['coincidencia'])>0):
            print("--------------------------------------------")
            print(f"id:{unit['index']}")
            print(f"coincidencia:{unit['coincidencia']}")
            print(f"en:\n{array_items[unit['index']]['carac']}")
            print("-------------------------------------------")
    os.system('pause')

           
def print_ordenados(array_items:list):#ordena la lista y la muestra organizada
    sorted_array = array_items.copy()
    for i in range(len(sorted_array)-1):
        for j in range(i+1,len(sorted_array)):
            if(sorted_array[i]['marca'] > sorted_array[j]['marca']):#ordeno por marca alfabeticamente
                aux = sorted_array[i]
                sorted_array[i] = sorted_array[j]
                sorted_array[j] = aux    
            elif((sorted_array[i]['marca'] == sorted_array[j]['marca']) and (sorted_array[i]['precio'] > sorted_array[j]['precio'])):#desempato con precio
                aux = sorted_array[i]
                sorted_array[i] = sorted_array[j]
                sorted_array[j] = aux    
    
    print(f"|{'id':^2s}|{'descripcion':^31s}|{'precio':^6s}|{'marca':^30s}|{'primer carac.':^30s}|")
    print(f"|--|-------------------------------|------|------------------------------|------------------------------|")
    for item in sorted_array:  
        carac = item['carac'].split('~')
        print(f"|{item['id']:2s}|{item['nombre']:^31s}|{float(item['precio']):^6.2f}|{item['marca']:^30s}|{carac[0]:^30s}|")

    os.system("pause")

def realizar_compras(array_items:list):
    loop_1 = True
    
    index_carrito = 0
    carrito = []
    while loop_1:
        print("-->Submenu compras-->")
        print("1-Realizar compra")
        print("2-Salir")
        opt_loop_1 = input("ingresar opcion: ")
        match(opt_loop_1):
            case '1':
                new_compra = {}
                print("<---COMPRAS--->")
                print("se mostraran insumos a partir de la marca ingresada.")
                for item in array_items:
                    print(item['marca'])

                input_marca = input("ingresar marca: ")
                input_marca = input_marca.lower()
                input_marca = input_marca.capitalize()

                sub_array = []
                print(f"|{'id':^2s}|{'descripcion':^31s}|{'precio':^6s}|{'marca':^30s}|{'primer carac.':^30s}|")
                for item in array_items:
                    if(input_marca == item['marca']):
                        sub_array.append(item)
                        carac = item['carac'].split('~')
                        print(f"|{item['id']:2s}|{item['nombre']:^31s}|{float(item['precio']):^6.2f}|{item['marca']:^30s}|{carac[0]:^30s}|")
                      
                input_id = int(input("ingrese el id del producto que desea comprar(numero): "))
                
                for item in array_items:
                    if(input_id == int(item['id']) and item['marca'] == input_marca):
                        new_compra.update({'id_item':int(item['id']),'nombre_item':item['nombre'],'marca_item':item['marca'],'precio_item':float(item['precio'].strip('$'))})
                      
                input_cant = int(input("ingresar cantidad del producto seleccionado: "))
                new_compra.update({'cant_item':input_cant})
                new_compra.update({'total_item':(new_compra['precio_item'] * new_compra['cant_item'])})
                
                carrito.append(new_compra)
                index_carrito+=1
                print("compra exitosa!!!")
                print(f"ticket compra: {new_compra}")
                os.system('pause')

                pass
            case '2':
                print("finalizando compra...generando recibo...")
                file_recibo = open("factura.txt","w")
                for i in range(len(carrito)):
                    file_recibo.write(f"recibo {i+1}\n")
                    file_recibo.write(f"info item= id: {carrito[i]['id_item']} nombre: {carrito[i]['nombre_item']} marca: {carrito[i]['marca_item']}\n")
                    file_recibo.write(f"factura= precio unitario: {carrito[i]['precio_item']}$ cantidad: {carrito[i]['nombre_item']} total: {carrito[i]['total_item']}$\n")
                    file_recibo.write("--------------------------------------------------------------------------------------------------------------------------------------------------\n")
                    
                file_recibo.close()
                print("archivo generado!")
                os.system("pause")

                break

def json_pass(array_items:list)->str:
    print("vaciar listas")
    array_redux = []
    path_json = 'insumos.json'
    for item in array_items:
        v = re.match("Alimento",item['nombre'])
        if(v):
            array_redux.append(item)
    file = open(path_json,"w")    
    json.dump(array_redux,file,indent=4,separators=(", "," : "))
    file.close()    
    print("hecho!")
    os.system('pause')
    return path_json
    
def print_json(path:str):
    print("contenido json:")
    with open(path,'r') as file:
        data_stream = json.load(file)
    
    print_ordenados(data_stream)
    os.system('pause')

def actualizar_precios(path_csv:str,array_items:list):
    #aplicar aumento de 8.4% a todos los insumos y escribirlo en el csv
    coef = 0.084 
    array_aumentos = list(map(lambda precio_insumo:float(precio_insumo['precio']) + (float(precio_insumo['precio']) * coef),array_items))
    for i in range(len(array_items)):
        array_items[i]['precio'] = str(array_aumentos[i])
    with open(path_csv,'w') as file:
        for item in array_items:    
            file.write(f"{item['id']},{item['nombre']},{item['marca']},${item['precio']:7.3f},{item['carac']}\n")


    os.system("pause")
