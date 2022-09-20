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
                global user_log
                user_log = login_input
                if ' ' in login_input:
                    print(f'\033[31mNÃO É PERMITIDO ESPAÇOS')
                else:
                    login_lst.append(login_input)
                    break
            while True:
                senha_input = input(f'\033[mRegistre sua senha: ')
                global user_pass
                user_pass = senha_input
                if ' ' in senha_input:
                    print(f'\033[31mNÃO É PERMITIDO ESPAÇOS')
                else:
                    senha_lst.append(senha_input)
                    break
            if home_input == 1:
            for i in range (len(login_lst)):
                user_log = str(input('Insira seu login: '))
                if user_log in login_lst:
                    print('Login correto')
                else:
                    print(f"""\033[m{'Login incorreto':-^50}""")
                    break
                user_pass = input('insira sua senha: ')
                if user_pass in senha_lst:
                    print('senha correta')
                    print(f"""\033[m{'Você esta logado':-^50}""")
                    break
                else:
                    print(f"""\033[m{'senha incorreta':-^50}""")
                    break
    registro(home_input)
