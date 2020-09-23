import random
import sys
import time
from article.lib import util
from article import baseball_models as b_models
from article import daily_news_models as d_models
from article.lib.core.log_helper import LogHelper

import pandas as pd


IS_INITIALIZE = None
MODEL_DICT = dict()
DYNAMIC_MODEL_DICT = dict()
DF_GROUP_DICT = dict()
VARIABLE_DICT = dict()
DF_PERSON = None
daily_news_method = None


def initialize():
        try:
            global IS_INITIALIZE
            global MODEL_DICT
            global DYNAMIC_MODEL_DICT

            global DF_GROUP_DICT
            global VARIABLE_DICT
            global DF_PERSON

            global daily_news_method

            if IS_INITIALIZE is None or IS_INITIALIZE is not True:
                start_time = time.time()
                # region Clear Values
                MODEL_DICT = dict()
                DYNAMIC_MODEL_DICT = dict()
                DF_GROUP_DICT = dict()
                VARIABLE_DICT = dict()
                daily_news_method = None

                MODEL_DICT = {
                    'method_info': d_models.MethodInfo,
                    'base_template': d_models.BaseTemplate,
                    'hitter_record_sentence': d_models.HitterRecordSentence,
                    'pitcher_record_sentence': d_models.PitcherRecordSentence,
                    'pitcher_season_record_sentence': d_models.PitcherSeasonRecordSentence,
                    'hitter_season_record_sentence': d_models.HitterSeasonRecordSentence,
                    'team_record_sentence': d_models.TeamRecordSentence,
                }
                DYNAMIC_MODEL_DICT = {
                    'common_dynamic_variable': d_models.CommonDynamicVariable,
                }

                for (name, model) in DYNAMIC_MODEL_DICT.items():
                    VARIABLE_DICT[name] = init_dynamic_variable(model)

                method_obj = d_models.MethodInfo.objects

                daily_news_method = get_dict_method(method_obj.filter(name__exact='daily_news'))

                DF_PERSON = pd.DataFrame(b_models.Person.objects.filter().values())

                LogHelper.instance().d('globals initialize')

                end_time = time.time()
                print('초기화 걸리는 시간 :', end_time-start_time)
                IS_INITIALIZE = True
            else:
                print('>>>>>>>>>> 초기화 완료 상태')

        except Exception as e:
            LogHelper.instance().e(e, file_name=sys._getframe().f_code.co_filename,
                                   func_name=sys._getframe().f_code.co_name)



def init_dynamic_variable(model):
    df_dynamic_group = pd.DataFrame(list(model.objects.values())).groupby(['group', 'name', 'rank'])

    var_dict = dict()
    for d in df_dynamic_group:
        var_name = d[0][1]  # name key
        var_list = d[1].to_dict('record')  # data value list

        selected_var_dict = random.choice(var_list)
        if selected_var_dict['use'] == 'F':
            continue

        if var_name in var_dict:
            var_dict[var_name].append(selected_var_dict)
        else:
            var_dict[var_name] = [selected_var_dict]

    return var_dict


def get_dict_method(object_value):
    return {row['kor']: row['method'] for row in iter(object_value.values())}


def define_method(obj, method_dict):
    for k, v in method_dict.items():
        setattr(obj, k, getattr(obj, v))


def get_random_sentence(text):
    temp_list = [d.strip() for d in text.split('@') if d]  # 공백제거
    if not temp_list:
        temp_list.append('')
    return random.choice(temp_list)

