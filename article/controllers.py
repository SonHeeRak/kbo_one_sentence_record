import time
import pandas as pd
from article.lib import util
from article.lib import globals as g
from article.lib.classes.daily_news import DailyNewsVariable
from article.lib.core.log_helper import LogHelper
from article.lib.sentence_template import DailyNewsTemplate


class DailyNews(object):
    def __init__(self, gmkey, player_type=None, pcode=None):
        g.initialize()

        self.gmkey = gmkey
        if player_type is not None:
            self.pcode = pcode
            if player_type == 'player':
                #queryset = g.b_models.Entry.objects.filter(gmkey=self.gmkey, pcode=self.pcode)
                #entry = pd.DataFrame(queryset.values())
                df_entry = util.get_cache_df_entry(gmkey)

                #if entry.iloc[-1].posi[-1] == '1':
                if df_entry[df_entry.pcode == self.pcode].iloc[-1].posi[-1] == '1':
                    self.player_type = 'pitcher'
                else:
                    self.player_type = 'hitter'
            else:
                self.player_type = player_type

        self.Hteam_code = gmkey[-3:-1]
        self.Ateam_code = gmkey[-5:-3]
        self.daily_news_var = None
        self.template_sentence = None

        self.hitter_df = util.get_hitter_in_gmkey(gmkey)
        self.pitcher_df = util.get_pitcher_in_gmkey(gmkey)

    def generate_hitter_daily_news(self):
        try:
            start = time.time()

            result_sentence = dict()
            Hteam_dict = {'team_code': self.Hteam_code,
                          'team_name': util.get_team_name(self.Hteam_code),
                          'season': self.hitter_df.iloc[0].gday[0:4]}
            Ateam_dict = {'team_code': self.Ateam_code,
                          'team_name': util.get_team_name(self.Ateam_code),
                          'season': self.hitter_df.iloc[0].gday[0:4]}

            # 타자별 기록
            Hteam_hitter_sentence_list = list()
            Ateam_hitter_sentence_list = list()

            hitter_pcode_list = [] if self.hitter_df is None else self.hitter_df.pcode.values.tolist()
            for pcode in hitter_pcode_list:
                hitter_sentence_dict = dict()
                if self.hitter_df[self.hitter_df.pcode == pcode].tb.values[0] == 'B':
                    self.daily_news_var = DailyNewsVariable(gmkey=self.gmkey, pcode=pcode, player_type=self.player_type)

                    template_sentence = DailyNewsTemplate(self.daily_news_var)
                    sentence_list = template_sentence.set_sentence()
                    sentence = ' '.join(sentence_list)

                    hitter_sentence_dict['pcode'] = pcode
                    hitter_sentence_dict['name'] = util.get_person_name(pcode)
                    hitter_sentence_dict['back_num'] = util.get_person_back_number(pcode)
                    hitter_sentence_dict['sentence_list'] = sentence_list
                    hitter_sentence_dict['sentence'] = sentence
                    Hteam_hitter_sentence_list.append(hitter_sentence_dict)
                else:
                    self.daily_news_var = DailyNewsVariable(gmkey=self.gmkey, pcode=pcode, player_type=self.player_type)

                    template_sentence = DailyNewsTemplate(self.daily_news_var)
                    sentence_list = template_sentence.set_sentence()
                    sentence = ' '.join(sentence_list)

                    hitter_sentence_dict['pcode'] = pcode
                    hitter_sentence_dict['name'] = util.get_person_name(pcode)
                    hitter_sentence_dict['back_num'] = util.get_person_back_number(pcode)
                    hitter_sentence_dict['sentence_list'] = sentence_list
                    hitter_sentence_dict['sentence'] = sentence
                    Ateam_hitter_sentence_list.append(hitter_sentence_dict)

            Hteam_dict['hitter_list'] = Hteam_hitter_sentence_list
            Ateam_dict['hitter_list'] = Ateam_hitter_sentence_list

            result_sentence['Hteam'] = Hteam_dict
            result_sentence['Ateam'] = Ateam_dict

            result = {
                'result_cd': 100,
                'result_msg': '성공',
                'game_key': self.gmkey,
                'result_sentence': result_sentence,
            }

            end = time.time()
            LogHelper.instance().d(end - start)

        except Exception as e:
            result = {
                'result_cd': 200,
                'result_msg': '실패',
                'contents': e,
            }

        return result

    def generate_pitcher_daily_news(self):
        try:
            start = time.time()

            result_sentence = dict()
            Hteam_dict = {'team_code': self.Hteam_code,
                          'team_name': util.get_team_name(self.Hteam_code),
                          'season': self.pitcher_df.iloc[0].gday[0:4]}
            Ateam_dict = {'team_code': self.Ateam_code,
                          'team_name': util.get_team_name(self.Ateam_code),
                          'season': self.pitcher_df.iloc[0].gday[0:4]}

            # 투수별 기록
            Hteam_pitcher_sentence_list = list()
            Ateam_pitcher_sentence_list = list()

            pitcher_pcode_list = [] if self.pitcher_df is None else self.pitcher_df.pcode.values.tolist()
            for pcode in pitcher_pcode_list:
                pitcher_sentence_dict = dict()
                if self.pitcher_df[self.pitcher_df.pcode == pcode].tb.values[0] == 'B':
                    self.daily_news_var = DailyNewsVariable(gmkey=self.gmkey, pcode=pcode, player_type=self.player_type)

                    template_sentence = DailyNewsTemplate(self.daily_news_var)
                    sentence_list = template_sentence.set_sentence()
                    sentence = ' '.join(sentence_list)

                    pitcher_sentence_dict['pcode'] = pcode
                    pitcher_sentence_dict['name'] = util.get_person_name(pcode)
                    pitcher_sentence_dict['back_num'] = util.get_person_back_number(pcode)
                    pitcher_sentence_dict['sentence_list'] = sentence_list
                    pitcher_sentence_dict['sentence'] = sentence
                    Hteam_pitcher_sentence_list.append(pitcher_sentence_dict)
                else:
                    self.daily_news_var = DailyNewsVariable(gmkey=self.gmkey, pcode=pcode, player_type=self.player_type)

                    template_sentence = DailyNewsTemplate(self.daily_news_var)
                    sentence_list = template_sentence.set_sentence()
                    sentence = ' '.join(sentence_list)

                    pitcher_sentence_dict['pcode'] = pcode
                    pitcher_sentence_dict['name'] = util.get_person_name(pcode)
                    pitcher_sentence_dict['back_num'] = util.get_person_back_number(pcode)
                    pitcher_sentence_dict['sentence_list'] = sentence_list
                    pitcher_sentence_dict['sentence'] = sentence
                    Ateam_pitcher_sentence_list.append(pitcher_sentence_dict)

            Hteam_dict['pitcher_list'] = Hteam_pitcher_sentence_list
            Ateam_dict['pitcher_list'] = Ateam_pitcher_sentence_list

            result_sentence['Hteam'] = Hteam_dict
            result_sentence['Ateam'] = Ateam_dict

            result = {
                'result_cd': 100,
                'result_msg': '성공',
                'game_key': self.gmkey,
                'result_sentence': result_sentence,
            }

            end = time.time()
            LogHelper.instance().d(end - start)

        except Exception as e:
            result = {
                'result_cd': 200,
                'result_msg': '실패',
                'contents': e,
            }

        return result

    def generate_team_daily_news(self):
        try:
            start = time.time()

            # 팀별 기록
            self.daily_news_var = DailyNewsVariable(gmkey=self.gmkey, player_type=self.player_type)

            template_sentence = DailyNewsTemplate(self.daily_news_var)
            sentence_list = template_sentence.set_sentence()
            sentence = ' '.join(sentence_list)

            result = {
                'result_cd': 100,
                'result_msg': '성공',
                'game_key': self.gmkey,
                'Hteam_code': self.Hteam_code,
                'Hteam_name': util.get_team_name(self.Hteam_code),
                'Ateam_code': self.Ateam_code,
                'Ateam_name': util.get_team_name(self.Ateam_code),
                'season': self.hitter_df.iloc[0].gday[0:4],
                'sentence': sentence,
            }

            end = time.time()
            LogHelper.instance().d(end - start)

        except Exception as e:
            result = {
                'result_cd': 200,
                'result_msg': '실패',
                'contents': e,
            }

        return result

    def generate_player_daily_news(self):
        try:
            start = time.time()

            # 팀별 기록
            self.daily_news_var = DailyNewsVariable(gmkey=self.gmkey, pcode=self.pcode, player_type=self.player_type)

            template_sentence = DailyNewsTemplate(self.daily_news_var)
            sentence_list = template_sentence.set_sentence()
            sentence = ' '.join(sentence_list)

            result = {
                'result_cd': 100,
                'result_msg': '성공',
                'game_key': self.gmkey,
                'Hteam_code': self.Hteam_code,
                'Hteam_name': util.get_team_name(self.Hteam_code),
                'Ateam_code': self.Ateam_code,
                'Ateam_name': util.get_team_name(self.Ateam_code),
                'season': self.hitter_df.iloc[0].gday[0:4],
                'sentence': sentence,
            }

            end = time.time()
            LogHelper.instance().d(end - start)

        except Exception as e:
            result = {
                'result_cd': 200,
                'result_msg': '실패',
                'contents': e,
            }

        return result

    def get_player_list(self):
        try:

            def add_list_person_info(row, append_list):
                dict_person = {
                    'pcode': row['pcode'],
                    'pname': util.get_person_name(row['pcode']),
                    'back_no': util.get_person_back_number(row['pcode'])
                }
                append_list.append(dict_person)

            away_pitcher_list = []
            home_pitcher_list = []
            away_hitter_list = []
            home_hitter_list = []

            for i, row in self.pitcher_df.iterrows():
                if row['tb'] == 'T':
                    add_list_person_info(row, away_pitcher_list)
                else:
                    add_list_person_info(row, home_pitcher_list)

            for i, row in self.hitter_df.iterrows():
                if row['tb'] == 'T':
                    add_list_person_info(row, away_hitter_list)
                else:
                    add_list_person_info(row, home_hitter_list)

            result = {
                'result_cd': 100,
                'result_msg': '성공',
                'game_key': self.gmkey,
                'Hteam_code': self.Hteam_code,
                'Hteam_name': util.get_team_name(self.Hteam_code),
                'Ateam_code': self.Ateam_code,
                'Ateam_name': util.get_team_name(self.Ateam_code),
                'season': self.hitter_df.iloc[0].gday[0:4],
                'away_pitcher_list': away_pitcher_list,
                'away_hitter_list': away_hitter_list,
                'home_pitcher_list': home_pitcher_list,
                'home_hitter_list': home_hitter_list,
            }
        except Exception as e:
            result = {
                'result_cd': 200,
                'result_msg': '실패',
                'contents': e,
            }

        return result
