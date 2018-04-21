from .super_manager import SuperQuerySet

class DisciplinaQuerySet (SuperQuerySet):

    def disciplinas_ativas(self):
        return self.filter(ativo=True)

DisciplinaManager = DisciplinaQuerySet.as_manager