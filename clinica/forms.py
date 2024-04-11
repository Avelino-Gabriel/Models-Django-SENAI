from django import forms
from .models import Especialidade, Medico

class AddEspecialidade(forms.ModelForm):

    class Meta:
        model = Especialidade
        fields = ('id_especialidade', 'nome', 'descricao')

class AddMedico(forms.ModelForm):

    class Meta:
        model = Medico
        fields = ('id_medico', 'nome', 'endereco', 'telefone', 'email', 'data_nascimento', 'crm', 'especialidade_id')