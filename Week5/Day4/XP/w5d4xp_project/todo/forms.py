from django import forms
from .models import Todo, Category

# class TodoForm(forms.ModelForm):
#     multiple_choice_field = forms.MultipleChoiceField(
#         choices=(),
#         widget=forms.RadioSelect
#     )
#
#     class Meta:
#         model = Todo
#         fields = ['__all__', 'multiple_choice_field']
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#         instances = Todo.objects.all()
#         choices = [(instance.id, str(instance)) for instance in instances]
#         self.fields['multiple_choice_field'].choices = choices

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'