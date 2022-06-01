from django.urls import path

from theme.views import ThemeHome, ModopHome, ThemeFiche, ModopFiche, CommentCreateViewTheme, CommentUpdateViewTheme, Historique


app_name = "theme"

urlpatterns = [
    path('T', ThemeHome.as_view(), name="Theme"),
    path('M', ModopHome.as_view(), name="Modop"),

    path('TD/<int:pk>', ThemeFiche.as_view(), name='Theme-detail'),
    path('MD/<int:pk>', ModopFiche.as_view(), name='Modop-detail'),

    path('MD/Create-Comment/<int:pk>', CommentCreateViewTheme.as_view(), name='Create-Comment-Theme-Modop'),

    path('TD/<int:pk>/Edit-Comment/', CommentUpdateViewTheme.as_view(), name='Edit-Comment-Theme-Modop'),

    path('TD-MD/Historique-Commentaire/<int:pk>/', Historique.as_view(), name='Historique-Commentaire'),

    # path('posteP/<int:pk>', PosteP.as_view(), name='PosteP'),
    # path('posteP/<int:pk>/CreateComment/', CommentCreateView.as_view(), name='Create-Comment'),
]
