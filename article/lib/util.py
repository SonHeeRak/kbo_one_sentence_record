from article.lib import globals as g
from datetime import datetime
import pandas as pd
from django.core.cache import cache
from article import baseball_models as b_models


def get_cache_df_entry(gmkey):
    cache_key = 'get_cache_df_entry_{gmkey}'.format(gmkey=gmkey)
    df_entry = cache.get(cache_key, None)
    if df_entry is None:
        queryset = g.b_models.Entry.objects.filter(gmkey=gmkey)
        df_entry = pd.DataFrame(queryset.values())
        cache.set(cache_key, df_entry, 60 * 10)

    return df_entry


def get_cache_df_entry_player(gmkey, pcode):
    cache_key = 'get_cache_df_entry_player_{gmkey}_{pcode}'.format(gmkey=gmkey, pcode=pcode)
    df_entry_player = cache.get(cache_key, None)
    if df_entry_player is None:
        df_entry = get_cache_df_entry(gmkey)
        if len(df_entry[df_entry.pcode == pcode]) > 0:
            df_entry_player = df_entry[df_entry.pcode == pcode]
            cache.set(cache_key, df_entry_player, 60 * 10)

    return df_entry_player


def get_person_name(person_code):
    '''
    result_name = ''
    query_result = g.b_models.Person.objects.filter(pcode=person_code).values()
    if query_result:
        query_result = query_result[0]
        result_name = query_result['name']
    '''
    result_name = ''
    temp = g.DF_PERSON[g.DF_PERSON.pcode == person_code]
    if len(temp) > 0:
        result_name = temp.iloc[0]['name']
    return result_name


def get_person_back_number(person_code):
    '''
    person_back_number = ''
    query_result = g.b_models.Person.objects.filter(pcode=person_code).values()
    if query_result:
        query_result = query_result[0]
        person_back_number = query_result['backnum']
    '''
    person_back_number = ''
    temp = g.DF_PERSON[g.DF_PERSON.pcode == person_code]
    if len(temp) > 0:
        person_back_number = temp.iloc[0]['backnum']
    return person_back_number


def get_score(gmkey, team):
    team_point = ''
    vsteam_point = ''
    query_result = g.b_models.Score.objects.filter(gmkey=gmkey).values()
    if query_result:
        query_result = query_result[0]
        if team == gmkey[-5:-3]:
            team_point = query_result['tpoint']
            vsteam_point = query_result['bpoint']
        else:
            team_point = query_result['bpoint']
            vsteam_point = query_result['tpoint']

    return team_point, vsteam_point


def get_stadium(gmkey):
    stadium_dic = {'창원': '창원 NC파크', '대구': '대구 삼성라이온즈파크', '고척': '고척 스카이돔',
                   '광주': '광주 기아챔피언스필드', '문학': '인천 SK행복드림구장', '수원': '수원 KT위즈파크',
                   '사직': '부산 사직야구장', '잠실': '잠실야구장', '대전': '대전 한화생명이글스파크',
                   '챔피언스 필드': '광주 기아챔피언스필드', '마산': '마산야구장', '울산': '울산 문수야구장',
                   '청주': '청주야구장', '포항': '포항야구장', '스카이돔': '고척 스카이돔',
                   '라이온즈 파크': '대구 삼성라이온즈파크', '문수': '울산 문수야구장'}
    stadium = ''
    query_result = g.b_models.Gameinfo.objects.filter(gmkey=gmkey).values()
    if query_result:
        query_result = query_result[0]
        stadium = query_result['stadium']

    return stadium_dic[stadium]


def get_finish(gmkey):
    is_finish = False
    team = ''
    vs_team = ''
    hitter = ''
    inn = 0
    how = ''
    query_result = g.b_models.GoodbyeRecord.objects.filter(g_id=gmkey).values()
    if query_result:
        query_result = query_result[0]
        is_finish = True
        team = query_result['t_cd']
        vs_team = query_result['opp_t_cd']
        hitter = query_result['bat_p_id']
        inn = query_result['inn_no']
        how = query_result['how_id']

    return is_finish, team, vs_team, hitter, inn, how


def get_team_name(team):
    team_name = ''
    team_name_dic = {'HH': '한화', 'HT': 'KIA', 'KT': 'KT', 'LG': 'LG', 'NC': 'NC',
                     'OB': '두산', 'SK': 'SK', 'SS': '삼성', 'WO': '키움', 'LT': '롯데'}
    if team in team_name_dic.keys():
        team_name = team_name_dic[team]

    return team_name


def get_hitter_in_gmkey(gmkey):
    hitter_df = None
    query_result = g.b_models.Hitter.objects.filter(gmkey=gmkey).exclude(name='합계').order_by('-tb', 'turn').values()
    if query_result:
        df_query_result = pd.DataFrame(query_result)
        hitter_df = df_query_result[['gday', 'tb', 'name', 'pcode', 'turn']]

    return hitter_df


def get_pitcher_in_gmkey(gmkey):
    pitcher_df = None
    query_result = g.b_models.Pitcher.objects.filter(gmkey=gmkey).exclude(name='합계').order_by('tb', 'pos').values()
    if query_result:
        df_query_result = pd.DataFrame(query_result)
        pitcher_df = df_query_result[['gday', 'tb', 'name', 'pcode', 'pos']]

    return pitcher_df


def get_player_chin(gmkey, pcode):
    player_chin = None

    df_entry_player = get_cache_df_entry_player(gmkey, pcode)
    if df_entry_player is not None and len(df_entry_player) > 0:
        player_chin = df_entry_player.iloc[0].chin

    return player_chin


def get_df_change_situation(player_type, gmkey, pcode):
    df_player_change_situation = None
    if player_type == 'pitcher':
        query_result = g.b_models.IeRecordMatrixMix.objects.filter(gameid=gmkey, pit_p_id=pcode).values()
    elif player_type == 'hitter':
        query_result = g.b_models.IeRecordMatrixMix.objects.filter(gameid=gmkey, bat_p_id=pcode).values()
    if query_result:
        df_player_change_situation = pd.DataFrame(query_result).iloc[0]

    return df_player_change_situation


def get_season_start_date(gmkey):
    cache_key = 'get_season_start_date_{gmkey}'.format(gmkey=gmkey)
    date = cache.get(cache_key, None)
    if date is None:
        query_result = g.b_models.Dailyrank.objects.filter(gday__gte=str(gmkey[0:4])+'0000').values()[0]
        if query_result:
            date = query_result['gday']
            cache.set(cache_key, date, 60 * 10)

    return date


def get_wpa_season_rank(player_type, gmkey):
    cache_key = 'get_wpa_season_rank_{player_type}_{gmkey}'.format(player_type=player_type, gmkey=gmkey)
    df_wpa_rank = cache.get(cache_key, None)
    if df_wpa_rank is None:
        if player_type == 'pitcher':
            season_start_date = datetime.strptime(get_season_start_date(gmkey), '%Y%m%d')
            query_result = g.b_models.IeRecordMatrixMix.objects.filter(reg_dt__gte=season_start_date,
                                                                       gameid__lte=gmkey).values()
            if query_result:
                df_wpa_rank = pd.DataFrame(query_result)
                df_wpa_rank['wpa_rt'] = df_wpa_rank.wpa_rt.apply(lambda x: x * -1)
                df_wpa_rank = df_wpa_rank.groupby('pit_p_id', as_index=False).wpa_rt.sum().\
                    sort_values('wpa_rt', ascending=False).reset_index(drop=True).head()
                df_wpa_rank = df_wpa_rank.astype({'pit_p_id': str})
                cache.set(cache_key, df_wpa_rank, 60 * 10)

        elif player_type == 'hitter':
            season_start_date = datetime.strptime(get_season_start_date(gmkey), '%Y%m%d')
            query_result = g.b_models.IeRecordMatrixMix.objects.filter(reg_dt__gte=season_start_date,
                                                                       gameid__lte=gmkey).values()

            if query_result:
                df_wpa_rank = pd.DataFrame(query_result)
                bat_wpa_rt = df_wpa_rank[df_wpa_rank.run_p_id == 0]
                run_wpa_rt = df_wpa_rank[df_wpa_rank.run_p_id != 0].rename(columns={'run_p_id': 'bat_p_id',
                                                                                    'bat_p_id': 'run_p_id'})
                df_wpa_rank = pd.concat([bat_wpa_rt, run_wpa_rt])
                df_wpa_rank = df_wpa_rank.groupby('bat_p_id', as_index=False).wpa_rt.sum().\
                    sort_values('wpa_rt', ascending=False).reset_index(drop=True).head()
                df_wpa_rank = df_wpa_rank.astype({'bat_p_id': str})
                cache.set(cache_key, df_wpa_rank, 60 * 10)

    return df_wpa_rank


def get_top_wpa_situation(player_type, gmkey):
    cache_key = 'get_top_wpa_situation_{player_type}_{gmkey}'.format(player_type=player_type, gmkey=gmkey)
    df_wpa_situation = cache.get(cache_key, None)

    if df_wpa_situation is None:
        if player_type == 'pitcher':
            query_result = g.b_models.IeRecordMatrixMix.objects.filter(gameid=gmkey).values()

            if query_result:
                df_wpa_situation = pd.DataFrame(query_result)
                df_wpa_situation['wpa_rt'] = df_wpa_situation.wpa_rt.apply(lambda x: x * -1)
                df_wpa_situation = df_wpa_situation.sort_values('wpa_rt', ascending=False).reset_index(drop=True).head()
                df_wpa_situation = df_wpa_situation.astype({'pit_p_id': str})
                cache.set(cache_key, df_wpa_situation, 60 * 10)

        elif player_type == 'hitter':
            query_result = g.b_models.IeRecordMatrixMix.objects.filter(gameid=gmkey).values()

            if query_result:
                df_wpa_situation = pd.DataFrame(query_result)
                df_wpa_situation = df_wpa_situation.sort_values('wpa_rt', ascending=False).reset_index(drop=True).head()
                df_wpa_situation = df_wpa_situation.astype({'bat_p_id': str})
                cache.set(cache_key, df_wpa_situation, 60 * 10)

    return df_wpa_situation


def get_wpa_daily_rank(player_type, gmkey):
    df_wpa_rank = None
    if player_type == 'pitcher':
        query_result = g.b_models.IeRecordMatrixMix.objects.filter(gameid=gmkey).values()
        if query_result:
            df_wpa_rank = pd.DataFrame(query_result)
            df_wpa_rank['wpa_rt'] = df_wpa_rank.wpa_rt.apply(lambda x: x * -1)
            df_wpa_rank = df_wpa_rank.groupby('pit_p_id', as_index=False).wpa_rt.sum().\
                sort_values('wpa_rt', ascending=False).reset_index(drop=True).head()
            df_wpa_rank = df_wpa_rank.astype({'pit_p_id': str})

    elif player_type == 'hitter':
        query_result = g.b_models.IeRecordMatrixMix.objects.filter(gameid=gmkey).values()
        if query_result:
            df_wpa_rank = pd.DataFrame(query_result)
            bat_wpa_rt = df_wpa_rank[df_wpa_rank.run_p_id == 0]
            run_wpa_rt = df_wpa_rank[df_wpa_rank.run_p_id != 0].rename(columns={'run_p_id': 'bat_p_id',
                                                                                'bat_p_id': 'run_p_id'})
            df_wpa_rank = pd.concat([bat_wpa_rt, run_wpa_rt])
            df_wpa_rank = df_wpa_rank.groupby('bat_p_id', as_index=False).wpa_rt.sum().\
                sort_values('wpa_rt', ascending=False).reset_index(drop=True).head()
            df_wpa_rank = df_wpa_rank.astype({'bat_p_id': str})

    return df_wpa_rank


def list_item_to_separate_text(items, separator=None):
    ret = ''
    if separator is None:
        separator = ''

    for value in items:
        ret += '{}{} '.format(value, separator)

    if len(ret) > 0:
        ret = ret.rstrip()
        ret = last_char_dump(ret)

    return ret


def last_char_dump(str_val):
    if str_val is not None and len(str_val) > 0 and (str_val[-1] == ',' or str_val[-1] == '와'):
        return str_val[:len(str_val) - 1]
    else:
        return str_val


