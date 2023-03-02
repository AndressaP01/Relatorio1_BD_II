from Aluno import Aluno
from Aula import Aula
from Professor import Professor

aluno1=Aluno('Beatriz')
aluno2=Aluno('Bianca')
aluno3=Aluno('Luís')

aula=Aula('Roberto','Banco de dados')
aula.adicionar_aluno(aluno1.nome)
aula.adicionar_aluno(aluno2.nome)
aula.adicionar_aluno(aluno3.nome)
aula.listar_presenca()