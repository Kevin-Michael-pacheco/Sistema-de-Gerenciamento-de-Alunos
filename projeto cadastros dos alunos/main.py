from aluno import Alunos
from turma import Turma
lista=[]
t=Turma(lista)

def main():
  while True:
    print('=============================Menu===============================')
    print('1-cadastrar aluno')
    print('2-listar alunos')
    print('3-procurar aluno')
    print('4-calcular media da turma')
    print('5-situação final')
    print('6-sair')
    print()
    opcao=input('digite a opção desejada: ')
    if opcao == '1':

        dicionario={}
        nome=input('digite o nome do aluno: ').strip()
        try:
            idade=int(input('digite a idade do aluno: '))
            if idade >=0:
                try:
                    nota=float(input('digite a nota: '))
                    if nota >=0:
                        dicionario['nome']=nome
                        dicionario['idade']=idade
                        dicionario['nota']=nota
                        lista.append(dicionario)
                        Alunos(nome,idade,nota)
                    else:
                        print('a nota não pode ser menor que zero')
                except ValueError:
                   print('ERRO.A nota tem que ser maior ou igual a 0 e não pode ser letras')
            else:
                print('a idade não pode ser menor que zero')
                
        except ValueError:
           print('ERRO.A idade tem que ser maio que 0 e não pode ser letras')    
    elif opcao == '2':
      t.listar_alunos()

    elif opcao == '3':
      t.procurar_aluno()

    elif opcao == '4':
      t.calcular_media_turma()
    
    elif opcao == '5':
      t.situacao()

    elif opcao == '6':
      print('programa encerrado')
      break

    else:
      print('digite somente opçoes disponiveis')

main()

      

