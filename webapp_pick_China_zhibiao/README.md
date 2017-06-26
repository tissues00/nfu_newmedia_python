# 中山大学南方学院 2016 - 2017 
# 文学与传媒系【Python】分组项目

webapp_pick_China_zhibiao
# 简介 
> **中国各省下列指标的某个年份数据查询
###> **地区生产总值**</br>
> **互联网上网人数(万人)**</br>
> **域名数(万个)**</br>
> **网站数(万个)**</br>
> **网页数(万个)**</br>
> **互联网宽带接入端口(万个)**</br>
> **互联网拨号用户(万户)**</br>
> **互联网宽带接入用户(万户)**</br>
> **城市宽带接入用户(万户)**</br>
> **农村宽带接入用户(万户)**</br>
> **年末常住人口(万人)**</br>

## 输入：
> **用户选择全国数据指标**</br>
> **用户选择查询省**</br>
> **用户选择查询年份**</br>
 **用户选择全国数据指标**</br>


## 输出：
> **用户选择全国数据指标**</br>
> **用户选择查询省**</br>
> **用户选择查询年份**</br>
> **用户得到该指标数据**</br>



## 从输入到输出，本组作品使用了：
### 模块
* [csv](http://baike.baidu.com/link?url=2LfE8T1ayJHkQSueL6tk3jkiOWJESDWdfNr-cEp5WDkuNEJzSbRhEqgiOU39LMq1wLNBfiBpejpkm6BmEOGOdq)
* [json](http://baike.baidu.com/link?url=IDtfAkimfLYAV3WQEmPbJT3eHkPx3RFTCLYjna0UaO1pkbV0eyrNNwf5pgwNJRpDU-IVOrPGAbZaMaN9EPnuta)
* [request](http://baike.baidu.com/item/Request/10991926)
### 数据
* [简中CLDR localenames](https://github.com/unicode-cldr/cldr-localenames-modern/blob/master/main/zh-Hans/territories.json)
* fsnd_data_tsv
### API
* [github](https://api.github.com/)
## Web App动作描述

以下按web 请求（web request） - web 响应 时序说明

1. 後端伺服器启动：执行 pick_a_GuangDong_zhibiao.py 启动後端伺服器，等待web 请求。启动成功应出现：  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

2. 前端浏览器web 请求：访问 http://127.0.0.1:5000/ 启动前端web 请求

3. 後端伺服器web 响应：[pick_a_GuangDong_zhibiao.py](pick_a_GuangDong_zhibiao.py) 中 执行 了@app.route('/') 下的 entry_page()函数，以HTML模版[templates/entry.html](templates/entry.html)及一个含指标代码及名称的字典（见代码 the_list_items = meta['cname']）产出的产生《欢迎来到网上全国数据指标器说明！》的HTML页面

4. 前端浏览器收到web 响应：出现HTML页面有HTML表单的输入 input 类型(type) 为"text"，变数名称(name)为'user_zb'，使用了HTML5的datalist 定义在 list="zbs" 及 datalist标签，详见HTML模版[templates/entry.html](templates/entry.html)

5. 前端浏览器web 请求：用户选取指标後按了提交钮「搞吧」，则产生新的web 请求，按照form元素中定义的method='POST' action='/pick_a_zb'，以POST为方法，动作为/pick_a_zb的web 请求

6. 後端服务器收到用户web 请求，匹配到@app.route('/pick_a_zb', methods=['POST'])的函数 pick_a_zb() 

7. [pick_a_GuangDong_zhibiao.py](pick_a_GuangDong_zhibiao.py) 中 def pick_a_zb() 函数，把用户提交的数据，以flask 模块request.form['user_zb']	取到Web 请求中，HTML表单变数名称user_zb的值，存放在user_zb这Python变数下，再使用flask模块render_template 函数以[templates/results.html](templates/results.html)模版为基础（输出），其中模版中the_zb的值，用user_zb这变数之值，其他4项值如此类推。

8. 前端浏览器收到web 响应：模版中[templates/results.html](templates/results.html) 的变数值正确的产生的话，前端浏览器会收到正确响应，看到指标的相关元数据。

## 作者成员：
二B 冯卓然
二B 何彩红
二B 陈梓君
二B 陈铮
二B 高祖炜
二B 符浩
