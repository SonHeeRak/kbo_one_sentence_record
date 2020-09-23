from article.lib.core.log_helper import LogHelper
from article.lib import util
from article.lib import globals as g
import sys
import pandas as pd


class DailyHitterRecord(object):
    def __init__(self, data_frame=None, gmkey=None, pcode=None):
        self.data_frame = data_frame
        self.gmkey = gmkey
        self.pcode = pcode

    def get_var(self):
        """
        데일리타자기록
        :return:
        """

        var = NamedVariable()
        try:
            df = self.data_frame

            hitter_name = util.get_person_name(self.pcode)

            hitter_turn = df.turn.values.sum()  # 타순
            is_starter = False  # 선발유무
            if hitter_turn[0] == '1':
                is_starter = True
            hitter_turn = hitter_turn[1]

            hitter_HR = df.hr.values.sum()  # 홈런
            is_HR = True  # 홈런유무
            if hitter_HR == 0:
                is_HR = False

            is_multi_position = False  # 멀티포지션 여부
            hitter_multi_position_text = ''
            hitter_position_list = self.get_multi_position(self.gmkey, self.pcode)
            if len(hitter_position_list) == 1:
                hitter_position_name = hitter_position_list[0]  # 포지션이름
            else:
                is_multi_position = True
                hitter_position_name = hitter_position_list[0]
                hitter_multi_position_list = hitter_position_list[1:]
                hitter_multi_position_text = util.list_item_to_separate_text(hitter_multi_position_list)

            hitter_PA = df.pa.values.sum()  # 타석수
            is_PA = False  # 타석여부
            if hitter_PA > 0:
                is_PA = True

            hitter_AB = df.ab.values.sum()  # 타수
            hitter_HIT = df.hit.values.sum()  # 안타
            is_HIT = False  # 안타유무
            if hitter_HIT > 0:
                is_HIT = True

            hitter_H2 = df.h2.values.sum()  # 2루타
            is_H2 = False  # 2루타유무
            if hitter_H2 > 0:
                is_H2 = True

            hitter_H3 = df.h3.values.sum()  # 3루타
            is_H3 = False  # 3루타유무
            if hitter_H3 > 0:
                is_H3 = True

            hitter_RBI = df.rbi.values.sum()  # 타점
            is_RBI = False  # 타점여부
            if hitter_RBI > 0:
                is_RBI = True

            hitter_RUN = df.run.values.sum()  # 득점
            is_RUN = False  # 득점여부
            if hitter_RUN > 0:
                is_RUN = True

            # 볼넷
            hitter_BB = df.bb.values.sum()
            is_BB = True  # 볼넷여부
            if hitter_BB == 0:
                is_BB = False

            # 도루 & 도루성공여부
            hitter_SB = df.sb.values.sum()  # 도루성공
            hitter_CS = df.cs.values.sum()  # 도루실패
            hitter_total_SB = int(hitter_SB) + int(hitter_CS)  # 도루 총개수
            is_SB = False  # 도루성공여부
            if hitter_SB > 0:
                is_SB = True

            hitter_hit_record_list = list()  # 경기장타기록
            if is_H2:
                hitter_hit_record_list.append('2루타 {}개'.format(hitter_H2))
            if is_H3:
                hitter_hit_record_list.append('3루타 {}개'.format(hitter_H3))
            if is_HR:
                hitter_hit_record_list.append('홈런 {}개'.format(hitter_HR))
            hitter_hit_record_text = util.list_item_to_separate_text(hitter_hit_record_list, separator=',')

            is_hitter_hit_record = False  # 경기장타기록 여부
            if len(hitter_hit_record_text) > 0:
                is_hitter_hit_record = True

            hitter_major_record_list = list()  # 경기주요기록
            if is_RBI:
                hitter_major_record_list.append('{}타점'.format(hitter_RBI))
            if is_RUN:
                hitter_major_record_list.append('{}득점'.format(hitter_RUN))
            if is_BB:
                hitter_major_record_list.append('{}볼넷'.format(hitter_BB))
            if is_SB:
                hitter_major_record_list.append('도루 {}번 시도해 {}번 성공'.format(hitter_total_SB, hitter_SB))
            hitter_major_record_text = util.list_item_to_separate_text(hitter_major_record_list)

            is_hitter_major_record = False  # 경기주요기록 여부
            if len(hitter_major_record_text) > 0:
                is_hitter_major_record = True

            hitter_chin = None  # 교체이닝
            is_chin_situation = False  # 교체시점 특이사항 여부
            hitter_chin_situation = ''  # 교체상황
            if not is_starter:
                hitter_chin = util.get_player_chin(self.gmkey, self.pcode)
                df_change_situation = util.get_df_change_situation('hitter', self.gmkey, self.pcode)  # 교체시점 DF
                if df_change_situation is not None:
                    hitter_chin_out_cn = df_change_situation.before_out_cn  # 교체시점 아웃카운트
                    hitter_chin_runner_sc = df_change_situation.before_runner_sc  # 교체시점 주자상황
                    if hitter_chin_out_cn > 0 or hitter_chin_runner_sc > 0:
                        is_chin_situation = True
                    if is_chin_situation:
                        hitter_chin_out_cn_text = str(hitter_chin_out_cn) if hitter_chin_out_cn != 0 else '무'
                        runner_sc_dic = {0: '주자가 없는', 1: '1루', 2: '2루', 3: '3루', 12: '1,2루', 13: '1,3루',
                                         23: '2,3루', 123: '만루'}
                        hitter_chin_runner_sc_text = runner_sc_dic[hitter_chin_runner_sc]
                        hitter_chin_situation = '{}사 {} 상황에서'.format(hitter_chin_out_cn_text,
                                                                     hitter_chin_runner_sc_text)

            # 타자팀, 상대팀 구분
            hitter_TB = df.tb.values.sum()
            if hitter_TB == 'T':
                hitter_team = self.gmkey[-5:-3]
                hitter_vsteam = self.gmkey[-3:-1]
            else:
                hitter_team = self.gmkey[-3:-1]
                hitter_vsteam = self.gmkey[-5:-3]

            hitter_team_score, hitter_vsteam_score = util.get_score(self.gmkey, hitter_team)  # 타자팀점수, 상대팀점수
            is_win = False  # 승여부
            if hitter_team_score > hitter_vsteam_score:
                is_win = True
            elif hitter_team_score == hitter_vsteam_score:
                is_win = 0

            stadium = util.get_stadium(self.gmkey)  # 경기장

            is_top_WPA = False  # WPA 상위여부
            hitter_WPA = None  # 승리확률기여도
            hitter_WPA_rank = None  # WPA 랭킹
            if self.pcode in util.get_wpa_daily_rank('hitter', self.gmkey).bat_p_id.tolist():
                is_top_WPA = True
                temp_df = util.get_wpa_daily_rank('hitter', self.gmkey)
                hitter_WPA = temp_df[temp_df.bat_p_id == self.pcode].wpa_rt.values.sum()
                hitter_WPA = str(round(hitter_WPA * 100, 1))
                hitter_WPA_rank = temp_df[temp_df.bat_p_id == self.pcode].index.values.sum() + 1

            is_top_WPA_situation = False  # WPA 상황 상위여부
            hitter_WPA_situation_list = list()  # WPA 상황 기록
            hitter_WPA_situation_text = ''  # WPA 상황 기록
            df_wpa_situation = util.get_top_wpa_situation('hitter', self.gmkey)
            if self.pcode in df_wpa_situation.bat_p_id.tolist():
                is_top_WPA_situation = True
                temp_df = df_wpa_situation[df_wpa_situation.bat_p_id == self.pcode]
                for i, row in temp_df.iterrows():
                    temp_list = list()
                    inn_no = row.inn_no
                    tb = '말' if row.tb_sc == 'B' else '초'
                    before_away_score = row.before_away_score_cn
                    before_score_gap = row.before_score_gap_cn * -1 if tb == '초' else row.before_score_gap_cn
                    livetext = row.livetext_if.split(':')[1].split('\r')[0].split('(')[0].strip()
                    temp_list.append('{}회{}'.format(inn_no, tb))
                    if before_score_gap > 0:
                        temp_list.append('{}점 이기고 있는 상황에서'.format(abs(before_score_gap)))
                    elif before_score_gap < 0:
                        temp_list.append('{}점 지고 있는 상황에서'.format(abs(before_score_gap)))
                    elif inn_no < 5:
                        temp_list.append('{}대{}의 상황에서'.format(before_away_score, before_away_score))
                    else:
                        temp_list.append('{}대{} 팽팽한 상황에서'.format(before_away_score, before_away_score))

                    temp_list.append('{}'.format(livetext))
                    hitter_WPA_situation_list.append(util.list_item_to_separate_text(temp_list))
                hitter_WPA_situation_text = util.list_item_to_separate_text(hitter_WPA_situation_list, separator=',')

            setattr(var, 'is_선발', is_starter)
            setattr(var, '선수이름', hitter_name)
            setattr(var, '포지션이름', hitter_position_name)
            setattr(var, '타순', hitter_turn)
            setattr(var, '타석수', hitter_PA)
            setattr(var, 'is_타석', is_PA)
            setattr(var, '타수', hitter_AB)
            setattr(var, '안타수', hitter_HIT if hitter_HIT != 0 else '무')
            setattr(var, 'WPA', hitter_WPA)
            setattr(var, 'is_top_WPA', is_top_WPA)
            setattr(var, 'WPA순위', hitter_WPA_rank)
            setattr(var, '경기장타기록', hitter_hit_record_text)
            setattr(var, 'is_경기장타기록', is_hitter_hit_record)
            setattr(var, '경기주요기록', hitter_major_record_text)
            setattr(var, 'is_경기주요기록', is_hitter_major_record)
            setattr(var, '타자팀', util.get_team_name(hitter_team))
            setattr(var, '상대팀', util.get_team_name(hitter_vsteam))
            setattr(var, 'is_타자팀승리', is_win)
            setattr(var, '경기장', stadium)
            setattr(var, '교체이닝', hitter_chin)
            setattr(var, '교체상황', hitter_chin_situation)
            setattr(var, 'is_교체상황', is_chin_situation)
            setattr(var, 'is_홈', True if hitter_TB == 'T' else False)
            setattr(var, 'is_top_WPA_상황', is_top_WPA_situation)
            setattr(var, 'top_WPA_상황', hitter_WPA_situation_text)
            setattr(var, 'is_멀티포지션', is_multi_position)
            setattr(var, '멀티포지션', hitter_multi_position_text)

        except Exception as e:
            LogHelper.instance().e(e, file_name=sys._getframe().f_code.co_filename,
                                   func_name=sys._getframe().f_code.co_name)

        return var

    @staticmethod
    def get_multi_position(gmkey, pcode):
        """
        멀티포지션
        :return:
        """
        position_dict = {'1': '투수', '2': '포수', '3': '1루수', '4': '2루수', '5': '3루수', '6': '유격수',
                         '7': '좌익수', '8': '중견수', '9': '우익수', 'D': '지명타자', 'H': '대타', 'R': '대주자'}

        '''
        position_list = list()
        query_result = g.b_models.Entry.objects.filter(gmkey=gmkey, pcode=pcode).values()
        if query_result:
            df = pd.DataFrame(query_result)
            for i, row in df.iterrows():
                position_list.append(position_dict[row['posi'][-1]])
        '''
        position_list = list()
        df_entry_player = util.get_cache_df_entry_player(gmkey, pcode)
        if df_entry_player is not None and len(df_entry_player) > 0:
            for i, row in df_entry_player.iterrows():
                position_list.append(position_dict[row['posi'][-1]])

        return position_list


class NamedVariable:
    pass
