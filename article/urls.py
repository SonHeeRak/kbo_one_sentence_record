from django.conf.urls import url, include
from rest_framework import routers
from . import views
from article.lib import globals as g

router = routers.DefaultRouter()
router.register(r'daily_news', views.DailyNewsViewSet)
router.register(r'person', views.PersonViewSet)
router.register(r'common_dynamic_variable', views.CommonDynamicVariable)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^daily_news/create_hitter', views.DailyNewsViewSet.as_view({'get': 'create_hitter'})),
    url(r'^daily_news/create_pitcher', views.DailyNewsViewSet.as_view({'get': 'create_pitcher'})),
    url(r'^daily_news/create_team', views.DailyNewsViewSet.as_view({'get': 'create_team'})),
    url(r'^daily_news/create_player', views.DailyNewsViewSet.as_view({'get': 'create_player'})),
    url(r'^daily_news/get_player_list', views.DailyNewsViewSet.as_view({'get': 'get_player_list'})),

]
