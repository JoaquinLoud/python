from menu import menu
def pintarMenu():
    op = menu()
    for clave in op[1]:
        if (op[0] == clave):
            print("Esta funcion se llama: ", op[1][clave][1])

if __name__ == "__main__":
    pintarMenu()