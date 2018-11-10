# qichacha_wenshu
使用scrapy框架爬取企企网站上公司的裁判文书信息
**https://www.qichacha.com/firm_576c21e3468a6b178bbf291e4820e896.html#susong**          
前面介绍了爬取企查查公司的基本信息，本次介绍公司的裁判文书信息，爬取文书信息时需要构造网页链接。         
## 正题          
&ensp;&ensp;&ensp;&ensp;点击“法律诉讼”，可以看到该内容的链接。           
![法律诉讼链接](https://github.com/wei523712/qichacha_wenshu/blob/master/image/%E8%A3%81%E5%88%A4%E6%96%87%E4%B9%A6%E9%93%BE%E6%8E%A5.png)   
<br>       </br>
&ensp;&ensp;&ensp;点击第二页发现页面链接没有变化，点击最后一页同样没有变化。              
<br>       </br>
![1页](https://github.com/wei523712/qichacha_wenshu/blob/master/image/%E7%AC%AC%E4%B8%80%E9%A1%B5.png)
![2页](https://github.com/wei523712/qichacha_wenshu/blob/master/image/%E7%AC%AC%E4%BA%8C%E9%A1%B5.png)
![206页](https://github.com/wei523712/qichacha_wenshu/blob/master/image/206%E9%A1%B5.png)           
 <br>       </br>          
&ensp;&ensp;&ensp;打开F12，点击network，清空，再次换页，点击Headers可以看到裁判文书的链接，get方法,  unique(即为网页链接中的数字)，companyname公司名，p页数，tab:susong,box:wenshu。这样便 可以构造裁判文书的链接。    
![构造](https://github.com/wei523712/qichacha_wenshu/blob/master/image/%E6%9E%84%E9%80%A0%E9%93%BE%E6%8E%A5.png)   
<br>       </br>
&ensp;&ensp;&ensp;进入构造的裁判文书的链接，可以看到如下：    
![image](https://github.com/wei523712/qichacha_wenshu/blob/master/image/%E8%BF%9B%E5%85%A5%E6%9E%84%E9%80%A0%E7%9A%84%E9%93%BE%E6%8E%A5.png)
<br>       </br>
&ensp;&ensp;&ensp;通过F12，同样可以看到进入裁判文书详情页的链接，通过xpath提取。同样，总页数可以通过xpath提取，通过正则表达式提出来     
![裁判文书详情页](https://github.com/wei523712/qichacha_wenshu/blob/master/image/%E6%8F%90%E5%8F%96%E6%96%87%E4%B9%A6%E8%AF%A6%E6%83%85%E9%A1%B5%E9%93%BE%E6%8E%A5.png)     
<br>       </br>
&ensp;&ensp;&ensp;进入裁判文书的详情页的界面如下图所示：    
![详情](https://github.com/wei523712/qichacha_wenshu/blob/master/image/%E8%AF%A6%E6%83%85%E9%A1%B5.png)
