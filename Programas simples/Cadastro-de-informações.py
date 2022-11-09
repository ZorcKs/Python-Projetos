success = '\033[32m'
error = '\033[31m'
tab_usuario = '\033[33m'
interface = '\033[34m'
usuario = []
cont = 0

def color(txt,cor):
    return cor + txt + '\033[0m'

while True:
    cont += 1
    print(color(f"\n♦ USUARIO {cont}",interface))
    nome = input(color("→ Digite seu nome: ",interface))
    altura = float(input(color("→ Digite sua altura: ",interface)))
    idade = int(input(color("→ Digite sua idade: ",interface)))
    usuario.append(f"""
====================
|Nome: {nome}
|Altura: {altura:.2f}
|Idade: {idade}
=====================""")
    while True:
        esc = input(color("\n→ Você quer cadastrar outro usuario?[s/n] ",interface)).lower()
        if "n" != esc != "s":
            print(color("\n•Opção inválida.",error))
        else:
            break

    if esc == "n":
        print(color("\nCadastro de usuarios concluido.",success))
        break        
    
while True:
    try:
        i = int(input(color("\n♦ Número 0 para sair.\n→ Quem quer chamar? USUARIO ",interface)))
        if i == 0:
            print(color("Saindo...",interface))
            break
        
        print(color(f"{usuario[i-1]}",tab_usuario))
    except ValueError:
        print(color("\n•Valor inválido.\n•Tente novamente.",error))
    except IndexError:
        print(color("\n•Usuario não cadastrado.\n•Tente novamente.",error))
    