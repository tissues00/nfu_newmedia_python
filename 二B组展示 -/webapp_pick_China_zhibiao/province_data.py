# -*- coding: utf-8 -*- 

class province_data_dict (object):

    def __init__(self, fn='data\province_code.tsv'):
       import csv
       with open(fn, 'r', encoding='utf8') as csvfile:
           reader = csv.DictReader(csvfile, fieldnames=['province_code', 'province_zh'], delimiter='\t')
           fieldnames = reader.fieldnames

           list_dict_province = []
           for row in reader:
                  list_dict_province.append(dict(row))

           self.code_zh = {d['province_code']:d['province_zh'] for d in list_dict_province}

    def country_name(self, province_code=''):
        province_zh =  self.code_zh.get(province_code, None)
        return (province_zh)