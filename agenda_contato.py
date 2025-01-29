""" 
Nesse desafio desenvolveremos uma agenda para salvar, editar, deletar e marcar um contato como favorito. 
"""


agenda_contatos=[]

def cadastrar_contato(digitar_nome, digitar_telefone, digitar_email):
    novo_contato={
    "Nome":digitar_nome,
    "Celular":digitar_telefone, 
    "E-mail":digitar_email, 
    "Favorito":False
    }
    
    agenda_contatos.append(novo_contato)
    
    print(
    """
====| Cadastro efetuado com sucesso |=====              
    """)
    return


def consultar_cadastro(agenda_contatos):
    for contato_vez in agenda_contatos:
        print(f"""
Nome:{contato_vez["Nome"]}
Celular:{contato_vez["Celular"]}
E-mail:{contato_vez["E-mail"]}
Favorito:{contato_vez["Favorito"]}""")
        
def editar_cadastro(agenda_contatos):
    contato_editado=input("\nDigite o nome do contato a ser editado: ").upper()
    contato_encontrado = False
    
    for contato_em_questao in agenda_contatos:
        if contato_em_questao["Nome"]==contato_editado:
            contato_encontrado = True
            while True:
                submenu_edtar=input("""
    Qual atributo deseja editar?
    1. Nome
    2. Celular
    3. E-mail
    4. Sair
    R: """)
                match submenu_edtar:
                    case "1":
                        novo_nome = str(input("\nDigite o novo nome do contato: ")).upper()
                        contato_em_questao["Nome"] = novo_nome
                        print("""
===========| Nome alterado |=============""")

                    case "2":
                        novo_celular = str(input("\nDigite o novo número para contato: ")).replace("(", "").replace(")", "").replace("-", "").replace(" ", "")
                        contato_em_questao["Celular"] = novo_celular
                        print("""
==========| Telefone alterado |==========""")
                        

                    case "3":
                        novo_email = str(input("\nDigite o novo e-mail para contato: ")).upper()
                        contato_em_questao["E-mail"] = novo_email
                        print("""
===========| E-mail alterado |============""")
                        
                            
                    case "4":
                        print("""
================| Saindo |================""")
                        break   
                        
                    case _:
                        print("""     
============| Entrada inválida |============ 
Digite apenas números entre 1 e 5.""") 
                break 
    if not contato_encontrado:
        print("""
======| Contato não encontrado |========""")
        
def marcar_favorito(agenda_contatos, contato_nome):
    contato_encontrado = False
    for contato in agenda_contatos:
        if contato["Nome"]==contato_nome:
            contato["Favorito"] = not contato["Favorito"]
            status = "favorito" if contato["Favorito"] else "não como favorito"
            print(f"""
Contato '{contato_nome}' agora está {status}.""")
            contato_encontrado = True
            break
        
    if not contato_encontrado:
        print(f"\nContato '{contato_nome}' não encontrado na agenda.")
    
def listar_favoritos(agenda_contatos):
    favoritos = [contato for contato in agenda_contatos if contato["Favorito"]]

    if favoritos:
        print("\n===== Lista de Contatos Favoritos =====")
        for contato in favoritos:
            print(f"""
Nome: {contato["Nome"]}
Celular: {contato["Celular"]}
E-mail: {contato["E-mail"]}
            """)
    else:
        print("\nNenhum contato foi marcado como favorito ainda.")


def excluir_contato(agenda_contatos):
    contato_excluido=input("\nDigite o nome do contato que você deseja excluir: ").upper()
    contato_encontrato=False
    
    for contato_vez in agenda_contatos:
        if contato_vez["Nome"]==contato_excluido:
            agenda_contatos.remove(contato_vez)
            contato_encontrato=True
            print("""
=====| Contato excluido com sucesso |=====""")



while True:
    try:
        menu = (input("""
==========================================
        xx AGENDA DE CONTATOS xx  
==========================================

Escolha uma opção:

1. Adicionar contato
2. Visualizar lista de contatos
3. Editar contato
4. Marcar/desmarcar contato como favorito
5. Visualizar lista de contatos favoritos
6. Apagar contato
7. Sair
R: """))
        
        match menu:
            case "1":
                digitar_nome = input("\nNome: ").upper()
                digitar_telefone = input("Celular: ").replace("(", "").replace(")", "").replace("-", "").replace(" ", "")
                digitar_email = input("E-mail: ").upper()
                cadastrar_contato(digitar_nome, digitar_telefone, digitar_email)

            case "2":
                print("\nContatos:")
                consultar_cadastro(agenda_contatos)
                
            case "3":
                print("\nLista de contatos:")
                consultar_cadastro(agenda_contatos)
                editar_cadastro(agenda_contatos)
                
            case "4":
                nome_contato = (input("\nDigite o nome do contato que deseja marcar como favorito: ")).upper()
                marcar_favorito(agenda_contatos, nome_contato)

            case "5":
                listar_favoritos(agenda_contatos)
                
            case "6":
                consultar_cadastro(agenda_contatos)
                excluir_contato(agenda_contatos)

            case "7":
                print("""
================| Saindo |================
""")
                break

            case _:
                print("""
============| Opção inválida |============ 
Favor escolher uma das opções informadas (1 a 7).""")

    except ValueError:
        print("""
============| Entrada inválida |============ 
Digite apenas números entre 1 e 7.""")
