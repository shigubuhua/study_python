'''
破解图片验证码
参考： https://www.shiyanlou.com/courses/364/labs/1165/document

'''
import hashlib  # 生成文件名用
import time  # 生成哈希值用
import math  # 计算向量空间用
import os
from PIL import Image

'''图片色彩模式转换'''

im = Image.open("captcha.gif")
im.convert("P")  # 图片转换为8位像素模式

his = im.histogram()  # 获取图片的直方图数据，分析其中颜色分布
# print(his)  # 打印直方图

values = {}
for i in range(256):  # 生成颜色分布的字典
    values[i] = his[i]

# 取颜色字典的最多颜色的前10位，并排序
for j, k in sorted(values.items(), key=lambda x: x[1], reverse=True)[:10]:
    print(j, k)

im2 = Image.new("P", im.size, 255)  # 创建新图片
for x in range(im.size[1]):
    for y in range(im.size[0]):
        pix = im.getpixel((y, x))
        if pix == 220 or pix == 227:  # 保留红色220。保留灰色227。为什么保留灰色？
            # if pix == 220:  # 保留红色220。保留灰色227。为什么保留灰色？
            # if pix == 227:  # 保留红色220。保留灰色227。为什么保留灰色？
            im2.putpixel((y, x), 0)

# im2.show()  # 显示图片，调用系统默认的图片查看软件

'''提取单个字符的图片'''

inletter = False
foundletter = False
start = 0
end = 0
letters = []  # 存放单个字符的起始和结束序列号

for y in range(im2.size[0]):
    for x in range(im2.size[1]):
        pix = im2.getpixel((y, x))
        if pix != 255:
            inletter = True
    if foundletter == False and inletter == True:
        foundletter = True
        start = y
    if foundletter == True and inletter == False:
        foundletter = False
        end = y
        letters.append((start, end))
    inletter = False

print(letters)

count = 0
for letter in letters:  # 切割需要验证的图片，并逐一保存分隔后的图片
    m = hashlib.md5()
    im3 = im2.crop((letter[0], 0, letter[1], im2.size[1]))
    m.update(("%s%s" % (time.time(), count)).encode(
        'utf-8'))  # unicode编码在hashing之前必须先encode
    im3.save("./%s.gif" % (m.hexdigest()))  # 用MD5作文件名
    count += 1

'''AI与向量空间图像识别'''


class VectorCompare(object):
    """计算矢量大小，实现向量空间"""

    # def __init__(self, concordance):
    #     self.concordance = concordance

    def magnitude(self, concordance):
        '''方均根大小'''
        total = 0
        for word, count in concordance.items():
            total += count ** 2
        return math.sqrt(total)

    def relation(self, concordance1, concordance2):
        '''计算矢量之间的cos值，比较两个字典类型并返回他们的相似度'''
        relevance = 0
        topvalue = 0
        for word, count in concordance1.items():
            if word in concordance2:  # py3 has not has_key
                topvalue += count * concordance2[word]
        return topvalue/(self.magnitude(concordance1)*self.magnitude(concordance2))


def buildvector(im):
    '''将图片转换为矢量'''
    d1 = {}
    count = 0
    for i in im.getdata():
        d1[count] = i
        count += 1
    return d1


v = VectorCompare()

iconset = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
           'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

imageset = []  # 训练集图片
for letter in iconset:  # 对数字和字母逐一进行矢量化，并建立字典
    for img in os.listdir(r"./iconset/%s/" % letter):
        temp = []
        if img != "Thumbs.db" and img != ".DS_Store":
            temp.append(buildvector(Image.open(
                r"./iconset/%s/%s" % (letter, img))))
        imageset.append({letter: temp})

count = 0
for letter in letters:  # 切割需要验证的图片，并逐一与训练集中的图片进行比较相似度
    m = hashlib.md5()
    im3 = im2.crop((letter[0], 0, letter[1], im2.size[1]))
    guess = []
    for image in imageset:
        for x, y in image.items():
            if len(y) != 0:
                guess.append((v.relation(y[0], buildvector(im3)), x))

    guess.sort(reverse=True)
    print("", guess[0])
    count += 1
