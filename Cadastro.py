class Pessoa:
    def __init__(self,nome,cpf,rg,dataNasc,telefone,endereco):
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.dataNasc = dataNasc
        self.telefone = telefone
        self.endereco = endereco

class Aluno(Pessoa):
    def __init__(self,nome,cpf,rg,dataNasc,telefone,endereco,ra,numMatricula,nomeCurso,dataMatricula):
        Pessoa.__init__(self.nome,cpf,rg,dataNasc,telefone,endereco)
        self.ra = ra
        self.numMatricula = numMatricula
        self.nomeCurso = nomeCurso
        self.dataMatricula = dataMatricula

class Professor(Pessoa):
    def __init__(self,nome,cpf,rg,dataNasc,telefone,endereco,Registro,Materia,):
