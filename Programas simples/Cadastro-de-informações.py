usuario = []
cont = 0

while True:
    cont += 1
    print("\n♦ USUARIO",cont)
    print("• SEU CODIGO PRECISA TER 5 DIGITOS")
    nome = input("→ Digite seu nome: ")
    altura = float(input("→ Digite sua altura: "))
    idade = input("→ Digite sua idade: ")
    usuario.append(f"""
====================
|Nome: {nome}
|Altura: {altura:.2f}
|Idade: {idade}
=====================""")
    while True:
        esc = input("\n→ Você quer cadastrar outro usuario?[s/n] ").lower()
        if "n" != esc != "s":
            print("\n•Erro!\n•Opção inválida.")
        else:
            break

    if esc == "n":
        break        
    
while True:
    try:
        i = int(input("\n♦ Número 0 para sair.\n→ Quem quer chamar? USUARIO "))
        if i == 0:
            print("Saindo...")
            break

        print(usuario[i-1])
    except ValueError:
        print("\n•Usuario não cadastrado.\n•Tente novamente")
    except IndexError:
        print("\n•Usuario não cadastrado.\n•Tente novamente")
    