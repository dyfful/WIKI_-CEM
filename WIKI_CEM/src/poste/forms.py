from django import forms

from poste.models import Commentaire, Poste


class Com(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['Poste', 'Nom', 'Titre', 'Contenu']

    def __init__(self, *args, **kwargs):
        super(Com, self).__init__(*args, **kwargs)
        # self.fields['Poste'].widget.attrs['disable'] = True
        # self.fields['Poste'].widget.attrs['readonly'] = True
        self.fields['Poste'].disabled = True


class Post(forms.ModelForm):
    class Meta:
        model = Poste
        fields = ['idRTE', 'libelle', 'Tension', 'TypePoste',
                  'Impact', 'protectionBarre', 'CCO', 'Filerie', 'AutomatismePoste', 'JDB', 'Groupement', 'Consigne']

    # def __init__(self, *args, **kwargs):
    #     super(Poste, self).__init__(*args, **kwargs)
    #     # self.fields['Poste'].widget.attrs['disable'] = True
    #     # self.fields['Poste'].widget.attrs['readonly'] = True
    #     self.fields['Poste'].disabled = True
