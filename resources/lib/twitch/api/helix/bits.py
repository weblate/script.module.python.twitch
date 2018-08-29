# -*- encoding: utf-8 -*-
# https://dev.twitch.tv/docs/api/reference

from ..parameters import PeriodHelix, IntRange
from ... import keys
from ...queries import HelixQuery as Qry
from ...queries import query


# required scope: bits:read
@query
def get_bits_leaderboard(count=10, period=PeriodHelix.ALL, started_at='', user_id='', use_app_token=False):
    q = Qry('bits/leaderboard', use_app_token=use_app_token)
    q.add_param(keys.COUNT, IntRange(1, 100).validate(count), 10)
    q.add_param(keys.PERIOD, PeriodHelix.validate(period), PeriodHelix.ALL)
    if period != PeriodHelix.ALL:
        q.add_param(keys.STARTED_AT, started_at, '')
    q.add_param(keys.USER_ID, user_id, '')

    return q
