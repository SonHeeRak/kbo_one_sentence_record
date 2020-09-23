from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie

from rest_framework.views import APIView
from rest_framework import viewsets
from . import serializers
from rest_framework.response import Response
from . import baseball_models as b_models
from . import daily_news_models as d_models
from .controllers import DailyNews


# Create your views here.

class DailyNewsViewSet(viewsets.ModelViewSet):
    queryset = b_models.Hitter.objects.all()
    serializer_class = serializers.HitterRecordSerializer

    @method_decorator(cache_page(60 * 30))
    def create_hitter(self, request):
        gmkey = request.query_params.get('gmkey')
        player_type = 'hitter'
        daily_news = DailyNews(gmkey=gmkey, player_type=player_type)
        result = daily_news.generate_hitter_daily_news()

        return Response(result)

    @method_decorator(cache_page(60 * 30))
    def create_pitcher(self, request):
        gmkey = request.query_params.get('gmkey')
        player_type = 'pitcher'
        daily_news = DailyNews(gmkey=gmkey, player_type=player_type)
        result = daily_news.generate_pitcher_daily_news()

        return Response(result)

    @method_decorator(cache_page(60 * 30))
    def create_team(self, request):
        gmkey = request.query_params.get('gmkey')
        player_type = 'team'
        daily_news = DailyNews(gmkey=gmkey, player_type=player_type)
        result = daily_news.generate_team_daily_news()

        return Response(result)

    #@method_decorator(cache_page(60 * 30))
    def create_player(self, request):
        gmkey = request.query_params.get('gmkey')
        pcode = request.query_params.get('pcode')
        player_type = 'player'
        daily_news = DailyNews(gmkey=gmkey, pcode=pcode, player_type=player_type)
        result = daily_news.generate_player_daily_news()

        return Response(result)

    @method_decorator(cache_page(60 * 30))
    def get_player_list(self, request):
        gmkey = request.query_params.get('gmkey')
        daily_news = DailyNews(gmkey=gmkey)
        result = daily_news.get_player_list()

        return Response(result)


class PersonViewSet(viewsets.ModelViewSet):
    queryset = b_models.Person.objects.all()
    serializer_class = serializers.PersonSerializer


class GamecontappViewSet(viewsets.ModelViewSet):
    queryset = b_models.Gamecontapp.objects.all()
    serializer_class = serializers.GamecontappSerializer

    def call(self, request):
        gmkey = request.query_params.get('gmkey')
        queryset = b_models.Gamecontapp.objects.filter(gmkey=gmkey)


class CommonDynamicVariable(viewsets.ModelViewSet):
    queryset = d_models.CommonDynamicVariable.objects.all()
    serializer_class = serializers.CommonDynamicVariableSerializer
