import re   
# text = "apple's prince $99,orange's prince is $10"
# ret = re.findall('\$\d+',text)
# print(ret)
# ret = re.sub('\$\d+',"0",text)
# print(ret)
# html ='''
# <dd class="job_bt">
#         <h3 class="description">职位描述：</h3>
#         <div class="job-detail">
#         <p>岗位职责：<br></p>
# <p>1、负责DevOps研发平台的设计、开发和优化工作；参与核心业务系统的技术规划和业务规划工作，深入理解业务需求，抽象系统模型，进行系统设计及开发工作。</p>
# <p>2、负责DevOps研发核心模块的代码开发、调试、维护工作，并协助其他开发人员解决技术问题。</p>
# <p>3、与需求方沟通需求，独立完成对需求的分析和设计工作。</p>
# <p>4、维护平台正常运行，及时排查和处理生产问题。</p>
# <p>5、在保障系统的稳定性，可维护性的基础上，快速响应业务需求。</p>
# <p>6、指导低级别工程师工作和成长。</p>
# <p><br></p>
# <p>任职条件：&nbsp;<br></p>
# <p>1、计算机或相关专业全日制本科及以上；</p>
# <p>2、精通Python开发，并具有3年以上Python开发经验，，</p>
# <p>3、熟练使用Python常用框架Django/Tornado/Flask，熟悉Restful API；</p>
# <p>4、了解分布式和微服务设计理念，熟练掌握常用的分布式开发框架，了解Kafka, Zookeeper等开源中间件。</p>
# <p>5、需具备独立数据库设计并且调优的能力；</p>
# <p>6有良好的编码习惯，对代码和设计质量有严格要求，重视Code Review</p>
# <p>7、熟悉Git，GitHub开发流程，了解敏捷开发方法和DevOps；</p>
# <p>8、具有良好的编程思想、沟通、团队合作精神、优&nbsp;&nbsp;&nbsp;&nbsp;秀的分析问题和解决问题的能力；具备强烈的责任心。</p>
#         </div>
#     </dd>
# '''
# ret = re.sub('<.+?>',"",html)
# print(ret)


# text = 'hello&world ni hao'
# ret = re.split('[^a-zA-Z]',text)
# print(ret)


# text = "the number is 20.50"
# # r = re.compile('\d+\.?\d*')
# r = re.compile(r"""
#     \d+  #小数点前面的数字
#     \.?  #小数点本身
#     \d*  #小数点后面的数字
# """,re.VERBOSE)
# ret = re.search(r,text)
# print(ret.group())
text = """
    <div class="cont">
        <div id="yizhua3b083e5700a" class="yizhu">
            <img src="https://song.gushiwen.org/siteimg/beipic.png" width="25" height="25" alt="背诵" onclick="OnBeisong('a3b083e5700a','http://m.gushiwen.org/default.aspx?page=1')" id="btnBeisonga3b083e5700a">
                <img style="display: block;" src="https://song.gushiwen.org/siteimg/shangpic.png" width="25" height="25" alt="赏析" onclick="OnShangxi('a3b083e5700a')" id="btnShangxia3b083e5700a">
                <img style="display: block;" src="https://song.gushiwen.org/siteimg/zhupic.png" width="25" height="25" alt="注释" onclick="OnZhushi('a3b083e5700a')" id="btnZhushia3b083e5700a">
                <img style="display: block;" src="https://song.gushiwen.org/siteimg/yipic.png" width="25" height="25" alt="译文" onclick="OnYiwen('a3b083e5700a')" id="btnYiwena3b083e5700a">
             
                <script type="text/javascript">
                    document.getElementById("btnShangxia3b083e5700a").style.display = "block";
                </script>
            
                <script type="text/javascript">
                    document.getElementById("btnZhushia3b083e5700a").style.display = "block";
                </script>
            
                <script type="text/javascript">
                    document.getElementById("btnYiwena3b083e5700a").style.display = "block";
                </script>
            
        </div>
        <p><a style="font-size:20px;line-height:24px; height:24px;" href="/shiwenv_a3b083e5700a.aspx"><b>牡丹</b></a></p>
        <p class="source"><a href="/shiwen/default.aspx?cstr=%e5%94%90%e4%bb%a3">唐代</a><span>：</span><a href="/search.aspx?value=%e5%be%90%e5%87%9d">徐凝</a></p>
        <div class="contson" id="contsona3b083e5700a" style="position:relative; z-index:0px;">
            何人不爱牡丹花，占断城中好物华。<br>疑是洛川神女作，千娇万态破朝霞。
        </div>
        </div>
"""
titles_re = re.compile(r'''
    <div\sclass="cont">.*?
    <b>(.*?)</b>',re.VERBOSE
''')
titles = re.search(titles_re,text,re.DOTALL)
print(titles.group())