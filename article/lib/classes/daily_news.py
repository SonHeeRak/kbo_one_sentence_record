from article.lib.classes.hitter_record import DailyHitterRecord
from article.lib.classes.pitcher_record import DailyPitcherRecord
from article.lib.classes.team_record import DailyTeamRecord
from article.lib.classes.pitcher_season_record import DailyPitcherSeasonRecord
from article.lib.classes.hitter_season_record import DailyHitterSeasonRecord
from article.lib import globals as g
from article.lib import util
import pandas as pd


class DailyNewsVariable(object):
    def __init__(self, gmkey, pcode=None, player_type=None):
        self.gmkey = gmkey
        self.game_year = gmkey[0:4]
        self.pcode = pcode
        self.player_type = player_type

        if self.player_type == 'pitcher':
            queryset = g.b_models.Pitcher.objects.filter(gmkey=self.gmkey, pcode=self.pcode).exclude(name='합계')
            df = pd.DataFrame(queryset.values())

            self.daily_news_type = '투수'

            daily_pitcher_record_var = DailyPitcherRecord(data_frame=df, gmkey=self.gmkey, pcode=self.pcode)
            setattr(self, '데일리투수기록', daily_pitcher_record_var.get_var())
            daily_pitcher_season_record_var = DailyPitcherSeasonRecord(gmkey=self.gmkey, pcode=self.pcode)
            setattr(self, '투수시즌기록', daily_pitcher_season_record_var.get_var())
        elif self.player_type == 'hitter':
            queryset = g.b_models.Hitter.objects.filter(gmkey=self.gmkey, pcode=self.pcode).exclude(name='합계')
            df = pd.DataFrame(queryset.values())

            self.daily_news_type = '타자'

            daily_hitter_record_var = DailyHitterRecord(data_frame=df, gmkey=self.gmkey, pcode=self.pcode)
            setattr(self, '데일리타자기록', daily_hitter_record_var.get_var())
            daily_hitter_season_record_var = DailyHitterSeasonRecord(gmkey=self.gmkey, pcode=self.pcode)
            setattr(self, '타자시즌기록', daily_hitter_season_record_var.get_var())
        elif self.player_type == 'team':
            self.daily_news_type = '팀'

            daily_team_record_var = DailyTeamRecord(gmkey=self.gmkey)
            setattr(self, '데일리팀기록', daily_team_record_var.get_var())

        g.define_method(self, g.daily_news_method)

        for k, v in g.VARIABLE_DICT['common_dynamic_variable'].items():
            setattr(self, k, v)

    def get_dict_var(self):
        return self.__dict__

    def is_daily_hitter_record(self):
        """
        is_데일리타자기록
        :return:
        """
        return True if self.daily_news_type == '타자' else False

    def is_daily_pitcher_record(self):
        """
        is_데일리투수기록
        :return:
        """
        return True if self.daily_news_type == '투수' else False

    def is_daily_pitcher_season_record(self):
        """
        is_데일리투수시즌기록
        :return:
        """
        return True if self.daily_news_type == '투수' else False

    def is_daily_hitter_season_record(self):
        """
        is_데일리타자시즌기록
        :return:
        """
        return True if self.daily_news_type == '타자' else False

    def is_daily_team_record(self):
        """
        is_데일리팀기록
        :return:
        """
        return True if self.daily_news_type == '팀' else False


