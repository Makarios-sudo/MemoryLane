from urllib import request
from django.db.models import fields
from .models import *
from django.forms import ModelForm



class CategoryForm(ModelForm):

    class Meta:
        model = Category
        fields = ["name"]



class MemoryForm(ModelForm):

    class Meta:
        model = Memory
        exclude = ['category']

    # def __init__(self, user=None, **kwargs):
    #     super(category, self).__init__(**kwargs)
    #     if category:
    #         self.fields['category'].queryset = models.Memory.objects.filter(user=request.user.profile)
