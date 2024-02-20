from pymongo import MongoClient
from Aluno import Aluno as aluno

def find():
    documentos=collection_aluno.find({},{"_id": 0})
    for doc in documentos: #pega a variavel de controle de dicionario por dicionario
        for chave in doc: #pega de nome em nome a onde esta contida a variavel
            print(chave,":",doc[chave])
        print('\n')

conexao=MongoClient("mongodb://localhost:27017")

#criar um banco de dados
escola=conexao["escola"] #<- O nome do banco no MongoDb vai ser a chave

#criar uma collection
collection_aluno=escola["alunos"]#<- O nome da collection no MongoDb vai ser a chave

while True:
    quantAlunos = collection_aluno.count_documents({}) # conta quantos doumentos tem no banco
    print(f'Alunos cadastrados no banco: {quantAlunos}')

    #pede informações
    nome=str(input('Qual é o nome do aluno: '))
    idade=int(input(f'Qual a idade de {nome}: '))
    media=float(input(f'Qual a media de {nome}: '))

    aluno1=aluno(media,nome,idade)#objeto aluno

    #(C) - Criando um documento
    collection_aluno.insert_one(aluno1.to_dict())

    documento=collection_aluno.find_one()

    print('Aluno inserido com o id: ',documento["_id"])

    print("O que tem no banco até agora: ")

    #Printa o que esta no banco
    find()

    #Altarar-----------------------------------------------------------------
    pontos_estras=int(input(f'O aluno {nome} merece pontos extras (s=1/n=2)'))

    if(pontos_estras==1):
        nota=float(input(f'Quantos pontos ele tirou na pratica? (0 á 2): '))

        #Verifica se a nota da pratica esta entre 0 e 2
        while nota>2 or nota<0:
            nota=float(input(f'Quantos pontos ele tirou na pratica? (0 á 2): '))


        #(U) - Atualizar um documento
        filtro={"nome":nome}

        resultado_update=collection_aluno.update_one(filtro, {"$set":{"media":media+nota}})

        if(resultado_update.modified_count==1):
            print('Modificado')

            find()

    elif(pontos_estras==2):
        print("Nada Modificado")
        find()

    #Apagar------------------------------------------------------------
    excluir=int(input('Você deseja apagar algum registro? (s=1,n=2): '))

    if(excluir==1):
        resultado_delete=''
        while True:
            nome_deletado=input('Digite o nome para deletar: ')
            filtro={"nome":nome_deletado}

            for nome_aluno in collection_aluno.find({}, {"_id": 0, "nome": 1}): # Excluímos o _id e incluímos o name
                if nome_aluno["nome"] == nome_deletado: # Verificamos o nome em vez do ID
                    resultado_delete = collection_aluno.delete_one({"nome": nome_deletado})
                    break
            else:
                print('Nome inexistente')
                continue

            break

        
        print(f'Deletado o aluno {nome_deletado}')
        find()

    elif(excluir==2):
        print("Nada deletado")
        find()

    #Sair-----------------------------------------------------------
    sair=int(input('Deseja adicionar mais algum aluno? (s=1,n=2): '))

    if(sair==1):
        continue
    elif(sair==2):
        break
    else:
        while not sair==1 or sair==2:
            sair=int(input('Deseja adicionar mais algum aluno? (s=1,n=2): '))