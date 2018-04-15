from django.db.models.query import QuerySet

class DisciplinaQuerySet (QuerySet):

    def disciplinas_ativas(self):
        return self.filter(ativo=True)

DisciplinaManager = DisciplinaQuerySet.as_manager