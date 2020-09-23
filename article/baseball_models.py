# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BallInfo(models.Model):
    p_se = models.IntegerField(db_column='P_SE', primary_key=True)  # Field name made lowercase.
    g_id = models.CharField(db_column='G_ID', max_length=13)  # Field name made lowercase.
    seq_no = models.IntegerField(db_column='SEQ_NO')  # Field name made lowercase.
    season_id = models.SmallIntegerField(db_column='SEASON_ID')  # Field name made lowercase.
    inn_no = models.IntegerField(db_column='INN_NO')  # Field name made lowercase.
    bat_around_no = models.IntegerField(db_column='BAT_AROUND_NO')  # Field name made lowercase.
    t_id = models.CharField(db_column='T_ID', max_length=2)  # Field name made lowercase.
    tb_sc = models.CharField(db_column='TB_SC', max_length=1)  # Field name made lowercase.
    bat_p_id = models.IntegerField(db_column='BAT_P_ID')  # Field name made lowercase.
    bat_turn_no = models.IntegerField(db_column='BAT_TURN_NO')  # Field name made lowercase.
    bat_order_no = models.IntegerField(db_column='BAT_ORDER_NO')  # Field name made lowercase.
    bat_direc_sc = models.CharField(db_column='BAT_DIREC_SC', max_length=1)  # Field name made lowercase.
    pit_p_id = models.IntegerField(db_column='PIT_P_ID')  # Field name made lowercase.
    pit_course_sc = models.CharField(db_column='PIT_COURSE_SC', max_length=1, blank=True, null=True)  # Field name made lowercase.
    pit_course_no = models.SmallIntegerField(db_column='PIT_COURSE_NO', blank=True, null=True)  # Field name made lowercase.
    pit_course_x_va = models.SmallIntegerField(db_column='PIT_COURSE_X_VA', blank=True, null=True)  # Field name made lowercase.
    pit_course_y_va = models.SmallIntegerField(db_column='PIT_COURSE_Y_VA', blank=True, null=True)  # Field name made lowercase.
    pit_kind_cd = models.IntegerField(db_column='PIT_KIND_CD', blank=True, null=True)  # Field name made lowercase.
    pit_speed_va = models.SmallIntegerField(db_column='PIT_SPEED_VA', blank=True, null=True)  # Field name made lowercase.
    pit_result_sc = models.CharField(db_column='PIT_RESULT_SC', max_length=1, blank=True, null=True)  # Field name made lowercase.
    pit_zone_sc = models.CharField(db_column='PIT_ZONE_SC', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cat_p_id = models.IntegerField(db_column='CAT_P_ID')  # Field name made lowercase.
    run_p_id = models.IntegerField(db_column='RUN_P_ID', blank=True, null=True)  # Field name made lowercase.
    run_bat_turn_no = models.IntegerField(db_column='RUN_BAT_TURN_NO', blank=True, null=True)  # Field name made lowercase.
    run_bat_order_no = models.IntegerField(db_column='RUN_BAT_ORDER_NO', blank=True, null=True)  # Field name made lowercase.
    how_id = models.CharField(db_column='HOW_ID', max_length=2, blank=True, null=True)  # Field name made lowercase.
    field_if = models.CharField(db_column='FIELD_IF', max_length=20, blank=True, null=True)  # Field name made lowercase.
    place_sc = models.CharField(db_column='PLACE_SC', max_length=1, blank=True, null=True)  # Field name made lowercase.
    before_strike_cn = models.IntegerField(db_column='BEFORE_STRIKE_CN')  # Field name made lowercase.
    before_ball_cn = models.IntegerField(db_column='BEFORE_BALL_CN')  # Field name made lowercase.
    before_b1_bat_turn_no = models.IntegerField(db_column='BEFORE_B1_BAT_TURN_NO', blank=True, null=True)  # Field name made lowercase.
    before_b1_bat_order_no = models.IntegerField(db_column='BEFORE_B1_BAT_ORDER_NO', blank=True, null=True)  # Field name made lowercase.
    before_b2_bat_turn_no = models.IntegerField(db_column='BEFORE_B2_BAT_TURN_NO', blank=True, null=True)  # Field name made lowercase.
    before_b2_bat_order_no = models.IntegerField(db_column='BEFORE_B2_BAT_ORDER_NO', blank=True, null=True)  # Field name made lowercase.
    before_b3_bat_turn_no = models.IntegerField(db_column='BEFORE_B3_BAT_TURN_NO', blank=True, null=True)  # Field name made lowercase.
    before_b3_bat_order_no = models.IntegerField(db_column='BEFORE_B3_BAT_ORDER_NO', blank=True, null=True)  # Field name made lowercase.
    after_strike_cn = models.IntegerField(db_column='AFTER_STRIKE_CN')  # Field name made lowercase.
    after_ball_cn = models.IntegerField(db_column='AFTER_BALL_CN')  # Field name made lowercase.
    after_b1_bat_turn_no = models.IntegerField(db_column='AFTER_B1_BAT_TURN_NO', blank=True, null=True)  # Field name made lowercase.
    after_b1_bat_order_no = models.IntegerField(db_column='AFTER_B1_BAT_ORDER_NO', blank=True, null=True)  # Field name made lowercase.
    after_b2_bat_turn_no = models.IntegerField(db_column='AFTER_B2_BAT_TURN_NO', blank=True, null=True)  # Field name made lowercase.
    after_b2_bat_order_no = models.IntegerField(db_column='AFTER_B2_BAT_ORDER_NO', blank=True, null=True)  # Field name made lowercase.
    after_b3_bat_turn_no = models.IntegerField(db_column='AFTER_B3_BAT_TURN_NO', blank=True, null=True)  # Field name made lowercase.
    after_b3_bat_order_no = models.IntegerField(db_column='AFTER_B3_BAT_ORDER_NO', blank=True, null=True)  # Field name made lowercase.
    out_cn = models.IntegerField(db_column='OUT_CN')  # Field name made lowercase.
    away_score_cn = models.IntegerField(db_column='AWAY_SCORE_CN')  # Field name made lowercase.
    home_score_cn = models.IntegerField(db_column='HOME_SCORE_CN')  # Field name made lowercase.
    operation_cd = models.IntegerField(db_column='OPERATION_CD', blank=True, null=True)  # Field name made lowercase.
    memo_cd = models.IntegerField(db_column='MEMO_CD', blank=True, null=True)  # Field name made lowercase.
    shift_cd = models.IntegerField(db_column='SHIFT_CD', blank=True, null=True)  # Field name made lowercase.
    hit_gr_x_va = models.SmallIntegerField(db_column='HIT_GR_X_VA', blank=True, null=True)  # Field name made lowercase.
    hit_gr_y_va = models.SmallIntegerField(db_column='HIT_GR_Y_VA', blank=True, null=True)  # Field name made lowercase.
    hit_gr_zone_no = models.CharField(db_column='HIT_GR_ZONE_NO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    hit_rank_sc = models.CharField(db_column='HIT_RANK_SC', max_length=1, blank=True, null=True)  # Field name made lowercase.
    hit_type_sc = models.CharField(db_column='HIT_TYPE_SC', max_length=1, blank=True, null=True)  # Field name made lowercase.
    pitchout_ck = models.TextField(db_column='PITCHOUT_CK', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pit_oppesed_ck = models.TextField(db_column='PIT_OPPESED_CK', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pickoff_ck = models.TextField(db_column='PICKOFF_CK', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ib_ck = models.TextField(db_column='IB_CK', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    connect_ck = models.TextField(db_column='CONNECT_CK', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    hit_advance_ck = models.TextField(db_column='HIT_ADVANCE_CK', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pit_attract_ck = models.TextField(db_column='PIT_ATTRACT_CK', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bound_ck = models.TextField(db_column='BOUND_CK', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    hr_distance_va = models.SmallIntegerField(db_column='HR_DISTANCE_VA', blank=True, null=True)  # Field name made lowercase.
    erun_pit_p_id = models.IntegerField(db_column='ERUN_PIT_P_ID', blank=True, null=True)  # Field name made lowercase.
    m_se = models.IntegerField(db_column='M_SE')  # Field name made lowercase.
    reg_dt = models.DateTimeField(db_column='REG_DT')  # Field name made lowercase.

    class Meta:
        app_label = 'baseball'
        managed = False
        db_table = 'ball_info'
        unique_together = (('p_se', 'g_id', 'seq_no'),)


class BallTimeInfo(models.Model):
    p_se = models.IntegerField(db_column='P_SE', primary_key=True)  # Field name made lowercase.
    g_id = models.CharField(db_column='G_ID', max_length=13)  # Field name made lowercase.
    seq_no = models.IntegerField(db_column='SEQ_NO')  # Field name made lowercase.
    pit_no = models.SmallIntegerField(db_column='PIT_NO')  # Field name made lowercase.
    pit_start_dt = models.DateTimeField(db_column='PIT_START_DT')  # Field name made lowercase.
    pit_end_dt = models.DateTimeField(db_column='PIT_END_DT', blank=True, null=True)  # Field name made lowercase.
    m_se = models.IntegerField(db_column='M_SE')  # Field name made lowercase.
    reg_dt = models.DateTimeField(db_column='REG_DT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        app_label = 'baseball'
        managed = False
        db_table = 'ball_time_info'
        unique_together = (('p_se', 'g_id', 'seq_no'),)


class Battotal(models.Model):
    pcode = models.CharField(db_column='PCODE', primary_key=True, max_length=5)  # Field name made lowercase.
    gyear = models.CharField(db_column='GYEAR', max_length=4)  # Field name made lowercase.
    team = models.CharField(db_column='TEAM', max_length=10, blank=True, null=True)  # Field name made lowercase.
    hra = models.FloatField(db_column='HRA', blank=True, null=True)  # Field name made lowercase.
    gamenum = models.IntegerField(db_column='GAMENUM', blank=True, null=True)  # Field name made lowercase.
    ab = models.IntegerField(db_column='AB', blank=True, null=True)  # Field name made lowercase.
    run = models.IntegerField(db_column='RUN', blank=True, null=True)  # Field name made lowercase.
    hit = models.IntegerField(db_column='HIT', blank=True, null=True)  # Field name made lowercase.
    h2 = models.IntegerField(db_column='H2', blank=True, null=True)  # Field name made lowercase.
    h3 = models.IntegerField(db_column='H3', blank=True, null=True)  # Field name made lowercase.
    hr = models.IntegerField(db_column='HR', blank=True, null=True)  # Field name made lowercase.
    tb = models.IntegerField(db_column='TB', blank=True, null=True)  # Field name made lowercase.
    rbi = models.IntegerField(db_column='RBI', blank=True, null=True)  # Field name made lowercase.
    sb = models.IntegerField(db_column='SB', blank=True, null=True)  # Field name made lowercase.
    cs = models.IntegerField(db_column='CS', blank=True, null=True)  # Field name made lowercase.
    sh = models.IntegerField(db_column='SH', blank=True, null=True)  # Field name made lowercase.
    sf = models.IntegerField(db_column='SF', blank=True, null=True)  # Field name made lowercase.
    bb = models.IntegerField(db_column='BB', blank=True, null=True)  # Field name made lowercase.
    hp = models.IntegerField(db_column='HP', blank=True, null=True)  # Field name made lowercase.
    kk = models.IntegerField(db_column='KK', blank=True, null=True)  # Field name made lowercase.
    gd = models.IntegerField(db_column='GD', blank=True, null=True)  # Field name made lowercase.
    err = models.IntegerField(db_column='ERR', blank=True, null=True)  # Field name made lowercase.
    score = models.IntegerField(db_column='SCORE', blank=True, null=True)  # Field name made lowercase.
    wpa = models.FloatField(db_column='WPA', blank=True, null=True)  # Field name made lowercase.
    war = models.FloatField(db_column='WAR', blank=True, null=True)  # Field name made lowercase.
    isop = models.FloatField(db_column='ISOP', blank=True, null=True)  # Field name made lowercase.
    babip = models.FloatField(db_column='BABIP', blank=True, null=True)  # Field name made lowercase.
    obp = models.FloatField(db_column='OBP', blank=True, null=True)  # Field name made lowercase.
    slg = models.FloatField(db_column='SLG', blank=True, null=True)  # Field name made lowercase.
    pa_flag = models.TextField(db_column='PA_FLAG', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    wrc_plus = models.FloatField(db_column='WRC_PLUS', blank=True, null=True)  # Field name made lowercase.
    woba = models.FloatField(db_column='WOBA', blank=True, null=True)  # Field name made lowercase.
    ops = models.FloatField(db_column='OPS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        app_label = 'baseball'
        managed = False
        db_table = 'battotal'
        unique_together = (('pcode', 'gyear'),)


class CancelGame(models.Model):
    gmkey = models.CharField(max_length=13)
    gyear = models.SmallIntegerField()
    reason = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        app_label = 'baseball'
        managed = False
        db_table = 'cancel_game'


class CdDetail(models.Model):
    cd_se = models.IntegerField(db_column='CD_SE', primary_key=True)  # Field name made lowercase.
    cm_se = models.IntegerField(db_column='CM_SE')  # Field name made lowercase.
    cd_nm = models.CharField(db_column='CD_NM', max_length=50)  # Field name made lowercase.
    join_cd = models.IntegerField(db_column='JOIN_CD', blank=True, null=True)  # Field name made lowercase.
    reg_dt = models.DateTimeField(db_column='REG_DT')  # Field name made lowercase.

    class Meta:
        app_label = 'baseball'
        managed = False
        db_table = 'cd_detail'


class CdMaster(models.Model):
    cm_se = models.IntegerField(db_column='CM_SE', primary_key=True)  # Field name made lowercase.
    cm_nm = models.CharField(db_column='CM_NM', max_length=50)  # Field name made lowercase.
    reg_dt = models.DateTimeField(db_column='REG_DT')  # Field name made lowercase.

    class Meta:
        app_label = 'baseball'
        managed = False
        db_table = 'cd_master'


class Dailyrank(models.Model):
    gday = models.CharField(db_column='GDAY', primary_key=True, max_length=8)  # Field name made lowercase.
    team = models.CharField(db_column='TEAM', max_length=2)  # Field name made lowercase.
    w = models.IntegerField(db_column='W')  # Field name made lowercase.
    l = models.IntegerField(db_column='L', blank=True, null=True)  # Field name made lowercase.
    d = models.IntegerField(db_column='D', blank=True, null=True)  # Field name made lowercase.
    ww = models.SmallIntegerField(db_column='WW', blank=True, null=True)  # Field name made lowercase.
    ll = models.SmallIntegerField(db_column='LL', blank=True, null=True)  # Field name made lowercase.
    dd = models.SmallIntegerField(db_column='DD', blank=True, null=True)  # Field name made lowercase.
    wp = models.FloatField(db_column='WP', blank=True, null=True)  # Field name made lowercase.
    rank = models.SmallIntegerField(db_column='RANK', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        app_label = 'baseball'
        managed = False
        db_table = 'dailyrank'
        unique_together = (('gday', 'team'),)


class Defen(models.Model):
    gmkey = models.CharField(db_column='GMKEY', max_length=13)  # Field name made lowercase.
    tb = models.CharField(db_column='TB', max_length=1)  # Field name made lowercase.
    oneturn = models.IntegerField(db_column='ONETURN', blank=True, null=True)  # Field name made lowercase.
    posi = models.CharField(db_column='POSI', max_length=5, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=15, blank=True, null=True)  # Field name made lowercase.
    po = models.IntegerField(db_column='PO', blank=True, null=True)  # Field name made lowercase.
    ass = models.IntegerField(db_column='ASS', blank=True, null=True)  # Field name made lowercase.
    err = models.IntegerField(db_column='ERR', blank=True, null=True)  # Field name made lowercase.
    dp = models.IntegerField(db_column='DP', blank=True, null=True)  # Field name made lowercase.
    pb = models.IntegerField(db_column='PB', blank=True, null=True)  # Field name made lowercase.
    gday = models.IntegerField(db_column='GDAY', blank=True, null=True)  # Field name made lowercase.
    turn = models.CharField(db_column='TURN', max_length=2, blank=True, null=True)  # Field name made lowercase.
    pcode = models.CharField(db_column='PCODE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    chin = models.IntegerField(db_column='CHIN', blank=True, null=True)  # Field name made lowercase.
    chturn = models.IntegerField(db_column='CHTURN', blank=True, null=True)  # Field name made lowercase.
    chbcnt = models.IntegerField(db_column='CHBCNT', blank=True, null=True)  # Field name made lowercase.
    chin2 = models.IntegerField(db_column='CHIN2', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        app_label = 'baseball'
        managed = False
        db_table = 'defen'


class DefenTot(models.Model):
    gyear = models.SmallIntegerField(db_column='GYEAR')  # Field name made lowercase.
    gmkey = models.CharField(db_column='GMKEY', max_length=13)  # Field name made lowercase.
    tb = models.CharField(db_column='TB', max_length=1)  # Field name made lowercase.
    oneturn = models.IntegerField(db_column='ONETURN', blank=True, null=True)  # Field name made lowercase.
    posi = models.CharField(db_column='POSI', max_length=5, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=15, blank=True, null=True)  # Field name made lowercase.
    po = models.IntegerField(db_column='PO', blank=True, null=True)  # Field name made lowercase.
    ass = models.IntegerField(db_column='ASS', blank=True, null=True)  # Field name made lowercase.
    err = models.IntegerField(db_column='ERR', blank=True, null=True)  # Field name made lowercase.
    dp = models.IntegerField(db_column='DP', blank=True, null=True)  # Field name made lowercase.
    pb = models.IntegerField(db_column='PB', blank=True, null=True)  # Field name made lowercase.
    gday = models.IntegerField(db_column='GDAY', blank=True, null=True)  # Field name made lowercase.
    turn = models.IntegerField(db_column='TURN', blank=True, null=True)  # Field name made lowercase.
    pcode = models.CharField(db_column='PCODE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    chin = models.IntegerField(db_column='CHIN', blank=True, null=True)  # Field name made lowercase.
    chturn = models.IntegerField(db_column='CHTURN', blank=True, null=True)  # Field name made lowercase.
    chbcnt = models.IntegerField(db_column='CHBCNT', blank=True, null=True)  # Field name made lowercase.
    chin2 = models.IntegerField(db_column='CHIN2', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        app_label = 'baseball'
        managed = False
        db_table = 'defen_tot'


class Entry(models.Model):
    gmkey = models.CharField(db_column='GMKEY', primary_key=True, max_length=13)  # Field name made lowercase.
    gyear = models.SmallIntegerField(db_column='GYEAR')  # Field name made lowercase.
    gday = models.CharField(db_column='GDAY', max_length=8, blank=True, null=True)  # Field name made lowercase.
    turn = models.CharField(db_column='TURN', max_length=2)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=15, blank=True, null=True)  # Field name made lowercase.
    pcode = models.CharField(db_column='PCODE', primary_key=True, max_length=10)  # Field name made lowercase.
    team = models.CharField(db_column='TEAM', max_length=1, blank=True, null=True)  # Field name made lowercase.
    posi = models.CharField(db_column='POSI', max_length=2)  # Field name made lowercase.
    chin = models.IntegerField(db_column='CHIN', blank=True, null=True)  # Field name made lowercase.
    chturn = models.CharField(db_column='CHTURN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    chbcnt = models.IntegerField(db_column='CHBCNT', blank=True, null=True)  # Field name made lowercase.
    chin2 = models.CharField(db_column='CHIN2', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        app_label = 'baseball'
        managed = False
        db_table = 'entry'


class Entrydaily(models.Model):
    gamedate = models.CharField(primary_key=True, max_length=8)
    tcode = models.CharField(max_length=20)
    pcode = models.CharField(max_length=10)
    reg = models.CharField(max_length=1, blank=True, null=True)
    inputtime = models.DateTimeField()

    class Meta:
        app_label = 'baseball'
        managed = False
        db_table = 'entrydaily'
        unique_together = (('gamedate', 'tcode', 'pcode'),)


class EntrydailyTot(models.Model):
    gyear = models.IntegerField(db_column='GYEAR')  # Field name made lowercase.
    gamedate = models.CharField(db_column='GAMEDATE', max_length=8)  # Field name made lowercase.
    tcode = models.CharField(db_column='TCODE', max_length=20)  # Field name made lowercase.
    pcode = models.CharField(db_column='PCODE', max_length=10)  # Field name made lowercase.
    reg = models.CharField(db_column='REG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    inputtime = models.DateTimeField(db_column='INPUTTIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        app_label = 'baseball'
        managed = False
        db_table = 'entrydaily_tot'


class Etcgame(models.Model):
    gmkey = models.CharField(primary_key=True, max_length=13)
    gyear = models.CharField(db_column='GYEAR', max_length=4)  # Field name made lowercase.
    ser = models.IntegerField()
    how = models.CharField(max_length=2, blank=True, null=True)
    name = models.CharField(max_length=16, blank=True, null=True)
    pcode = models.CharField(db_column='PCODE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    inn = models.CharField(max_length=2, blank=True, null=True)
    name2 = models.CharField(max_length=16, blank=True, null=True)
    pcode2 = models.CharField(db_column='PCODE2', max_length=10, blank=True, null=True)  # Field name made lowercase.
    etc1 = models.CharField(max_length=40, blank=True, null=True)
    etc2 = models.CharField(max_length=26, blank=True, null=True)
    team = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        app_label = 'baseball'
        managed = False
        db_table = 'etcgame'
        unique_together = (('gmkey', 'gyear', 'ser'),)


class Gamecontapp(models.Model):
    gmkey = models.CharField(db_column='GMKEY', primary_key=True, max_length=13)  # Field name made lowercase.
    gyear = models.SmallIntegerField(db_column='GYEAR')  # Field name made lowercase.
    gday = models.CharField(db_column='GDAY', max_length=8)  # Field name made lowercase.
    serno = models.SmallIntegerField(db_column='SERNO')  # Field name made lowercase.
    turn = models.CharField(db_column='TURN', max_length=2)  # Field name made lowercase.
    inn = models.IntegerField(db_column='INN')  # Field name made lowercase.
    tb = models.CharField(db_column='TB', max_length=1)  # Field name made lowercase.
    inn2 = models.CharField(db_column='INN2', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ocount = models.CharField(db_column='OCOUNT', max_length=1, blank=True, null=True)  # Field name made lowercase.
    bcount = models.CharField(db_column='BCOUNT', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rturn = models.CharField(db_column='RTURN', max_length=2, blank=True, null=True)  # Field name made lowercase.
    how = models.CharField(db_column='HOW', max_length=2, blank=True, null=True)  # Field name made lowercase.
    field = models.CharField(db_column='FIELD', max_length=25, blank=True, null=True)  # Field name made lowercase.
    place = models.CharField(db_column='PLACE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    hitter = models.CharField(db_column='HITTER', max_length=10, blank=True, null=True)  # Field name made lowercase.
    hitname = models.CharField(db_column='HITNAME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    pitname = models.CharField(db_column='PITNAME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    pitcher = models.CharField(db_column='PITCHER', max_length=10, blank=True, null=True)  # Field name made lowercase.
    catname = models.CharField(db_column='CATNAME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    catcher = models.CharField(db_column='CATCHER', max_length=10, blank=True, null=True)  # Field name made lowercase.
    bcnt = models.CharField(db_column='BCNT', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tscore = models.SmallIntegerField(db_column='TSCORE', blank=True, null=True)  # Field name made lowercase.
    bscore = models.SmallIntegerField(db_column='BSCORE', blank=True, null=True)  # Field name made lowercase.
    base1b = models.CharField(db_column='BASE1B', max_length=2, blank=True, null=True)  # Field name made lowercase.
    base2b = models.CharField(db_column='BASE2B', max_length=2, blank=True, null=True)  # Field name made lowercase.
    base3b = models.CharField(db_column='BASE3B', max_length=2, blank=True, null=True)  # Field name made lowercase.
    base1a = models.CharField(db_column='BASE1A', max_length=2, blank=True, null=True)  # Field name made lowercase.
    base2a = models.CharField(db_column='BASE2A', max_length=2, blank=True, null=True)  # Field name made lowercase.
    base3a = models.CharField(db_column='BASE3A', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        app_label = 'baseball'
        managed = False
        db_table = 'gamecontapp'
        unique_together = (('gmkey', 'serno'),)


class Gameinfo(models.Model):
    gmkey = models.CharField(db_column='GmKey', primary_key=True, max_length=13)  # Field name made lowercase.
    gday = models.CharField(db_column='Gday', max_length=8)  # Field name made lowercase.
    dbhd = models.CharField(db_column='Dbhd', max_length=10)  # Field name made lowercase.
    stadium = models.CharField(db_column='Stadium', max_length=20)  # Field name made lowercase.
    vteam = models.CharField(db_column='Vteam', max_length=2)  # Field name made lowercase.
    hteam = models.CharField(db_column='Hteam', max_length=2)  # Field name made lowercase.
    sttm = models.CharField(db_column='Sttm', max_length=4)  # Field name made lowercase.
    entm = models.CharField(db_column='Entm', max_length=4, blank=True, null=True)  # Field name made lowercase.
    dltm = models.CharField(db_column='Dltm', max_length=4, blank=True, null=True)  # Field name made lowercase.
    gmtm = models.CharField(db_column='Gmtm', max_length=4, blank=True, null=True)  # Field name made lowercase.
    stad = models.CharField(db_column='Stad', max_length=8, blank=True, null=True)  # Field name made lowercase.
    umpc = models.CharField(db_column='Umpc', max_length=8, blank=True, null=True)  # Field name made lowercase.
    ump1 = models.CharField(db_column='Ump1', max_length=8, blank=True, null=True)  # Field name made lowercase.
    ump2 = models.CharField(db_column='Ump2', max_length=8, blank=True, null=True)  # Field name made lowercase.
    ump3 = models.CharField(db_column='Ump3', max_length=8, blank=True, null=True)  # Field name made lowercase.
    umpl = models.CharField(db_column='Umpl', max_length=8, blank=True, null=True)  # Field name made lowercase.
    umpr = models.CharField(db_column='Umpr', max_length=8, blank=True, null=True)  # Field name made lowercase.
    scoa = models.CharField(db_column='Scoa', max_length=8, blank=True, null=True)  # Field name made lowercase.
    scob = models.CharField(db_column='Scob', max_length=8, blank=True, null=True)  # Field name made lowercase.
    temp = models.CharField(db_column='Temp', max_length=3, blank=True, null=True)  # Field name made lowercase.
    mois = models.CharField(db_column='Mois', max_length=3, blank=True, null=True)  # Field name made lowercase.
    weath = models.CharField(db_column='Weath', max_length=2, blank=True, null=True)  # Field name made lowercase.
    wind = models.CharField(db_column='Wind', max_length=3, blank=True, null=True)  # Field name made lowercase.
    wins = models.CharField(db_column='Wins', max_length=5, blank=True, null=True)  # Field name made lowercase.
    gweek = models.CharField(db_column='Gweek', max_length=2, blank=True, null=True)  # Field name made lowercase.
    crowd = models.IntegerField(db_column='Crowd', blank=True, null=True)  # Field name made lowercase.
    chajun = models.CharField(db_column='Chajun', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        app_label = 'baseball'
        managed = False
        db_table = 'gameinfo'


class GoodbyeRecord(models.Model):
    gb_sc = models.CharField(db_column='GB_SC', primary_key=True, max_length=10)  # Field name made lowercase.
    total_no = models.IntegerField(db_column='TOTAL_NO')  # Field name made lowercase.
    season_no = models.IntegerField(db_column='SEASON_NO')  # Field name made lowercase.
    g_id = models.CharField(db_column='G_ID', max_length=13)  # Field name made lowercase.
    g_ds = models.CharField(db_column='G_DS', max_length=8)  # Field name made lowercase.
    daynight_sc = models.CharField(db_column='DAYNIGHT_SC', max_length=1)  # Field name made lowercase.
    t_cd = models.CharField(db_column='T_CD', max_length=2)  # Field name made lowercase.
    t_nm = models.CharField(db_column='T_NM', max_length=10)  # Field name made lowercase.
    opp_t_cd = models.CharField(db_column='OPP_T_CD', max_length=2)  # Field name made lowercase.
    opp_t_nm = models.CharField(db_column='OPP_T_NM', max_length=10)  # Field name made lowercase.
    stadium_nm = models.CharField(db_column='STADIUM_NM', max_length=10)  # Field name made lowercase.
    bat_p_id = models.IntegerField(db_column='BAT_P_ID')  # Field name made lowercase.
    bat_p_nm = models.CharField(db_column='BAT_P_NM', max_length=20)  # Field name made lowercase.
    pit_p_id = models.IntegerField(db_column='PIT_P_ID')  # Field name made lowercase.
    pit_p_nm = models.CharField(db_column='PIT_P_NM', max_length=20)  # Field name made lowercase.
    cat_p_id = models.IntegerField(db_column='CAT_P_ID')  # Field name made lowercase.
    cat_p_nm = models.CharField(db_column='CAT_P_NM', max_length=20)  # Field name made lowercase.
    ser_no = models.SmallIntegerField(db_column='SER_NO')  # Field name made lowercase.
    inn_no = models.IntegerField(db_column='INN_NO')  # Field name made lowercase.
    strike_cn = models.IntegerField(db_column='STRIKE_CN')  # Field name made lowercase.
    ball_cn = models.IntegerField(db_column='BALL_CN')  # Field name made lowercase.
    out_cn = models.IntegerField(db_column='OUT_CN')  # Field name made lowercase.
    base_cn = models.IntegerField(db_column='BASE_CN')  # Field name made lowercase.
    base_sc = models.IntegerField(db_column='BASE_SC')  # Field name made lowercase.
    how_id = models.CharField(db_column='HOW_ID', max_length=5)  # Field name made lowercase.
    ph_ck = models.TextField(db_column='PH_CK')  # Field name made lowercase. This field type is a guess.
    field_if = models.CharField(db_column='FIELD_IF', max_length=10, blank=True, null=True)  # Field name made lowercase.
    reg_dt = models.DateTimeField(db_column='REG_DT')  # Field name made lowercase.

    class Meta:
        app_label = 'baseball'
        managed = False
        db_table = 'goodbye_record'
        unique_together = (('gb_sc', 'total_no'),)


class Hitter(models.Model):
    gmkey = models.CharField(db_column='GMKEY', primary_key=True, max_length=13)  # Field name made lowercase.
    gday = models.CharField(db_column='GDAY', max_length=8)  # Field name made lowercase.
    tb = models.CharField(db_column='TB', max_length=1, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    pcode = models.CharField(db_column='PCODE', max_length=5)  # Field name made lowercase.
    turn = models.CharField(db_column='TURN', max_length=2, blank=True, null=True)  # Field name made lowercase.
    oneturn = models.CharField(db_column='ONETURN', max_length=1, blank=True, null=True)  # Field name made lowercase.
    pa = models.IntegerField(db_column='PA', blank=True, null=True)  # Field name made lowercase.
    ab = models.IntegerField(db_column='AB', blank=True, null=True)  # Field name made lowercase.
    rbi = models.IntegerField(db_column='RBI', blank=True, null=True)  # Field name made lowercase.
    run = models.IntegerField(db_column='RUN', blank=True, null=True)  # Field name made lowercase.
    hit = models.IntegerField(db_column='HIT', blank=True, null=True)  # Field name made lowercase.
    h2 = models.IntegerField(db_column='H2', blank=True, null=True)  # Field name made lowercase.
    h3 = models.IntegerField(db_column='H3', blank=True, null=True)  # Field name made lowercase.
    hr = models.IntegerField(db_column='HR', blank=True, null=True)  # Field name made lowercase.
    sb = models.IntegerField(db_column='SB', blank=True, null=True)  # Field name made lowercase.
    cs = models.IntegerField(db_column='CS', blank=True, null=True)  # Field name made lowercase.
    sh = models.IntegerField(db_column='SH', blank=True, null=True)  # Field name made lowercase.
    sf = models.IntegerField(db_column='SF', blank=True, null=True)  # Field name made lowercase.
    bb = models.IntegerField(db_column='BB', blank=True, null=True)  # Field name made lowercase.
    ib = models.IntegerField(db_column='IB', blank=True, null=True)  # Field name made lowercase.
    hp = models.IntegerField(db_column='HP', blank=True, null=True)  # Field name made lowercase.
    kk = models.IntegerField(db_column='KK', blank=True, null=True)  # Field name made lowercase.
    gd = models.IntegerField(db_column='GD', blank=True, null=True)  # Field name made lowercase.
    err = models.IntegerField(db_column='ERR', blank=True, null=True)  # Field name made lowercase.
    lob = models.IntegerField(db_column='LOB', blank=True, null=True)  # Field name made lowercase.
    score = models.IntegerField(db_column='SCORE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        app_label = 'baseball'
        managed = False
        db_table = 'hitter'
        unique_together = (('gmkey', 'pcode', 'gday'),)


class HitterHitDirection(models.Model):
    gyear = models.SmallIntegerField(blank=True, null=True)
    hitname = models.CharField(max_length=20, blank=True, null=True)
    team = models.CharField(max_length=255, blank=True, null=True)
    hit = models.IntegerField(blank=True, null=True)
    # ���� = models.IntegerField(blank=True, null=True)
    # �� = models.IntegerField(blank=True, null=True)
    # ���� = models.IntegerField(blank=True, null=True)
    # �� = models.IntegerField(blank=True, null=True)
    # ���� = models.IntegerField(blank=True, null=True)
    # �� = models.IntegerField(blank=True, null=True)

    class Meta:
        app_label = 'baseball'
        managed = False
        db_table = 'hitter_hit_direction'


class HitterHitDirectionTot(models.Model):
    gmkey = models.SmallIntegerField(db_column='GMKEY', blank=True, null=True)  # Field name made lowercase.
    hitname = models.CharField(max_length=20, blank=True, null=True)
    team = models.CharField(max_length=255, blank=True, null=True)
    hit = models.IntegerField(blank=True, null=True)
    # ���� = models.IntegerField(blank=True, null=True)
    # �� = models.IntegerField(blank=True, null=True)
    # ���� = models.IntegerField(blank=True, null=True)
    # �� = models.IntegerField(blank=True, null=True)
    # ���� = models.IntegerField(blank=True, null=True)
    # �� = models.IntegerField(blank=True, null=True)

    class Meta:
        app_label = 'baseball'
        managed = False
        db_table = 'hitter_hit_direction_tot'


class HrTotal(models.Model):
    no = models.IntegerField(db_column='No')  # Field name made lowercase.
    gmkey = models.CharField(max_length=13, blank=True, null=True)
    gday = models.CharField(max_length=8, blank=True, null=True)
    gweek = models.CharField(max_length=2, blank=True, null=True)
    dn = models.CharField(max_length=2, blank=True, null=True)
    hitter = models.CharField(db_column='Hitter', max_length=10, blank=True, null=True)  # Field name made lowercase.
    hitname = models.CharField(max_length=20, blank=True, null=True)
    team = models.CharField(max_length=4, blank=True, null=True)
    stadium = models.CharField(max_length=6, blank=True, null=True)
    vsteam = models.CharField(max_length=4, blank=True, null=True)
    pitcher = models.CharField(db_column='Pitcher', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pitname = models.CharField(max_length=20, blank=True, null=True)
    serno = models.IntegerField(db_column='Serno', blank=True, null=True)  # Field name made lowercase.
    inn = models.IntegerField(blank=True, null=True)
    tb = models.CharField(db_column='TB', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ocount = models.CharField(max_length=1, blank=True, null=True)
    # ���� = models.CharField(max_length=3, blank=True, null=True)
    runner = models.CharField(db_column='Runner', max_length=3, blank=True, null=True)  # Field name made lowercase.
    bcnt = models.CharField(max_length=3, blank=True, null=True)
    field = models.CharField(max_length=4, blank=True, null=True)
    meter = models.CharField(db_column='Meter', max_length=10, blank=True, null=True)  # Field name made lowercase.
    game = models.SmallIntegerField(db_column='Game', blank=True, null=True)  # Field name made lowercase.
    record_dt = models.DateTimeField(db_column='RECORD_DT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        app_label = 'baseball'
        managed = False
        db_table = 'hr_total'


class IeBatterrecord(models.Model):
    gameid = models.CharField(db_column='GAMEID', primary_key=True, max_length=20)  # Field name made lowercase.
    gyear = models.SmallIntegerField(db_column='GYEAR')  # Field name made lowercase.
    batorder = models.IntegerField(db_column='BATORDER')  # Field name made lowercase.
    position = models.IntegerField(db_column='POSITION')  # Field name made lowercase.
    positionname = models.CharField(db_column='POSITIONNAME', max_length=20)  # Field name made lowercase.
    playername = models.CharField(db_column='PLAYERNAME', max_length=20)  # Field name made lowercase.
    playerid = models.CharField(db_column='PLAYERID', max_length=20)  # Field name made lowercase.
    seqno = models.IntegerField(db_column='SEQNO')  # Field name made lowercase.
    oab = models.IntegerField(db_column='OAB')  # Field name made lowercase.
    run = models.IntegerField(db_column='RUN')  # Field name made lowercase.
    h1 = models.IntegerField(db_column='H1')  # Field name made lowercase.
    h2 = models.IntegerField(db_column='H2')  # Field name made lowercase.
    h3 = models.IntegerField(db_column='H3')  # Field name made lowercase.
    hr = models.IntegerField(db_column='HR')  # Field name made lowercase.
    rbi = models.IntegerField(db_column='RBI')  # Field name made lowercase.
    steal = models.IntegerField(db_column='STEAL')  # Field name made lowercase.
    cs = models.IntegerField(db_column='CS')  # Field name made lowercase.
    sh = models.IntegerField(db_column='SH')  # Field name made lowercase.
    sf = models.IntegerField(db_column='SF')  # Field name made lowercase.
    bb = models.IntegerField(db_column='BB')  # Field name made lowercase.
    hbp = models.IntegerField(db_column='HBP')  # Field name made lowercase.
    so = models.IntegerField(db_column='SO')  # Field name made lowercase.
    dp = models.IntegerField(db_column='DP')  # Field name made lowercase.
    tp = models.IntegerField(db_column='TP')  # Field name made lowercase.
    bhome = models.IntegerField(db_column='BHOME')  # Field name made lowercase.

    class Meta:
        app_label = 'baseball'
        managed = False
        db_table = 'ie_batterrecord'
        unique_together = (('gameid', 'gyear', 'batorder', 'playerid', 'seqno'),)


class IeBatterrecord2(models.Model):
    gameid = models.CharField(db_column='gameID', primary_key=True, max_length=13)  # Field name made lowercase.
    gyear = models.SmallIntegerField(db_column='GYEAR')  # Field name made lowercase.
    batorder = models.IntegerField(db_column='BatOrder')  # Field name made lowercase.
    position = models.IntegerField(db_column='Position')  # Field name made lowercase.
    positionname = models.CharField(db_column='PositionName', max_length=20)  # Field name made lowercase.
    playername = models.CharField(db_column='PlayerName', max_length=15)  # Field name made lowercase.
    playerid = models.CharField(db_column='PlayerID', max_length=10)  # Field name made lowercase.
    seqno = models.IntegerField(db_column='SeqNO')  # Field name made lowercase.
    oab = models.IntegerField(db_column='OAB')  # Field name made lowercase.
    run = models.IntegerField(db_column='Run')  # Field name made lowercase.
    h1 = models.IntegerField(db_column='H1')  # Field name made lowercase.
    h2 = models.IntegerField(db_column='H2')  # Field name made lowercase.
    h3 = models.IntegerField(db_column='H3')  # Field name made lowercase.
    hr = models.IntegerField(db_column='HR')  # Field name made lowercase.
    rbi = models.IntegerField(db_column='RBI')  # Field name made lowercase.
    steal = models.IntegerField(db_column='Steal')  # Field name made lowercase.
    cs = models.IntegerField(db_column='CS')  # Field name made lowercase.
    sh = models.IntegerField(db_column='SH')  # Field name made lowercase.
    sf = models.IntegerField(db_column='SF')  # Field name made lowercase.
    bb = models.IntegerField(db_column='BB')  # Field name made lowercase.
    hbp = models.IntegerField(db_column='HBP')  # Field name made lowercase.
    so = models.IntegerField(db_column='SO')  # Field name made lowercase.
    dp = models.IntegerField(db_column='DP')  # Field name made lowercase.
    tp = models.IntegerField(db_column='TP')  # Field name made lowercase.
    er = models.IntegerField(db_column='ER')  # Field name made lowercase.
    bhome = models.IntegerField(db_column='bHome')  # Field name made lowercase.

    class Meta:
        app_label = 'baseball'
        managed = False
        db_table = 'ie_batterrecord2'
        unique_together = (('gameid', 'gyear', 'batorder', 'playerid', 'seqno'),)


class IeGamelist(models.Model):
    gameid = models.CharField(db_column='gameID', primary_key=True, max_length=13)  # Field name made lowercase.
    gyear = models.SmallIntegerField(db_column='GYEAR')  # Field name made lowercase.
    homename = models.CharField(db_column='HomeName', max_length=8)  # Field name made lowercase.
    homemascot = models.CharField(db_column='HomeMascot', max_length=20)  # Field name made lowercase.
    visitname = models.CharField(db_column='VisitName', max_length=8)  # Field name made lowercase.
    visitmascot = models.CharField(db_column='VisitMascot', max_length=20)  # Field name made lowercase.

    class Meta:
        app_label = 'baseball'
        managed = False
        db_table = 'ie_gamelist'
        unique_together = (('gameid', 'gyear'),)


class IeInningrecord(models.Model):
    gameid = models.CharField(primary_key=True, max_length=13)
    gyear = models.SmallIntegerField()
    inning = models.IntegerField()
    tb = models.CharField(max_length=1)
    run = models.IntegerField(blank=True, null=True)
    hit = models.IntegerField(blank=True, null=True)
    err = models.IntegerField(blank=True, null=True)
    bb = models.IntegerField(blank=True, null=True)
    lob = models.IntegerField(blank=True, null=True)
    hr = models.IntegerField(blank=True, null=True)
    hp = models.IntegerField(blank=True, null=True)

    class Meta:
        app_label = 'baseball'
        managed = False
        db_table = 'ie_inningrecord'
        unique_together = (('gameid', 'gyear', 'inning', 'tb'),)


class IeLivetextScoreMix(models.Model):
    gameid = models.CharField(db_column='gameID', primary_key=True, max_length=13)  # Field name made lowercase.
    gyear = models.SmallIntegerField(db_column='GYEAR')  # Field name made lowercase.
    seqno = models.IntegerField(db_column='seqNO')  # Field name made lowercase.
    inning = models.IntegerField(blank=True, null=True)
    ilsun = models.IntegerField(blank=True, null=True)
    btop = models.IntegerField(db_column='bTop', blank=True, null=True)  # Field name made lowercase.
    ballcount = models.IntegerField(blank=True, null=True)
    ball_type = models.CharField(max_length=10, blank=True, null=True)
    strike = models.IntegerField(blank=True, null=True)
    ball = models.IntegerField(blank=True, null=True)
    out = models.IntegerField(blank=True, null=True)
    pitcher = models.CharField(max_length=10, blank=True, null=True)
    batter = models.CharField(max_length=10, blank=True, null=True)
    catcher = models.CharField(max_length=10, blank=True, null=True)
    runner = models.CharField(max_length=10, blank=True, null=True)
    batorder = models.IntegerField(blank=True, null=True)
    batstartorder = models.IntegerField(blank=True, null=True)
    batresult = models.CharField(db_column='batResult', max_length=50, blank=True, null=True)  # Field name made lowercase.
    base1 = models.IntegerField(blank=True, null=True)
    base2 = models.IntegerField(blank=True, null=True)
    base3 = models.IntegerField(blank=True, null=True)
    a_score = models.IntegerField(db_column='A_Score', blank=True, null=True)  # Field name made lowercase.
    h_score = models.IntegerField(db_column='H_Score', blank=True, null=True)  # Field name made lowercase.
    a_run = models.IntegerField(db_column='A_Run', blank=True, null=True)  # Field name made lowercase.
    h_run = models.IntegerField(db_column='H_Run', blank=True, null=True)  # Field name made lowercase.
    a_hit = models.IntegerField(db_column='A_Hit', blank=True, null=True)  # Field name made lowercase.
    h_hit = models.IntegerField(db_column='H_Hit', blank=True, null=True)  # Field name made lowercase.
    a_error = models.IntegerField(db_column='A_Error', blank=True, null=True)  # Field name made lowercase.
    h_error = models.IntegerField(db_column='H_Error', blank=True, null=True)  # Field name made lowercase.
    a_ballfour = models.IntegerField(db_column='A_BallFour', blank=True, null=True)  # Field name made lowercase.
    h_ballfour = models.IntegerField(db_column='H_BallFour', blank=True, null=True)  # Field name made lowercase.
    livetext = models.CharField(db_column='LiveText', max_length=200, blank=True, null=True)  # Field name made lowercase.
    textstyle = models.IntegerField(db_column='textStyle', blank=True, null=True)  # Field name made lowercase.
    state_sc = models.IntegerField(db_column='STATE_SC', blank=True, null=True)  # Field name made lowercase.
    how = models.CharField(db_column='HOW', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        app_label = 'baseball'
        managed = False
        db_table = 'ie_livetext_score_mix'
        unique_together = (('gameid', 'gyear', 'seqno'),)


class IePitcherrecord(models.Model):
    gameid = models.CharField(db_column='GAMEID', primary_key=True, max_length=20)  # Field name made lowercase.
    gyear = models.SmallIntegerField(db_column='GYEAR')  # Field name made lowercase.
    playername = models.CharField(db_column='PLAYERNAME', max_length=30)  # Field name made lowercase.
    playerid = models.CharField(db_column='PLAYERID', max_length=20)  # Field name made lowercase.
    seqno = models.IntegerField(db_column='SEQNO')  # Field name made lowercase.
    inning = models.CharField(db_column='INNING', max_length=10)  # Field name made lowercase.
    pa = models.IntegerField(db_column='PA')  # Field name made lowercase.
    pitchballcnt = models.IntegerField(db_column='PITCHBALLCNT')  # Field name made lowercase.
    pitchstrikecnt = models.IntegerField(db_column='PITCHSTRIKECNT')  # Field name made lowercase.
    oab = models.IntegerField(db_column='OAB')  # Field name made lowercase.
    run = models.IntegerField(db_column='RUN')  # Field name made lowercase.
    hit = models.IntegerField(db_column='HIT')  # Field name made lowercase.
    hr = models.IntegerField(db_column='HR')  # Field name made lowercase.
    sh = models.IntegerField(db_column='SH')  # Field name made lowercase.
    sf = models.IntegerField(db_column='SF')  # Field name made lowercase.
    bb = models.IntegerField(db_column='BB')  # Field name made lowercase.
    hbp = models.IntegerField(db_column='HBP')  # Field name made lowercase.
    so = models.IntegerField(db_column='SO')  # Field name made lowercase.
    bk = models.IntegerField(db_column='BK')  # Field name made lowercase.
    wp = models.IntegerField(db_column='WP')  # Field name made lowercase.
    er = models.IntegerField(db_column='ER')  # Field name made lowercase.
    bhome = models.IntegerField(db_column='BHOME')  # Field name made lowercase.

    class Meta:
        app_label = 'baseball'
        managed = False
        db_table = 'ie_pitcherrecord'
        unique_together = (('gameid', 'gyear', 'playerid', 'bhome'),)


class IePitcherrecord2(models.Model):
    gameid = models.CharField(db_column='gameID', primary_key=True, max_length=13)  # Field name made lowercase.
    gyear = models.SmallIntegerField(db_column='GYEAR')  # Field name made lowercase.
    playername = models.CharField(db_column='PlayerName', max_length=15)  # Field name made lowercase.
    playerid = models.CharField(db_column='PlayerID', max_length=10)  # Field name made lowercase.
    seqno = models.IntegerField(db_column='SeqNO')  # Field name made lowercase.
    inning = models.CharField(db_column='Inning', max_length=5)  # Field name made lowercase.
    pa = models.IntegerField(db_column='PA', blank=True, null=True)  # Field name made lowercase.
    ab = models.IntegerField(db_column='AB')  # Field name made lowercase.
    pitchballcnt = models.IntegerField(db_column='PitchBallCnt')  # Field name made lowercase.
    pitchstrikecnt = models.IntegerField(db_column='PitchStrikeCnt')  # Field name made lowercase.
    oab = models.IntegerField(db_column='OAB')  # Field name made lowercase.
    run = models.IntegerField(db_column='Run')  # Field name made lowercase.
    hit = models.IntegerField(db_column='Hit')  # Field name made lowercase.
    hr = models.IntegerField(db_column='HR')  # Field name made lowercase.
    sh = models.IntegerField(db_column='SH')  # Field name made lowercase.
    sf = models.IntegerField(db_column='SF')  # Field name made lowercase.
    bb = models.IntegerField(db_column='BB')  # Field name made lowercase.
    hbp = models.IntegerField(db_column='HBP')  # Field name made lowercase.
    so = models.IntegerField(db_column='SO')  # Field name made lowercase.
    bk = models.IntegerField(db_column='BK')  # Field name made lowercase.
    wp = models.IntegerField(db_column='WP')  # Field name made lowercase.
    er = models.IntegerField(db_column='ER')  # Field name made lowercase.
    h2 = models.IntegerField(db_column='H2', blank=True, null=True)  # Field name made lowercase.
    h3 = models.IntegerField(db_column='H3', blank=True, null=True)  # Field name made lowercase.
    steal = models.IntegerField(db_column='STEAL', blank=True, null=True)  # Field name made lowercase.
    cs = models.IntegerField(db_column='CS', blank=True, null=True)  # Field name made lowercase.
    ib = models.IntegerField(db_column='IB', blank=True, null=True)  # Field name made lowercase.
    dp = models.IntegerField(db_column='DP', blank=True, null=True)  # Field name made lowercase.
    tp = models.IntegerField(db_column='TP', blank=True, null=True)  # Field name made lowercase.
    err = models.IntegerField(db_column='ERR', blank=True, null=True)  # Field name made lowercase.
    bhome = models.IntegerField(db_column='bHome')  # Field name made lowercase.

    class Meta:
        app_label = 'baseball'
        managed = False
        db_table = 'ie_pitcherrecord2'
        unique_together = (('gameid', 'gyear', 'playerid'),)


class IeRecordMatrixMix(models.Model):
    gameid = models.CharField(db_column='GAMEID', primary_key=True, max_length=13)  # Field name made lowercase.
    gyear = models.SmallIntegerField(db_column='GYEAR')  # Field name made lowercase.
    seqno = models.SmallIntegerField(db_column='SEQNO')  # Field name made lowercase.
    inn_no = models.IntegerField(db_column='INN_NO')  # Field name made lowercase.
    bat_around_no = models.IntegerField(db_column='BAT_AROUND_NO')  # Field name made lowercase.
    tb_sc = models.CharField(db_column='TB_SC', max_length=1)  # Field name made lowercase.
    before_out_cn = models.SmallIntegerField(db_column='BEFORE_OUT_CN')  # Field name made lowercase.
    before_away_score_cn = models.SmallIntegerField(db_column='BEFORE_AWAY_SCORE_CN')  # Field name made lowercase.
    before_home_score_cn = models.SmallIntegerField(db_column='BEFORE_HOME_SCORE_CN')  # Field name made lowercase.
    before_score_gap_cn = models.SmallIntegerField(db_column='BEFORE_SCORE_GAP_CN')  # Field name made lowercase.
    before_runner_sc = models.SmallIntegerField(db_column='BEFORE_RUNNER_SC')  # Field name made lowercase.
    after_out_cn = models.SmallIntegerField(db_column='AFTER_OUT_CN')  # Field name made lowercase.
    after_away_score_cn = models.SmallIntegerField(db_column='AFTER_AWAY_SCORE_CN')  # Field name made lowercase.
    after_home_score_cn = models.SmallIntegerField(db_column='AFTER_HOME_SCORE_CN')  # Field name made lowercase.
    after_score_gap_cn = models.SmallIntegerField(db_column='AFTER_SCORE_GAP_CN')  # Field name made lowercase.
    after_runner_sc = models.SmallIntegerField(db_column='AFTER_RUNNER_SC')  # Field name made lowercase.
    bat_p_id = models.IntegerField(db_column='BAT_P_ID', blank=True, null=True)  # Field name made lowercase.
    pit_p_id = models.IntegerField(db_column='PIT_P_ID', blank=True, null=True)  # Field name made lowercase.
    run_p_id = models.IntegerField(db_column='RUN_P_ID', blank=True, null=True)  # Field name made lowercase.
    how_id = models.CharField(db_column='HOW_ID', max_length=4, blank=True, null=True)  # Field name made lowercase.
    livetext_if = models.CharField(db_column='LIVETEXT_IF', max_length=400, blank=True, null=True)  # Field name made lowercase.
    before_we_rt = models.FloatField(db_column='BEFORE_WE_RT', blank=True, null=True)  # Field name made lowercase.
    after_we_rt = models.FloatField(db_column='AFTER_WE_RT', blank=True, null=True)  # Field name made lowercase.
    wpa_rt = models.FloatField(db_column='WPA_RT', blank=True, null=True)  # Field name made lowercase.
    li_rt = models.FloatField(db_column='LI_RT', blank=True, null=True)  # Field name made lowercase.
    re_rt = models.FloatField(db_column='RE_RT', blank=True, null=True)  # Field name made lowercase.
    reg_dt = models.DateField(db_column='REG_DT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        app_label = 'baseball'
        managed = False
        db_table = 'ie_record_matrix_mix'
        unique_together = (('gameid', 'gyear', 'seqno'),)


class IeScoreinning(models.Model):
    gameid = models.CharField(db_column='gameID', primary_key=True, max_length=13)  # Field name made lowercase.
    gyear = models.SmallIntegerField(db_column='GYEAR')  # Field name made lowercase.
    inning = models.IntegerField()
    score = models.IntegerField(db_column='Score')  # Field name made lowercase.
    bhome = models.IntegerField(db_column='bHome')  # Field name made lowercase.

    class Meta:
        app_label = 'baseball'
        managed = False
        db_table = 'ie_scoreinning'
        unique_together = (('gameid', 'gyear', 'inning', 'bhome'),)


class KboEtcgame(models.Model):
    gmkey = models.CharField(db_column='GMKEY', primary_key=True, max_length=13)  # Field name made lowercase.
    gday = models.CharField(db_column='GDAY', max_length=8)  # Field name made lowercase.
    seq = models.IntegerField(db_column='SEQ')  # Field name made lowercase.
    how = models.CharField(db_column='HOW', max_length=16)  # Field name made lowercase.
    result = models.CharField(db_column='RESULT', max_length=255)  # Field name made lowercase.

    class Meta:
        app_label = 'baseball'
        managed = False
        db_table = 'kbo_etcgame'
        unique_together = (('gmkey', 'seq'),)


class KboEtcgameTot(models.Model):
    gyear = models.SmallIntegerField(db_column='GYEAR')  # Field name made lowercase.
    gmkey = models.CharField(db_column='GMKEY', max_length=13)  # Field name made lowercase.
    gday = models.CharField(db_column='GDAY', max_length=8)  # Field name made lowercase.
    seq = models.IntegerField(db_column='SEQ')  # Field name made lowercase.
    how = models.CharField(db_column='HOW', max_length=16)  # Field name made lowercase.
    result = models.CharField(db_column='RESULT', max_length=255)  # Field name made lowercase.

    class Meta:
        app_label = 'baseball'
        managed = False
        db_table = 'kbo_etcgame_tot'


class KboHitzone(models.Model):
    gmkey = models.CharField(primary_key=True, max_length=13)
    gyear = models.SmallIntegerField(db_column='GYEAR')  # Field name made lowercase.
    inn = models.IntegerField()
    tb = models.CharField(max_length=1)
    ilsun = models.IntegerField()
    batorder = models.IntegerField()
    ballcount = models.IntegerField()
    x = models.IntegerField()
    y = models.IntegerField()
    batter = models.CharField(max_length=10)
    pitcher = models.CharField(max_length=10)
    seqno = models.IntegerField()
    inputtime = models.DateTimeField()

    class Meta:
        app_label = 'baseball'
        managed = False
        db_table = 'kbo_hitzone'
        unique_together = (('gmkey', 'gyear', 'inn', 'tb', 'ilsun', 'batorder', 'ballcount'),)


class KboPitzone(models.Model):
    gmkey = models.CharField(primary_key=True, max_length=13)
    gyear = models.CharField(max_length=4)
    inn = models.SmallIntegerField()
    tb = models.CharField(max_length=10)
    ilsun = models.CharField(max_length=1)
    batstartorder = models.SmallIntegerField()
    batorder = models.SmallIntegerField()
    ballcount = models.SmallIntegerField()
    ball = models.CharField(max_length=1)
    stuff = models.CharField(max_length=4)
    zonex = models.SmallIntegerField()
    zoney = models.SmallIntegerField()
    speed = models.SmallIntegerField()
    x = models.SmallIntegerField()
    y = models.SmallIntegerField()
    batter = models.CharField(max_length=10, blank=True, null=True)
    pitcher = models.CharField(max_length=10, blank=True, null=True)
    seqno = models.SmallIntegerField()
    inputtime = models.DateTimeField()

    class Meta:
        app_label = 'baseball'
        managed = False
        db_table = 'kbo_pitzone'
        unique_together = (('gmkey', 'gyear', 'seqno'),)


class MatrixBasic(models.Model):
    season_id = models.SmallIntegerField(db_column='SEASON_ID')  # Field name made lowercase.
    out_cn = models.IntegerField(db_column='OUT_CN')  # Field name made lowercase.
    runner_sc = models.IntegerField(db_column='RUNNER_SC')  # Field name made lowercase.
    re_rt = models.FloatField(db_column='RE_RT', blank=True, null=True)  # Field name made lowercase.
    reg_dt = models.DateTimeField(db_column='REG_DT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        app_label = 'baseball'
        managed = False
        db_table = 'matrix_basic'


class MatrixDetail(models.Model):
    season_id = models.SmallIntegerField(db_column='SEASON_ID', primary_key=True)  # Field name made lowercase.
    inn_no = models.IntegerField(db_column='INN_NO')  # Field name made lowercase.
    tb_sc = models.CharField(db_column='TB_SC', max_length=1)  # Field name made lowercase.
    out_cn = models.IntegerField(db_column='OUT_CN')  # Field name made lowercase.
    runner_sc = models.IntegerField(db_column='RUNNER_SC')  # Field name made lowercase.
    score_gap_cn = models.SmallIntegerField(db_column='SCORE_GAP_CN')  # Field name made lowercase.
    we_rt = models.FloatField(db_column='WE_RT', blank=True, null=True)  # Field name made lowercase.
    li_rt = models.FloatField(db_column='LI_RT')  # Field name made lowercase.
    reg_dt = models.DateTimeField(db_column='REG_DT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        app_label = 'baseball'
        managed = False
        db_table = 'matrix_detail'
        unique_together = (('season_id', 'inn_no', 'tb_sc', 'out_cn', 'runner_sc', 'score_gap_cn'),)


class Person(models.Model):
    gyear = models.SmallIntegerField(db_column='GYEAR', primary_key=True)  # Field name made lowercase.
    pcode = models.CharField(db_column='PCODE', max_length=10)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    team = models.CharField(db_column='TEAM', max_length=8, blank=True, null=True)  # Field name made lowercase.
    t_id = models.CharField(db_column='T_ID', max_length=2, blank=True, null=True)  # Field name made lowercase.
    pos = models.CharField(db_column='POS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    position = models.CharField(db_column='POSITION', max_length=4, blank=True, null=True)  # Field name made lowercase.
    backnum = models.CharField(db_column='BACKNUM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cname = models.CharField(db_column='CNAME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    eng_nm = models.CharField(db_column='ENG_NM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hittype = models.CharField(db_column='HITTYPE', max_length=8, blank=True, null=True)  # Field name made lowercase.
    birth = models.CharField(db_column='BIRTH', max_length=8, blank=True, null=True)  # Field name made lowercase.
    height = models.CharField(db_column='HEIGHT', max_length=3, blank=True, null=True)  # Field name made lowercase.
    weight = models.CharField(db_column='WEIGHT', max_length=3, blank=True, null=True)  # Field name made lowercase.
    indate = models.CharField(db_column='INDATE', max_length=8, blank=True, null=True)  # Field name made lowercase.
    promise = models.CharField(db_column='PROMISE', max_length=12, blank=True, null=True)  # Field name made lowercase.
    money = models.CharField(db_column='MONEY', max_length=12, blank=True, null=True)  # Field name made lowercase.
    fa_mo = models.CharField(db_column='FA_MO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    addr = models.CharField(db_column='ADDR', max_length=70, blank=True, null=True)  # Field name made lowercase.
    career = models.CharField(db_column='CAREER', max_length=70, blank=True, null=True)  # Field name made lowercase.
    career2 = models.CharField(db_column='CAREER2', max_length=30, blank=True, null=True)  # Field name made lowercase.
    school_ele_nm = models.CharField(db_column='SCHOOL_ELE_NM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    school_mid_nm = models.CharField(db_column='SCHOOL_MID_NM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    school_high_nm = models.CharField(db_column='SCHOOL_HIGH_NM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    school_uni_nm = models.CharField(db_column='SCHOOL_UNI_NM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    school_grad_nm = models.CharField(db_column='SCHOOL_GRAD_NM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nickname = models.CharField(db_column='NICKNAME', max_length=15, blank=True, null=True)  # Field name made lowercase.
    hobby = models.CharField(db_column='HOBBY', max_length=20, blank=True, null=True)  # Field name made lowercase.
    entry = models.CharField(db_column='ENTRY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    img1 = models.CharField(db_column='IMG1', max_length=10, blank=True, null=True)  # Field name made lowercase.
    img2 = models.CharField(db_column='IMG2', max_length=10, blank=True, null=True)  # Field name made lowercase.
    job_cd = models.SmallIntegerField(db_column='JOB_CD', blank=True, null=True)  # Field name made lowercase.
    active_cd = models.SmallIntegerField(db_column='ACTIVE_CD', blank=True, null=True)  # Field name made lowercase.
    contract_cd = models.SmallIntegerField(db_column='CONTRACT_CD', blank=True, null=True)  # Field name made lowercase.
    national_cd = models.SmallIntegerField(db_column='NATIONAL_CD', blank=True, null=True)  # Field name made lowercase.
    army_cd = models.SmallIntegerField(db_column='ARMY_CD', blank=True, null=True)  # Field name made lowercase.
    draft_me = models.CharField(db_column='DRAFT_ME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    blood_sc = models.CharField(db_column='BLOOD_SC', max_length=3, blank=True, null=True)  # Field name made lowercase.
    reg_dt = models.DateTimeField(db_column='REG_DT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        app_label = 'baseball'
        managed = False
        db_table = 'person'
        unique_together = (('gyear', 'pcode'),)


class Pitcher(models.Model):
    gmkey = models.CharField(db_column='GMKEY', primary_key=True, max_length=13)  # Field name made lowercase.
    gday = models.CharField(db_column='GDAY', max_length=8)  # Field name made lowercase.
    tb = models.CharField(db_column='TB', max_length=1, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=20, blank=True, null=True)  # Field name made lowercase.
    pcode = models.CharField(db_column='PCODE', max_length=5)  # Field name made lowercase.
    pos = models.CharField(db_column='POS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    start = models.CharField(db_column='START', max_length=3, blank=True, null=True)  # Field name made lowercase.
    quit = models.CharField(db_column='QUIT', max_length=3, blank=True, null=True)  # Field name made lowercase.
    cg = models.IntegerField(db_column='CG', blank=True, null=True)  # Field name made lowercase.
    sho = models.IntegerField(db_column='SHO', blank=True, null=True)  # Field name made lowercase.
    wls = models.CharField(db_column='WLS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    hold = models.SmallIntegerField(db_column='HOLD', blank=True, null=True)  # Field name made lowercase.
    inn = models.CharField(db_column='INN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    inn2 = models.IntegerField(db_column='INN2', blank=True, null=True)  # Field name made lowercase.
    bf = models.IntegerField(db_column='BF', blank=True, null=True)  # Field name made lowercase.
    pa = models.IntegerField(db_column='PA', blank=True, null=True)  # Field name made lowercase.
    ab = models.IntegerField(db_column='AB', blank=True, null=True)  # Field name made lowercase.
    hit = models.IntegerField(db_column='HIT', blank=True, null=True)  # Field name made lowercase.
    h2 = models.IntegerField(db_column='H2', blank=True, null=True)  # Field name made lowercase.
    h3 = models.IntegerField(db_column='H3', blank=True, null=True)  # Field name made lowercase.
    hr = models.IntegerField(db_column='HR', blank=True, null=True)  # Field name made lowercase.
    sb = models.IntegerField(db_column='SB', blank=True, null=True)  # Field name made lowercase.
    cs = models.IntegerField(db_column='CS', blank=True, null=True)  # Field name made lowercase.
    sh = models.IntegerField(db_column='SH', blank=True, null=True)  # Field name made lowercase.
    sf = models.IntegerField(db_column='SF', blank=True, null=True)  # Field name made lowercase.
    bb = models.IntegerField(db_column='BB', blank=True, null=True)  # Field name made lowercase.
    ib = models.IntegerField(db_column='IB', blank=True, null=True)  # Field name made lowercase.
    hp = models.IntegerField(db_column='HP', blank=True, null=True)  # Field name made lowercase.
    kk = models.IntegerField(db_column='KK', blank=True, null=True)  # Field name made lowercase.
    gd = models.IntegerField(db_column='GD', blank=True, null=True)  # Field name made lowercase.
    wp = models.IntegerField(db_column='WP', blank=True, null=True)  # Field name made lowercase.
    bk = models.IntegerField(db_column='BK', blank=True, null=True)  # Field name made lowercase.
    err = models.IntegerField(db_column='ERR', blank=True, null=True)  # Field name made lowercase.
    r = models.IntegerField(db_column='R', blank=True, null=True)  # Field name made lowercase.
    er = models.IntegerField(db_column='ER', blank=True, null=True)  # Field name made lowercase.
    score = models.IntegerField(db_column='SCORE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        app_label = 'baseball'
        managed = False
        db_table = 'pitcher'
        unique_together = (('gmkey', 'pcode', 'gday'),)


class Pitchrecord2011(models.Model):
    gameid = models.CharField(db_column='GAMEID', primary_key=True, max_length=13)  # Field name made lowercase.
    gyear = models.SmallIntegerField(db_column='GYEAR')  # Field name made lowercase.
    tb = models.IntegerField(db_column='TB')  # Field name made lowercase.
    inning = models.IntegerField(db_column='INNING')  # Field name made lowercase.
    at_bat = models.IntegerField(db_column='AT_BAT')  # Field name made lowercase.
    at_bat_pitch_cnt = models.IntegerField(db_column='AT_BAT_PITCH_CNT')  # Field name made lowercase.
    pitcher_league_cd = models.CharField(db_column='PITCHER_LEAGUE_CD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    pitcher_team_city = models.CharField(db_column='PITCHER_TEAM_CITY', max_length=30, blank=True, null=True)  # Field name made lowercase.
    pitcher_team_nm = models.CharField(db_column='PITCHER_TEAM_NM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    pitcher_team_cd = models.CharField(db_column='PITCHER_TEAM_CD', max_length=3, blank=True, null=True)  # Field name made lowercase.
    pitcher_first_nm = models.CharField(db_column='PITCHER_FIRST_NM', max_length=30)  # Field name made lowercase.
    pitcher_last_nm = models.CharField(db_column='PITCHER_LAST_NM', max_length=30)  # Field name made lowercase.
    pitcher_mlbid = models.CharField(db_column='PITCHER_MLBID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pitcher_guid = models.CharField(db_column='PITCHER_GUID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    batter_league_cd = models.CharField(db_column='BATTER_LEAGUE_CD', max_length=5, blank=True, null=True)  # Field name made lowercase.
    batter_team_city = models.CharField(db_column='BATTER_TEAM_CITY', max_length=30, blank=True, null=True)  # Field name made lowercase.
    batter_team_nm = models.CharField(db_column='BATTER_TEAM_NM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    batter_team_cd = models.CharField(db_column='BATTER_TEAM_CD', max_length=3, blank=True, null=True)  # Field name made lowercase.
    batter_first_nm = models.CharField(db_column='BATTER_FIRST_NM', max_length=30)  # Field name made lowercase.
    batter_last_nm = models.CharField(db_column='BATTER_LAST_NM', max_length=30)  # Field name made lowercase.
    batter_mlbid = models.IntegerField(db_column='BATTER_MLBID', blank=True, null=True)  # Field name made lowercase.
    batter_guid = models.CharField(db_column='BATTER_GUID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    stance = models.CharField(db_column='STANCE', max_length=3, blank=True, null=True)  # Field name made lowercase.
    top_sz = models.FloatField(db_column='TOP_SZ', blank=True, null=True)  # Field name made lowercase.
    top_sz_kor = models.FloatField(db_column='TOP_SZ_KOR', blank=True, null=True)  # Field name made lowercase.
    bottom_sz = models.FloatField(db_column='BOTTOM_SZ', blank=True, null=True)  # Field name made lowercase.
    bottom_sz_kor = models.FloatField(db_column='BOTTOM_SZ_KOR', blank=True, null=True)  # Field name made lowercase.
    outs = models.IntegerField(db_column='OUTS', blank=True, null=True)  # Field name made lowercase.
    balls = models.IntegerField(db_column='BALLS', blank=True, null=True)  # Field name made lowercase.
    strikes = models.IntegerField(db_column='STRIKES', blank=True, null=True)  # Field name made lowercase.
    calls = models.CharField(db_column='CALLS', max_length=30, blank=True, null=True)  # Field name made lowercase.
    umpire_mlbid = models.IntegerField(db_column='UMPIRE_MLBID', blank=True, null=True)  # Field name made lowercase.
    pitch_type = models.CharField(db_column='PITCH_TYPE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    pitch_id = models.CharField(db_column='PITCH_ID', max_length=30)  # Field name made lowercase.
    pitch_start_time = models.FloatField(db_column='PITCH_START_TIME', blank=True, null=True)  # Field name made lowercase.
    pitch_start_speed = models.FloatField(db_column='PITCH_START_SPEED', blank=True, null=True)  # Field name made lowercase.
    pitch_start_speed_kor = models.FloatField(db_column='PITCH_START_SPEED_KOR', blank=True, null=True)  # Field name made lowercase.
    pitch_end_speed = models.FloatField(db_column='PITCH_END_SPEED', blank=True, null=True)  # Field name made lowercase.
    pitch_end_speed_kor = models.FloatField(db_column='PITCH_END_SPEED_KOR', blank=True, null=True)  # Field name made lowercase.
    reported_speed = models.FloatField(db_column='REPORTED_SPEED', blank=True, null=True)  # Field name made lowercase.
    reported_speed_kor = models.FloatField(db_column='REPORTED_SPEED_KOR', blank=True, null=True)  # Field name made lowercase.
    curve_start_y = models.FloatField(db_column='CURVE_START_Y', blank=True, null=True)  # Field name made lowercase.
    curve_start_y_kor = models.FloatField(db_column='CURVE_START_Y_KOR', blank=True, null=True)  # Field name made lowercase.
    arc_break_x = models.FloatField(db_column='ARC_BREAK_X', blank=True, null=True)  # Field name made lowercase.
    arc_break_x_kor = models.FloatField(db_column='ARC_BREAK_X_KOR', blank=True, null=True)  # Field name made lowercase.
    arc_break_z = models.FloatField(db_column='ARC_BREAK_Z', blank=True, null=True)  # Field name made lowercase.
    arc_break_z_kor = models.FloatField(db_column='ARC_BREAK_Z_KOR', blank=True, null=True)  # Field name made lowercase.
    arc_break_magnitude = models.FloatField(db_column='ARC_BREAK_MAGNITUDE', blank=True, null=True)  # Field name made lowercase.
    arc_break_magnitude_kor = models.FloatField(db_column='ARC_BREAK_MAGNITUDE_KOR', blank=True, null=True)  # Field name made lowercase.
    deflection_break_x = models.FloatField(db_column='DEFLECTION_BREAK_X', blank=True, null=True)  # Field name made lowercase.
    deflection_break_x_kor = models.FloatField(db_column='DEFLECTION_BREAK_X_KOR', blank=True, null=True)  # Field name made lowercase.
    deflection_break_z = models.FloatField(db_column='DEFLECTION_BREAK_Z', blank=True, null=True)  # Field name made lowercase.
    deflection_break_z_kor = models.FloatField(db_column='DEFLECTION_BREAK_Z_KOR', blank=True, null=True)  # Field name made lowercase.
    deflection_break_magnitude = models.FloatField(db_column='DEFLECTION_BREAK_MAGNITUDE', blank=True, null=True)  # Field name made lowercase.
    deflection_break_magnitude_kor = models.FloatField(db_column='DEFLECTION_BREAK_MAGNITUDE_KOR', blank=True, null=True)  # Field name made lowercase.
    break_angle = models.FloatField(db_column='BREAK_ANGLE', blank=True, null=True)  # Field name made lowercase.
    spin_angle = models.FloatField(db_column='SPIN_ANGLE', blank=True, null=True)  # Field name made lowercase.
    spin_rate = models.FloatField(db_column='SPIN_RATE', blank=True, null=True)  # Field name made lowercase.
    cross_plate_x = models.FloatField(db_column='CROSS_PLATE_X', blank=True, null=True)  # Field name made lowercase.
    cross_plate_y = models.FloatField(db_column='CROSS_PLATE_Y', blank=True, null=True)  # Field name made lowercase.
    cross_plate_z = models.FloatField(db_column='CROSS_PLATE_Z', blank=True, null=True)  # Field name made lowercase.
    x0 = models.FloatField(db_column='X0', blank=True, null=True)  # Field name made lowercase.
    x0_kor = models.FloatField(db_column='X0_KOR', blank=True, null=True)  # Field name made lowercase.
    y0 = models.FloatField(db_column='Y0', blank=True, null=True)  # Field name made lowercase.
    y0_kor = models.FloatField(db_column='Y0_KOR', blank=True, null=True)  # Field name made lowercase.
    z0 = models.FloatField(db_column='Z0', blank=True, null=True)  # Field name made lowercase.
    z0_kor = models.FloatField(db_column='Z0_KOR', blank=True, null=True)  # Field name made lowercase.
    vx0 = models.FloatField(db_column='VX0', blank=True, null=True)  # Field name made lowercase.
    vx0_kor = models.FloatField(db_column='VX0_KOR', blank=True, null=True)  # Field name made lowercase.
    vy0 = models.FloatField(db_column='VY0', blank=True, null=True)  # Field name made lowercase.
    vy0_kor = models.FloatField(db_column='VY0_KOR', blank=True, null=True)  # Field name made lowercase.
    vz0 = models.FloatField(db_column='VZ0', blank=True, null=True)  # Field name made lowercase.
    vz0_kor = models.FloatField(db_column='VZ0_KOR', blank=True, null=True)  # Field name made lowercase.
    ax = models.FloatField(db_column='AX', blank=True, null=True)  # Field name made lowercase.
    ax_kor = models.FloatField(db_column='AX_KOR', blank=True, null=True)  # Field name made lowercase.
    ay = models.FloatField(db_column='AY', blank=True, null=True)  # Field name made lowercase.
    ay_kor = models.FloatField(db_column='AY_KOR', blank=True, null=True)  # Field name made lowercase.
    az = models.FloatField(db_column='AZ', blank=True, null=True)  # Field name made lowercase.
    az_kor = models.FloatField(db_column='AZ_KOR', blank=True, null=True)  # Field name made lowercase.
    avg_lop_error = models.FloatField(db_column='AVG_LOP_ERROR', blank=True, null=True)  # Field name made lowercase.
    avg_lop_error_kor = models.FloatField(db_column='AVG_LOP_ERROR_KOR', blank=True, null=True)  # Field name made lowercase.
    lop_error_at_plate = models.FloatField(db_column='LOP_ERROR_AT_PLATE', blank=True, null=True)  # Field name made lowercase.
    lop_error_at_plate_kor = models.FloatField(db_column='LOP_ERROR_AT_PLATE_KOR', blank=True, null=True)  # Field name made lowercase.
    mlb_break_y = models.CharField(db_column='MLB_BREAK_Y', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mlb_break_angle = models.CharField(db_column='MLB_BREAK_ANGLE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mlb_break_length = models.CharField(db_column='MLB_BREAK_LENGTH', max_length=50, blank=True, null=True)  # Field name made lowercase.
    venue_id = models.IntegerField(db_column='VENUE_ID', blank=True, null=True)  # Field name made lowercase.
    operator_first_nm = models.CharField(db_column='OPERATOR_FIRST_NM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    operator_last_nm = models.CharField(db_column='OPERATOR_LAST_NM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    inputtime = models.DateTimeField(db_column='INPUTTIME', blank=True, null=True)  # Field name made lowercase.
    inputtime_2i = models.DateTimeField(db_column='INPUTTIME_2I', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        app_label = 'baseball'
        managed = False
        db_table = 'pitchrecord_2011'
        unique_together = (('gameid', 'gyear', 'tb', 'inning', 'at_bat', 'at_bat_pitch_cnt', 'pitcher_first_nm', 'pitcher_last_nm', 'batter_first_nm', 'batter_last_nm', 'pitch_id'),)


class Pittotal(models.Model):
    pcode = models.CharField(db_column='PCODE', primary_key=True, max_length=5)  # Field name made lowercase.
    gyear = models.CharField(db_column='GYEAR', max_length=4)  # Field name made lowercase.
    team = models.CharField(db_column='TEAM', max_length=10, blank=True, null=True)  # Field name made lowercase.
    era = models.FloatField(db_column='ERA', blank=True, null=True)  # Field name made lowercase.
    gamenum = models.IntegerField(db_column='GAMENUM', blank=True, null=True)  # Field name made lowercase.
    cg = models.IntegerField(db_column='CG', blank=True, null=True)  # Field name made lowercase.
    sho = models.IntegerField(db_column='SHO', blank=True, null=True)  # Field name made lowercase.
    w = models.IntegerField(db_column='W', blank=True, null=True)  # Field name made lowercase.
    l = models.IntegerField(db_column='L', blank=True, null=True)  # Field name made lowercase.
    sv = models.IntegerField(db_column='SV', blank=True, null=True)  # Field name made lowercase.
    hold = models.PositiveIntegerField(db_column='HOLD', blank=True, null=True)  # Field name made lowercase.
    bf = models.IntegerField(db_column='BF', blank=True, null=True)  # Field name made lowercase.
    inn = models.CharField(db_column='INN', max_length=15, blank=True, null=True)  # Field name made lowercase.
    inn2 = models.IntegerField(db_column='INN2', blank=True, null=True)  # Field name made lowercase.
    hit = models.IntegerField(db_column='HIT', blank=True, null=True)  # Field name made lowercase.
    hr = models.IntegerField(db_column='HR', blank=True, null=True)  # Field name made lowercase.
    bb = models.IntegerField(db_column='BB', blank=True, null=True)  # Field name made lowercase.
    hp = models.IntegerField(db_column='HP', blank=True, null=True)  # Field name made lowercase.
    kk = models.IntegerField(db_column='KK', blank=True, null=True)  # Field name made lowercase.
    r = models.IntegerField(db_column='R', blank=True, null=True)  # Field name made lowercase.
    er = models.IntegerField(db_column='ER', blank=True, null=True)  # Field name made lowercase.
    score = models.IntegerField(db_column='SCORE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        app_label = 'baseball'
        managed = False
        db_table = 'pittotal'
        unique_together = (('pcode', 'gyear'),)


class PittypeHitterStats(models.Model):
    gyear = models.SmallIntegerField(db_column='GYEAR')  # Field name made lowercase.
    hitter = models.CharField(db_column='HITTER', primary_key=True, max_length=10)  # Field name made lowercase.
    team = models.CharField(db_column='TEAM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    hitname = models.CharField(db_column='HITNAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lab = models.SmallIntegerField(db_column='LAB', blank=True, null=True)  # Field name made lowercase.
    lhit = models.SmallIntegerField(db_column='LHIT', blank=True, null=True)  # Field name made lowercase.
    lrun = models.SmallIntegerField(db_column='LRUN', blank=True, null=True)  # Field name made lowercase.
    lrbi = models.SmallIntegerField(db_column='LRBI', blank=True, null=True)  # Field name made lowercase.
    lhr = models.SmallIntegerField(db_column='LHR', blank=True, null=True)  # Field name made lowercase.
    lbb = models.SmallIntegerField(db_column='LBB', blank=True, null=True)  # Field name made lowercase.
    lkk = models.SmallIntegerField(db_column='LKK', blank=True, null=True)  # Field name made lowercase.
    rab = models.SmallIntegerField(db_column='RAB', blank=True, null=True)  # Field name made lowercase.
    rhit = models.SmallIntegerField(db_column='RHIT', blank=True, null=True)  # Field name made lowercase.
    rrun = models.SmallIntegerField(db_column='RRUN', blank=True, null=True)  # Field name made lowercase.
    rrbi = models.SmallIntegerField(db_column='RRBI', blank=True, null=True)  # Field name made lowercase.
    rhr = models.SmallIntegerField(db_column='RHR', blank=True, null=True)  # Field name made lowercase.
    rbb = models.SmallIntegerField(db_column='RBB', blank=True, null=True)  # Field name made lowercase.
    rkk = models.SmallIntegerField(db_column='RKK', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        app_label = 'baseball'
        managed = False
        db_table = 'pittype_hitter_stats'
        unique_together = (('hitter', 'gyear'),)


class PlayerInjury(models.Model):
    pcode = models.CharField(db_column='PCODE', primary_key=True, max_length=10)  # Field name made lowercase.
    injury_start_dt = models.CharField(db_column='INJURY_START_DT', max_length=8)  # Field name made lowercase.
    injury_part_id = models.IntegerField(db_column='INJURY_PART_ID')  # Field name made lowercase.
    t_id = models.CharField(db_column='T_ID', max_length=2)  # Field name made lowercase.
    injury_id = models.IntegerField(db_column='INJURY_ID')  # Field name made lowercase.
    ocsy_id = models.IntegerField(db_column='OCSY_ID')  # Field name made lowercase.
    injury_end_dt = models.CharField(db_column='INJURY_END_DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    injury_side_sc = models.CharField(db_column='INJURY_SIDE_SC', max_length=1, blank=True, null=True)  # Field name made lowercase.
    injury_level_id = models.IntegerField(db_column='INJURY_LEVEL_ID', blank=True, null=True)  # Field name made lowercase.
    ocme_id = models.IntegerField(db_column='OCME_ID', blank=True, null=True)  # Field name made lowercase.
    cure_id = models.IntegerField(db_column='CURE_ID', blank=True, null=True)  # Field name made lowercase.
    recurrence_ck = models.TextField(db_column='RECURRENCE_CK', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sub_p_id = models.CharField(db_column='SUB_P_ID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    entry_off_dt = models.CharField(db_column='ENTRY_OFF_DT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    now_state_id = models.IntegerField(db_column='NOW_STATE_ID', blank=True, null=True)  # Field name made lowercase.
    etc_me = models.CharField(db_column='ETC_ME', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    reg_dt = models.DateTimeField(db_column='REG_DT')  # Field name made lowercase.

    class Meta:
        app_label = 'baseball'
        managed = False
        db_table = 'player_injury'
        unique_together = (('pcode', 'injury_start_dt', 'injury_part_id'),)


class PsHitter(models.Model):
    gmkey = models.CharField(db_column='GMKEY', primary_key=True, max_length=13)  # Field name made lowercase.
    gday = models.CharField(db_column='GDAY', max_length=8)  # Field name made lowercase.
    tb = models.CharField(db_column='TB', max_length=1)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=10)  # Field name made lowercase.
    pcode = models.CharField(db_column='PCODE', max_length=10)  # Field name made lowercase.
    turn = models.CharField(db_column='TURN', max_length=5, blank=True, null=True)  # Field name made lowercase.
    oneturn = models.CharField(db_column='ONETURN', max_length=5, blank=True, null=True)  # Field name made lowercase.
    pa = models.IntegerField(db_column='PA')  # Field name made lowercase.
    ab = models.IntegerField(db_column='AB')  # Field name made lowercase.
    rbi = models.IntegerField(db_column='RBI')  # Field name made lowercase.
    run = models.IntegerField(db_column='RUN')  # Field name made lowercase.
    hit = models.IntegerField(db_column='HIT')  # Field name made lowercase.
    h2 = models.IntegerField(db_column='H2')  # Field name made lowercase.
    h3 = models.IntegerField(db_column='H3')  # Field name made lowercase.
    hr = models.IntegerField(db_column='HR')  # Field name made lowercase.
    sb = models.IntegerField(db_column='SB')  # Field name made lowercase.
    cs = models.IntegerField(db_column='CS')  # Field name made lowercase.
    sh = models.IntegerField(db_column='SH')  # Field name made lowercase.
    sf = models.IntegerField(db_column='SF')  # Field name made lowercase.
    bb = models.IntegerField(db_column='BB')  # Field name made lowercase.
    ib = models.IntegerField(db_column='IB')  # Field name made lowercase.
    hp = models.IntegerField(db_column='HP')  # Field name made lowercase.
    kk = models.IntegerField(db_column='KK')  # Field name made lowercase.
    gd = models.IntegerField(db_column='GD')  # Field name made lowercase.
    err = models.IntegerField(db_column='ERR')  # Field name made lowercase.
    lob = models.IntegerField(db_column='LOB')  # Field name made lowercase.
    score = models.IntegerField(db_column='SCORE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        app_label = 'baseball'
        managed = False
        db_table = 'ps_hitter'
        unique_together = (('gmkey', 'pcode'),)


class PsPitcher(models.Model):
    gmeky = models.CharField(db_column='GMEKY', max_length=13)  # Field name made lowercase.
    gday = models.CharField(db_column='GDAY', max_length=8, blank=True, null=True)  # Field name made lowercase.
    tb = models.CharField(db_column='TB', max_length=1, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pcode = models.CharField(db_column='PCODE', max_length=10)  # Field name made lowercase.
    pos = models.CharField(db_column='POS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    start = models.IntegerField(db_column='START', blank=True, null=True)  # Field name made lowercase.
    quit = models.IntegerField(db_column='QUIT', blank=True, null=True)  # Field name made lowercase.
    cg = models.IntegerField(db_column='CG')  # Field name made lowercase.
    sho = models.IntegerField(db_column='SHO')  # Field name made lowercase.
    wls = models.CharField(db_column='WLS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    hold = models.SmallIntegerField(db_column='HOLD')  # Field name made lowercase.
    inn = models.CharField(db_column='INN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    inn2 = models.IntegerField(db_column='INN2')  # Field name made lowercase.
    bf = models.IntegerField(db_column='BF')  # Field name made lowercase.
    pa = models.IntegerField(db_column='PA')  # Field name made lowercase.
    ab = models.IntegerField(db_column='AB')  # Field name made lowercase.
    hit = models.IntegerField(db_column='HIT')  # Field name made lowercase.
    h2 = models.IntegerField(db_column='H2')  # Field name made lowercase.
    h3 = models.IntegerField(db_column='H3')  # Field name made lowercase.
    hr = models.IntegerField(db_column='HR')  # Field name made lowercase.
    sb = models.IntegerField(db_column='SB')  # Field name made lowercase.
    cs = models.IntegerField(db_column='CS')  # Field name made lowercase.
    sh = models.IntegerField(db_column='SH')  # Field name made lowercase.
    sf = models.IntegerField(db_column='SF')  # Field name made lowercase.
    bb = models.IntegerField(db_column='BB')  # Field name made lowercase.
    ib = models.IntegerField(db_column='IB')  # Field name made lowercase.
    hp = models.IntegerField(db_column='HP')  # Field name made lowercase.
    kk = models.IntegerField(db_column='KK')  # Field name made lowercase.
    gd = models.IntegerField(db_column='GD')  # Field name made lowercase.
    wp = models.IntegerField(db_column='WP')  # Field name made lowercase.
    bk = models.IntegerField(db_column='BK')  # Field name made lowercase.
    err = models.IntegerField(db_column='ERR')  # Field name made lowercase.
    r = models.IntegerField(db_column='R')  # Field name made lowercase.
    er = models.IntegerField(db_column='ER')  # Field name made lowercase.
    score = models.IntegerField(db_column='SCORE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        app_label = 'baseball'
        managed = False
        db_table = 'ps_pitcher'


class PsSchedule(models.Model):
    g_id = models.CharField(db_column='G_ID', primary_key=True, max_length=13)  # Field name made lowercase.
    sr_id = models.IntegerField(db_column='SR_ID')  # Field name made lowercase.
    g_dt = models.CharField(db_column='G_DT', max_length=8)  # Field name made lowercase.
    g_week = models.CharField(db_column='G_WEEK', max_length=2, blank=True, null=True)  # Field name made lowercase.
    a_id = models.CharField(db_column='A_ID', max_length=2)  # Field name made lowercase.
    a_nm = models.CharField(db_column='A_NM', max_length=5)  # Field name made lowercase.
    h_id = models.CharField(db_column='H_ID', max_length=2)  # Field name made lowercase.
    h_nm = models.CharField(db_column='H_NM', max_length=3)  # Field name made lowercase.
    s_id = models.CharField(db_column='S_ID', max_length=5, blank=True, null=True)  # Field name made lowercase.
    s_nm = models.CharField(db_column='S_NM', max_length=5, blank=True, null=True)  # Field name made lowercase.
    dh_id = models.IntegerField(db_column='DH_ID')  # Field name made lowercase.
    a_pit_cd = models.IntegerField(db_column='A_PIT_CD', blank=True, null=True)  # Field name made lowercase.
    h_pit_cd = models.IntegerField(db_column='H_PIT_CD', blank=True, null=True)  # Field name made lowercase.
    g_tm = models.CharField(db_column='G_TM', max_length=10, blank=True, null=True)  # Field name made lowercase.
    a_score_cn = models.IntegerField(db_column='A_SCORE_CN')  # Field name made lowercase.
    h_score_cn = models.IntegerField(db_column='H_SCORE_CN')  # Field name made lowercase.

    class Meta:
        app_label = 'baseball'
        managed = False
        db_table = 'ps_schedule'


class Score(models.Model):
    gmkey = models.CharField(db_column='GMKEY', primary_key=True, max_length=13)  # Field name made lowercase.
    gday = models.CharField(db_column='GDAY', max_length=8)  # Field name made lowercase.
    number_1t = models.IntegerField(db_column='1T', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1b = models.IntegerField(db_column='1B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2t = models.IntegerField(db_column='2T', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2b = models.IntegerField(db_column='2B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3t = models.IntegerField(db_column='3T', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3b = models.IntegerField(db_column='3B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_4t = models.IntegerField(db_column='4T', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_4b = models.IntegerField(db_column='4B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_5t = models.IntegerField(db_column='5T', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_5b = models.IntegerField(db_column='5B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_6t = models.IntegerField(db_column='6T', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_6b = models.IntegerField(db_column='6B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_7t = models.IntegerField(db_column='7T', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_7b = models.IntegerField(db_column='7B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_8t = models.IntegerField(db_column='8T', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_8b = models.IntegerField(db_column='8B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_9t = models.IntegerField(db_column='9T', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_9b = models.IntegerField(db_column='9B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_10t = models.IntegerField(db_column='10T', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_10b = models.IntegerField(db_column='10B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_11t = models.IntegerField(db_column='11T', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_11b = models.IntegerField(db_column='11B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_12t = models.IntegerField(db_column='12T', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_12b = models.IntegerField(db_column='12B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_13t = models.IntegerField(db_column='13T', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_13b = models.IntegerField(db_column='13B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_14t = models.IntegerField(db_column='14T', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_14b = models.IntegerField(db_column='14B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_15t = models.IntegerField(db_column='15T', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_15b = models.IntegerField(db_column='15B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_16t = models.IntegerField(db_column='16T', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_16b = models.IntegerField(db_column='16B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_17t = models.IntegerField(db_column='17T', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_17b = models.IntegerField(db_column='17B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_18t = models.IntegerField(db_column='18T', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_18b = models.IntegerField(db_column='18B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_19t = models.IntegerField(db_column='19T', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_19b = models.IntegerField(db_column='19B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_20t = models.IntegerField(db_column='20T', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_20b = models.IntegerField(db_column='20B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_21t = models.IntegerField(db_column='21T', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_21b = models.IntegerField(db_column='21B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_22t = models.IntegerField(db_column='22T', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_22b = models.IntegerField(db_column='22B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_23t = models.IntegerField(db_column='23T', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_23b = models.IntegerField(db_column='23B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_24t = models.IntegerField(db_column='24T', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_24b = models.IntegerField(db_column='24B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_25t = models.IntegerField(db_column='25T', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_25b = models.IntegerField(db_column='25B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    tpoint = models.IntegerField(db_column='TPOINT', blank=True, null=True)  # Field name made lowercase.
    bpoint = models.IntegerField(db_column='BPOINT', blank=True, null=True)  # Field name made lowercase.
    thit = models.IntegerField(db_column='THIT', blank=True, null=True)  # Field name made lowercase.
    bhit = models.IntegerField(db_column='BHIT', blank=True, null=True)  # Field name made lowercase.
    terr = models.IntegerField(db_column='TERR', blank=True, null=True)  # Field name made lowercase.
    berr = models.IntegerField(db_column='BERR', blank=True, null=True)  # Field name made lowercase.
    tbbhp = models.IntegerField(db_column='TBBHP', blank=True, null=True)  # Field name made lowercase.
    bbbhp = models.IntegerField(db_column='BBBHP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        app_label = 'baseball'
        managed = False
        db_table = 'score'
        unique_together = (('gmkey', 'gday'),)


class SeasonHitterDirection(models.Model):
    gyear = models.SmallIntegerField(db_column='GYEAR', primary_key=True)  # Field name made lowercase.
    pcode = models.IntegerField(db_column='PCODE')  # Field name made lowercase.
    left_rt = models.FloatField(db_column='LEFT_RT', blank=True, null=True)  # Field name made lowercase.
    center_rt = models.FloatField(db_column='CENTER_RT', blank=True, null=True)  # Field name made lowercase.
    right_rt = models.FloatField(db_column='RIGHT_RT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        app_label = 'baseball'
        managed = False
        db_table = 'season_hitter_direction'
        unique_together = (('gyear', 'pcode'),)


class SeasonHitterHotzone(models.Model):
    gyear = models.SmallIntegerField(db_column='GYEAR', primary_key=True)  # Field name made lowercase.
    pcode = models.IntegerField(db_column='PCODE')  # Field name made lowercase.
    zone_no = models.IntegerField(db_column='ZONE_NO')  # Field name made lowercase.
    hra_rt = models.FloatField(db_column='HRA_RT', blank=True, null=True)  # Field name made lowercase.
    kk_cn = models.IntegerField(db_column='KK_CN', blank=True, null=True)  # Field name made lowercase.
    kk_rt = models.IntegerField(db_column='KK_RT', blank=True, null=True)  # Field name made lowercase.
    pit_cn = models.IntegerField(db_column='PIT_CN', blank=True, null=True)  # Field name made lowercase.
    pit_rt = models.IntegerField(db_column='PIT_RT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        app_label = 'baseball'
        managed = False
        db_table = 'season_hitter_hotzone'
        unique_together = (('gyear', 'pcode', 'zone_no'),)


class SeasonHitterVspitcher(models.Model):
    gyear = models.SmallIntegerField(db_column='GYEAR', primary_key=True)  # Field name made lowercase.
    hitter = models.IntegerField(db_column='HITTER')  # Field name made lowercase.
    pitcher = models.IntegerField(db_column='PITCHER')  # Field name made lowercase.
    pa_cn = models.IntegerField(db_column='PA_CN', blank=True, null=True)  # Field name made lowercase.
    ab_cn = models.IntegerField(db_column='AB_CN', blank=True, null=True)  # Field name made lowercase.
    hit_cn = models.IntegerField(db_column='HIT_CN', blank=True, null=True)  # Field name made lowercase.
    h2_cn = models.IntegerField(db_column='H2_CN', blank=True, null=True)  # Field name made lowercase.
    h3_cn = models.IntegerField(db_column='H3_CN', blank=True, null=True)  # Field name made lowercase.
    hr_cn = models.IntegerField(db_column='HR_CN', blank=True, null=True)  # Field name made lowercase.
    rbi_cn = models.IntegerField(db_column='RBI_CN', blank=True, null=True)  # Field name made lowercase.
    bbhp_cn = models.IntegerField(db_column='BBHP_CN', blank=True, null=True)  # Field name made lowercase.
    kk_cn = models.IntegerField(db_column='KK_CN', blank=True, null=True)  # Field name made lowercase.
    gd_cn = models.IntegerField(db_column='GD_CN', blank=True, null=True)  # Field name made lowercase.
    hra_rt = models.FloatField(db_column='HRA_RT', blank=True, null=True)  # Field name made lowercase.
    obp_rt = models.FloatField(db_column='OBP_RT', blank=True, null=True)  # Field name made lowercase.
    slg_rt = models.FloatField(db_column='SLG_RT', blank=True, null=True)  # Field name made lowercase.
    ops_rt = models.FloatField(db_column='OPS_RT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        app_label = 'baseball'
        managed = False
        db_table = 'season_hitter_vspitcher'
        unique_together = (('gyear', 'hitter', 'pitcher'),)


class SeasonLeaguePitkind(models.Model):
    gyear = models.SmallIntegerField(db_column='GYEAR', primary_key=True)  # Field name made lowercase.
    pitkind_sc = models.CharField(db_column='PITKIND_SC', max_length=10)  # Field name made lowercase.
    speed_va = models.FloatField(db_column='SPEED_VA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        app_label = 'baseball'
        managed = False
        db_table = 'season_league_pitkind'
        unique_together = (('gyear', 'pitkind_sc'),)


class SeasonPitcherHotzone(models.Model):
    gyear = models.SmallIntegerField(db_column='GYEAR', primary_key=True)  # Field name made lowercase.
    pcode = models.IntegerField(db_column='PCODE')  # Field name made lowercase.
    zone_no = models.IntegerField(db_column='ZONE_NO')  # Field name made lowercase.
    hra_rt = models.FloatField(db_column='HRA_RT', blank=True, null=True)  # Field name made lowercase.
    kk_cn = models.IntegerField(db_column='KK_CN', blank=True, null=True)  # Field name made lowercase.
    kk_rt = models.IntegerField(db_column='KK_RT', blank=True, null=True)  # Field name made lowercase.
    pit_cn = models.IntegerField(db_column='PIT_CN', blank=True, null=True)  # Field name made lowercase.
    pit_rt = models.IntegerField(db_column='PIT_RT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        app_label = 'baseball'
        managed = False
        db_table = 'season_pitcher_hotzone'
        unique_together = (('gyear', 'pcode', 'zone_no'),)


class SeasonPitcherPitkind(models.Model):
    gyear = models.SmallIntegerField(db_column='GYEAR', primary_key=True)  # Field name made lowercase.
    pcode = models.IntegerField(db_column='PCODE')  # Field name made lowercase.
    pitkind_sc = models.CharField(db_column='PITKIND_SC', max_length=10)  # Field name made lowercase.
    speed_va = models.FloatField(db_column='SPEED_VA', blank=True, null=True)  # Field name made lowercase.
    pit_rt = models.FloatField(db_column='PIT_RT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        app_label = 'baseball'
        managed = False
        db_table = 'season_pitcher_pitkind'
        unique_together = (('gyear', 'pcode', 'pitkind_sc'),)


class SeasonPlayerDefen(models.Model):
    gyear = models.SmallIntegerField(db_column='GYEAR', primary_key=True)  # Field name made lowercase.
    pcode = models.IntegerField(db_column='PCODE')  # Field name made lowercase.
    pos_sc = models.CharField(db_column='POS_SC', max_length=1)  # Field name made lowercase.
    po_cn = models.IntegerField(db_column='PO_CN', blank=True, null=True)  # Field name made lowercase.
    ass_cn = models.IntegerField(db_column='ASS_CN', blank=True, null=True)  # Field name made lowercase.
    gdp_cn = models.IntegerField(db_column='GDP_CN', blank=True, null=True)  # Field name made lowercase.
    fpct_rt = models.FloatField(db_column='FPCT_RT', blank=True, null=True)  # Field name made lowercase.
    pb_cn = models.IntegerField(db_column='PB_CN', blank=True, null=True)  # Field name made lowercase.
    sb_cn = models.IntegerField(db_column='SB_CN', blank=True, null=True)  # Field name made lowercase.
    cs_cn = models.IntegerField(db_column='CS_CN', blank=True, null=True)  # Field name made lowercase.
    cs_rt = models.FloatField(db_column='CS_RT', blank=True, null=True)  # Field name made lowercase.
    poff_cn = models.IntegerField(db_column='POFF_CN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        app_label = 'baseball'
        managed = False
        db_table = 'season_player_defen'
        unique_together = (('gyear', 'pcode', 'pos_sc'),)


class SeasonPlayerWar(models.Model):
    gyear = models.SmallIntegerField(db_column='GYEAR', primary_key=True)  # Field name made lowercase.
    pcode = models.IntegerField(db_column='PCODE')  # Field name made lowercase.
    war_rt = models.FloatField(db_column='WAR_RT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        app_label = 'baseball'
        managed = False
        db_table = 'season_player_war'
        unique_together = (('gyear', 'pcode'),)


class Stadium(models.Model):
    gyear = models.IntegerField(db_column='GYEAR', primary_key=True)  # Field name made lowercase.
    stadiumcd = models.CharField(db_column='STADIUMCD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    stadiumid = models.IntegerField(db_column='STADIUMID')  # Field name made lowercase.
    stadiumname = models.CharField(db_column='STADIUMNAME', max_length=10, blank=True, null=True)  # Field name made lowercase.
    stadium_full_name = models.CharField(db_column='STADIUM_FULL_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    area = models.CharField(db_column='AREA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    leftlen = models.SmallIntegerField(db_column='LEFTLEN', blank=True, null=True)  # Field name made lowercase.
    centerlen = models.SmallIntegerField(db_column='CENTERLEN', blank=True, null=True)  # Field name made lowercase.
    rightlen = models.SmallIntegerField(db_column='RIGHTLEN', blank=True, null=True)  # Field name made lowercase.
    capacity = models.IntegerField(db_column='CAPACITY', blank=True, null=True)  # Field name made lowercase.
    left_center_len = models.SmallIntegerField(db_column='LEFT_CENTER_LEN', blank=True, null=True)  # Field name made lowercase.
    right_center_len = models.SmallIntegerField(db_column='RIGHT_CENTER_LEN', blank=True, null=True)  # Field name made lowercase.
    height = models.DecimalField(db_column='HEIGHT', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    infiled_green = models.CharField(db_column='INFILED_GREEN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    outfiled_green = models.CharField(db_column='OUTFILED_GREEN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dimension = models.IntegerField(db_column='DIMENSION', blank=True, null=True)  # Field name made lowercase.
    style = models.CharField(db_column='STYLE', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        app_label = 'baseball'
        managed = False
        db_table = 'stadium'
        unique_together = (('gyear', 'stadiumid'),)


class StatsCdDetail(models.Model):
    cd_se = models.IntegerField(db_column='CD_SE')  # Field name made lowercase.
    cm_se = models.IntegerField(db_column='CM_SE')  # Field name made lowercase.
    cd_nm = models.CharField(db_column='CD_NM', max_length=50)  # Field name made lowercase.
    join_cd = models.CharField(db_column='JOIN_CD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    reg_dt = models.DateTimeField(db_column='REG_DT')  # Field name made lowercase.

    class Meta:
        app_label = 'baseball'
        managed = False
        db_table = 'stats_cd_detail'


class StatsGameTsPit(models.Model):
    le_id = models.SmallIntegerField(db_column='LE_ID', primary_key=True)  # Field name made lowercase.
    sr_id = models.SmallIntegerField(db_column='SR_ID')  # Field name made lowercase.
    g_id = models.CharField(db_column='G_ID', max_length=13)  # Field name made lowercase.
    pit_id = models.CharField(db_column='PIT_ID', max_length=13)  # Field name made lowercase.
    season_id = models.SmallIntegerField(db_column='SEASON_ID')  # Field name made lowercase.
    inn_no = models.IntegerField(db_column='INN_NO')  # Field name made lowercase.
    bat_around_no = models.IntegerField(db_column='BAT_AROUND_NO')  # Field name made lowercase.
    tb_sc = models.CharField(db_column='TB_SC', max_length=1)  # Field name made lowercase.
    t_id = models.CharField(db_column='T_ID', max_length=2)  # Field name made lowercase.
    bat_p_id = models.IntegerField(db_column='BAT_P_ID')  # Field name made lowercase.
    bat_order_no = models.IntegerField(db_column='BAT_ORDER_NO')  # Field name made lowercase.
    bat_pa_no = models.IntegerField(db_column='BAT_PA_NO')  # Field name made lowercase.
    pit_p_id = models.IntegerField(db_column='PIT_P_ID')  # Field name made lowercase.
    pit_no = models.SmallIntegerField(db_column='PIT_NO')  # Field name made lowercase.
    pa_pit_no = models.IntegerField(db_column='PA_PIT_NO')  # Field name made lowercase.
    pit_kind_cd = models.IntegerField(db_column='PIT_KIND_CD')  # Field name made lowercase.
    pit_result_sc = models.CharField(db_column='PIT_RESULT_SC', max_length=1)  # Field name made lowercase.
    sz_top_va = models.FloatField(db_column='SZ_TOP_VA', blank=True, null=True)  # Field name made lowercase.
    sz_bottom_va = models.FloatField(db_column='SZ_BOTTOM_VA', blank=True, null=True)  # Field name made lowercase.
    pit_course_sc = models.CharField(db_column='PIT_COURSE_SC', max_length=1, blank=True, null=True)  # Field name made lowercase.
    pit_course_no = models.IntegerField(db_column='PIT_COURSE_NO', blank=True, null=True)  # Field name made lowercase.
    pit_start_speed_va = models.FloatField(db_column='PIT_START_SPEED_VA', blank=True, null=True)  # Field name made lowercase.
    rpoint_x_va = models.FloatField(db_column='RPOINT_X_VA', blank=True, null=True)  # Field name made lowercase.
    rpoint_z_va = models.FloatField(db_column='RPOINT_Z_VA', blank=True, null=True)  # Field name made lowercase.
    rpoint_speed_x_va = models.FloatField(db_column='RPOINT_SPEED_X_VA', blank=True, null=True)  # Field name made lowercase.
    rpoint_speed_y_va = models.FloatField(db_column='RPOINT_SPEED_Y_VA', blank=True, null=True)  # Field name made lowercase.
    rpoint_speed_z_va = models.FloatField(db_column='RPOINT_SPEED_Z_VA', blank=True, null=True)  # Field name made lowercase.
    rpoint_accel_x_va = models.FloatField(db_column='RPOINT_ACCEL_X_VA', blank=True, null=True)  # Field name made lowercase.
    rpoint_accel_y_va = models.FloatField(db_column='RPOINT_ACCEL_Y_VA', blank=True, null=True)  # Field name made lowercase.
    rpoint_accel_z_va = models.FloatField(db_column='RPOINT_ACCEL_Z_VA', blank=True, null=True)  # Field name made lowercase.
    movement_x_va = models.FloatField(db_column='MOVEMENT_X_VA', blank=True, null=True)  # Field name made lowercase.
    movement_z_va = models.FloatField(db_column='MOVEMENT_Z_VA', blank=True, null=True)  # Field name made lowercase.
    spin_rt = models.FloatField(db_column='SPIN_RT', blank=True, null=True)  # Field name made lowercase.
    location_x_va = models.FloatField(db_column='LOCATION_X_VA', blank=True, null=True)  # Field name made lowercase.
    location_z_va = models.FloatField(db_column='LOCATION_Z_VA', blank=True, null=True)  # Field name made lowercase.
    pit_drop_va = models.FloatField(db_column='PIT_DROP_VA', blank=True, null=True)  # Field name made lowercase.
    cat_p_id = models.IntegerField(db_column='CAT_P_ID')  # Field name made lowercase.
    how_id = models.CharField(db_column='HOW_ID', max_length=2, blank=True, null=True)  # Field name made lowercase.
    field_if = models.CharField(db_column='FIELD_IF', max_length=20, blank=True, null=True)  # Field name made lowercase.
    place_sc = models.CharField(db_column='PLACE_SC', max_length=1, blank=True, null=True)  # Field name made lowercase.
    before_strike_cn = models.IntegerField(db_column='BEFORE_STRIKE_CN')  # Field name made lowercase.
    before_ball_cn = models.IntegerField(db_column='BEFORE_BALL_CN')  # Field name made lowercase.
    out_cn = models.IntegerField(db_column='OUT_CN')  # Field name made lowercase.
    away_score_cn = models.IntegerField(db_column='AWAY_SCORE_CN')  # Field name made lowercase.
    home_score_cn = models.IntegerField(db_column='HOME_SCORE_CN')  # Field name made lowercase.
    before_runner_cn = models.IntegerField(db_column='BEFORE_RUNNER_CN', blank=True, null=True)  # Field name made lowercase.
    before_runner_sc = models.IntegerField(db_column='BEFORE_RUNNER_SC', blank=True, null=True)  # Field name made lowercase.
    reg_dt = models.DateTimeField(db_column='REG_DT')  # Field name made lowercase.

    class Meta:
        app_label = 'baseball'
        managed = False
        db_table = 'stats_game_ts_pit'
        unique_together = (('le_id', 'sr_id', 'g_id', 'pit_id'),)


class TeamName(models.Model):
    team = models.CharField(primary_key=True, max_length=2)
    team_kor = models.CharField(max_length=10)

    class Meta:
        app_label = 'baseball'
        managed = False
        db_table = 'team_name'
        unique_together = (('team', 'team_kor'),)


class Teamrank(models.Model):
    gyear = models.CharField(db_column='GYEAR', primary_key=True, max_length=4)  # Field name made lowercase.
    rank = models.IntegerField(db_column='RANK')  # Field name made lowercase.
    league = models.CharField(db_column='LEAGUE', max_length=5, blank=True, null=True)  # Field name made lowercase.
    team = models.CharField(db_column='TEAM', max_length=12)  # Field name made lowercase.
    game = models.IntegerField(db_column='GAME', blank=True, null=True)  # Field name made lowercase.
    win = models.IntegerField(db_column='WIN', blank=True, null=True)  # Field name made lowercase.
    lose = models.IntegerField(db_column='LOSE', blank=True, null=True)  # Field name made lowercase.
    same = models.IntegerField(db_column='SAME', blank=True, null=True)  # Field name made lowercase.
    wra = models.FloatField(db_column='WRA', blank=True, null=True)  # Field name made lowercase.
    ab = models.IntegerField(db_column='AB', blank=True, null=True)  # Field name made lowercase.
    hit = models.IntegerField(db_column='HIT', blank=True, null=True)  # Field name made lowercase.
    hr = models.IntegerField(db_column='HR', blank=True, null=True)  # Field name made lowercase.
    sb = models.IntegerField(db_column='SB', blank=True, null=True)  # Field name made lowercase.
    run = models.IntegerField(db_column='RUN', blank=True, null=True)  # Field name made lowercase.
    inn = models.CharField(db_column='INN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    inn2 = models.IntegerField(db_column='INN2', blank=True, null=True)  # Field name made lowercase.
    r = models.IntegerField(db_column='R', blank=True, null=True)  # Field name made lowercase.
    er = models.IntegerField(db_column='ER', blank=True, null=True)  # Field name made lowercase.
    err = models.IntegerField(db_column='ERR', blank=True, null=True)  # Field name made lowercase.
    hra = models.CharField(db_column='HRA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lra = models.CharField(db_column='LRA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bra = models.CharField(db_column='BRA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    era = models.CharField(db_column='ERA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dra = models.CharField(db_column='DRA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    continue_field = models.CharField(db_column='CONTINUE', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    h2 = models.IntegerField(db_column='H2', blank=True, null=True)  # Field name made lowercase.
    h3 = models.IntegerField(db_column='H3', blank=True, null=True)  # Field name made lowercase.
    bb = models.IntegerField(db_column='BB', blank=True, null=True)  # Field name made lowercase.
    hp = models.IntegerField(db_column='HP', blank=True, null=True)  # Field name made lowercase.
    sf = models.IntegerField(db_column='SF', blank=True, null=True)  # Field name made lowercase.
    sort_rank = models.IntegerField(db_column='SORT_RANK', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        app_label = 'baseball'
        managed = False
        db_table = 'teamrank'
        unique_together = (('gyear', 'team', 'rank'),)


class TeamrankDaily(models.Model):
    gyear = models.CharField(db_column='GYEAR', primary_key=True, max_length=13)  # Field name made lowercase.
    rank = models.IntegerField(db_column='RANK', blank=True, null=True)  # Field name made lowercase.
    league = models.CharField(db_column='LEAGUE', max_length=13, blank=True, null=True)  # Field name made lowercase.
    team = models.CharField(db_column='TEAM', max_length=13)  # Field name made lowercase.
    game = models.IntegerField(db_column='GAME', blank=True, null=True)  # Field name made lowercase.
    win = models.IntegerField(db_column='WIN', blank=True, null=True)  # Field name made lowercase.
    lose = models.IntegerField(db_column='LOSE', blank=True, null=True)  # Field name made lowercase.
    same = models.IntegerField(db_column='SAME', blank=True, null=True)  # Field name made lowercase.
    wra = models.FloatField(db_column='WRA', blank=True, null=True)  # Field name made lowercase.
    ab = models.IntegerField(db_column='AB', blank=True, null=True)  # Field name made lowercase.
    hit = models.IntegerField(db_column='HIT', blank=True, null=True)  # Field name made lowercase.
    hr = models.IntegerField(db_column='HR', blank=True, null=True)  # Field name made lowercase.
    sb = models.IntegerField(db_column='SB', blank=True, null=True)  # Field name made lowercase.
    run = models.IntegerField(db_column='RUN', blank=True, null=True)  # Field name made lowercase.
    inn = models.CharField(db_column='INN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    inn2 = models.IntegerField(db_column='INN2', blank=True, null=True)  # Field name made lowercase.
    r = models.IntegerField(db_column='R', blank=True, null=True)  # Field name made lowercase.
    er = models.IntegerField(db_column='ER', blank=True, null=True)  # Field name made lowercase.
    err = models.IntegerField(db_column='ERR', blank=True, null=True)  # Field name made lowercase.
    hra = models.CharField(db_column='HRA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lra = models.CharField(db_column='LRA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    bra = models.CharField(db_column='BRA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    era = models.CharField(db_column='ERA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dra = models.CharField(db_column='DRA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    continue_field = models.CharField(db_column='CONTINUE', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    h2 = models.IntegerField(db_column='H2', blank=True, null=True)  # Field name made lowercase.
    h3 = models.IntegerField(db_column='H3', blank=True, null=True)  # Field name made lowercase.
    bb = models.IntegerField(db_column='BB', blank=True, null=True)  # Field name made lowercase.
    hp = models.IntegerField(db_column='HP', blank=True, null=True)  # Field name made lowercase.
    sf = models.IntegerField(db_column='SF', blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(max_length=10)

    class Meta:
        app_label = 'baseball'
        managed = False
        db_table = 'teamrank_daily'
        unique_together = (('gyear', 'team', 'date'),)
