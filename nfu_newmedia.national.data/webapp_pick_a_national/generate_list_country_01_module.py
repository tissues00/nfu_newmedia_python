# -*- coding: utf-8 -*- 
# 函数化，以备import 调用模块（module）

def get_national_name(fn='data\national.tsv'):
   import csv
   with open(fn, 'r', encoding='utf8') as csvfile:
       reader = csv.DictReader(csvfile, fieldnames=['c_code', 'c_name'], delimiter='\t')
       fieldnames = reader.fieldnames

       list_dict_national = []
       for row in reader:
          list_dict_national.append(dict(row))

       data = {d['c_code']:d['c_name'] for d in list_dict_national}
   return(data)

def national_name(c_code=''):
    d = get_national_name()
    c_name =  d.get(c_code, None)
    return (c_name)

#測試   
print (country_name('CN'))
print (country_name('SG'))
print (country_name('ZZ'))
print (country_name('ABC'))
print (country_name(''))
 
