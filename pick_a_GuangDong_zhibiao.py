# -*- coding: utf-8 -*- 
# 使用模块module country
import csv
import national  
c = national.national_list_name()
c_list = [c.data[k] for k in sorted(c.data.keys())]
c_dict_reverse = {v:k for k, v in c.data.items()}


from flask import Flask, render_template, request, escape
import province_data 
p = province_data.province_data_dict()
p_dict_reverse = {v:k for k, v in p.code_zh.items()}
p_list = [k for k in p_dict_reverse.keys()]
p_dict_order = {k:v for k, v in p.code_zh.items()}



app = Flask(__name__)

@app.route('/')
@app.route('/entry')

def entry_page() -> 'html':
    """Display this webapp's HTML form."""

	
    return render_template('entry.html',
                           the_list_items = c_list, 
						   the_province_list=p_list,
                           the_title='欢迎来到全国数据指标选择器')

@app.route('/pick_a_GuangDong_zhibao', methods=['POST'])
def pick_a_GuangDong_zhibao() -> 'html':
	"""提取用户web 请求POST方法提交的数据（输入），不执行任何动作（处理），直接返回（输出）。"""	
	province_zb= request.form['user_GuangDong_zhibao']
	province_zb_pass=c_dict_reverse[province_zb]
	province_dq_ban= request.form['user_GuangDong_place']
	province_dq_pass=p_dict_reverse[province_dq_ban]
	province_sj_pass= request.form['user_GuangDong_zh_year']
	with open('fsnd_data.tsv', 'r', encoding='utf8') as data:
		line = data.readlines()
	pass_zb=[i for i in line if province_zb_pass in i]
	pass_dq=[i for i in pass_zb if province_dq_pass in i]
	pass_time=[i for i in pass_dq if province_sj_pass in i]
	pass_time_ = pass_time[0].split('\t')[1]
	
	return render_template('results.html',
                           the_title = '以下是您选取的数据：',
						   the_selsct_zb=province_zb,
						   the_selsct_dq=province_dq_ban,
						   the_selsct_sj=province_sj_pass,
                           the_national_name = pass_time_,
                           )

if __name__ == '__main__':
    app.run(debug=True)
