# -*- coding: utf-8 -*- 
# 使用模块module country
import national
c = national.national_list_name()
c_list = [c.data[k] for k in sorted(c.data.keys())]
c_dict_reverse = {v:k for k, v in c.data.items()}


from flask import Flask, render_template, request, escape

app = Flask(__name__)

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    """Display this webapp's HTML form."""
    return render_template('entry.html',
                           the_title='欢迎来到网上 国家数据指标选择器！')

@app.route('/pick_a_GuangDong_zhibiao', methods=['POST'])
def pick_a_GuangDong_zhibiao() -> 'html':
    """提取用户web 请求POST方法提交的数据（输入），不执行任何动作（处理），直接返回（输出）。"""
    user_GuangDong_zhibiao_name = request.form['user_GuangDong_zhibiao']	
    user_GuangDong_code = c_dict_reverse[user_GuangDong_name]	
    return render_template('results.html',
                           the_title = '以下是您选取的数据：',
                           the_GuangDong_zhibiao_code = user_GuangDong_zhibiao_code,
                           the_GuangDong_zhibiao_name = user_GuangDong_zhibiao_name,
                           )

if __name__ == '__main__':
    app.run(debug=True)
