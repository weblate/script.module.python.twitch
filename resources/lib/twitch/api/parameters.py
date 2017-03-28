# -*- encoding: utf-8 -*-
from base64 import b64decode


class _Parameter(object):
    _valid = []

    @classmethod
    def validate(cls, value):
        if value in cls._valid:
            return value
        raise ValueError(value)


class Period(_Parameter):
    WEEK = 'week'
    MONTH = 'month'
    ALL = 'all'
    _valid = [WEEK, MONTH, ALL]


class Boolean(_Parameter):
    TRUE = 'true'
    FALSE = 'false'

    _valid = [TRUE, FALSE]


class Direction(_Parameter):
    DESC = 'desc'
    ASC = 'asc'

    _valid = [DESC, ASC]


class SortBy(_Parameter):
    CREATED_AT = 'created_at'
    LAST_BROADCAST = 'last_broadcast'
    LOGIN = 'login'

    _valid = [CREATED_AT, LAST_BROADCAST, LOGIN]


class VideoSort(_Parameter):
    VIEWS = 'views'
    TIME = 'time'

    _valid = [VIEWS, TIME]


class BroadcastType(_Parameter):
    ARCHIVE = 'archive'
    HIGHLIGHT = 'highlight'
    UPLOAD = 'upload'

    _valid = [ARCHIVE, HIGHLIGHT, UPLOAD]

    @classmethod
    def validate(cls, value):
        split_values = value.split(',')
        for val in split_values:
            if val not in cls._valid:
                raise ValueError(value)
        return value


class StreamType(_Parameter):
    LIVE = 'live'
    PLAYLIST = 'playlist'
    ALL = 'all'

    _valid = [LIVE, PLAYLIST, ALL]


class Cursor(_Parameter):
    @classmethod
    def validate(cls, value):
        try:
            decoded = int(b64decode(value))
            return value
        except ValueError:
            raise ValueError(value)


class Language(_Parameter):
    ALL = 'all'
    # add twitch supported language codes
    _valid = [ALL]

    @classmethod
    def validate(cls, value):
        split_values = value.split(',')
        for val in split_values:
            if val not in cls._valid:
                raise ValueError(value)
        return value


class Duration(_Parameter):
    _valid = [30, 60, 90, 120, 150, 180]
