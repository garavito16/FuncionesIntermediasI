x = [ [5,2,3], [10,8,9] ] 
estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

z[0]["x"] = 15
print(z)
estudiantes[0]["last_name"] = "Bryant"
print(estudiantes)
directorio_deportes["fútbol"][0] = "Andrés"
print(directorio_deportes)
z[0]["y"] = 30
print(z)


print("----------------------------------")


estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterateDictionary(estudiantes):
    for i in range(len(estudiantes)):
        output = ""
        cant = 0
        for clave in estudiantes[i]:
            output += (clave) + " - " + estudiantes[i][clave]
            cant+=1
            if cant< len(estudiantes[i]):
                output += ", "
        print(output)

iterateDictionary(estudiantes)

print("----------------------------------")

def iterateDictionary2(key_name, some_list):
    for i in range(len(some_list)):
        for clave in some_list[i]:
            if clave == key_name:
                print(some_list[i][clave])

iterateDictionary2('first_name', estudiantes)
iterateDictionary2('last_name', estudiantes)

print("----------------------------------")

def printInfo(some_dict):
    for clave in some_dict:
        print(len(some_dict[clave]),clave.upper())
        for i in range (len(some_dict[clave])):
            print(some_dict[clave][i])

dojo = {
    'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)