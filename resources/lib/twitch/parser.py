# -*- encoding: utf-8 -*-
import re

from twitch.logging import log

_m3u_pattern = re.compile(
        r'#EXT-X-MEDIA:TYPE=VIDEO.*'
        r'GROUP-ID="(?P<group_id>[^"]*)",'
        r'NAME="(?P<group_name>[^"]*)"[,=\w]*\n'
        r'#EXT-X-STREAM-INF:.*\n('
        r'?P<url>http.*)')


def m3u8(f):
    def m3u8_wrapper(*args, **kwargs):
        return m3u8_to_list(f(*args, **kwargs))
    return m3u8_wrapper


def m3u8_to_dict(string):
    log.debug('m3u8_to_dict called for:\n{}'.format(string))
    d = dict()
    matches = re.finditer(_m3u_pattern, string)
    for m in matches:
        d[m.group('group_name')] = m.group('url')
        if m.group('group_id') == 'chunked':
            d.update({'Source': m.group('url')})  # ensure Source stream identified for consistency

    log.debug('m3u8_to_dict result:\n{}'.format(d))
    return d


def m3u8_to_list(string):
    log.debug('m3u8_to_list called for:\n{}'.format(string))
    l = list()
    matches = re.finditer(_m3u_pattern, string)
    chunked = None
    for m in matches:
        l.append((m.group('group_name'), m.group('url')))
        if m.group('group_id') == 'chunked':
            chunked = m.group('url')
    if (chunked) and (not any(re.match('[Ss]ource', name) for name, url in l)):
        l.insert(0, ('Source', chunked))

    log.debug('m3u8_to_list result:\n{}'.format(l))
    return l
