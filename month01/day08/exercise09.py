# 练习2：定义函数,改造 day03/exercise02  day03/exercise04
def get_course_info(number):
    '''
        获取课程内容信息介绍
    '''
    course_info = {
        '一': 'Python语言核心编程',
        '二': 'Python高级软件技术',
        '三': 'Web 全栈',
        '四': '网络爬虫',
        '五': '数据分析、人工智能'
    }
    return course_info[number] if number in course_info else "无内容"


print(get_course_info("四"))
