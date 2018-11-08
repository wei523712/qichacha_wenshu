import re
# url = 'https://www.qichacha.com/company_getinfos?unique=7e802636e7203d6229183addfc428e1e&companyname=%E5%8C%97%E4%BA%AC%E5%BC%80%E5%BF%83%E9%BA%BB%E8%8A%B1%E5%A8%B1%E4%B9%90%E6%96%87%E5%8C%96%E4%BC%A0%E5%AA%92%E8%82%A1%E4%BB%BD%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8&tab=susong&box=wenshu&p=16459656958'
# # pattern = u'(https:.+)p=1'
# pattern = u'(https:.*?p=)\d+'
# next_link = re.findall(pattern,url)
# print(next_link)
# https://www.qichacha.com/company_getinfos?
# unique=576c21e3468a6b178bbf291e4820e896
# &companyname=%E5%8C%97%E4%BA%AC%E7%99%BE%E5%BA%A6%E7%BD%91%E8%AE%AF%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8
# &p=1
# &tab=assets&box=zhuanli
# &zlpublicationyear=&zlipclist=&zlkindcode=&zllegalstatus=
# a = ['1', '2', '3', '4', '5', '>', ' ...600']
# c = []
# for i in a:
#     b = re.findall('\d+',i)
#     if b != []:
#         c.append(b[0])
# print(c)
# print(max(c))
# print(c[-1])

# from fake_useragent import UserAgent
#
# ua = UserAgent()
# print(ua.random)
# print(ua.random)
# print(ua.random)
# print(ua.random)
# print(ua.random)
# print(ua.random)
# print(ua.random)a
import chardet
# f = open('name.txt','r',encoding='utf-8')  #
# f1 = open('result2.txt','r',encoding='utf-8')
# f2 = open('result3.txt','w',encoding='utf-8')
# list = []
# for obj in f1:
#     obj = obj.strip()
#     list.append(obj)
# for obj1 in f:
#     obj1 = obj1.strip()
#     if obj1 not in list:
#         f2.write(obj1 + '\n')
