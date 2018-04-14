import pytest
from lms_app.models import Aluno, Disciplina, Professor

@pytest.mark.django_db
def test_add_disciplinas_aluno():
    p = Professor(nome='Fernando Sousa')    
    assert p.get_sobrenome() == 'Sousa'
