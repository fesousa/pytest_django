from django.db.models.query import QuerySet

class SuperQuerySet (QuerySet):

    def disciplinas_ativas(self):
        return self.filter(ativo=True)

SuperManager = SuperQuerySet.as_manager