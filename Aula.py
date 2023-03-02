class Aula:
    lista = []
    def __init__(self,professor,assunto):
        self.professor=professor
        self.assunto=assunto


    def adicionar_aluno(self,aluno):

        self.lista.append(aluno)


    def listar_presenca(self):
        print("Presenca na aula sobre "+self.assunto+" ministrada pelo professor "+self.professor)
        print(self.lista)

