from article.lib.core.log_helper import LogHelper
from article.lib import globals as g
from article.lib import util
import sys
import pandas as pd


class DailyHitterSeasonRecord(object):
    def __init__(self, gmkey=None, pcode=None):
        self.gmkey = gmkey
        self.gyear = gmkey[0:4]
        self.gday = gmkey[0:8]
        self.pcode = pcode
        self.continuous_HIT = 0
        self.continuous_on_base = 0
        self.continuous_RBI = 0
        self.last_continuous_HIT = 0
        self.last_continuous_on_base = 0
        self.last_continuous_RBI = 0

    def get_var(self):
        """
        타자시즌기록
        :return:
        """

        var = NamedVariable()
        try:
            query_result = g.b_models.Hitter.objects.filter(gmkey__startswith=self.gyear,
                                                            gmkey__lte=self.gmkey, pcode=self.pcode).values()
            df = pd.DataFrame(query_result)

            hitter_game_cn = len(df)  # 시즌 경기출장수
            is_first_game = False  # 첫경기여부
            if hitter_game_cn == 1:
                is_first_game = True

            hitter_AB = df.ab.sum()  # 시즌 타수
            hitter_HIT = df.hit.sum()  # 시즌 안타수

            hitter_HRA = '0.000'
            if hitter_AB > 0:
                hitter_HRA = str(round(hitter_HIT / hitter_AB, 3))  # 시즌 타율
                if len(hitter_HRA) == 4:
                    hitter_HRA = str(hitter_HRA) + '0'
                elif len(hitter_HRA) == 3:
                    hitter_HRA = str(hitter_HRA) + '00'

            hitter_con_HIT = self.get_continuous_hit(df)  # 연속 안타
            is_con_HIT = False  # 연속안타여부
            if hitter_con_HIT > 1:
                is_con_HIT = True

            is_last_con_HIT = False  # 지속된 연속안타 여부
            hitter_last_con_HIT = 0
            if hitter_con_HIT == 0:
                hitter_last_con_HIT = self.get_last_continuous_hit(df)  # 지속된 연속 안타
                if hitter_last_con_HIT >= 2:
                    is_last_con_HIT = True

            hitter_con_on_base = self.get_continuous_on_base(df)  # 연속 출루
            is_con_on_base = False  # 연속출루여부
            if hitter_con_on_base > 1:
                is_con_on_base = True

            is_last_con_on_base = False  # 지속된 연속출루 여부
            hitter_last_con_on_base = 0
            if hitter_con_on_base == 0:
                hitter_last_con_on_base = self.get_last_continuous_on_base(df)  # 지속된 연속 출루
                if hitter_last_con_on_base >= 2:
                    is_last_con_on_base = True

            hitter_con_RBI = self.get_continuous_rbi(df)  # 연속 타점
            is_con_RBI = False  # 연속타점여부
            if hitter_con_RBI > 1:
                is_con_RBI = True

            is_last_con_RBI = False  # 지속된 연속타점 여부
            hitter_last_con_RBI = 0
            if hitter_con_RBI == 0:
                hitter_last_con_RBI = self.get_last_continuous_on_base(df)  # 지속된 연속 타점
                if hitter_last_con_RBI >= 2:
                    is_last_con_RBI = True

            continuous_record_list = list()  # 연속기록
            if is_con_HIT:
                continuous_record_list.append('{}경기 연속 안타'.format(hitter_con_HIT))
            if is_con_RBI:
                continuous_record_list.append('{}경기 연속 타점'.format(hitter_con_RBI))
            if is_con_on_base:
                continuous_record_list.append('{}경기 연속 출루'.format(hitter_con_on_base))
            continuous_record_text = util.list_item_to_separate_text(continuous_record_list)

            is_con_record = False  # 연속기록여부
            is_last_con_record = False  # 지속된연속기록여부
            if len(continuous_record_text) > 0:
                is_con_record = True
            else:
                if is_last_con_HIT:
                    continuous_record_list.append('{}경기 연속 안타'.format(hitter_last_con_HIT))
                if is_last_con_on_base:
                    continuous_record_list.append('{}경기 연속 출루'.format(hitter_last_con_on_base))
                if is_last_con_RBI:
                    continuous_record_list.append('{}경기 연속 타점'.format(hitter_last_con_RBI))
                continuous_record_text = util.list_item_to_separate_text(continuous_record_list)

                if len(continuous_record_text) > 0:
                    is_last_con_record = True

            hitter_HR = df.hr.sum()  # 시즌 홈런수
            is_HR = False  # 시즌 홈런여부
            if hitter_HR > 0:
                is_HR = True

            hitter_SB = df.sb.sum()  # 시즌 도루수
            is_SB = False  # 시즌 도루여부
            if hitter_SB > 0:
                is_SB = True

            hitter_RBI = df.rbi.sum()  # 시즌 타점
            is_RBI = False  # 시즌 타점여부
            if hitter_RBI > 0:
                is_RBI = True

            hitter_RUN = df.run.sum()  # 시즌 득점
            is_RUN = False  # 시즌 득점여부
            if hitter_RUN > 0:
                is_RUN = True

            season_record_list = list()  # 시즌기록
            if is_HR:
                season_record_list.append('{}홈런'.format(hitter_HR))
            if is_RBI:
                season_record_list.append('{}타점'.format(hitter_RBI))
            if is_RUN:
                season_record_list.append('{}득점'.format(hitter_RUN))
            if is_SB:
                season_record_list.append('{}도루'.format(hitter_SB))
            season_record_text = util.list_item_to_separate_text(season_record_list)

            is_season_record = False  # 시즌기록 여부
            if len(season_record_text) > 0:
                is_season_record = True

            is_season_top_WPA = False  # 시즌 WPA 상위여부
            hitter_season_WPA = None  # 시즌승리확률기여도
            hitter_season_WPA_rank = None  # 시즌 WPA 랭킹
            if self.pcode in util.get_wpa_season_rank('hitter', self.gmkey).bat_p_id.tolist():
                is_season_top_WPA = True
                #temp_df = g.df_wpa_season_rank
                temp_df = util.get_wpa_season_rank('hitter', self.gmkey)
                hitter_season_WPA = temp_df[temp_df.bat_p_id == self.pcode].wpa_rt.values.sum()
                hitter_season_WPA = str(round(hitter_season_WPA, 3))
                if len(hitter_season_WPA) == 3:
                    hitter_season_WPA = hitter_season_WPA + '00'
                if len(hitter_season_WPA) == 4:
                    hitter_season_WPA = hitter_season_WPA + '0'
                hitter_season_WPA_rank = temp_df[temp_df.bat_p_id == self.pcode].index.values.sum() + 1

            setattr(var, '게임수', hitter_game_cn)
            setattr(var, 'is_첫경기', is_first_game)
            setattr(var, '타율', hitter_HRA)
            setattr(var, '연속기록', continuous_record_text)
            setattr(var, 'is_연속기록', is_con_record)
            setattr(var, 'is_지속된연속기록', is_last_con_record)
            setattr(var, '시즌기록', season_record_text)
            setattr(var, 'is_시즌기록', is_season_record)
            setattr(var, 'is_시즌상위_WPA', is_season_top_WPA)
            setattr(var, '시즌WPA', hitter_season_WPA)
            setattr(var, '시즌WPA순위', hitter_season_WPA_rank)

        except Exception as e:
            LogHelper.instance().e(e, file_name=sys._getframe().f_code.co_filename,
                                   func_name=sys._getframe().f_code.co_name)

        return var

    def get_continuous_hit(self, data_frame):
        """
        연속안타
        :param data_frame:
        :return:
        """

        df = data_frame
        if len(df) > 0:
            gday = df.gday.values.tolist()[-1]
            if df[df.gday == gday].hit.values[0] > 0:
                self.continuous_HIT += 1
                df = df[df.gday.lt(gday)]
                self.get_continuous_hit(df)

        return self.continuous_HIT

    def get_last_continuous_hit(self, data_frame):
        """
        지속된연속안타
        :param data_frame:
        :return:
        """

        df = data_frame
        if len(df) > 0:
            gday = df.gday.values.tolist()[-1]
            if df[df.gday == gday].hit.values[0] == 0:
                df = df[df.gday.lt(gday)]
                self.last_continuous_HIT += self.get_continuous_hit(df)

        return self.last_continuous_HIT

    def get_continuous_on_base(self, data_frame):
        """
        연속출루
        :param data_frame:
        :return:
        """

        df = data_frame
        if len(df) > 0:
            gday = df.gday.values.tolist()[-1]
            if df[df.gday == gday][['hit', 'bb', 'hp']].sum(axis=1).values[0] > 0:
                self.continuous_on_base += 1
                df = df[df.gday.lt(gday)]
                self.get_continuous_on_base(df)

        return self.continuous_on_base

    def get_last_continuous_on_base(self, data_frame):
        """
        지속된연속출루
        :param data_frame:
        :return:
        """

        df = data_frame
        if len(df) > 0:
            gday = df.gday.values.tolist()[-1]
            if df[df.gday == gday][['hit', 'bb', 'hp']].sum(axis=1).values[0] == 0:
                df = df[df.gday.lt(gday)]
                self.last_continuous_on_base += self.get_continuous_on_base(df)

        return self.continuous_on_base

    def get_continuous_rbi(self, data_frame):
        """
        연속타점
        :param data_frame:
        :return:
        """

        df = data_frame
        if len(df) > 0:
            gday = df.gday.values.tolist()[-1]
            if df[df.gday == gday].rbi.values[0] > 0:
                self.continuous_RBI += 1
                df = df[df.gday.lt(gday)]
                self.get_continuous_rbi(df)

        return self.continuous_RBI

    def get_last_continuous_rbi(self, data_frame):
        """
        지속된연속타점
        :param data_frame:
        :return:
        """

        df = data_frame
        if len(df) > 0:
            gday = df.gday.values.tolist()[-1]
            if df[df.gday == gday].rbi.values[0] == 0:
                df = df[df.gday.lt(gday)]
                self.last_continuous_RBI += self.get_continuous_rbi(df)

        return self.last_continuous_RBI


class NamedVariable:
    pass
