from PIL import Image
import argparse

# 命令行参数
parser = argparse.ArgumentParser(description="图片转为字符画")
parser.add_argument('input_file', help="输入文件")
parser.add_argument('-o', '--output', help='输出文件')
parser.add_argument('-w', '--width', type=int, default=80, help="输出字符画的宽度")
parser.add_argument('-t', '--height', type=int, default=80, help="输出字符画的高度")

args = parser.parse_args()

IMG = args.input_file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

ascii_char = list(
    "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


def get_char(r, g, b, alpha=256):
    """
    rgb图片转义为字符串
    """
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256 + 1) / length
    return ascii_char[int(gray / unit)]


if __name__ == '__main__':
    print(args.input_file.split("."))

    im = Image.open(IMG)
    im = im.resize((WIDTH, HEIGHT), Image.NEAREST)
    print("图像信息： 格式 %s ， 尺寸 %d X %d ，  模式 %s" % (im.format, *im.size, im.mode))

    txt = ""

    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j, i)))
        txt += "\n"

    print(txt)

    if OUTPUT:
        output_name = OUTPUT
    else:
        output_name = args.input_file.split(".")[0]+"_output.txt"

    with open(output_name, "w") as f:
        f.write(txt)
