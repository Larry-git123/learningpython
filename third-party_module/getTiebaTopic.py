import requests
import re

def getHtml(url):
    f = requests.get(url)
    print('Status:', f.status_code)
    return f.text
    
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