import random
options = [["piedra", 1], ["esponja", 2], ["pistola", 3], ["lobo", 4], ["rayo", 5], ["arbol", 6], ["diablo", 7], ["humano", 8], ["dragon", 9], ["serpiente", 10], ["agua", 11], ["tijera", 12], ["aire", 13], ["fuego", 14], ["papel", 15]] 
random_option = random.randint( 0, len(options)-1)
option_computer = options[random_option]
option_user = []
print("¿Que quieres saca piedra, esponja, pistola, lobo, rayo, arbol, diablo, humano, dragon, serpiente, agua, tijera, aire, fuego, papel?")
def option_user(options):
    valid_option = True
    option_return = []
    while valid_option:
        option_str_user = input().lower()
        for i in range(len(options)):
            if option_str_user in options[i]:
                option_return = options[i]
                valid_option = False
        if valid_option:
            print("Has introducido mal tu opción intenta escribirlo bien ahora")
    return option_return
option_user = option_user(options)
def form(option_computer, option_user):
    if option_computer[1] % 2 != 0:
        option_computer[1] *= -1
        option_user[1] *= -1
    if option_user[1] %2 != 0:
        option_computer[1] *= -1
        option_user[1] *= -1
form(option_computer, option_user)
def result(option_computer, option_user):
    if option_computer == option_user:
        print("La maquina ha sacado " + option_computer[0] + " habeis empatado")
    else:
        if option_computer[1]>option_user[1]:
            print("La maquina ha sacado " + option_computer[0] + " ,has perdido")
        else:
            print("La maquina ha sacado " + option_computer[0] + " ,has ganado")
result(option_computer, option_user)