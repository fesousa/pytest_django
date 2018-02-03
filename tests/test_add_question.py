from polls.models import Question
import pytest
from django.utils import timezone

@pytest.mark.django_db
def test_add_question():
    q = Question(question_text='Questao teste', pub_date=timezone.now())
    q.save()
    assert  q.id == 1