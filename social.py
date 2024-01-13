import time
class RedeSocial:
             def __init__(self,nome,idade,senha):
                     self.nome=nome
                     self.idade=idade
                     self.senha=senha
                     print(f'Bem Vindo(a) de Volta {nome} sua senha é {senha} atualmente tem {idade} anos.')

             def amigos(nome=str,contatos=0):
                    while True:
                     nome=nome
                     contatos=tuple()
                     try:
                       lista=list
                       nome=str(input('*Adicionar:'))
                
                     except KeyboardInterrupt:
                                # break
                                print('\n\033[31mUsuário saiu inesperadamente :(\033[m')
                                break
                     except ValueError:
                            print('Digite somente LETRAS!!')

                     contatos=tuple()
                     contatos={'nome':nome}
                     
                #      time.sleep(2)
                     print('pesquisando...')
                     time.sleep(2)
                    #  print(f'{nome} foi encontrado')
                     if nome :
                             
                               print(f'{nome} foi encontrado')
                        #        lista=[]
                        #        lista.append(nome)
                               time.sleep(1)
                               print(f'sua lista de amigos foi atualizada.. ({lista})') 
                               try:   
                                d =int(input('*adicionar:[1para sim 2 para não]'))
                        #        except KeyboardInterrupt:
                        #                 print('\n\033[31mUsuário saiu inesperadamente :(\033[m')
                                if d > 2:
                                        print('Ops!!')
                                else:        
                                     if d ==2:
                                       print(contatos)
                                       print('lista atualizada com Sucesso!!')
                                       break    
                               except KeyboardInterrupt:
                                       print('\n\033[31mUsuário saiu inesperadamente :(\033[m')
                                       break
             def publicar(mensagem=str):
                     mensagem=mensagem
                     mensagem=str(input('No que está Pensando? '))
                     
                     print('Publicando...')
                     time.sleep(3)
                     print(mensagem)
                                      
             def Comentar_post(opção=str,coment=str):
                while True:
                     print('[1]NOTÍCIAS')
                     print('[2]FAMOSOS')
                     print('[3]NATUREZA')
                     opção= int(input('qual post você deseja ver?'))
                     if opção ==1:
                             print('Japão aumenta números de militares\n para salvar vitímas de terremotos...') 
                             coment=str(input('comentar:'))
                             print(coment)
                             print('Publicando..')
                             time.sleep(3)
                             print(coment)               
                     if opção ==2:
                             print('Morre Cantor famoso do sertanejo...')
                             coment=str(input('comentar:'))
                             print('Publicando...')
                             time.sleep(3)
                             
                             print(coment)
                     if opção ==3:
                             print('Doença do Cervo Zumbi gera alerta nos Estados Unidos...') 
                             coment=str(input('comentar:'))
                             
                             
                             print('Publicando...')
                             time.sleep(3)
                             print(coment)
                     break
             def busca_usuario(us=list,busca=str):
                     
                     us=['João ','karine','Pablo','Ana','Julia','Henrique','Paula','Marcos','Pedro'.title()]
                     busca= str(input('buscar Usuario:')).title()
                     if busca in us:
                             print(f'{busca} foi encontrado!')
                     else:
                             print('Usuario não encontrado')
class CriandoConta(RedeSocial): 
                def __init__(cls,nome=str,idade=int,senha=int):
                            cls.nome=nome
                            cls.idade=idade
                            cls.senha=senha
                while True:
                        try:
                       
                            nome=str(input('Nome do usuário:'))
                            idade=int(input('Sua Idade atual:'))
                        
                               
                            senha=str(input('Crie uma nova senha(somente números de 0-9,letras a-z e um caracteres(@#$%*)): '))
                        except (KeyboardInterrupt):
                                print('\033[31mHouve um erro inesperado :(\033[m')
                                break
                        else:
                                print(f'Sua conta foi criada : nome de {nome}, de {idade} anos e senha é {senha}')        
                        break    