hobbies = []
for i in range(3):
    hobbies.append(input('Ingrese un hobbie: '))
with open('miHobbieFavorito.txt.', 'a') as file:
    for hobby in hobbies:
        file.write('\n' + hobby)
