from django import forms
from zone.models import Commentaire


class zoneForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['Zone', 'Nom', 'Titre', 'Contenu']
        # fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(zoneForm, self).__init__(*args, **kwargs)
        # self.fields['Poste'].widget.attrs['disable'] = True
        # self.fields['Poste'].widget.attrs['readonly'] = True
        self.fields['Zone'].disabled = True
