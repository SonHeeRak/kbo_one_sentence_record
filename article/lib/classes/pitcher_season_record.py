from article.lib.core.log_helper import LogHelper
from article.lib import globals as g
from article.lib import util
import sys
import pandas as pd


class DailyPitcherSeasonRecord(object):
    def __init__(self, gmkey=None, pcode=None):
        self.gmkey = gmkey
        self.gyear = gmkey[0:4]
        self.gday = gmkey[0:8]
        self.pcode = pcode
        self.continuous_win = 0
        self.continuous_QS = 0
        self.last_continuous_win = 0
        self.last_continuous_qs = 0

    def get_var(self):
        """
        투수시즌기록
        :return:
        """

        var = NamedVariable()
        try:
            query_result = g.b_models.Pitcher.objects.filter(gmkey__startswith=self.gyear,
                                                             gmkey__lte=self.gmkey, pcode=self.pcode).values()
            df = pd.DataFrame(query_result)

            pitcher_ERA = round(df.er.sum() * 9 / (df.inn2.sum() / 3), 2)  # 방어율
            lastgame_df = df[df.gday.lt(self.gmkey[0:8])]
            pitcher_last_ERA = round(lastgame_df.er.sum() * 9 / (lastgame_df.inn2.sum() / 3), 2)  # 이전경기 방어율
            is_era_up = False
            if pitcher_last_ERA < pitcher_ERA:
                is_era_up = True
            pitcher_ERA_dif = pitcher_ERA - pitcher_last_ERA

            pitcher_ERA = str(round(df.er.sum() * 9 / (df.inn2.sum() / 3), 2))  # 시즌 방어율
            if len(pitcher_ERA) == 3:
                pitcher_ERA = str(pitcher_ERA) + '0'

            is_ERA_0 = False  # 시즌 방어율 0
            if pitcher_ERA == '0.00':
                is_ERA_0 = True

            pitcher_game_cn = len(df)  # 게임수
            is_first_game = False  # 첫경기 여부
            if pitcher_game_cn == 1:
                is_first_game = True

            pitcher_starter_cn = len(df[df.start == '1'])  # 선발 경기수
            pitcher_relief_cn = pitcher_game_cn - pitcher_starter_cn

            pitcher_win_cn = len(df[df.wls == 'W'])  # 승수
            is_win = False  # 승리 여부
            if pitcher_win_cn > 0:
                is_win = True

            pitcher_lose_cn = len(df[df.wls == 'L'])  # 패수

            pitcher_save_cn = len(df[df.wls == 'S'])  # 세이브수
            is_save = False  # 세이브 여부
            if pitcher_save_cn > 0:
                is_save = True

            pitcher_hold_cn = len(df[df.hold == 1])  # 홀드수
            is_hold = False  # 홀드 여부
            if pitcher_hold_cn > 0:
                is_hold = True

            pitcher_con_win = self.get_continuous_win(df)  # 연승
            is_con_win = False  # 연승여부
            if pitcher_con_win > 1:
                is_con_win = True

            is_last_con_win = False  # 지속된 연승 여부
            pitcher_last_con_win = 0
            if pitcher_con_win == 0:
                pitcher_last_con_win = self.get_last_continuous_win(df)  # 지속된 연승
                if pitcher_last_con_win >= 2:
                    is_last_con_win = True

            pitcher_con_qs = self.get_continuous_qs(df)  # 연속 QS
            is_con_qs = False  # 연속 QS여부
            if pitcher_con_qs > 1:
                is_con_qs = True

            is_last_con_qs = False  # 지속된 QS 여부
            pitcher_last_con_qs = 0
            if pitcher_con_qs == 0:
                pitcher_last_con_qs = self.get_last_continuous_qs(df)  # 지속된 QS
                if pitcher_last_con_qs >= 2:
                    is_last_con_qs = True

            continuous_record_list = list()  # 연속기록
            if is_con_win:
                continuous_record_list.append('{}연승'.format(pitcher_con_win))
            if is_con_qs:
                continuous_record_list.append('{}연속 퀄리티스타트'.format(pitcher_con_qs))
            continuous_record_text = util.list_item_to_separate_text(continuous_record_list)

            is_con_record = False  # 연속기록여부
            is_last_con_record = False  # 지속된연속기록여부
            if len(continuous_record_text) > 0:
                is_con_record = True
            else:
                if is_last_con_win:
                    continuous_record_list.append('{}연승'.format(pitcher_last_con_win))
                if is_last_con_qs:
                    continuous_record_list.append('{}연속 퀄리티스타트'.format(pitcher_last_con_qs))
                continuous_record_text = util.list_item_to_separate_text(continuous_record_list)

                if len(continuous_record_text) > 0:
                    is_last_con_record = True

            # 시즌 퀄리티스타트수
            pitcher_qs_cn = len(df[(df.inn2 >= 18) & (df.er <= 3) & (df.pos == '11')])
            is_qs = False  # 퀄리티스타트여부
            if pitcher_qs_cn > 0:
                is_qs = True

            season_relief_record_list = list()  # 시즌불펜기록
            if is_win:
                season_relief_record_list.append('{}승'.format(pitcher_win_cn))
            if is_hold:
                season_relief_record_list.append('{}홀드'.format(pitcher_hold_cn))
            if is_save:
                season_relief_record_list.append('{}세이브'.format(pitcher_save_cn))
            season_relief_record_text = util.list_item_to_separate_text(season_relief_record_list)

            is_season_relief_record = False  # 시즌불펜기록 여부
            if len(season_relief_record_text) > 0:
                is_season_relief_record = True

            is_season_top_WPA = False  # 시즌 WPA 상위여부
            pitcher_season_WPA = None  # 시즌승리확률기여도
            pitcher_season_WPA_rank = None  # 시즌 WPA 랭킹
            if self.pcode in util.get_wpa_season_rank('pitcher', self.gmkey).pit_p_id.tolist():
                is_season_top_WPA = True
                #temp_df = g.df_wpa_season_rank
                temp_df = util.get_wpa_season_rank('pitcher', self.gmkey)
                pitcher_season_WPA = temp_df[temp_df.pit_p_id == self.pcode].wpa_rt.values.sum()
                pitcher_season_WPA = str(round(pitcher_season_WPA, 3))
                if len(pitcher_season_WPA) == 3:
                    pitcher_season_WPA = pitcher_season_WPA + '00'
                if len(pitcher_season_WPA) == 4:
                    pitcher_season_WPA = pitcher_season_WPA + '0'
                pitcher_season_WPA_rank = temp_df[temp_df.pit_p_id == self.pcode].index.values.sum() + 1

            setattr(var, '방어율', pitcher_ERA)
            setattr(var, 'is_방어율0', is_ERA_0)
            setattr(var, 'is_방어율up', is_era_up)
            setattr(var, '방어율차이', pitcher_ERA_dif)
            setattr(var, '연속기록', continuous_record_text)
            setattr(var, 'is_연속기록', is_con_record)
            setattr(var, 'is_지속된연속기록', is_last_con_record)
            setattr(var, 'is_첫경기', is_first_game)
            setattr(var, '게임수', pitcher_game_cn)
            setattr(var, '선발경기수', pitcher_starter_cn)
            setattr(var, '불펜경기수', pitcher_relief_cn)
            setattr(var, '승수', pitcher_win_cn)
            setattr(var, 'is_승', is_win)
            setattr(var, '패수', pitcher_lose_cn)
            setattr(var, 'QS수', pitcher_qs_cn)
            setattr(var, 'is_QS', is_qs)
            setattr(var, '시즌불펜기록', season_relief_record_text)
            setattr(var, 'is_시즌불펜기록', is_season_relief_record)
            setattr(var, 'is_시즌상위_WPA', is_season_top_WPA)
            setattr(var, '시즌WPA', pitcher_season_WPA)
            setattr(var, '시즌WPA순위', pitcher_season_WPA_rank)

        except Exception as e:
            LogHelper.instance().e(e, file_name=sys._getframe().f_code.co_filename,
                                   func_name=sys._getframe().f_code.co_name)

        return var

    def get_continuous_qs(self, data_frame):
        """
        연속QS
        :param data_frame:
        :return:
        """

        df = data_frame
        if len(df) > 0:
            gday = df.gday.values.tolist()[-1]
            if df[df.gday == gday].inn2.values[0] >= 18 and df[df.gday == gday].er.values[0] <= 3:
                self.continuous_QS += 1
                df = df[df.gday.lt(gday)]
                self.get_continuous_qs(df)

        return self.continuous_QS

    def get_last_continuous_qs(self, data_frame):
        """
        지속된 연속QS
        :param data_frame:
        :return:
        """

        df = data_frame
        if len(df) > 0:
            gday = df.gday.values.tolist()[-1]
            if df[df.gday == gday].inn2.values[0] < 18 or df[df.gday == gday].er.values[0] > 3:
                df = df[df.gday.lt(gday)]
                self.last_continuous_qs += self.get_continuous_qs(df)

        return self.last_continuous_qs

    def get_continuous_win(self, data_frame):
        """
        연승
        :param data_frame:
        :return:
        """

        df = data_frame
        if len(df) > 0:
            gday = df.gday.values.tolist()[-1]
            if df[df.gday == gday].wls.values[0] == 'W':
                self.continuous_win += 1
                df = df[df.gday.lt(gday)]
                self.get_continuous_win(df)

        return self.continuous_win

    def get_last_continuous_win(self, data_frame):
        """
        지속된 연승
        :param data_frame:
        :return:
        """

        df = data_frame
        if len(df) > 0:
            gday = df.gday.values.tolist()[-1]
            if df[df.gday == gday].wls.values[0] != 'W':
                df = df[df.gday.lt(gday)]
                self.last_continuous_win += self.get_continuous_win(df)

        return self.last_continuous_win


class NamedVariable:
    pass
