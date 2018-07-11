from urllib import request
import re

def getHtml(url):
    with request.urlopen(url) as f:
        print('Status: ', f.status, f.reason)
        html = f.read()
    #将html内容从bytes转为str
    return html.decode('utf-8')
    
def getTopic(html):
    topicRe = re.compile(r'class="topic_name">[\w“”？！]+<')
    topiclist = re.findall(topicRe, html)
    #将话题文字过滤出来
    index = 0
    for topic in topiclist:
        topiclist[index] = re.split(r'[<>]', topic)[1]
        index += 1
    return topiclist
    
if __name__ == '__main__':
    testurl = 'http://tieba.baidu.com/p/2460150866'
    html = getHtml(testurl)
    topiclist = getTopic(html)
    for topic in topiclist:
        print(topic)