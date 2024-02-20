from Pessoa import Pessoa

class Aluno(Pessoa):
   def __init__(self, nota, nome, idade,data_criacao):
       super().__init__(nome, idade)
       self.nota = nota
       self.data_criacao=data_criacao

   def getNota(self):
       return self.nota

   def setNota(self, nota):
       self.nota = nota

   def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Nota: {self.nota}")
        print(f"Data Criação: {self.data_criacao}")

   def to_dict(self):
        return {
            "media": self.nota,
            "nome": self.nome,
            "idade": self.idade,
            "data_criação": self.data_criacao
        }
