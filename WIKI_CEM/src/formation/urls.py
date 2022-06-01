from django.urls import path

from formation.views import FormationHome, FormationHomeInfo

app_name = "formation"

urlpatterns = [
    path('formation-home', FormationHome.as_view(), name="Formation-Home"),
    path('formation-detail', FormationHomeInfo.as_view(), name="Formation-Home-Info"),
    # path('<int:pk>', ZoneHomeCategorieZone.as_view(), name='Zone-detail'),
    # path('<int:pk>/CreateComment/', CommentCreateZoneView.as_view(), name='Create-Comment-Zone'),

    # path('<int:pk>/CreateComment/', CommentCreateViewTheme.as_view(), name='Create-Comment-Theme'),

    # path('posteP/<int:pk>', PosteP.as_view(), name='PosteP'),
    # path('posteP/<int:pk>/CreateComment/', CommentCreateView.as_view(), name='Create-Comment'),
]
