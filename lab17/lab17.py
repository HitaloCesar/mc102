import re

class EmailInvalido(Exception):
    pass

class SenhaFraca(Exception):
    pass

class RAInvalido(Exception):
    pass

class Repositorio:
    def __init__(self):
        self.alunos = []

    def testeRa(self, ra):
        for i in range(len(self.alunos)):
            if ra == self.alunos[i].ra:
                return False
        return True

    def testeSenha(self, senha):
        lista = list(senha)
        caractereEspecial = ["!","@","#","$","&","*" ]
        letrasMaiusculas = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        letrasMinusculas = []
        for i in range(len(letrasMaiusculas)):
            letrasMinusculas.append(letrasMaiusculas[i].lower() )
        flagCE = False
        flagLM = False
        cont = 0
        for m in range(2):
           for i in range(10):
                if str(i) in lista:
                    lista.remove(str(i))
                    cont+=1
        if cont < 2:
            return False
        cont = 0
        for i in range(len(caractereEspecial)):
            if caractereEspecial[i] in lista:
                flagCE = True
                break
        if flagCE == False:
            return False
        for i in range(len(letrasMaiusculas)):
            if letrasMaiusculas[i] in lista:
                flagLM = True
                break
        if flagLM == False:
            return False

        for m in range(2):
            for i in letrasMinusculas:
                if i in lista:
                    lista.remove(i)
                    cont+=1
        if cont < 2:
            return False
        return True


    def testeEmail(self, email):
        emaill = re.compile(r'\w+@\w+\.\w+(\.\w+)?')
        if emaill.search(email):
            return True
        return False
    #Este método recebe o parâmetro aluno e o insere no repositório
    def adicionar(self, aluno):
        if not self.testeRa(aluno.ra):
            raise RAInvalido
        if not self.testeSenha(aluno.senha) :
            raise SenhaFraca
        if not self.testeEmail(aluno.email) :
            raise EmailInvalido
        else:
            self.alunos.append(aluno)
    #Este método recebe o parâmetro aluno e altera, no repositório, os dados do aluno com RA igual a aluno.ra

    def alterar(self, aluno):
        a = 0
        if self.testeRa(aluno.ra):
            raise RAInvalido
        if not self.testeSenha(aluno.senha) :
            raise SenhaFraca
        if not self.testeEmail(aluno.email) :
            raise EmailInvalido
        else:
            for i in range(len(self.alunos)):
                if aluno.ra == self.alunos[i].ra:
                    a = i

            self.alunos[a] = aluno 
    #Este método recebe o parâmetro ra e deve retornar o aluno que possui o RA informado como parâmetro
    def achaAluno(self, ra):
        for i in range(len(self.alunos)):
            if self.alunos[i].ra == ra:
                return self.alunos[i]
        raise RAInvalido

    #Este método recebe o parâmetro ra e deve remover o aluno correspondente do repositório
    def remover(self, ra):

        for i in range(len(self.alunos)):
            if self.alunos[i].ra == ra:
                self.alunos.remove(self.alunos[i])
                return
        raise RAInvalido
        
    #Este método exclui todos os alunos do repositório.
    def limparRepositorio(self):
        self.alunos = []
