from article.lib.core.log_helper import LogHelper
from article.lib import util
from article.lib import globals as g
import sys
import pandas as pd


class DailyPitcherRecord(object):
    def __init__(self, data_frame=None, gmkey=None, pcode=None):
        self.data_frame = data_frame
        self.gmkey = gmkey
        self.gyear = gmkey[0:4]
        self.gday = gmkey[0:8]
        self.pcode = pcode

    def get_var(self):
        """
        데일리투수기록
        :return:
        """

        var = NamedVariable()
        try:
            df = self.data_frame

            pitcher_START = df.start.values.sum()
            is_starter = False  # 선발
            if pitcher_START == '1':
                is_starter = True

            # 투수팀, 상대팀 구분
            pitcher_TB = df.tb.values.sum()
            if pitcher_TB == 'T':
                pitcher_team = self.gmkey[-5:-3]
                pitcher_vsteam = self.gmkey[-3:-1]
            else:
                pitcher_team = self.gmkey[-3:-1]
                pitcher_vsteam = self.gmkey[-5:-3]

            stadium = util.get_stadium(self.gmkey)  # 경기장

            pitcher_QUIT = df.quit.values.sum()
            is_last_pitcher = False  # 마무리여부
            if pitcher_QUIT == '1':
                is_last_pitcher = True

            is_shutout = False  # 완투 유무
            if is_starter and is_last_pitcher:
                is_shutout = True

            pitcher_INN = df.inn.values.sum().split(' ')  # 이닝
            if len(pitcher_INN) > 1 and pitcher_INN[0] != '0':
                pitcher_INN = pitcher_INN[0] + '#과 ' + pitcher_INN[1]
            elif len(pitcher_INN) > 1 and pitcher_INN[0] == '0':
                pitcher_INN = pitcher_INN[1]
            else:
                pitcher_INN = pitcher_INN[0]

            pitcher_INN2 = df.inn2.values.sum()  # 잡은 아웃카운트
            is_5INN = False  # 5이닝 이상 여부
            if pitcher_INN2 >= 15:
                is_5INN = True

            pitcher_HIT = df.hit.values.sum()  # 피안타
            is_HIT = False  # 피안타 유무
            if pitcher_HIT > 0:
                is_HIT = True

            pitcher_KK = df.kk.values.sum()  # 탈삼진
            is_KK = False  # 탈삼진 유무
            if pitcher_KK > 0:
                is_KK = True

            pitcher_R = df.r.values.sum()  # 실점
            is_R = False  # 실점유무
            if pitcher_R > 0:
                is_R = True

            pitcher_ER = df.er.values.sum()  # 자책점
            is_ER = False  # 자책점유무
            if pitcher_ER > 0:
                is_ER = True

            pitcher_BB = df.bb.values.sum()  # 볼넷
            is_BB = False  # 볼넷유무
            if pitcher_BB > 0:
                is_BB = True

            pitcher_BF = df.bf.values.sum()  # 투구수

            pitcher_WLS = df.wls.values.sum()  # 승패세여부
            is_win_pitcher = False  # 승리투수 여부
            is_save_pitcher = False
            is_lose_pitcher = False
            if pitcher_WLS == 'W':
                is_win_pitcher = True
            elif pitcher_WLS == 'S':
                is_save_pitcher = True
            elif pitcher_WLS == 'L':
                is_lose_pitcher = True

            pitcher_HOLD = df.hold.values.sum()  # 홀드
            is_hold = False  # 홀드여부
            if pitcher_HOLD == 1:
                is_hold = True

            is_QS = False
            if pitcher_INN2 >= 18 and pitcher_ER <= 3:
                is_QS = True

            is_QSP = False
            if pitcher_INN2 >= 21 and pitcher_ER <= 3:
                is_QSP = True

            # 투수팀 스코어, 상대팀 스코어
            pitcher_team_point, pitcher_vsteam_point = util.get_score(self.gmkey, pitcher_team)
            # 투수팀 승패여부
            is_win = False
            if pitcher_team_point > pitcher_vsteam_point:
                is_win = True

            is_top_WPA = False  # WPA 상위여부
            pitcher_WPA = None  # 승리확률기여도
            pitcher_WPA_rank = None  # WPA 랭킹
            if self.pcode in util.get_wpa_daily_rank('pitcher', self.gmkey).pit_p_id.tolist():
                is_top_WPA = True
                temp_df = util.get_wpa_daily_rank('pitcher', self.gmkey)
                pitcher_WPA = temp_df[temp_df.pit_p_id == self.pcode].wpa_rt.values.sum()
                pitcher_WPA = str(round(pitcher_WPA * 100, 1))
                pitcher_WPA_rank = temp_df[temp_df.pit_p_id == self.pcode].index.values.sum() + 1

            is_top_WPA_situation = False  # WPA 상황 상위여부
            pitcher_WPA_situation_list = list()  # WPA 상황 기록
            pitcher_WPA_situation_text = ''  # WPA 상황 기록
            df_wpa_situation = util.get_top_wpa_situation('pitcher', self.gmkey)

            if self.pcode in df_wpa_situation.pit_p_id.tolist():
                is_top_WPA_situation = True
                temp_df = df_wpa_situation[df_wpa_situation.pit_p_id == self.pcode]
                for i, row in temp_df.iterrows():
                    temp_list = list()
                    inn_no = row.inn_no
                    tb = '말' if row.tb_sc == 'B' else '초'
                    before_away_score = row.before_away_score_cn
                    before_score_gap = row.before_score_gap_cn if tb == '초' else row.before_score_gap_cn * -1
                    before_runner_sc = str(row.before_runner_sc)
                    runner_sc = '{}'.format(before_runner_sc[0])
                    for idx in range(1, len(before_runner_sc)):
                        runner_sc += ', {}'.format(before_runner_sc[idx])
                    runner_sc = runner_sc + '루'
                    before_runner_sc = '만루' if before_runner_sc == '123' else runner_sc
                    hitter_name = row.livetext_if.split(':')[0].strip()
                    livetext = row.livetext_if.split(':')[1].split('\r')[0].split('(')[0].strip()
                    temp_list.append('{}회{}'.format(inn_no, tb))
                    if before_runner_sc == '0':
                        temp_list.append('주자 {}'.format(before_runner_sc))
                    if before_score_gap > 0:
                        temp_list.append('{}점 이기고 있는 상황에서'.format(abs(before_score_gap)))
                    elif before_score_gap < 0:
                        temp_list.append('{}점 지고 있는 상황에서'.format(abs(before_score_gap)))
                    elif inn_no < 5:
                        temp_list.append('{}대{}의 상황에서'.format(before_away_score, before_away_score))
                    else:
                        temp_list.append('{}대{} 팽팽한 상황에서'.format(before_away_score, before_away_score))
                    temp_list.append('{}#를 {}'.format(hitter_name, livetext))
                    pitcher_WPA_situation_list.append(util.list_item_to_separate_text(temp_list))
                pitcher_WPA_situation_text = util.list_item_to_separate_text(pitcher_WPA_situation_list, separator=',')

            pitcher_chin = None  # 교체이닝
            is_chin_situation = False  # 교체시점 특이사항 여부
            pitcher_chin_situation = ''  # 교체상황
            if not is_starter:
                pitcher_chin = util.get_player_chin(self.gmkey, self.pcode)
                df_change_situation = util.get_df_change_situation('pitcher', self.gmkey, self.pcode)  # 교체시점 DF
                pitcher_chin_out_cn = df_change_situation.before_out_cn  # 교체시점 아웃카운트
                pitcher_chin_runner_sc = df_change_situation.before_runner_sc  # 교체시점 주자상황
                if pitcher_chin_out_cn > 0 or pitcher_chin_runner_sc > 0:
                    is_chin_situation = True
                if is_chin_situation:
                    pitcher_chin_out_cn_text = str(pitcher_chin_out_cn) if pitcher_chin_out_cn != 0 else '무'
                    runner_sc_dic = {0: '주자가 없는', 1: '1루', 2: '2루', 3: '3루', 12: '1,2루', 13: '1,3루',
                                     23: '2,3루', 123: '만루'}
                    pitcher_chin_runner_sc_text = runner_sc_dic[pitcher_chin_runner_sc]
                    pitcher_chin_situation = '{}사 {} 상황에서'.format(pitcher_chin_out_cn_text,
                                                                  pitcher_chin_runner_sc_text)

            setattr(var, '선수이름', util.get_person_name(self.pcode))
            setattr(var, 'is_QS', is_QS)
            setattr(var, 'is_QSP', is_QSP)
            setattr(var, '포지션', '선발투수' if is_starter else '마무리투수' if is_last_pitcher and is_win else '구원투수')
            setattr(var, 'is_선발', is_starter)
            setattr(var, '이닝', pitcher_INN)
            setattr(var, 'is_5이닝이상', is_5INN)
            setattr(var, '잡은아웃', pitcher_INN2)
            setattr(var, '피안타', pitcher_HIT)
            setattr(var, 'is_피안타', is_HIT)
            setattr(var, '탈삼진', pitcher_KK)
            setattr(var, 'is_탈삼진', is_KK)
            setattr(var, '실점', pitcher_R if is_R else '무')
            setattr(var, 'is_실점', is_R)
            setattr(var, '자책점', pitcher_ER)
            setattr(var, 'is_자책점', is_ER)
            setattr(var, '볼넷', pitcher_BB)
            setattr(var, 'is_볼넷', is_BB)
            setattr(var, '투수팀', util.get_team_name(pitcher_team))
            setattr(var, '상대팀', util.get_team_name(pitcher_vsteam))
            setattr(var, '경기장', stadium)
            setattr(var, 'is_완투', is_shutout)
            setattr(var, '투구수', pitcher_BF)
            setattr(var, 'is_승리투수', is_win_pitcher)
            setattr(var, 'is_홀드', is_hold)
            setattr(var, 'is_패전투수', is_lose_pitcher)
            setattr(var, 'is_세이브투수', is_save_pitcher)
            setattr(var, 'is_마무리', is_last_pitcher)
            setattr(var, 'is_승패', is_win)
            setattr(var, '투수기록', self.get_pitcher_record())
            setattr(var, 'WPA', pitcher_WPA)
            setattr(var, 'is_top_WPA', is_top_WPA)
            setattr(var, 'WPA순위', pitcher_WPA_rank)
            setattr(var, 'is_top_WPA_상황', is_top_WPA_situation)
            setattr(var, 'top_WPA_상황', pitcher_WPA_situation_text)
            setattr(var, '교체이닝', pitcher_chin)
            setattr(var, '교체상황', pitcher_chin_situation)
            setattr(var, 'is_교체상황', is_chin_situation)
            setattr(var, 'is_홈', True if pitcher_TB == 'T' else False)

        except Exception as e:
            LogHelper.instance().e(e, file_name=sys._getframe().f_code.co_filename,
                                   func_name=sys._getframe().f_code.co_name)

        return var

    def get_pitcher_record(self):
        """
        데일리투수기록.투수기록
        :return:
        """

        var = NamedVariable()
        try:
            query_result = g.b_models.Pitcher.objects.filter(gmkey__startswith=self.gyear,
                                                             gmkey__lte=self.gmkey, pcode=self.pcode).values()
            df = pd.DataFrame(query_result)

            pitcher_win_cn = len(df[(df.wls == 'W') & (df.pos == '11')])  # 시즌 승수

            # 시즌 퀄리티스타트수
            pitcher_qs_cn = len(df[(df.inn2 >= 18) & (df.er <= 3) & (df.pos == '11')])

            # 시즌 퀄리티스타트플러스수
            pitcher_qsp_cn = len(df[(df.inn2 >= 21) & (df.er <= 3) & (df.pos == '11')])

            setattr(var, '승수', pitcher_win_cn)
            setattr(var, 'QS수', pitcher_qs_cn)
            setattr(var, 'QSP수', pitcher_qsp_cn)

        except Exception as e:
            LogHelper.instance().e(e, file_name=sys._getframe().f_code.co_filename,
                                   func_name=sys._getframe().f_code.co_name)

        return var


class NamedVariable:
    pass
