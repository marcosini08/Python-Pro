# Programa "Sistema para estacionamento privado"
# UFRN/Ceres- Algoritmos e Lógica de Programação
# Made by Sir Marcos Vinícius Naturalista de Pub
# Início:

print('\n       Sistema para estacionamento da empresa\n')
from time import sleep
sleep(2.27)






from datetime import datetime
from datetime import date
import pickle
#LE: listagem pra guardar informações de estacionagem (ns) de tal ou qual cliente
lE={}
#Hor e Mes E: taxa de cobrança do estacionamento por hora e por mês 
horE=0.80
mesE=150
# Client: dicionário de clientes; veic: dicionário de veículos 
# Veic: dicionário do histórico de veículos usados pelo cliente
# Ces: contas de estacionamento
# Divc
# TempEs: tempo de um estacionamento






## Validando ou não a existência de arquivos (com ou sem valores)

#CArq: clientes já cadastrados
try:
  cArq=open("client.dat", "rb")
  client=pickle.load(cArq)
  cArq.close()
except IOError or FileNotFoundError:
  print("Não há clientela.")
  client={}
  cArq=open('client.dat', 'wb')
  pickle.dump(client, cArq)
  cArq.close()
sleep(1.27)


#
#vArq: arquivato de veículos já cadastrados
try:
  vArq=open("veic.dat", "rb")
  veic=pickle.load(vArq)
  vArq.close()
except IOError or FileNotFoundError:
  print("Não há veículos cadastrados.")
  veic={}
  vArq=open('veic.dat', 'wb')
  pickle.dump(veic, vArq)
  vArq.close()
sleep(0.12)


#
#cesArq: arquivato de contas de estacionamento já cadastradas
try:
  cesArq=open("ces.dat", "rb")
  ces=pickle.load(cesArq)
  cesArq.close()
except IOError or FileNotFoundError:
  print("Não há veículos cadastrados.")
  ces={}
  cesArq=open('ces.dat', 'wb')
  pickle.dump(ces, cesArq)
  cesArq.close()
sleep(0.12)


#
#divcArq: arquivato de dívida do cliente
try:
  divcArq=open("divc.dat", "rb")
  divc=pickle.load(divcArq)
  divcArq.close()
except IOError or FileNotFoundError:
  print("Não há dívidas cadastradas.")
  divc={}
  divcArq=open('divc.dat', 'wb')
  pickle.dump(divc, divcArq)
  divcArq.close()
sleep(0.12)


#
#tempEsArq: arquivato de dívida do cliente
try:
  tempEsArq=open("tempEs.dat", "rb")
  tempEs=pickle.load(tempEsArq)
  tempEsArq.close()
except IOError or FileNotFoundError:
  print("Não há dívidas cadastradas.")
  tempEs={}
  tempEsArq=open('tempEs.dat', 'wb')
  pickle.dump(tempEs, tempEsArq)
  tempEsArq.close()
sleep(3)


#Navegando por seções (...)
# Sec: escolha de seção


sec=int(input('\nPor qual seção queres navegar?\nDigite o número correspondente à seção desejada.\n 1- Usuário\n 2- Veículo\n 3- Comprovante de estacionamento e pagamento\n 0- Encerrar operações\n --> '))
















            #########   O INÍCIO   #########                 
while sec!=0:







#                    MAPA DA SEQUÊNCIA DO CÓDIGO
#Seção 1: tal linha - tal
#Seção 2: tal - tal 
#Seção 3: tal - resto.







  if sec==1:
    #Início da seção cliente
    # SecU: menu da seção Usuário
    secU=int(input("""
    \n \n \nSeção CONTAS\nPróxima ação:
    1 - Cadastrar conta
	2 - Exibir uma certa conta
	3 - Alterar alguma conta
	4 - Excluir conta
	5 - Listar Todas
	0 - Encerrar Seção 'Contas'
     --> """))
    while secU!=0:

      if secU==1:
        ###  Ajustar a seção Usuário de acordo com as
        ###  mudanças na seção Veículos
        cpf=input('\nPrimeiro, informe o Cpf do novo usuário (apenas números): ')
        if cpf in client:
          print("Usuário já cadastrado.")
        else:
          nome=input('\nQual o nome do cliente?\n --> ')
          mail=input('Agora insira o e-mail do novo cadastro: ')
          fone=input('Por fim, seu nº de telefone: ')
          client[cpf]=[nome, mail, fone]
        

      elif secU==2:
        # Search: insere um nome de um item no dicionário de usuários, que será buscado
        search=input('\nInsira o cpf da conta a ser procurada: ')
        if search in client:
          print('\n \nCadastro {}\nNome: {}\nE-mail: {}\nTelefone: {}'.format(search, client[search][0], client[search][1], client[search][2]))
        else:
          print('Este cadastro não existe.')

      elif secU==3:
        cpf=input('\nInsira o cpf da conta a ser mudada: ')
        if cpf not in client:
          print('- Usuário não existe! -')
        else:
          nome=input('\nInsira novamente o nome do cliente.\n --> ')
          mail=input('Agora insira de novo o e-mail do cadastro: ')
          fone=input('Por fim, o nº de telefone: ')
          client[cpf][0]=nome
          client[cpf][1]=mail
          client[cpf][2]=fone
          print('\nUsuário alterado com sucesso!')

      elif secU==4:
        cpf=input('\nInsira o cpf da conta a ser APAGADA: ')
        if cpf not in client:
          print('- Esse usuário aí ? "Nunca nem vi..."')
        else:
          client.pop(cpf)
          print('"Eliminado!"')
          
      elif secU==5:
        print('\n \nCadastros:\n \n')
        for cads in client:
          print('** Cadastro {} \nNome: {}\nE-mail: {}\nTelefone: {}'.format(cads, client[cads][0], client[cads][1], client[cads][2]), end='\n \n')

      else:
        print("""
  \n \n \nVocê escolheu uma ação inexistente!
          Tente novamente...
    """)
      cArq= open("client.dat", "wb")
      pickle.dump(client, cArq)
      cArq.close()
      secU=int(input("""
    \n \n \nSeção CONTAS\nPróxima ação:
    1 - Cadastrar conta
	2 - Exibir uma certa conta
	3 - Alterar alguma conta
	4 - Excluir conta
	5 - Listar Todas
	0 - Encerrar Seção 'Contas'
     --> """))
    print('\nSeção "Contas" fechada.')










  elif sec==2:
  #Início da seção Veículos
    secV=int(input("""
    \n \n \nVEÍCULOS\nPróximo ato:
    1 - Cadastrar veículo em conta
	2 - Exibir um veículo
	3 - Alterar infos dum veículo da conta
	4 - Excluir veículo
	5 - Listar Todos os veículos do usuário
	0 - Encerrar Seção 'Veículos' 
     --> """))
    conta=input('\nDigite o ID -cpf- da conta que quer utilizar\n -->  ')
    cont=0
    while conta not in client and cont!=6:
      cont+=1
      sele=input('\n \nConta errada ou inexistente. Quer ver as contas? Se sim, digite SIM (sim): ')
      if sele.upper()=='SIM':
        print('\nCadastros:\n \n')
        for cads in client:
          print('** {}\nNome: {}'.format(cads, client[cads][0]), end='\n')
      else:
        print('Ok.')
      conta=input('\n \nDigite uma conta válida.\n -->  ')
    if cont==6:
      print('\nTentativas excedidas... Voltando ao menu principal.', end='\n \n')
      break
    while secV!=0:

      if secV==1:
      # Pcar: id da placa do carro
      # Car: marca do carro. Ex: Ford, Mercedes, Ferrari, Gol...
# Usar só a placa no registro do carro
        #Pcar: id placa do carro; Car: Marca do carro: Ferrari, Fiat, Gol etc.
        pcar=input('\n \nPrimeiro, insira a placa do veículo: ')
        car=input('Qual a marca do carro?\n -->  ')
        # Mcar: modelo do automóvel
        mcar=input('Agora informe seu modelo: ')
        ano=input('O ano de fabricação: ')
        cor=input('A cor: ')
        km=input('A quilometragem (se não, insira 0 (zero)) é: ')
        veic[pcar]=[car, mcar, ano, cor, km]
        client[conta].append(pcar)

      elif secV==2:
        vIc=input('\nDigite a placa do veículo: ')
        while vIc not in client[conta]:
          sele=input('\n \nVeículo inexistente. Quer ver os veículos do proprietário? Digite SIM (sim) para ver: ')
          if sele.upper()=='SIM':
            print('\nVeículos de {} cadastrados:\n \n'.format(client[conta][0]))
            for cads in range (3, len(client[conta])):
              print('** Placa: {}\nMarca: {}'.format(client[conta][cads], veic[client[conta][cads]][0]), end='\n')
          else:
            print('Ok.')
          vIc=input('\n \nDigite uma placa de veículo válida.\n -->  ')
        print('\n** Marca: {}\nModelo: {}\nAno: {}\nCor: {}\nQuilometragem: {}'.format(veic[vIc][0], veic[vIc][1], veic[vIc][2], veic[vIc][3], veic[vIc][4]))

      elif secV==3:
        #Muda: mudar informação do carro
        muda=input('\n \nQue informação você quer mudar do carro?\nEscolha e digite o número correspondente.\n1- Cor\n2- Quilometragem\n -->  ')
        while muda!='1' and muda!='2':
          muda=input('\n1- Alteração de cor\n2- Alteração de Quilometragem\n --> ')
        vIc=input('\nDigite a placa do veículo, ao qual\nterá informações modificadas: ')
        cont=0
        while vIc not in client[conta] and cont!=6:
          cont+=1
          sele=input('\n \nVeículo inexistente. Quer ver os veículos do proprietário? Digite SIM (sim) para ver: ')
          if sele.upper()=='SIM':
            print('\nVeículos de {} cadastrados:\n \n'.format(client[conta][0]))
            for cads in range (3, len(client[conta]), 3):
              print('** Placa: {}\nMarca: {}'.format(client[conta][cads], veic[client[conta][cads]][0]), end='\n')
          else:
            print('Ok.')
          vIc=input('\n \nDigite uma placa de veículo válida.\n -->  ')
        if cont==6:
          #               AJEITAR
          break
        if muda=='1':
          #Ncor: Nova cor em imposição
          ncor=input('\nInsira a nova cor do veículo: ')
          veic[vIc][3]=ncor
        else:
          #Nqui: Nova quilometragem, em imposição
          nqui=input('\nInsira a quilometragem atual do veículo: ')
          veic[vIc][4]=nqui

      elif secV==4:
        vIc=input('\nAgora insira a placa do veículo a ser excluído: ')
        while vIc not in client[conta]:
          sele=input('\n \nVeículo inexistente. Quer ver os veículos do proprietário? Digite SIM (sim) para ver: ')
          if sele.upper()=='SIM':
            print('\nVeículos de {} cadastrados:\n \n'.format(client[conta][0]))
            for cads in range (3, len(client[conta]), 3):
              print('** Placa: {}\nMarca: {}'.format(client[conta][cads], veic[client[conta][cads]][0]), end='\n')
          else:
            print('Ok.')
          vIc=input('\n \nDigite uma placa de veículo válida.\n -->  ')
        client[conta].remove(vIc)
        del (veic[vIc])
        print('\nVeículo eliminado!')

      elif secV==5:
        print('\n \n \n \nVeículos de {} cadastrados:\n \n'.format(client[conta][0]))
        for cads in range (3, len(client[conta]), 1):
          print('** Placa: {}\nMarca: {}\nModelo: {}\nAno: {}\nCor: {}\nQuilometragem: {}'.format(client[conta][cads], veic[client[conta][cads]][0], veic[client[conta][cads]][1], veic[client[conta][cads]][2], veic[client[conta][cads]][3], veic[client[conta][cads]][4]), end='\n \n')
      else:
        print('\nTente digitar a opção certa...')
      vArq= open("veic.dat", "wb")
      pickle.dump(veic, vArq)
      vArq.close()
      secV=int(input("""
    \n \n \nVEÍCULOS\nPróximo ato na seção veículos:
    1 - Cadastrar veículo
	2 - Exibir um veículo
	3 - Alterar infos dum veículo da conta
	4 - Excluir veículo
	5 - Listar Todos os veículos do usuário
	0 - Encerrar Seção 'Veículos' 
     --> """))
    print('Seção fechada')









 
  elif sec==3:
    secT=int(input("""
    \n \n \nSeção ESTACIONAMENTO\nPróxima ação:
    1 - Adicionando conta de estacionamento

  2 - Detectar e contabilizar estacionagem

	3 - Exibir ou atualizar dívidas, ou exibir estacionagens de conta

	4 - Ver flow de movimento ou cobrança por períodos, individual ou conjuntamente

  5- Comparar usuários mais consistentes

	6 - Excluindo (Apagando) conta, ou seus dados

  7 - Frequência de estacionamento e cobrança, em certo período
  
  0 - Encerrar seção 'Estacionamento'
     --> """))
    #Início da seção Ticket   -    Nota-Treino
#    secT=int(input("""
#    \n \n \nSeção ESTACIONAMENTO\nPróxima ação:
#    1 - Adicionando conta
#  2 - Detectar e contabilizar estacionagem
#	3 - Exibindo conta
#	4 - Alterando conta
#	5 - Excluindo conta
#  6 - Mostrar todas as contas (e suas dívidas, e ou pagamentos, e sua frequência de uso por dia)
#  7 - Comparar a frequência de uso de estacionamento dos usuários
#  8 - Frequência de estacionamento e cobrança, em certo período
#  0 - Encerrar seção 'Estacionamento'
#     --> """))
    while secT!=0:

      if secT==1:
        #NCE: id da nova conta de estacionamento a cadastrar
        nCE=str(input('Insira o cpf do cliente, desde que ele já esteja cadastrado com uma conta: '))
        #Contador de tentativas
        contT=0
        while nCE not in client and contT<5:
          sele=input('\n \nConta errada ou inexistente. Quer ver as contas? Se sim, digite "SIM": ')
          if sele.upper()=='SIM':
            print('\nCadastros:\n \n')
            for cads in client:
              print('** {}\nNome: {}\nE-mail: {}\nFone: {}'.format(cads, client[cads][0], client[cads][1], client[cads][2]), end='\n \n')
          else:
            print('Ok.')
          contT+=1
          if contT==6:
            print('\nNão colocou até agora uma conta válida. Cadastre uma nova ou descubra uma existente voltando à seção "Clientes".')
            break
          nCE=input('\n \nDigite uma conta válida.\n -->  ')
        if nCE not in client:
          print("\nCliente inexistente !!")
          break
        if nCE not in ces:
          ces[nCE]=[]
        else:
          print('\nEsta conta de estacionamento já está cadastrada!')   

      elif secT==2:
        pres=int(input('\nE então, um veículo entrou no estacionamento, \nou está a sair?\n1- Entrou\n2- Está a sair\n \n -->  '))
        if pres==1:    
          nCE=str(input('\n \nInsira o cpf do cliente, desde que ele já esteja cadastrado com uma conta: '))
          if nCE not in client:
            print('\n \n \nEsta conta precisa ser cadastrada pro estacionamento.\nVolte à seção CLIENTE e a cadastre')
            break
          else:           
            pla=str(input("\nA placa do carro é:  "))
            # horaE: hora de entrada, no formato de tempo
            horaE=datetime.now()
            # hE: horaE em string
            hE=horaE.strftime("%d/%m/%Y - %H:%M:%S")
          
# ***    ------------->   CONSERTAR AQUI   <-------------    ***
# ***    ------------->   ARQUIVAR ALGO    <-------------    ***
            tempEs[nCE]=[pla, hE]
        elif pres==2:
          nCE=str(input('\n \nInsira o cpf do cliente, desde que ele já esteja cadastrado com uma conta: '))
          #horaS: hora de saída, em formato tempo
          horaS=datetime.now()
          # hS: horaS em string
          hS=horaS.strftime("%d/%m/%Y - %H:%M:%S")
          if nCE not in client:
            print('\n \n \nEsta conta ainda precisa ser cadastrada pro estacionamento.')
            break
          else:
            contT=0
            while nCE not in ces:
              contT+=1
              sele=input('\n \nConta errada ou inexistente na seção estacionar.\nQuer ver as contas? Se sim, digite "SIM": ')
              if sele.upper()=='SIM':
                print('\nCadastros:\n \n')
                for cads in client:
                  print('** {}\nNome: {}\nE-mail: {}\nFone: {}'.format(cads, client[cads][0], client[cads][1], client[cads][2]), end='\n \n')
              else:
                print('Ok.')
              nCE=str(input('\n \nInsira o cpf do cliente, desde que ele já esteja cadastrado com uma conta: '))
              if contT==6:
                print('\nNão colocou até agora uma conta válida. Cadastre uma nova ou descubra uma existente voltando à seção "Clientes".')
                break
            if contT==6:
                print('\n \nDa próxima vez, digite uma conta válida.\n -->  ')
                break
          if len(tempEs)>=1:
            lE[nCE]=[]
            lE[nCE].append(tempEs[nCE][0])
            lE[nCE].append(tempEs[nCE][1])
            lE[nCE].append(hS)
            # hora (E e S) F: hora de entrada e saída finais, reconvertidas em tempo novamente. 
            horaEF=datetime.strptime(lE[nCE][1], "%d/%m/%Y - %H:%M:%S")
            horaSF=data1f=datetime.strptime(lE[nCE][2], "%d/%m/%Y - %H:%M:%S")
            # timin (P e F) variável de diferença de tempo, e de diferença de tempo em decimal/float (segundos)  
            timinP=horaSF-horaEF
            timinF=timinP.total_seconds()
            # timinU: resultado final, em horas
            timinU=round(timinF/3600, 4)
            lE[nCE].append(timinU)
            lE[nCE].append(round(timinU*0.5, 2))
            ces[nCE].append(lE[nCE])
            print('')
            lE={}
            tempEs={}
            conta=0
            if nCE not in divc:
              divc[nCE]=[]
            else:
              print('\nEsta conta de estacionamento já está cadastrada!')  
            divc[nCE].append(round(timinU*0.5, 2))
            #Adicionar o horário de saída
            #Comentário de cima pode estar errado
          else:
            print('\n \n \nProsseguindo, volte ao menu Estacionagem. Deves inserir a entrada de um carro...')





      elif secT==3:
        #divE: dívida particular
        divE=0
        conta=input('\nDigite o id -cpf- do usuário ao qual\nquer mexer nas dívidas ou\nver histórico de estacionamentos\n -->  ')
        cont=0
        while conta not in ces and cont!=6:
          cont+=1
          sele=input('\n \nConta errada ou inexistente. Quer ver as contas? Se sim, digite "SIM": ')
          if sele.upper()=='SIM':
            print('\n \nCadastros:\n')
            for cads in ces.keys():
              print(cads, end="\n")
          else:
            print('Tente outra vez.')
            conta=input('\nDigite o id/cpf do usuário ao qual\nquer mexer nas dívidas ou\nver histórico de estacionamentos\n -->  ')
        if cont==6:
          print('\nTentativas excedidas.\nCadastre o usuário na seção de estacionamento.')
          cont=0
          break
        # Nact: próxima decisão
        nact=int(input('\n \nEscolha uma ação:\n1- Ver dívida d\n2- Pagar dívida\n3- Visualizar estacionagens do usuário\n  -->  '))
        if nact==1:
          for vlrs in divc[conta]:
            divE+=vlrs
          print('\n \n \nDívida de {}: R$ {}.'.format(client[conta][0], round(divE, 2)))
        elif nact==2:
          paga=float(input('\nDigite o valor, em reais, que vais pagar.\nPara valores decimais, use o ponto (.)\nao invés de vírgula(,).\nExemplo certo: 65.40    ->Ex. errado: 65,40\n  -->  '))
          if conta not in divc:
            divc[conta]=[]
          else:
            print('\nEsta conta de estacionamento já está cadastrada!')  
          divc[conta].append(-(round(paga, 2)))
        else:
          #HEsta: histórico de estacionamentos de beltrano(a) de tal
          print('\n \n \nHistórico de estacionamentos de {}'.format(client[conta][0]), end="\n")
          for hEsta in ces[conta]:
            print(hEsta, end="\n")

      elif secT==4:
        print('otttgi')

      elif secT==5:
        print('owmlwe')

      elif secT==6:
        print('tweiwo')

      elif secT==7:
        print('axffytvadxare')

      elif secT==8:
        print('APcahdbha')
        
      else:
        print('\nValor inválido.')
        
      cesArq= open("ces.dat", "wb")
      pickle.dump(ces, cesArq)
      cesArq.close()

      divcArq= open("divc.dat", "wb")
      pickle.dump(divc, divcArq)
      divcArq.close()

      tempEsArq= open("tempEs.dat", "wb")
      pickle.dump(tempEs, tempEsArq)
      tempEsArq.close()

      secT=int(input("""
    \n \n \nSeção ESTACIONAMENTO\nPróxima ação:
    1 - Adicionando conta de estacionamento

  2 - Detectar e contabilizar estacionagem

	3 - Exibir ou atualizar dívidas, ou exibir estacionagens de conta

	4 - Ver flow de movimento ou cobrança por períodos, individual ou conjuntamente

  5- Comparar usuários mais consistentes

	6 - Excluindo (Apagando) conta, ou seus dados

  7 - Frequência de estacionamento e cobrança, em certo período
  
  0 - Encerrar seção 'Estacionamento'
     --> """))
    print('\nSeção encerrada!')









    
  else:
    print('\nSeção inválida!')
  sec=int(input('\nPor qual seção queres navegar?\nDigite o número correspondente à seção desejada.\n 1- Usuário\n 2- Veículo\n 3- Comprovante de estacionamento e pagamento\n --> '))







cArq= open("client.dat", "wb")
pickle.dump(client, cArq)
cArq.close()

vArq= open("veic.dat", "wb")
pickle.dump(veic, vArq)
vArq.close()

cesArq= open("ces.dat", "wb")
pickle.dump(ces, cesArq)
cesArq.close()

divcArq= open("divc.dat", "wb")
pickle.dump(divc, divcArq)
divcArq.close()

tempEsArq= open("tempEs.dat", "wb")
pickle.dump(tempEs, tempEsArq)
tempEsArq.close()






print('\n \n \n \n \nObrigado por usar nosso pro!')
#ticket=#Apunhado de variáveis
#cpf
#placa
#dataEnt
#dataSaí
#horaEnt
#horaSaí
#-
###Valor
##Preço hora mensal:
#R$ 00,50 (Fifty Cent)


#site sobre removedores:

#http://turing.com.br/pydoc/2.7/tutorial/datastructures.html


#Python do alemão: https://www.youtube.com/watch?v=Gojqw9BQ5qY
