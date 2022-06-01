from django.urls import path

from poste.views import Poste
from poste.views import Home, PosteSearch, PosteRT, PosteP, CommentCreateView, CommentUpdateView, SchemaPreferentielUpdateView, AutreParticulariterUpdateView
from poste.views import showList, search_poste, Historique, autocomplete, SupprimerCommentaire, PosteUpdateView
app_name = "poste"

urlpatterns = [
    path('', Home.as_view(), name="Home"),
    path('search', search_poste),
    path('search/autocomplete', autocomplete, name="autocomplete"),

    path('poste-search', PosteSearch.as_view(), name='PosteSearch'),
    path('poste-search-result/<str:lettreRechercher>', PosteRT.as_view(), name='PosteRT'),
    path('poste/sB', showList.as_view(), name='sB'),
    path('poste-detail/<int:pk>', PosteP.as_view(), name='PosteP'),
    path('poste-detail/edit-poste/<int:pk>', PosteUpdateView.as_view(), name='PosteUpdate'),
    path('poste-detail/Historique-Comment/<int:pk>', Historique.as_view(), name='HistoriqueCommentaire'),
    path('poste-detail/Supprimer-Comment/<int:pk>', SupprimerCommentaire, name='SupprimerCommentaire'),
    # path('', Historique.as_view(), name='HistoriqueCommentaire'),
    path('poste-detail/<int:pk>/Create-Comment/', CommentCreateView.as_view(), name='Create-Comment'),
    path('poste-detail/<int:pk>/Create-Comment-Edit/', CommentUpdateView.as_view(), name='Create-Comment-Edit'),
    path('poste-detail/<int:pk>/Create-Comment-Edit/SP', SchemaPreferentielUpdateView.as_view(), name='Create-SP-Edit'),
    path('poste-detail/<int:pk>/Create-Comment-Edit/AP', AutreParticulariterUpdateView.as_view(), name='Create-AP-Edit')
]
