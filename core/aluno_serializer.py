from rest_framework import serializers
from core.models import Aluno


class AlunoSerilazer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'
