def lines(file):
    '''生成器，在文本最后加一空行'''
    for line in file:
        yield line
    yield '\n'  # 最后返回一个空行


def blocks(file):
    '''生成器，生成单独的文本块'''
    block = []
    for line in lines(file):
        if line.strip():  # 不是空行则添加到块列表
            block.append(line)
        elif block:  # 如果是空行，且块列表不为空，则返回合并块列表，并清空块列表
            yield ''.join(block).strip()
            block = []


if __name__ == '__main__':
    file = "test.txt"
    print("=" * 60)
    with open(file) as f:
        print("[the blocks]:")
        print("-" * 60)
        print(list(blocks(f)))
        print("-" * 60)
    print("=" * 60)
    with open(file) as f:
        print("[the lines in blocks]:")
        print("-" * 60)
        for i in blocks(f):
            print(i)
            print("-" * 60)
