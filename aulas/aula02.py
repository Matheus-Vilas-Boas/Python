###c1 = {1,2,3,4,5}
#c2 = {5,6,7,8,9,10}
#c1.add(25)
#c1.update([25,6,7,4])
#print('União entre c1 e c2: ', c1 | c2)
#print('Interseção entre c1 e c2: ', c1 & c2)
#print('Diferença entre c1 e c2: ', c1 - c2)
###
# EXERCÍCIO PRATICO

#Alunos da escola mundial

ING = {'Julia', 'Marcos', 'Pedro','Alice','Fernanda','Matheus','Yuri','Sara'}
ESP = {'Fuad', 'Víctor Hugo', 'Ântonio', 'Pedro','Igor','Ana Lívia', 'Jonh','Carlos'}
FRA = {'Maria Eduarda', 'Gustavo', 'Paulo', 'Fernanda', 'Yago', 'Diogo', 'Luiza', 'Heitor'}

#união
TodosAlunos = ING | ESP | FRA

# Intersecção de alunos de mais de um curso
AlunosEmMaisDeUmCurso = (ING & ESP) | (ING & FRA) | (ESP & FRA)


#OUTPUT
print('-=' *60)
print(f'Todos os alunos da escola mundial: {TodosAlunos}')
print('-=' *60)
print(f'Alunos matriculados em mais de um curço: {AlunosEmMaisDeUmCurso}')
print('-=' *60)