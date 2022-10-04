#   Essa biblioteca é so pra criptografia pra fazer graça :)
import hashlib

def registrar():
    user = input('Registre o usuário: ')
    pwd = input('Registre a senha: ')
    conf_pwd = input('Confirme a senha: ')
    if conf_pwd == pwd:
        enc = conf_pwd.encode()
        hash1 = hashlib.md5(enc).hexdigest()

    with open('registros.txt', 'w') as f:
        f.write(user + '\n')
        f.write(hash1)
    f.close()
    print('Registrado com sucesso!')


def login():
    user = input('Coloque seu usuário: ')
    pwd = input('Coloque sua senha: ')
    auth = pwd.encode()
    auth_hash = hashlib.md5(auth).hexdigest()
    with open('registros.txt', 'r') as f:
        stored_user, stored_pwd = f.readlines().split('\n')
    f.close()
    if user == stored_user and auth_hash == stored_pwd:
        print(f'Logado com sucesso, {user}!')
    else:
        print('Login falhou! \n')


def excluir():
    with open('registros.txt', 'r') as fr:
        lines = fr.readlines()
        ptr = 1
        # Tem que rodar 2 vezes pra apagar a senha tbm :(
        ptr_del = int(input('Escolha a linha que quer excluir(Verifique no registros.txt): '))

        with open('registros.txt', 'w') as fw:
            for line in lines:
                if ptr != ptr_del:
                    fw.write(line)
                ptr += 1
    print("Deletado!")


def alterar():
    search_text = input('Confirme seu usuário: ')
    replace_text = input('Coloque o usuário novo: ')
  
    with open('registros.txt', 'r') as f:
        data = f.read()    
    
    data = data.replace(search_text, replace_text)
  
    with open('registros.txt', 'w') as f:
        f.write(data)

    print("Nome de usuário troca com sucesso!")


while True:
    print("********** Sistema de Login **********")
    print("1.Registrar")
    print("2.Login")
    print("3.Excluir")
    print("4.Alterar")
    print("5.Sair")
    ch = int(input("Escolha: "))
    if ch == 1:
        registrar()
    elif ch == 2:
        login()
    elif ch == 3:
        excluir()
    elif ch == 4:
        alterar()
    elif ch == 5:
        break
    else:
        print("Escolha uma opção válida!")