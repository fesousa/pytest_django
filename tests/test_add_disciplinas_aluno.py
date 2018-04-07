import pytest
from lms_app.models import Aluno, Disciplina

@pytest.mark.django_db
def test_add_disciplinas_aluno():
    d1 = Disciplina(nome = 'LP2', carga_horaria=20, valor=150)
    d2 = Disciplina(nome = 'TecWeb', carga_horaria=30, valor = 200)
    d1.save()
    d2.save()
    a = Aluno(nome = 'Fernando',ra=123456, desconto=10)
    a.save()
    a.disciplinas.set([d1,d2])
    a.save()    

    assert a.get_mensalidade() == 315
