class Turma:
  def __init__(self,lista):
    self.lista = lista

  def listar_alunos(self):
    self.contar_lista=len(self.lista)
    if self.contar_lista == 0:
      print('não tem nenhum aluno cadastrado ainda')
    else:
        for aluno in self.lista:
            print(f'nome: {aluno['nome']} | idade: {aluno['idade']} | nota: {aluno['nota']}')
    

  def procurar_aluno(self):
    self.contar_lista=len(self.lista)
    if self.contar_lista == 0:
       print('nenhum aluno foi  cadastrado ainda')
    else:
        self.procurando=True
        self.nome=input('digite o nome do aluno que deseja saber os dados: ').strip()
        for aluno in self.lista:
            if self.nome == aluno['nome']:
                print(f'nome: {aluno['nome']} | idade: {aluno['idade']} | nota: {aluno['nota']} ')
                self.procurando=False
                break
        if self.procurando == True :
            print('aluno não cadastrado')
   



  def calcular_media_turma(self):
    self.soma=0
    self.qtd_alunos=1
    self.contar_lista = len(self.lista)
    if self.contar_lista == 0:
        print('não tem nenhum aluno cadastrado ainda')
    else:
       for aluno in self.lista:
        self.soma+=aluno['nota']
        self.qtd_alunos+=1
       self.media=self.soma/self.qtd_alunos
       print('a media da turma e de',self.media)

  def situacao(self):
    self.contar_lista = len(self.lista)
    if self.contar_lista == 0:
       print('não tem nenhum aluno cadastrado ainda')
    else:
        for aluno in self.lista:
          if aluno['nota'] >=60:
            print(f'aluno: {aluno['nome']}  esta aprovado')
        else:
            print(f'aluno: {aluno['nome']} esta reprovado')