import os
import html2text
# import jieba.analyse

h = html2text.HTML2Text()
h.ignore_links = True
h.ignore_emphasis = True

def extract(input_folder, middle_folder, output_folder, category):
    path_r = os.path.abspath(input_folder)
    path_s = os.path.abspath(middle_folder)
    path_n = os.path.abspath(output_folder)

    n = 1
    for i in os.listdir(path_r):
        print(n)
        if i.endswith('.htm') or i.startswith('20') or i.endswith('.mht'):
            fname = os.path.join(path_r,i)

            # 读取 php 文件，提取标题、时间，并转换为 markdown 文件，并使用 jieba 从标题提取关键字
            with open(fname,"r", encoding='GBK') as f:
                date = i.split(' ')[0]
                title = i.split(' ')[1].strip('.php')
                title = title.replace('[','【')
                title = title.replace(']','】')
                # tags = jieba.analyse.extract_tags(title, topK=2)
                # if len(tags) == 1:
                #     tags.append('1984')
                # elif len(tags) == 0:
                #     tags = ['1984','bbs']
                # print(tags)

                # 关键词提取效果太差，故 disable

                fname = date + '-' + title + '.md'
                print(fname)

                content = h.handle(f.read())
                f_save = os.path.join(path_s, fname)
                with open(f_save,"w") as f:
                    f.write(content)

            # 剔除噪音行
            with open(f_save, "r") as f:
                new = []
                lines = f.readlines()[32:]
                for line in lines:
                    ignore = ('Processed in','CopyRight','浏览器支持说明','查看详细资料','查看个人网站',
                    '顾问：','编辑：','技术：','内容','##### 标题','#### 快速回复主题','  * 发布投票','  * 发新话题',
                    '![](images/default/reply.gif)','  * 多功能小黑屋','收藏 订阅 推荐 打印','.  ',
                    '![](http://messenger.services.live.com/','cn)',
                    '![QQ](images/default/qq.gif)',
                    '> ![](http://www.1984bbs.com/images/common/back.gif)',
                    '> ![](http://doubans.com/images/common/back.gif)',
                    '站务','  * Live!大讲堂','  * 罗马假日公寓','  * 国家局域网研究所','  * 开放社会资料室','  * 雅典学院',
                    '  * 自由新闻社','沙龙','发表话题[完成后可按','‹‹ 上一主题','引用 回复 TOP','|','---|')
                    if line.startswith(ignore):
                        continue
                    if line.startswith("##"):
                        line = line.replace('#','').lstrip()
                    if line.startswith('1984bbs是一个非营利项目'):
                        line = '---' + '\n\n' + '[Terminusbot](https://github.com/TerminusBot) 整理，讨论请前往 [2049bbs.xyz](http://2049bbs.xyz/)' + '\n\n' + '---' + '\n'
                    line = line.replace('|', ' ')
                    new.append(line)
                    new.append('\n')

            # 生成 jekyll serve 需要的文件格式
            f_output = os.path.join(path_n, fname)
            with open(f_output, 'w') as f:
                f.write('---' + '\n')
                f.write('layout: default' + '\n\n')
                tags: 北京驱逐
                f.write("date: " + date + '\n\n')
                f.write("title: " + title + '\n\n')
                # f.write("tags: " + tags[0] + " " + tags[1] + '\n\n')
                f.write("categories: " + category + '\n\n')
                f.write('---' + '\n\n')
                f.writelines(new)

        n += 1

extract('sbb4891/1自由新闻社', 'sbb4891/1', 'sbb4891/11', '自由新闻社')
extract('sbb4891/2雅典学院', 'sbb4891/2', 'sbb4891/22', '雅典学院')
extract('sbb4891/3开放社会资料室', 'sbb4891/3', 'sbb4891/33', '开放社会资料室')
extract('sbb4891/4国家局域网研究所', 'sbb4891/4', 'sbb4891/44', '国家局域网研究所')
extract('sbb4891/5罗马假日公寓', 'sbb4891/5', 'sbb4891/55', '罗马假日公寓')

# extract('sbb4891/大讲堂', 'sbb4891/6', 'sbb4891/66', '大讲堂')
