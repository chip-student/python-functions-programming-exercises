# Your code goes here:
def render_person(name, datebirth, color, age, genero):
    concatena = name +' is a '+ str(age) +' years old '+ genero +' born on ' + datebirth + ' with ' + color +' eyes'
    return concatena 


# Do not edit below this line
print(render_person('Bob', '05/22/1983', 'green', 23, 'male'))