import jieba
#结巴分词分为三种模式：精确模式(默认)、全模式和搜索引擎模式，下面对这三种模式分析
s = u'我想和女朋友一起去巴黎铁塔参观和闲逛'
#精确分割
cut = jieba.cut(s)
print(cut)
print(','.join(cut))

#全模式分割
#把文本尽可能的分割更多的词
print(','.join(jieba.cut(s,cut_all=True)))

#搜索引擎模式
#有从小到大的感觉
print(','.join(jieba.cut_for_search(s)))
'''
并行分词

在文本数据量非常大的时候，为了提高分词效率，开启并行分词就很有必要了。
jieba支持并行分词，基于python自带的multiprocessing模块，但要注意的是在windows环境下不支持。
用法：

#开启并行分词模式，参数为并发执行的进程数

jieba.enable_parallel(s)

#关闭并行分词模式

jieba.disable_parallel()
'''