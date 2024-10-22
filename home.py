import forca_dificil
import facil
import prints
prints.printes().verdola()
escolha = input("Escolha \n[1] Fácil  \n[2] Médio \n[3] Díficil \n>>>")
try:
    match escolha:
            case '1':
                facil.forca_facil().facil_forca()
            case '2':
                print("teste")
            case '3':
                forca_dificil.testcc().dificil()
            case _:
                print("Erro")
except ValueError as error_value:
    print(error_value)
        