# qichacha_wenshu
使用scrapy框架爬取企企网站上公司的裁判文书信息
**https://www.qichacha.com/firm_576c21e3468a6b178bbf291e4820e896.html#susong**          
&ensp;&ensp;&ensp;&ensp;前面介绍了爬取企查查公司的基本信息，本次介绍公司的裁判文书信息，爬取文书信息时需要构造网页链接。         
## 正题          
&ensp;&ensp;&ensp;&ensp;点击“法律诉讼”，可以看到该内容的链接。           
![法律诉讼链接]()            
&ensp;&ensp;&ensp;&ensp；点击第二页发现页面链接没有变化，点击最后一页同样没有变化。         
![1页]()
![2页]()
![206页]()           
           
&ensp;&ensp;&ensp;&ensp；打开F12，点击network，清空，再次换页，点击Headers可以看到裁判文书的链接，get方法,  unique(即为网页链接中的数字)，companyname公司名，p页数，tab:susong,box:wenshu。这样便 可以构造裁判文书的链接。    
进入构造的裁判文书的链接，可以看到如下：    
![进入构造页]()          

&ensp;&ensp;&ensp;&ensp；通过F12，同样可以看到进入裁判文书详情页的链接，通过xpath提取。     
![裁判文书详情页]()
