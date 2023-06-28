from rest_framework.viewsets import ModelViewSet
from core.aluno_serializer import AlunoSerilazer
from core.models import Aluno


class AlunoViewset(ModelViewSet):
    serializer_class = AlunoSerilazer
    queryset = Aluno.objects.all()

