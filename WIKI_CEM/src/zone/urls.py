from django.urls import path

from zone.views import ZoneHome, ZoneHomeCategorieZone, CommentCreateZoneView, CommentUpdateZoneView, HistoriqueZone

app_name = "zone"

urlpatterns = [
    path('', ZoneHome.as_view(), name="Zone-Home"),
    path('zone-detail/<int:pk>', ZoneHomeCategorieZone.as_view(), name='Zone-detail'),
    path('zone-detail/Historique-Comment/<int:pk>', HistoriqueZone.as_view(), name='HistoriqueCommentaire'),

    path('<int:pk>/Create-Comment-Zone/', CommentCreateZoneView.as_view(), name='Create-Comment-Zone'),
    path('<int:pk>/Edit-Comment-Zone/', CommentUpdateZoneView.as_view(), name='Create-Comment-Edit'),

    # path('<int:pk>/CreateComment/', CommentCreateViewTheme.as_view(), name='Create-Comment-Theme'),

    # path('posteP/<int:pk>', PosteP.as_view(), name='PosteP'),
    # path('posteP/<int:pk>/CreateComment/', CommentCreateView.as_view(), name='Create-Comment'),
]
