import sys
import os
import _io
from collections import namedtuple
from PIL import Image


class Nude(object):
    """裸体类"""

    Skin = namedtuple("Skin", "id skin region x y")

    def __init__(self, path_or_imgObj):
        if isinstance(path_or_imgObj, Image.Image):  # 如果为Image对象，则直接赋值
            self.image = path_or_imgObj
        elif isinstance(path_or_imgObj, str):  # 如果是str类型，可能是路径的字符串，则打开文件
            self.image = Image.open(path_or_imgObj)

        bands = self.image.getbands()  # 获取图片所有色彩通道
        if len(bands) == 1:  # 若为单通道图片（即灰度图），则将其转为RGB图
            new_img = Image.new("RGB", self.image.size)  # 新建同样大小的RGB图
            new_img.paste(self.image)  # 拷贝原图片到新图片，PIL自动进行通道转换
            f = self.image.filename
            self.image = new_img  # 替换原有的图片，使用新的RGB格式图片
            self.image.filename = f

        self.skin_map = []  # 所有像素的skin对象，
        self.detected_regions = []  # 检测到的皮肤区域，索引是皮肤区域号，元素是skin对象列表
        self.merge_regions = []  # 元素为待合并区域号，
        self.skin_regions = []  # 合并后的皮肤区域
        self.last_from, self.last_to = -1, -1  # 最近合并的两个区域的区域号，初始为-1和-1
        self.result = None  # 色情图片的判断结果
        self.message = None  # 处理得到的信息
        self.width, self.height = self.image.size  # 图片的宽和高
        self.total_pixels = self.width * self.height  # 图片的总像素

    def _classify_skin(self, r, g, b):  # 基于像素的肤色检测

        # 根据rgb的值判断肤色
        rgb_classifier = r > 95 and g > 40 and g < 100 and b > 20 and \
            max([r, g, b]) - min([r, g, b]) > 15 and \
            abs(r - g) > 15 and r > g and r > b

        # 根据处理后的RGB的值判定
        nr, ng, nb = self._to_normalized(r, g, b)
        norm_rgb_classifier = nr/ng > 1.185 and \
            float(r * b) / ((r + g + b)**2) > 0.107 and \
            float(r * g) / ((r + g + b)**2) > 0.112

        # HSV 颜色模式下的判定
        h, s, v = self._to_hsv(r, g, b)
        hsv_classifier = h > 0 and h < 35 and s > 0.23 and s < 0.68

        # YCbCr 颜色模式下的判定
        y, cb, cr = self._to_ycbcr(r, g, b)
        ycbcr_classifier = 97.5 <= cb <= 142.5 and 134 <= cr <= 176

        # 效果不是很好，还需要改进公式
        # return rgb_classifier or norm_rgb_classifier or hsv_classifier or ycbcr_classifier
        return ycbcr_classifier

    def _to_normalized(self, r, g, b):
        if r == 0:
            r = 0.0001
        if g == 0:
            g = 0.0001
        if b == 0:
            b = 0.0001
        _sum = float(r + g + b)
        return [r/_sum, g/_sum, b/_sum]

    def _to_ycbcr(self, r, g, b):
        # 公式来源：
        # http://stackoverflow.com/questions/19459831/rgb-to-ycbcr-conversion-problems
        y = .299*r + .587*g + .114*b
        cb = 128 - 0.168736*r - 0.331364*g + 0.5*b
        cr = 128 + 0.5*r - 0.418688*g - 0.081312*b
        return y, cb, cr

    def _to_hsv(self, r, g, b):
        h = 0
        _sum = float(r+g+b)
        _max = float(max([r, g, b]))
        _min = float(min([r, g, b]))
        diff = float(_max - _min)
        if _sum == 0:
            _sum = 0.0001
        if _max == r:
            if diff == 0:
                h = sys.maxsize
            else:
                h = (g - b) / diff
        elif _max == g:
            h = 2 + ((g - r) / diff)
        else:
            h = 4 + ((r - g) / diff)

        h *= 60
        if h < 0:
            h += 360

        return [h, 1.0 - (3.0 * (_min / _sum)), (1/3) * _max]

    def _add_merge(self, _from, _to):
        '''接收两个区域号，将之添加到merge_regions'''

        # 两个区域号赋值给类属性
        self.last_from = _from
        self.last_to = _to

        from_index = -1  # 记录 self.merge_regions 的某个索引值，初始化为 -1
        to_index = -1  # 记录 self.merge_regions 的某个索引值，初始化为 -1

        for index, region in enumerate(self.merge_regions):
            # 遍历merge_regions中的元素
            for r_index in region:
                if r_index == _from:
                    from_index = index
                if r_index == _to:
                    to_index = index

        if from_index != -1 and to_index != -1:  # 两个区域号都存在于merge_regions
            if from_index != to_index:
                self.merge_regions[from_index].extend(
                    self.merge_regions[to_index])
                del(self.merge_regions[to_index])
            return

        if from_index == -1 and to_index == -1:  # 两个区域号都不存在于merge_regions
            self.merge_regions.append([_from, _to])  # 创建新的区域号列表
            return

        if from_index != -1 and to_index == -1:  # 两个区域号有一个存在于merge_regions
            self.merge_regions[from_index].append(_to)  # 将不存在的添加到另一个区域号所在列表
            return

        if from_index == -1 and to_index != -1:  # 两个区域号有一个存在于merge_regions
            self.merge_regions[to_index].append(_from)  # 将不存在的添加到另一个区域号所在列表
            return

    def _merge(self, detected_regions, merge_regions):
        '''合并merge_regions中的区域号所代表的区域得到新的皮肤区域列表'''

        new_detected_regions = []  # 其中的元素即代表皮肤区域，元素索引为区域号

        for index, region in enumerate(merge_regions):
            try:
                new_detected_regions[index]
            except IndexError:
                new_detected_regions.append([])
            for r_index in region:
                new_detected_regions[index].extend(detected_regions[r_index])
                detected_regions[r_index] = []

        for region in detected_regions:  # 添加剩下的其余皮肤区域到 new_detected_regions
            if len(region) > 0:
                new_detected_regions.append(region)

        self._clear_regions(new_detected_regions)  # 清理 new_detected_regions

    def _clear_regions(self, detected_regions):  # 只保存像素数大于指定数量的皮肤区域
        for region in detected_regions:
            if len(region) > 30:
                self.skin_regions.append(region)

    def _analyse_regions(self):  # 判断区域是否色情

        if len(self.skin_regions) < 3:  # 如果皮肤区域小于 3 个，不是色情
            self.message = "皮肤区域大小：({_skin_regions_size})，小于3".format(
                _skin_regions_size=len(self.skin_regions))
            self.result = False
            return self.result

        self.skin_regions = sorted(
            self.skin_regions, key=lambda s: len(s), reverse=True)

        # 计算皮肤总像素数
        total_skin = float(
            sum([len(skin_region)for skin_region in self.skin_regions]))

        if total_skin / self.total_pixels * 100 < 15:  # 如果皮肤区域与整个图像的比值小于 15%，那么不是色情图片
            self.message = "总的皮肤区域：({:.2f})，低于15".format(
                total_skin / self.total_pixels * 100)
            self.result = False
            return self.result

        if len(self.skin_regions[0]) / total_skin * 100 < 45:  # 如果最大皮肤区域小于总皮肤面积的 45%
            self.message = "最大的皮肤区域：({:.2f})，低于45".format(
                len(self.skin_regions[0]) / self.total_pixels * 100)
            self.result = False
            return self.result

        if len(self.skin_regions) > 60:
            self.message = "皮肤区域总数:({})，大于60".format(len(self.skin_regions))
            self.result = False
            return self.result

        self.message = "裸露过多，色情？！"
        self.result = True
        return self.result

    def inspect(self):  # 输出信息格式
        _image = "{} {} {}X{}".format(
            self.image.filename, self.image.format, self.width, self.height)
        return "{_image}: result={_result} message='{_message}'".format(
            _image=_image, _result=self.result, _message=self.message)

    def resize(self, maxwidth=1000, maxheight=1000):
        """
        为了提高效率，如有必要，缩小原图片的尺寸，
        基于最大宽高，按比例重设图片大小，
        注意：这可能影响检测算法的结果

        如果没有变化返回 0
        原宽度大于 maxwidth 返回 1
        原高度大于 maxheight 返回 2
        原宽高大于 maxwidth, maxheight 返回 3

        maxwidth - 图片最大宽度
        maxheight - 图片最大高度
        传递参数时都可以设置为 False 来忽略
        """

        ret = 0  # 存储返回值

        if maxwidth:  # False则忽略
            if self.width > maxwidth:
                wpercent = maxwidth / self.width
                hsize = int(self.height * wpercent)
                fname = self.image.filename
                # Image.LANCZOS重采样滤波器，用来抗锯齿
                self.image = self.image.resize(
                    (maxwidth, hsize), Image.LANCZOS)
                self.image.filename = fname
                self.width, self.height = self.image.size
                self.total_pixels = self.width * self.height  # 图片的总像素
                ret += 1

        if maxheight:  # False则忽略
            if self.height > maxheight:
                hpercent = maxheight / self.height
                wsize = int(self.width * hpercent)
                fname = self.image.filename
                # Image.LANCZOS重采样滤波器，用来抗锯齿
                self.image = self.image.resize(
                    (wsize, maxheight), Image.LANCZOS)
                self.image.filename = fname
                self.width, self.height = self.image.size
                self.total_pixels = self.width * self.height  # 图片的总像素
                ret += 2
        return ret

    def parse(self):
        '''解析图片'''

        if self.result is not None:  # 若已有结果，则返回本对象
            return self

        pixels = self.image.load()  # 获得图片所有像素数据

        # 遍历所有的像素，为每个像素创建Skin对象
        # 完成皮肤区域region的初步划分
        for y in range(self.height):
            for x in range(self.width):
                # 得到像素的RGB三个通道的值
                # [x, y] 是 [(x, y)] 的简便写法
                r = pixels[x, y][0]
                g = pixels[x, y][1]
                b = pixels[x, y][2]
                isSkin = True if self._classify_skin(
                    r, g, b) else False  # 判断是否为肤色
                # 为每个像素分配id值从1到height*width
                _id = x + y * self.width + 1  # x和y的值从0开始
                # 为每个像素创建Skin对象，并添加到skin_map中
                self.skin_map.append(self.Skin(_id, isSkin, None, x, y))
                if not isSkin:  # 不是肤色的像素，跳出本次循环，遍历下一个像素
                    continue

                # 若当前像素是肤色，则遍历临近像素，
                # 左方，左上方，正上方，右上方
                # 注意：_id与索引值差1，左上角为原点
                check_indexes = [_id - 2,               # 左
                                 _id - self.width - 2,  # 左上
                                 _id - self.width - 1,  # 上
                                 _id - self.width]      # 右上

                region = -1  # 区域号，初始-1
                for index in check_indexes:  # 遍历每一个相邻像素的索引
                    try:
                        # 相邻像素是否能够索引到
                        # 因为左上角的开始区域有的没有相邻的
                        # 左方，左上方，正上方，右上方 的像素
                        self.skin_map[index]
                    except IndexError as e:
                        break
                    smi = self.skin_map[index]
                    if smi.skin:  # 若相邻像素为肤色
                        # 若相邻像素和当前像素的region均为有效值，且二者不同，
                        # 且尚未添加相同的合并任务
                        if (smi.region != None and
                            region != None and
                            region != -1 and
                            smi.region != region and
                            self.last_from != region and
                                self.last_to != smi.region):
                            # 添加合并两个区域的合并任务
                            # 区域号添加到 self.merge_regions中
                            self._add_merge(region, smi.region)
                        region = smi.region  # 记录相邻像素的区域号

                #　遍历完相邻像素后，若region仍为-1，说明：
                # 当前像素是肤色，而相邻的像素都不是肤色
                if region == -1:
                    # 更改属性为新的区域号，注意：
                    # 元组不可直接改变，索引与_id差1
                    _skin = self.skin_map[_id - 1]._replace(
                        region=len(self.detected_regions))  # namedtuple
                    self.skin_map[_id - 1] = _skin
                    # 将此像素所在的区域创建为新区域
                    self.detected_regions.append([self.skin_map[_id - 1]])
                elif region != None:  # 不为-1，且不为None，说明为有效的区域号
                    # 将此区域的region区域号改为与相邻像素相同
                    _skin = self.skin_map[_id - 1]._replace(region=region)
                    self.skin_map[_id - 1] = _skin
                    # 向这个区域的像素列表中添加此像素
                    self.detected_regions[region].append(
                        [self.skin_map[_id - 1]])

        # 完成所有区域的合并，合并整理后的区域存储到self.merge_regions
        self._merge(self.detected_regions, self.merge_regions)
        # 分析皮肤区域，得到判定结果
        self._analyse_regions()
        return self

    def showSkinRegions(self):
        '''皮肤区域可视化'''

        if self.result is None:  # 没有结果则返回
            return

        skinIdSet = set()  # 皮肤像素的id
        simage = self.image  # 原图拷贝
        simageData = simage.load()  # 加载数据

        for sr in self.skin_regions:  # 存入皮肤区域的id
            # print(sr)
            for pixel in sr:
                # print(pixel)
                if isinstance(pixel, list):
                    skinIdSet.add(pixel[0].id)
                else:
                    skinIdSet.add(pixel.id)

        for pixel in self.skin_map:  # 将图像中的皮肤像素设为白色，其余设为黑色
            if pixel.id not in skinIdSet:
                simageData[pixel.x, pixel.y] = 0, 0, 0
            else:
                simageData[pixel.x, pixel.y] = 250, 250, 250

        filePath = os.path.abspath(self.image.filename)
        fileDirectory = os.path.dirname(filePath) + "/"
        fileFullName = os.path.basename(filePath)
        fileName, fileExtName = os.path.splitext(fileFullName)  # 分离文件名和扩展名

        # 保存图片
        print("准备保存皮肤区域可视化图片")
        simage.save("{}{}_{}{}".format(
            fileDirectory, fileName, 'Nude' if self.result else 'Normal', fileExtName))


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Detect nudity in images.')
    parser.add_argument('files', metavar='image', nargs='+',
                        help='Images you wish to test')
    parser.add_argument('-r', '--resize', action='store_true',
                        help='Reduce image size to increase speed of scanning')
    parser.add_argument('-v', '--visualization', action='store_true',
                        help='Generating areas of skin image')

    args = parser.parse_args()

    for fname in args.files:
        if os.path.isfile(fname):
            n = Nude(fname)
            if args.resize:
                n.resize(maxheight=800, maxwidth=600)
            n.parse()
            if args.visualization:
                n.showSkinRegions()
            print(n.result, n.inspect())
        else:
            print(fname, "is not a file")
