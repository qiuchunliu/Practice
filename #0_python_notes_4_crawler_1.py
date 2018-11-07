# CREATED FOR CRAWLER NOTES


def f1():
    from urllib import request
    from urllib import parse

    url = 'http://www.baidu.com/'

    def urlopen():
        res = request.urlopen('http://www.baidu.com/')
        print(res.read())  # 获取页面内容
        print(res.readline())  # 显示第一行
        print(res.readlines())  # 逐行显示返回内容
        print(res.getcode())  # 状态码

    def urlretreieve(urll):
        # 内容下载
        res = request.urlretrieve(urll, filename=None)
        # 后续可以用，比如下载音乐的时候
        return res

    def urlencode():
        parmas = {'name': '学习', 'time': 'always'}
        parmas1 = {'name': 'learn', 'time': 'always'}
        resu = parse.urlencode(parmas)
        resu1 = parse.urlencode(parmas1)
        print(resu)
        # name=%E5%AD%A6%E4%B9%A0&time=always
        # 通常网址都是这么编码中文的
        print(resu1)
        # name=learn&time=always
        # 编码英文

    def parse_qs():
        dic = {'name': '学习', 'time': 'always'}
        dic_qs = parse.urlencode(dic)
        # 编码
        re_dic_qs = parse.parse_qs(dic_qs)
        print(re_dic_qs)
        # 解码
        # {'name': ['学习'], 'time': ['always']}

    def urlparse():
        # 或者是 parse.urlsplit()
        # 结果是一样的，只不过没有 parmas
        urlll = 'https://www.baidu.com/s?wd=python'
        url_parse = parse.urlparse(urlll)
        print(url_parse)
        # ParseResult(scheme='https', netloc='www.baidu.com',
        # path='/s', params='', query='wd=python', fragment='')

    def request_requests():
        urrl = 'a link'
        head = {'headers'}
        # 设置好请求头
        req = request.Request(urrl, headers=head, data=None, method=None,
                              origin_req_host=None, unverifiable=False)
        # 这相当于对请求信息进行一个封装
        # 这个比较麻烦。。。
        resp = request.urlopen(req)
        # 这个才是请求返回的内容
        return resp

    def proxyhandler():
        # 代理的使用
        handler = request.ProxyHandler({'http': '175.155.138.207:1133'})
        opener = request.build_opener(handler)
        req = request.Request('https://www.baidu.com/')
        resp = opener.open(req)
        print(resp.read())

    urlopen()
    urlretreieve(url)
    urlencode()
    parse_qs()
    urlparse()
    request_requests()
    proxyhandler()


def f2():
    # 通过设置 cookie 可以实现登录状态的记录
    # 实现虚拟登录
    from urllib import request

    url = 'http://www.renren.com/880151247/profile'
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0',
        'Cookie': 'anonymid=jo73oup2-7mbhdy; depovince=FJ; jebecookies=f98bac52-2349-4f7'
                  '2-abc9-2b77def22f30|||||; _r01_=1; JSESSIONID=abcW_EEqFtFRefA6uaUBw; i'
                  'ck_login=6a33b3d8-136e-4d41-9b7d-c8bac5a5f7e5; jebe_key=931a5507-799'
                  '9-4fe6-bd62-7ab3a13b8c7f%7Ca022c303305d1b2ab6b5089643e4b5de%7C154159'
                  '1442485%7C1%7C1541591442005; _de=EA5778F44555C091303554EBBEB4676C696'
                  'BF75400CE19CC; p=a9b3d2156bb6bd11811381636e27a2761; first_login_fl'
                  'ag=1; ln_uact=970138074@qq.com; ln_hurl=http://hdn.xnimg.cn/photos/h'
                  'dn121/20170428/1700/main_nhiB_aebd0000854a1986.jpg; t=45d9c68156235e'
                  'bf4502538b5636a55f1; societyguester=45d9c68156235ebf4502538b5636a55f'
                  '1; id=443362311; xnsid=11fd6553; loginfrom=syshome; wp_fold=0; XNES'
                  'SESSIONID=b09c0ab67707; WebOnLineNotice_443362311=1'
    }
    # 加了 cookie 信息后，记录了登录状态。
    req = request.Request(url, headers=head)
    response = request.urlopen(req)
    # ↓写到网页文件里，便于查看
    with open('temp.html', 'w', encoding='utf-8') as fp:
        # 设置了 encoding='utf-8' 后正常显示中文了，否则乱码
        fp.write(response.read().decode('utf-8'))
    # print(response.read().decode('utf-8'))


def f3():
    # 使用 requests
    # 关于编码的解码
    import requests

    url = 'https://www.baidu.com/'
    res = requests.get(url)
    res_decode = res.content.decode('utf-8')
    # 1、对其进行解码
    res.encoding = res.apparent_encoding
    res_text = res.text
    # 2、找到编码方式后进行解码

    # 两种方式都可以
    print(res_text == res_decode)  # True


def f4():
    # 使用 params 在get() 方法里传入请求头
    import requests

    url = 'https://www.baidu.com/s'
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'
    }
    params = {
        'wd': 'python'
    }
    # 对于 get() 方法， 请求内容使用 params={}
    # 对于 post() 方法，请求使用 data={}
    res = requests.get(url, params=params, headers=head)
    with open('baidupython.html', 'w', encoding='utf-8') as ff:
        ff.write(res.content.decode('utf-8'))
        # res.content 是一个直接从服务器获取的数据，是 bytes 类型，需要解码
        # res.text 是一个解码后的数据


def f5():
    # 使用 data 在 post() 方法里传入请求头
    import requests

    url = 'https://www.lagou.com/jobs/positionAjax.json?city=北京&needAddtionalResult=false'
    head = {
        'Host': 'www.lagou.com',
        'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0',
        'X-Anit-Forge-Code': '0',
        'X-Anit-Forge-Token': 'None',
        'X-Requested-With': 'XMLHttpRequest'
    }
    data = {
        'first': 'true',
        'kd': 'python',
        'pn': '1'
    }
    # 对于 get() 方法， 请求内容使用 params={}
    # 对于 post() 方法，请求使用 data={}
    res = requests.post(url, data=data, headers=head)
    res.encoding = res.apparent_encoding
    print(res.text)
    # 返回一个字典形式的结果。含有所需信息


def f6():
    # requests 使用代理
    import requests

    url = 'http://httpbin.org/ip'
    # 代理的设置
    proxy = {
        'http': '115.223.220.29:9000'
    }

    res = requests.get(url, proxies=proxy)
    res.encoding = res.apparent_encoding
    print(res.text)
    # 返回代理的ip地址


def f7():
    pass


