login_lst = []
senha_lst = []
while True:
    home_input = int(input(f"""\033[m{'Sorveteria Napolitano':-^50}
[1] LOGIN
[2] REGISTRAR

Escolha: """))
    if home_input > 2 or home_input <= 0:
        print(f'\033[31mESCOLHA UM OPÇÃO VÁLIDA')
    def registro(home_input_par):
        if home_input_par == 2:
            while True:
                login_input = input(f'\033[mRegistre seu login: ')
                if ' ' in login_input:
                    print(f'\033[31mNÃO É PERMITIDO ESPAÇOS')
                else:
                    login_lst.append(login_input)
                    break
            while True:
                senha_input = input(f'\033[mRegistre sua senha: ')
                if ' ' in senha_input:
                    print(f'\033[31mNÃO É PERMITIDO ESPAÇOS')
                else:
                    senha_lst.append(senha_input)
                    break
    registro(home_input)