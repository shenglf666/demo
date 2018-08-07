from wx_sdk.wx_sdk import wx_post_req
# 失信被执行人信息
url = 'https://way.jd.com/XinShu/executedList'
params = {
    'entityName' : '简广斌',
    'entityId' : '51022419720920149X',
    'btype' : '1',
    'appkey' : '631a176a370b187e66338657e0f9bb4a'
    }
response1 = wx_post_req( url, params )

# 个人诉讼被执行信息
url = 'https://way.jd.com/blueocean/ent_mgr_negative_performed'
params = {
    'personName' : '陈首跃',
    'idNumber' : '350425195902132635',
    'pageNo' : '1',
    'pageSize' : '10',
    'appkey' : '631a176a370b187e66338657e0f9bb4a'
    }
response2 = wx_post_req( url, params )

# 企业工商信息
url = 'https://way.jd.com/jindidata/company_info'
params = {
    'id' : '22822',
    'appkey' : '631a176a370b187e66338657e0f9bb4a'
    }
response3 = wx_post_req( url, params )

# 企业经营异常查询
url = 'https://way.jd.com/freedt/getAbnormalListByName'
params = {
    'name' : '深圳市东桥再生资源有限公司',
    'skip' : '0',
    'appkey' : '631a176a370b187e66338657e0f9bb4a'
    }
response4 = wx_post_req( url, params )

# 涉案涉诉负面信息
url = 'https://way.jd.com/Lawxin/Search'
params = {
    'stype' : '1',
    'n' : '牟宗祥',
    'id' : '370704193510140814',
    'appkey' : '631a176a370b187e66338657e0f9bb4a'
    }
response5 = wx_post_req( url, params )

# 税务负面信息查询
url = 'https://way.jd.com/XinShu/taxBlack'
params = {
    'taxName' : '苏州京奥广告传媒有限公司',
    'idCard' : '',
    'taxNo' : '',
    'appkey' : '631a176a370b187e66338657e0f9bb4a'
    }
response6 = wx_post_req( url, params )

# 企业工商年报信息
url = 'https://way.jd.com/freedt/getReportListByName'
params = {
    'keyword' : '小米科技有限责任公司',
    'appkey' : '631a176a370b187e66338657e0f9bb4a'
    }
response7 = wx_post_req( url, params )

# 企业信用等级查询
# 需要企业用户

# 企业对外投资
url = 'https://way.jd.com/hxdcdk/enterprise'
params = {
    'entName' : '小米科技有限责任公司',
    'appkey' : '631a176a370b187e66338657e0f9bb4a'
    }
response9 = wx_post_req( url, params )

# 企业新闻信息查询
url = 'https://way.jd.com/jindidata/news_info'
params = {
    'name' : '北京百度网讯科技有限公司',
    'appkey' : '631a176a370b187e66338657e0f9bb4a'
    }
response10 = wx_post_req( url, params )

# 企业图谱
url = 'https://way.jd.com/HiKnowledge/graphDetail'
bodyStr = 'allowBody=010000&allowAtts=010000' #body中的内容
params = {
    'entId' : '7bbdmDM38BxztY6vwGAla6x4tjEdaXcgk/awuZ9F+3hd/hYfFbGJfZbqdtsSH2nOVsrdiQfbGc3jvm4oLZkMNPb3W54uSCla//XXNvZk9tFBn/wc4xiicSl5cTH5n3OLsXoFY8SoTK9LoZdfOktwDlIgj2T7cXo',
    'step' : '1',
    'appkey' : '631a176a370b187e66338657e0f9bb4a'
    }
response11 = wx_post_req( url, params, bodyStr=bodyStr )

# 企业变更记录
url = 'https://way.jd.com/qixinshuzhi/ent_Change'
params = {
    'EntName' : '小米科技有限责任公司',
    'appkey' : '631a176a370b187e66338657e0f9bb4a'
    }
response12 = wx_post_req( url, params )

# 企业负面信息
url = 'https://way.jd.com/jdcredit/NegativeInfo'
params = {
    'queryString' : '小米科技有限责任公司',
    'appkey' : '631a176a370b187e66338657e0f9bb4a'
    }
response13 = wx_post_req( url, params )

# 企业主要财务指标
url = 'https://way.jd.com/inspur/getFinancialIndexsByName'
params = {
    'companyName' : '方大集团',
    'pageIndex' : '2',
    'pageSize' : '2',
    'appkey' : '631a176a370b187e66338657e0f9bb4a'
    }
response14 = wx_post_req( url, params )

# 新闻舆情数据实时搜索
url = 'https://way.jd.com/mkst/search__news'
params = {
    'startdate' : '20170106',
    'enddate' : '20170806',
    'pageno' : '1',
    'isDedup' : 'true',
    'sortType' : '0',
    'sortOrder' : '1',
    'needSummary' : 'true',
    'newsSites' : 'sohu.com,sina.com.cn',
    'negValue' : '2',
    'searchTarget' : '2',
    'newsType' : '1',
    'keys' : '("中国" AND "北京" AND "长城") OR ("慕田峪" OR "八达岭" OR "司马台")',
    'appkey' : '631a176a370b187e66338657e0f9bb4a'
    }
response15 = wx_post_req( url, params )

# 全网舆情接口
url = 'https://way.jd.com/BeijingMaoXianQiuInc/cio'
params = {
    'keywords' : '人工智能',
    'scope' : 'zhihuitem,newsitem,powechatitem,poweiboitem,toutiaoitem',
    'access_token' : 'jdwxjcloud',
    'limit' : '20',
    'offset' : '0',
    'time_gt' : '2017-11-24',
    'time_lte' : '2017-12-12',
    'appkey' : '631a176a370b187e66338657e0f9bb4a'
    }
response16 = wx_post_req( url, params )

# 新浪微舆情（应用）

print(response16.text)


