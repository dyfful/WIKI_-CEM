from django import forms

from theme.models import Commentaire


class ficheForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['Fiche','Nom', 'Titre', 'Contenu']

    def __init__(self, *args, **kwargs):
        super(ficheForm, self).__init__(*args, **kwargs)
        # self.fields['Poste'].widget.attrs['disable'] = True
        # self.fields['Poste'].widget.attrs['readonly'] = True
        self.fields['Fiche'].disabled = True
