from article.lib.core.log_helper import LogHelper
from article.lib import util
from article.lib import globals as g
import sys
import pandas as pd
from django.db.models import Q


class DailyTeamRecord(object):
    def __init__(self, gmkey=None):
        self.gmkey = gmkey

    def get_var(self):
        """
        데일리팀기록
        :return:
        """

        var = NamedVariable()
        try:
            df = self.get_team_in_gmkey(self.gmkey)

            is_first_game = False  # 첫경기 여부
            if len(df) == 2:
                is_first_game = True

            is_20_game_over = False  # 20경기 이상 여부
            if len(df) > 40:
                is_20_game_over = True

            Hteam = self.gmkey[-3:-1]  # 홈팀
            Ateam = self.gmkey[-5:-3]  # 어웨이팀

            Hteam_score, Ateam_score = util.get_score(self.gmkey, Hteam)  # 홈팀, 어웨이팀 점수
            is_big_score = False  # 점수차 큰 게임
            is_one_score = False  # 한점차 게임
            if abs(Hteam_score - Ateam_score) >= 6:
                is_big_score = True
            elif abs(Hteam_score - Ateam_score) == 1:
                is_one_score = True

            is_Hteam_first_win, is_Hteam_win = self.get_is_win(self.gmkey, Hteam)  # 홈팀 첫승 여부, 홈팀 승 여부
            is_Ateam_first_win, is_Ateam_win = self.get_is_win(self.gmkey, Ateam)  # 어웨이팀 첫승 여부, 어웨이팀 승 여부

            # 홈팀 연승, 연패 수
            Hteam_continuous_win_cn, Hteam_continuous_lose_cn = self.get_continuous_win_lose(df, Hteam)
            # 어웨이팀 연승, 연패 수
            Ateam_continuous_win_cn, Ateam_continuous_lose_cn = self.get_continuous_win_lose(df, Ateam)

            # 홈팀 연승, 연패 여부
            is_Hteam_continous_win, is_Hteam_continous_lose = \
                self.get_is_continuous_win_lose(is_Hteam_win, Hteam_continuous_win_cn, Hteam_continuous_lose_cn)
            # 어웨이팀 연승, 연패 여부
            is_Ateam_continous_win, is_Ateam_continous_lose = \
                self.get_is_continuous_win_lose(is_Ateam_win, Ateam_continuous_win_cn, Ateam_continuous_lose_cn)

            # 이전 경기까지 지속된 홈팀 연승, 연패 수
            Hteam_last_continuous_win_cn, Hteam_last_continuous_lose_cn = self.get_last_continuous_win_lose(df, Hteam)
            # 이전 경기까지 지속된 어웨이팀 연승, 연패 수
            Ateam_last_continuous_win_cn, Ateam_last_continuous_lose_cn = self.get_last_continuous_win_lose(df, Ateam)

            # 홈팀 지속 연승, 연패 여부
            is_Hteam_last_continous_win, is_Hteam_last_continous_lose = \
                self.get_is_last_continuous_win_lose(is_Hteam_win,
                                                     Hteam_last_continuous_win_cn, Hteam_last_continuous_lose_cn)
            # 어웨이팀 지속 연승, 연패 여부
            is_Ateam_last_continous_win, is_Ateam_last_continous_lose = \
                self.get_is_last_continuous_win_lose(is_Ateam_win,
                                                     Ateam_last_continuous_win_cn, Ateam_last_continuous_lose_cn)

            Hteam_name = util.get_team_name(Hteam)  # 홈팀이름
            Ateam_name = util.get_team_name(Ateam)  # 어웨이팀이름

            Hteam_win_cn = df[df.team == Hteam].iloc[-1].win  # 시즌 홈팀 승수
            Ateam_win_cn = df[df.team == Ateam].iloc[-1].win  # 시즌 어웨이팀 승수

            # 끝내기 여부, 끝내기 팀, 상대팀, 타자, 투수, 이닝, 안타종류
            is_finish, finish_team, vs_team, hitter, inn, how = util.get_finish(self.gmkey)

            # 선발투수 승리 여부
            if is_Hteam_win:
                is_pitcher_win, pitcher = self.get_pitcher_record(self.gmkey, 'B')
            else:
                is_pitcher_win, pitcher = self.get_pitcher_record(self.gmkey, 'T')

            # 팀순위, 게임차
            Hteam_rank = None
            Ateam_rank = None
            Hteam_up_rank = None
            Ateam_up_rank = None
            is_Hteam_top_rank = False  # 홈팀 순위 1위 여부
            is_Ateam_top_rank = False  # 어웨팀 순위 1위 여부
            Hteam_compare_team = ''  # 홈팀보다 상위팀
            Ateam_compare_team = ''  # 어웨이팀보다 상위팀
            Hteam_gb_dif = 0  # 순위가 한단계 높은 팀과 홈팀의 경기차
            Ateam_gb_dif = 0  # 순위가 한단계 높은 팀과 어웨이팀의 경기차
            is_Hteam_gb_down = False  # 홈팀 경기차 줄었는지 여부
            is_Ateam_gb_down = False  # 어웨이팀 경기차 줄었는지 여부
            is_Hteam_rank_down = False  # 홈팀 순위 상승 여부
            is_Ateam_rank_down = False  # 어웨이팀 순위 상승 여부

            # 팀 이름 딕셔너리
            team_name_dic = {'HH': '한화', 'HT': '기아', 'KT': 'KT', 'LG': 'LG', 'NC': 'NC',
                             'OB': '두산', 'SK': 'SK', 'SS': '삼성', 'WO': '우리', 'LT': '롯데'}
            name_to_code_dic = {v: k for k, v in team_name_dic.items()}

            gb_df = self.get_game_behind(self.gmkey)
            last_gb_df = self.get_last_game_behind(self.gmkey)
            if last_gb_df is not None:
                gb_merge_df = pd.merge(last_gb_df, gb_df, on='team', suffixes=('_ex', '_pr'))
                gb_merge_df['is_rank_change'] = gb_merge_df.rank_ex != gb_merge_df.rank_pr
                gb_merge_df['gb_dif'] = gb_merge_df.gb_ex - gb_merge_df.gb_pr
                gb_merge_df['is_gb_change'] = gb_merge_df.gb_ex != gb_merge_df.gb_pr

                # 순위표
                rank_ex = gb_merge_df['rank_ex'].sort_values().tolist()
                rank_pr = gb_merge_df['rank_pr'].sort_values().tolist()

                Hteam_rank = gb_merge_df[gb_merge_df.team == team_name_dic[Hteam]].iloc[-1].rank_pr  # 홈팀 순위
                last_Hteam_rank = gb_merge_df[gb_merge_df.team == team_name_dic[Hteam]].iloc[-1].rank_ex  # 전날 홈팀 순위
                if last_Hteam_rank - Hteam_rank > 0:
                    is_Hteam_rank_down = True
                elif last_Hteam_rank - Hteam_rank == 0:
                    is_Hteam_rank_down = -1
                Hteam_up_rank = Hteam_rank - 1  # 홈팀보다 상위팀 순위
                Ateam_rank = gb_merge_df[gb_merge_df.team == team_name_dic[Ateam]].iloc[-1].rank_pr  # 어웨이팀 순위
                last_Ateam_rank = gb_merge_df[gb_merge_df.team == team_name_dic[Ateam]].iloc[-1].rank_ex  # 전날 어웨이팀 순위

                if last_Ateam_rank - Ateam_rank > 0:
                    is_Ateam_rank_down = True
                elif last_Ateam_rank - Ateam_rank == 0:
                    is_Ateam_rank_down = -1
                Ateam_up_rank = Ateam_rank - 1  # 어웨이팀보다 상위팀 순위

                if Hteam_rank == 1:
                    is_Hteam_top_rank = True
                    # 2위 팀
                    Hteam_compare_team = gb_merge_df[gb_merge_df.rank_pr == rank_pr[Hteam_rank]].iloc[-1].team
                    # 1위와 2위 경기차
                    Hteam_gb_dif = gb_merge_df[gb_merge_df.rank_pr == rank_pr[Hteam_rank]].iloc[-1].gb_pr
                    # 전날 1위와 2위 경기차
                    last_Hteam_gb_dif = gb_merge_df[gb_merge_df.rank_ex == rank_ex[Hteam_rank]].iloc[-1].gb_ex
                    if last_Hteam_gb_dif - Hteam_gb_dif > 0:
                        is_Hteam_gb_down = True
                    elif last_Hteam_gb_dif - Hteam_gb_dif == 0:
                        is_Hteam_gb_down = -1
                elif Hteam_rank > 1:
                    # 1위와 홈팀 경기차
                    Hteam_gb = gb_merge_df[gb_merge_df.team == team_name_dic[Hteam]].iloc[-1].gb_pr
                    # 상위팀
                    Hteam_compare_team = gb_merge_df[gb_merge_df.rank_pr == rank_pr[Hteam_rank - 2]].iloc[-1].team
                    # 1위와 상위팀 경기차
                    rank_up_gb = gb_merge_df[gb_merge_df.rank_pr == rank_pr[Hteam_rank - 2]].iloc[-1].gb_pr
                    # 홈팀과 상위팀 경기차
                    Hteam_gb_dif = Hteam_gb - rank_up_gb
                    # 전날 1위와 홈팀 경기차
                    last_Hteam_gb = gb_merge_df[gb_merge_df.team == team_name_dic[Hteam]].iloc[-1].gb_ex
                    # 전날 1위와 상위팀 경기차
                    last_rank_up_gb = gb_merge_df[gb_merge_df.rank_ex == rank_ex[Hteam_rank - 2]].iloc[-1].gb_ex
                    # 전날 홈팀과 상위팀 경기차
                    last_Hteam_gb_dif = last_Hteam_gb - last_rank_up_gb
                    if last_Hteam_gb_dif - Hteam_gb_dif > 0:
                        is_Hteam_gb_down = True
                    elif last_Hteam_gb_dif - Hteam_gb_dif == 0:
                        is_Hteam_gb_down = -1
                if Ateam_rank == 1:
                    is_Ateam_top_rank = True
                    # 2위 팀
                    Ateam_compare_team = gb_merge_df[gb_merge_df.rank_pr == rank_pr[Ateam_rank]].iloc[-1].team
                    # 1위와 2위 경기차
                    Ateam_gb_dif = gb_merge_df[gb_merge_df.rank_pr == rank_pr[Ateam_rank]].iloc[-1].gb_pr
                    # 전날 1위와 2위 경기차
                    last_Ateam_gb_dif = gb_merge_df[gb_merge_df.rank_ex == rank_ex[Ateam_rank]].iloc[-1].gb_ex
                    if last_Ateam_gb_dif - Ateam_gb_dif > 0:
                        is_Ateam_gb_down = True
                    elif last_Ateam_gb_dif - Ateam_gb_dif == 0:
                        is_Ateam_gb_down = -1
                elif Ateam_rank > 1:
                    # 1위와 어웨이팀 경기차
                    Ateam_gb = gb_merge_df[gb_merge_df.team == team_name_dic[Ateam]].iloc[-1].gb_pr
                    # 상위팀
                    Ateam_compare_team = gb_merge_df[gb_merge_df.rank_pr == rank_pr[Ateam_rank - 2]].iloc[-1].team
                    # 1위와 상위팀 경기차
                    rank_up_gb = gb_merge_df[gb_merge_df.rank_pr == rank_pr[Ateam_rank - 2]].iloc[-1].gb_pr
                    # 어웨이팀과 상위팀 경기차
                    Ateam_gb_dif = Ateam_gb - rank_up_gb
                    # 전날 1위와 어웨이팀 경기차
                    last_Ateam_gb = gb_merge_df[gb_merge_df.team == team_name_dic[Ateam]].iloc[-1].gb_ex
                    # 전날 1위와 상위팀 경기차
                    last_rank_up_gb = gb_merge_df[gb_merge_df.rank_ex == rank_ex[Ateam_rank - 2]].iloc[-1].gb_ex
                    # 전날 어웨이팀과 상위팀 경기차
                    last_Ateam_gb_dif = last_Ateam_gb - last_rank_up_gb
                    if last_Ateam_gb_dif - Ateam_gb_dif > 0:
                        is_Ateam_gb_down = True
                    if last_Ateam_gb_dif - Ateam_gb_dif == 0:
                        is_Ateam_gb_down = -1

            # 상대성적
            rs_df = self.get_relative_score(self.gmkey)  # relative score

            rs_dic = {Hteam: 0, Ateam: 0}  # 상대성적 딕셔너리
            for i, row in rs_df.iterrows():
                if row['tb'] == 'T':
                    rs_dic[row['gmkey'][8:10]] += 1
                else:
                    rs_dic[row['gmkey'][10:12]] += 1

            Hteam_rs = rs_dic[Hteam]  # 홈팀 상대성적
            Ateam_rs = rs_dic[Ateam]  # 어웨이팀 상대성적
            is_Hteam_rs_win = False  # 홈팀 상대성적 승리여부
            if Hteam_rs - Ateam_rs > 0:
                is_Hteam_rs_win = True
            elif Hteam_rs - Ateam_rs == 0:
                is_Hteam_rs_win = -1

            setattr(var, 'is_첫경기', is_first_game)
            setattr(var, 'is_20경기', is_20_game_over)
            setattr(var, '홈팀', Hteam_name)
            setattr(var, '어웨이팀', Ateam_name)
            setattr(var, '홈팀승수', Hteam_win_cn)
            setattr(var, '어웨이팀승수', Ateam_win_cn)
            setattr(var, '홈팀스코어', Hteam_score)
            setattr(var, '어웨이팀스코어', Ateam_score)
            setattr(var, 'is_대파', is_big_score)
            setattr(var, 'is_한점차', is_one_score)
            setattr(var, 'is_끝내기', is_finish)
            setattr(var, '끝내기팀', util.get_team_name(finish_team))
            setattr(var, '끝내기당한팀', util.get_team_name(vs_team))
            setattr(var, '끝내기타자', util.get_person_name(hitter))
            setattr(var, '끝내기이닝', '연장' if int(inn) > 9 else '{}회말'.format(inn))
            setattr(var, '끝내기안타', '홈런' if how == 'HR' else '안타')
            setattr(var, 'is_선발투수승', is_pitcher_win)
            setattr(var, '선발투수', util.get_person_name(pitcher))
            setattr(var, 'is_홈팀첫승', is_Hteam_first_win)
            setattr(var, 'is_어웨이팀첫승', is_Ateam_first_win)
            setattr(var, 'is_홈팀승', is_Hteam_win)
            setattr(var, 'is_어웨이팀승', is_Ateam_win)
            setattr(var, '홈팀연승수', Hteam_continuous_win_cn)
            setattr(var, '홈팀연패수', Hteam_continuous_lose_cn)
            setattr(var, '어웨이팀연승수', Ateam_continuous_win_cn)
            setattr(var, '어웨이팀연패수', Ateam_continuous_lose_cn)
            setattr(var, 'is_홈팀연승', is_Hteam_continous_win)
            setattr(var, 'is_홈팀연패', is_Hteam_continous_lose)
            setattr(var, 'is_어웨이팀연승', is_Ateam_continous_win)
            setattr(var, 'is_어웨이팀연패', is_Ateam_continous_lose)
            setattr(var, '홈팀지속연승수', Hteam_last_continuous_win_cn)
            setattr(var, '홈팀지속연패수', Hteam_last_continuous_lose_cn)
            setattr(var, '어웨이팀지속연승수', Ateam_last_continuous_win_cn)
            setattr(var, '어웨이팀지속연패수', Ateam_last_continuous_lose_cn)
            setattr(var, 'is_홈팀지속연승', is_Hteam_last_continous_win)
            setattr(var, 'is_홈팀지속연패', is_Hteam_last_continous_lose)
            setattr(var, 'is_어웨이팀지속연승', is_Ateam_last_continous_win)
            setattr(var, 'is_어웨이팀지속연패', is_Ateam_last_continous_lose)
            setattr(var, '홈팀순위', Hteam_rank)
            setattr(var, 'is_홈팀순위_down', is_Hteam_rank_down)
            setattr(var, '홈팀상위팀', util.get_team_name(name_to_code_dic[Hteam_compare_team]))
            setattr(var, '홈팀상위팀순위', Hteam_up_rank)
            setattr(var, 'is_홈팀1위', is_Hteam_top_rank)
            setattr(var, '홈팀경기차', int(Hteam_gb_dif) if str(Hteam_gb_dif)[-1] == '0' else Hteam_gb_dif)
            setattr(var, 'is_홈팀경기차_down', is_Hteam_gb_down)
            setattr(var, '어웨이팀순위', Ateam_rank)
            setattr(var, 'is_어웨이팀순위_down', is_Ateam_rank_down)
            setattr(var, '어웨이팀상위팀', util.get_team_name(name_to_code_dic[Ateam_compare_team]))
            setattr(var, '어웨이팀상위팀순위', Ateam_up_rank)
            setattr(var, 'is_어웨이팀1위', is_Ateam_top_rank)
            setattr(var, '어웨이팀경기차', int(Ateam_gb_dif) if str(Ateam_gb_dif)[-1] == '0' else Ateam_gb_dif)
            setattr(var, 'is_어웨이팀경기차_down', is_Ateam_gb_down)
            setattr(var, '홈팀상대성적', Hteam_rs)
            setattr(var, '어웨이팀상대성적', Ateam_rs)
            setattr(var, 'is_홈팀상대성적_win', is_Hteam_rs_win)

        except Exception as e:
            LogHelper.instance().e(e, file_name=sys._getframe().f_code.co_filename,
                                   func_name=sys._getframe().f_code.co_name)

        return var

    @staticmethod
    def get_team_in_gmkey(gmkey):
        """
        양 팀의 경기 dataframe
        :param gmkey:
        :return:
        """
        team_df = None
        team_name_dic = {'HH': '한화', 'HT': '기아', 'KT': 'KT', 'LG': 'LG', 'NC': 'NC',
                         'OB': '두산', 'SK': 'SK', 'SS': '삼성', 'WO': '우리', 'LT': '롯데'}
        name_to_code_dic = {v: k for k, v in team_name_dic.items()}
        query_result = g.b_models.TeamrankDaily.objects.filter(date__gte=util.get_season_start_date(gmkey), date__lte=gmkey[0:8]) & (
                g.b_models.TeamrankDaily.objects.filter(team=team_name_dic[gmkey[-5:-3]]) |
                g.b_models.TeamrankDaily.objects.filter(team=team_name_dic[gmkey[-3:-1]]))
        if query_result:
            team_df = pd.DataFrame(query_result.values())
            team_df.team = team_df.team.apply(lambda x: name_to_code_dic[x])

        return team_df

    @staticmethod
    def get_is_win(gmkey, team):
        """
        팀 첫승, 승 여부
        :param gmkey:
        :param team:
        :return:
        """
        is_first_win = False
        is_win = False
        query_result = g.b_models.Dailyrank.objects.filter(gday=gmkey[0:8], team=team).values()[0]
        if query_result:
            if query_result['w'] == 1 and query_result['ww'] == 1:
                is_first_win = True
                is_win = True
            elif query_result['w'] == 1:
                is_win = True
            elif query_result['w'] == 2:
                is_win = True

        return is_first_win, is_win

    @staticmethod
    def get_continuous_win_lose(data_frame, team):
        """
        연승, 연패
        :param data_frame:
        :param team:
        :return:
        """
        df = data_frame[data_frame.team == team]

        continuous_win_cn = 0
        continuous_lose_cn = 0
        if len(df) > 1:
            continue_sc = df.iloc[-1].continue_field
            if continue_sc[1] == '승':
                continuous_win_cn = continue_sc[0]
            elif continue_sc[1] == '패':
                continuous_lose_cn = continue_sc[0]

        return continuous_win_cn, continuous_lose_cn

    @staticmethod
    def get_last_continuous_win_lose(data_frame, team):
        """
        이전 경기까지 지속된 연승, 연패
        :param data_frame:
        :param team:
        :return:
        """
        df = data_frame[data_frame.team == team]

        last_continuous_win_cn = 0
        last_continuous_lose_cn = 0
        if len(df) > 1:
            continue_sc = df.iloc[-2].continue_field
            if continue_sc[1] == '승':
                last_continuous_win_cn = continue_sc[0]
            elif continue_sc[1] == '패':
                last_continuous_lose_cn = continue_sc[0]

        return last_continuous_win_cn, last_continuous_lose_cn

    @staticmethod
    def get_is_continuous_win_lose(is_win, continuous_win_cn, continuous_lose_cn):
        """
        지속된 연승, 연패 여부
        :param is_win:
        :param continuous_win_cn:
        :param continuous_lose_cn:
        :return:
        """
        is_continous_win = False  # 연승여부
        is_continous_lose = False  # 연패여부
        if is_win:
            if int(continuous_win_cn) > 1:
                is_continous_win = True
            elif int(continuous_lose_cn) > 1:
                is_continous_lose = True
        else:
            if int(continuous_win_cn) > 1:
                is_continous_win = True
            elif int(continuous_lose_cn) > 1:
                is_continous_lose = True

        return is_continous_win, is_continous_lose

    @staticmethod
    def get_is_last_continuous_win_lose(is_win, last_continuous_win_cn, last_continuous_lose_cn):
        """
        이전 경기까지 지속된 연승, 연패 여부
        :param is_win:
        :param last_continuous_win_cn:
        :param last_continuous_lose_cn:
        :return:
        """
        is_last_continous_win = False  # 연승여부
        is_last_continous_lose = False  # 연패여부
        if is_win:
            if int(last_continuous_lose_cn) > 1:
                is_last_continous_lose = True
        else:
            if int(last_continuous_win_cn) > 1:
                is_last_continous_win = True

        return is_last_continous_win, is_last_continous_lose

    @staticmethod
    def get_pitcher_record(gmkey, tb):
        """
        선발투수 승리 여부
        :param gmkey:
        :return:
        """
        is_win = False
        pitcher = ''
        query_result = g.b_models.Pitcher.objects.filter(gmkey=gmkey, start='1', tb=tb).exclude(name='합계').values()
        if query_result:
            query_result = query_result[0]
            if query_result['wls'] == 'W':
                is_win = True
            pitcher = query_result['pcode']

        return is_win, pitcher

    @staticmethod
    def get_game_behind(gmkey):
        """
        경기차
        :param gmkey:
        :return:
        """
        df = None
        query_result = g.b_models.TeamrankDaily.objects.filter(date=gmkey[0:8]).values()
        if query_result:
            df = pd.DataFrame(query_result)
            rank_1st = df[df['rank'] == 1].iloc[-1]
            df['gb'] = ((rank_1st.win - rank_1st.lose) - (df['win'] - df['lose'])) / 2
            df = df[['team', 'rank', 'gb', 'date']]

        return df

    @staticmethod
    def get_last_game_behind(gmkey):
        """
        지난 경기차
        :param gmkey:
        :return:
        """
        df = None
        query_result = g.b_models.TeamrankDaily.objects.filter(date__startswith=gmkey[0:4],
                                                               date__lt=gmkey[0:8]).values()
        if query_result:
            df = pd.DataFrame(query_result)
            last_date = df.date.max()
            df = df[df.date == last_date]
            rank_1st = df[df['rank'] == 1].iloc[-1]
            df['gb'] = ((rank_1st.win - rank_1st.lose) - (df['win'] - df['lose'])) / 2
            df = df[['team', 'rank', 'gb', 'date']]

        return df

    @staticmethod
    def get_relative_score(gmkey):
        """
        상대성적
        :param gmkey:
        :return:
        """
        df = None
        query_result = g.b_models.Pitcher.objects.all().filter(Q(gday__startswith=gmkey[0:4],
                                                                 gday__lte=gmkey[0:8],
                                                                 gmkey__endswith=gmkey[8:10]+gmkey[10:12]+'0') |
                                                               Q(gday__startswith=gmkey[0:4],
                                                                 gday__lte=gmkey[0:8],
                                                                 gmkey__endswith=gmkey[10:12]+gmkey[8:10]+'0')).\
            filter(name='합계').values()
        if query_result:
            df = pd.DataFrame(query_result)
            df = df[['gmkey', 'tb', 'wls']]
            df = df[df.wls == 'W']

        return df


class NamedVariable:
    pass
