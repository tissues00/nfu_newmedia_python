# 中山大学南方学院 2016 - 2017 
# 文学与传媒系【Python】分组项目

webapp_pick_China_zhibiao

英文项目名称webapp_pick_China_zhibiao，China指中国大陆,zhibiao意思为”指标”，就是指在中国大陆中相关资指标的说明。
# 简介 
> 中国大陆各省份不同指标查询，输入方面用户可输入想查询的指标，选取相应的省份以及年份例如（山东省，2010，地区生产总值），输出方面则是所选取的省份年份及其对应的指标数据资料，数据来源于国家数据网取得的json档。
### 指标如下：
> **地区生产总值**</br>
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

3. 後端伺服器web 响应：[pick_a_GuangDong_zhibiao.py](pick_a_GuangDong_zhibiao.py) 中 执行 了@app.route('/') 下的 entry_page()函数，以HTML模版[templates/entry.html](templates/entry.html)及一个含指标代码及名称的字典（见代码 the_list_items = c_list,the_province_list=p_list,）产出的产生《欢迎来到网上全国数据指标器》的HTML页面

4. 前端浏览器收到web 响应：出现HTML页面有HTML表单的输入 select类型，变数名称(name)为'pick_a_GuangDong_zhibao'，'user_GuangDong_place','user_GuangDong_zh_year'使用了HTML5的 select 元素，详见见HTML模版[templates/entry.html](templates/entry.html)

5. 前端浏览器web 请求：用户选取指标後按了提交钮「搞吧」，则产生新的web 请求，按照form元素中定义的method='POST' action='/pick_a_GuangDong_zhibao'，以POST为方法，动作为/pick_a_GuangDong_zhibao的web 请求

6. 後端服务器收到用户web 请求，匹配到@app.route('/pick_a_GuangDong_zhibao', methods=['POST'])的函数 pick_a_GuangDong_zhibao() 

7. [pick_a_GuangDong_zhibiao.py](pick_a_GuangDong_zhibiao.py) 中 def pick_a_GuangDong_zhibao()  函数，把用户提交的数据，以flask 模块request.form['pick_a_GuangDong_zhibao'],request.form['user_GuangDong_place'],request.form['user_GuangDong_zh_year']	取到Web 请求中，HTML表单变数名称pick_a_GuangDong_zhibao的值，存放在province_zb这Python变数下，再使用flask模块render_template 函数以[templates/results.html](templates/results.html)模版为基础（输出），其中模版中province_zb的值，用这变数之值，其他3项值如此类推。

8. 前端浏览器收到web 响应：模版中[templates/results.html](templates/results.html) 的变数值正确的产生的话，前端浏览器会收到正确响应，看到指标的相关元数据。

## 作者成员：
[见_team_/_team_.tsv](_team_/_team_.tsv)
