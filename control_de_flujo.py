lista = [1, 2, 3, 4, '5', 'hola', False]

diccionario = [
    {
    'uno': 1,
    'dos': 2
    },
    {
    'tres': 3,
    'cuatro': 4
    }
]

users = [
    {
        'name': 'Juan',
        'username': 'juan123',
        'email': 'juan123@gmail.com'
    },
    {
        'name': 'Pedro',
        'username': 'pedro123',
        'email': 'pedro123@gmail.com'
    },
    {
        'name': 'Maria',
        'username': 'maria123',
        'email': 'maria123@gmail.com'
    },
    {
        'name': 'Jose',
        'username': 'jose123',
        'email': 'jose123@gmail.com'
    }
]
# Es mas recomendable usar len(lista) que 7 ya que si se agrega un elemento a la lista 
# el numero 7 ya no abarcaria todos los elementos de la lista

print(len(lista))

# for i in range(len(lista)):
#     print(lista[i])

# for element in lista:
#     print(element)

for element in diccionario:
    print(element)

# for i in range (len(users)):
#     print(users[i]['name'])
#     print(users[i]['email'])

for user in users:
    print(user['name'])
    print(user['email'])  
    
    if user['name'] == 'Juan':
        print('Es Juan')
    elif user['name'] == 'Maria':
        print('Es Maria')  
    else:
        print('No es Juan ni Maria')  

    # A partir de Python 3 Switch ya no existe de manera nativa
    # switch user['name']:
    #     case 'Maria':
    #         print('Es Maria')
    #     case 'Juan':
    #         print('Es Juan')    