# Passo 1: Cadastro de Login e de Senha

print("\n• Seu login dever ter pelo menos 5 caracteres ")
while True:
    Clogin = input("\nCadastre seu login: ").strip()
        # contador perfeito de caracteres
    if len("".join(Clogin.split())) < 5:
        print("O login deve ter no minimo 5 caracteres!")
    else:
        break

print("""\n• Sua senha deve ter entre 6 e 8 caracteres
• Não pode ser igual ao seu Login
• Deve conter apenas letras""")
while True:
    Csenha = input("\nCadastre sua senha: ").strip()
    if len("".join(Csenha.split())) < 6 or len("".join(Csenha.split())) > 8:
        print("A senha deve ter entre 6 e 8 caracteres!")
    elif Clogin == Csenha:
        print("Login e senha não podem ser iguais")    
    elif Csenha.isalpha() == False:
        print("A senha deve conter apenas letras")
    else:
        print("Tudo OK\nCadastro completo")
        break    

# Passo 2: Solicitar Login e Senha.

print("\n|Insira o Login e Senha|")
while True:
    login = input("\nLogin: ").strip()
    if login != Clogin:
        print("Login não encontrado.")
    else:
        break

while True:
    senha = input("\nSenha: ").strip()
    if senha != Csenha:
        print("Senha não encontrada.")
    else:
        break

# Passo 3: Inclusão e validação de informações

print("\n• Nome completo com pelo menos 5 caracteres e sem números")
while True:
    nome = input("\nNome: ").strip()
    if len("".join(nome.split())) < 5:
        print("O nome deve ter no minimo 5 caracteres!")
        # Verificador para não ter nada alem de letras
    elif "".join(nome.split()).isalpha() == False:
        print("O nome deve conter apenas letras")
    else:
        break

print("\n• Idade entre 0 e 100 anos")
while True:
    idade = int(input("\nIdade: "))
    if idade < 0 or idade > 100:
        print("Sua idade deve ser entre 0 e 100 anos.")
    else:
        break

print("""\n• RG entre 8 e 12 digitos
• Apenas digitos""")
while True:
    rg = input("\nRG: ").strip()
    if len("".join(rg.split())) < 8 or len("".join(rg.split())) > 12:
        print("O RG deve ter entre 8 e 12 digitos.")
        # Verificador para não ter nada alem de números
    elif rg.isnumeric() == False:
        print("O RG deve conter apenas digitos.")
    else:
       break

print("""\n• CPF com 11 digitos obrigatorios
• Apenas digitos""")
while True:
    cpf = input("\nCPF: ").strip()
    if len("".join(cpf.split())) != 11:
        print("seu CPF precisar ter exatamente 11 digitos.")
    elif cpf.isnumeric() == False:
        print("O CPF deve conter apenas digitos.")
    else:
        break

print("""\n• Salário deve ser maior que R$0
 { Favor substituir a "," por "." } """)
while True:
    salario = float(input("\nSalário: "))
    if salario <= 0:
        print("Seu salário precisa ser maior que R$0.")
    else:
        break

print("\n• Sexo 'M' 'F' ou 'O'")
while True:
    sexo = input("\nSexo: ").upper().strip()
    if sexo == "M":
        sexo = "Masculino"
        break
    elif sexo == "F":
        sexo = "Feminino"
        break
    elif sexo == "O":
        sexo = "Outros"
        break
    else:
        print("Escolha apenas entre as opções.")

print("\n• Estado Civil 'solteiro' 'casado' ou 'divorciado'")
while True:
    estadoC = input("\nEsctado Civil: ").capitalize().strip()
    if estadoC != "Solteiro" and estadoC != "Casado" and estadoC != "Divorciado": 
        print("Escolha apenas entre as opções.")
    else:
        break

# passo 4: Validação de dependetes

while True:
    dependente = input("\nTem dependentes? [S/N] : ").upper().strip()
    if dependente == "S":
        dependente = "Sim"
        print("\n• Nome completo do dependente com pelo menos 5 caracteres e sem números.")
        while True:
            nomedep = input("\nNome do dependente: ").strip()
            if len("".join(nomedep.split())) < 5:
                print("O nome do dependente deve ter no minimo 5 caracteres.")
            elif "".join(nomedep.split()).isalpha() == False:
                print("O nome do dependente deve conter apenas letras.")
            else:
                break

        print("• Idade entre 0 e 18 anos")
        while True:
            idadedep = int(input("\nIdade do dependente: "))
            if idadedep < 0 or idadedep > 18:
                print("A idade do dependete deve ser entre 0 e 18 anos.")
            else:
                break

        print("""• CPF do dependente com 11 digitos obrigatorios
• Apenas digitos""")
        while True:
            cpfdep = input("\nCPF do dependente: ").strip()
            if len("".join(cpfdep.split())) != 11:
                print("O CPF do dependete precisar ter exatamente 11 digitos.")
            elif cpfdep.isnumeric() == False:
                print("O CPF do dependente deve conter apenas digitos.")
            else:
                break

        print("\n• Sexo 'M' 'F' ou 'O'")
        while True:
            sexodep = input("\nSexo do dependente: ").upper().strip()
            if sexodep == "M":
                sexodep = "Masculino"
                break
            elif sexodep == "F":
                sexodep = "Feminino"
                break
            elif sexodep == "O":
                sexodep = "Outros"
                break
            else:
                print("Escolha apenas entre as opções.")

        break
    elif dependente == "N":
        dependente = "Não"
        break
    else:
        print("Esconlha apenas entre as opções.")

# Passo 5: Exibir todas as informações

print(f"""
§==============================§
| INFORMAÇÕES DO(A) USUARIO(A) |
§==============================§
♦ Nome: {nome}
♦ Idade: {idade} Anos
♦ RG: {rg}
♦ CPF: {cpf}
♦ Salário: R${salario:.2f}
♦ Sexo: {sexo}
♦ Estado Civil: {estadoC}
♦ Dependentes: {dependente}
§==============================§
""")

if dependente ==  "Sim":
    print(f""" 
§==============================§
| INFORMAÇÕES DO(A) DEPENDENTE |
§==============================§
♦ Nome: {nomedep}
♦ Idade: {idadedep} Anos
♦ CPF: {cpfdep}
♦ Sexo: {sexodep}
§==============================§
""")
