# -*- coding: utf-8 -*-


def str_filter(string):
    string = string.replace('，', ' ')
    string = string.replace('。', ' ')
    string = string.replace('“', ' ')
    string = string.replace('”', ' ')
    string = string.replace('?', ' ')
    string = string.replace('；', ' ')
    string = string.replace('：', ' ')
    string = string.replace('(', ' ')
    string = string.replace(')', ' ')
    string = string.replace('―', ' ')
    return string.replace('　', ' ')


def fun(file_name):
    # 读取文档内容
    with open(file_name) as file_link:
        file_content = file_link.read()

    # 去除标点符号按空格切割
    words_list = str_filter(file_content).split()
    ##words_lists = lists.read().split(" ") 
    # 统计二元词组
    words_dict = {}
  #  for i in range(len(words_list)-1):
  #      if len(words_list[i]) >= 2 and len(words_list[i+1]) >= 2: 
#	        key = words_list[i] + " " + words_list[i+1]
 #           if key not in words_dict:
  #              words_dict[key] = 1
  #          else:
  #              words_dict[key] += 1

   	
	#length = len(words_list)
    for i in range(0, len(words_list)-1):
        first_word = words_list[i] #当前词
        second_word = words_list[i+1] #下一个词

        if len(first_word) >= 4 and len(second_word) >= 4: #去掉单字词
            tuple_word = first_word + " " + second_word    #组成二元词组
            #print(tuple_word)
            if tuple_word not in words_dict:
                words_dict[tuple_word] = 1
            else:
                words_dict[tuple_word] +=1 # 统计次数
                #print dicts[tuple_word]

    sorted_list = sorted(words_dict.items(), key=lambda x: x[1], reverse=True)
    return sorted_list[:10]

result = fun('happiness_seg.txt')
for s in result:
    print "词组[%s]  %d 次" % (s[0], s[1])
