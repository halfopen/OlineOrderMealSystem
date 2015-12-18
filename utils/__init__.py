# -*- coding: utf-8 -*-
import urllib2
import httplib
from django.http import HttpResponse
from django.utils import simplejson

def fwrite(data, filepath, listname):
    '''
    将[{}, {}, {}...]类型数据写入文件
    '''
    fout = open(filepath, 'w')
    fout.write('# -*- coding:utf-8 -*-\n')
    fout.write('%s = [\n' % listname)
    for d in data:
        fout.write('{')
        for key, val in d.items():
            val = val.replace(' ','').replace('\t', '')
            val = val.replace('\r','').replace('\n', '')
            fout.write('"%s": "%s",\n ' % (key.encode('UTF-8'), val.encode('UTF-8')))
        fout.write('},\n')
    fout.write(']')
    fout.close()


def get_json(url, time=5):
    '''从指定url获取json数据'''
    try:
        json = urllib2.urlopen(url, timeout = time)
    except:
        return {}
    return simplejson.load(json)


def render_json(dic):
    '''返回json数据'''
    json = simplejson.dumps(dic, ensure_ascii=False)
    mimetype = 'application/json'
    return HttpResponse(json, mimetype=mimetype)
