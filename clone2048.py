
'''
2048游戏
参考
https://www.shiyanlou.com/courses/368/labs/1172/document

游戏状态机/有限状态机（FSM）：初始--游戏--胜利--失败--结束

                init

        win     game        gameover

                exit

state 存储当前状态， state_actions 这个词典变量作为状态转换的规则，
它的 key 是状态，value 是返回下一个状态的函数

'''


import curses
from random import randrange, choice  # generate and place new tile
from collections import defaultdict


ACTIONS = ['Up', 'Left', 'Down', 'Right', 'Restart', 'Exit']  # 用户行为
LETTER_CODERS = [ord(ch) for ch in 'WASDRQwasdrq']  # 用户输入上 左 下 右 重置 退出
ACTIONS_DICT = dict(zip(LETTER_CODERS, ACTIONS * 2))


def get_user_action(keybaord):
    '''处理用户输入，阻塞+循环，直到获得用户有效输入才返回对应行为'''
    char = 'N'
    while char not in ACTIONS_DICT:
        char = keybaord.getch()
    return ACTIONS_DICT[char]


def transpose(field):
    '''矩阵转置'''
    print('in transpose the field is ', field)
    print('transpose return', [list(row) for row in zip(*field)])
    return [list(row) for row in zip(*field)]


def invert(field):
    '''矩阵逆转，行反序'''
    return [row[::-1] for row in field]


class GameField(object):
    """
    创建棋盘：
    4 X 4
    """

    def __init__(self, height=4, width=4, win=2048):
        self.height = height            # 棋盘高
        self.width = width              # 棋盘宽
        self.win_value = win            # 过关分数
        self.score = 0                  # 当前分数
        self.highscore = 0              # 最高分
        self.reset()                    # 棋盘重置
        # self.field = [[0 for i in range(self.width)]
        #               for j in range(self.height)]  # 首先生成行值（全部为0），然后生成多行

    def spawn(self):
        '''随机生成一个2或一个4'''
        new_element = 4 if randrange(100) > 89 else 2
        (i, j) = choice([(i, j) for i in range(self.width)
                         for j in range(self.height)
                         if self.field[i][j] == 0])  # 随机选择没有数值的棋格
        self.field[i][j] = new_element

    def reset(self):
        '''重置棋盘'''
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.field = [[0 for i in range(self.width)]
                      for j in range(self.height)]  # 首先生成行值（全部为0），然后生成多行
        self.spawn()
        self.spawn()  # 一次出两个数

    def draw(self, screen):
        '''绘制游戏界面'''
        help_string1 = ' (W)Up  (S)Down  (A)Left  (D)Right '
        help_string2 = '      (R)Restart  (Q)Exit '
        gameover_string = '         GAME OVER '
        win_string = '         YOU WIN ! '

        def cast(string):
            '''打字符串'''
            screen.addstr(string + '\n')

        def draw_hor_separator():
            '''绘制水平线，并计数'''
            line = '+' + ('+------' * self.width + '+')[1:]
            separator = defaultdict(lambda: line)
            if not hasattr(draw_hor_separator, "counter"):  # 给函数定义了计数属性
                draw_hor_separator.counter = 0
            cast(separator[draw_hor_separator.counter])
            draw_hor_separator.counter += 1

        def draw_row(row):
            '''画一行'''
            cast(''.join('|{: ^5} '.format(num)
                         if num > 0 else '|      ' for num in row) + '|')

        screen.clear()

        cast('SCORE: ' + str(self.score))
        if self.highscore != 0:
            cast('HIGHSCORE: ' + str(self.highscore))
        for row in self.field:
            draw_hor_separator()
            draw_row(row)

        draw_hor_separator()

        if self.is_win():
            cast(win_string)
        else:
            if self.is_gameover():
                cast(gameover_string)
            else:
                cast(help_string1)
        cast(help_string2)

    def move(self, direction):
        '''走一步棋'''
        # 通过转置（列变成行，使用行合并的操作）和逆转（右移逆转后，使用向左合并的方法操作）
        def move_row_left(row):
            '''一行向左合并'''
            def tighten(row):
                '''压缩行，把非0元素向左移动'''
                new_row = [i for i in row if i != 0]
                new_row += [0 for i in range(len(row) - len(new_row))]
                return new_row

            def merge(row):
                '''合并临近元素'''
                pair = False
                new_row = []
                for i in range(len(row)):
                    if pair:
                        new_row.append(2 * row[i])
                        self.score += 2 * row[i]
                        pair = False
                    else:
                        if i + 1 < len(row) and row[i] == row[i + 1]:
                            pair = True
                            new_row.append(0)
                        else:
                            new_row.append(row[i])
                assert len(new_row) == len(row)
                return new_row
            return tighten(merge(tighten(row)))  # 先移动再合并，最后再移动

        moves = {}
        moves['Left'] = lambda field: [move_row_left(row) for row in field]
        moves['Right'] = lambda field: invert(moves['Left'](invert(field)))
        moves['Up'] = lambda field: transpose(moves['Left'](transpose(field)))
        moves['Down'] = lambda field: transpose(
            moves['Right'](transpose(field)))
        if direction in moves:
            if self.move_is_possible(direction):
                print('in GameField.move the self.field is ', self.field)
                self.field = moves[direction](self.field)
                self.spawn()
                return True
            else:
                return False

    def is_win(self):
        '''判断胜利'''
        return any(any(i >= self.win_value for i in row) for row in self.field)

    def is_gameover(self):
        '''判断失败'''
        return not any(self.move_is_possible(move) for move in ACTIONS)

    def move_is_possible(self, direction):
        '''判断能否移动'''
        def row_is_left_movalbe(row):
            '''是否可以向左移动'''
            print("run row_is_left_movalbe ")

            def change(i):
                '''棋格是否可以改变'''
                if row[i] == 0 and row[i + 1] != 0:  # 有空位
                    return True
                if row[i] != 0 and row[i + 1] == row[i]:  # 可合并
                    return True
                return False
            return any(change(i) for i in range(len(row) - 1))

        check = {}
        check['Left'] = lambda field: any(
            row_is_left_movalbe(row) for row in field)
        check['Right'] = lambda field: check['Left'](invert(field))
        check['Up'] = lambda field: check['Left'](transpose(field))
        check['Down'] = lambda field: check['Right'](transpose(field))
        if direction in check:
            print('in GameField.move_is_possible the direction is ',
                  direction)
            print('in GameField.move_is_possible the self.field is ',
                  self.field)
            return check[direction](self.field)
        else:
            return False


def main(stdscr):
    '''主逻辑'''

    def init():
        '''初始化'''
        game_field.reset()  # 重置棋盘
        print('in main.init the game_field.field is ', game_field.field)
        return 'Game'

    def not_game(state):
        '''不在游戏中，游戏胜利或者失败'''
        game_field.draw(stdscr)  # GameOver或者Win的界面
        action = get_user_action(stdscr)  # 读取用户输入得到actions，判断重启游戏或者退出
        responses = defaultdict(lambda: state)  # 默认是当前状态循环，直到新行为
        responses['Restart'], responses['Exit'] = 'Init', 'Exit'  # 不同行为转换到不同状态
        return responses[action]

    def game():
        '''正在游戏'''
        print('in main.game the game_field.field is ', game_field.field)
        game_field.draw(stdscr)  # 画出当前棋盘状态
        acion = get_user_action(stdscr)  # 读取用户输入，得到action
        print('in main.game the game_field.field is ', game_field.field)
        if acion == 'Restart':
            return 'Init'
        if acion == 'Exit':
            return 'Exit'
        if game_field.move(acion):  # 成功移动一步
            if game_field.is_win():  # 胜利
                return 'Win'
            if game_field.is_gameover():  # 失败
                return 'GameOver'
        return 'Game'  # 最后的状态选择是在game中继续循环

    state_actions = {
        'Init': init,
        'Win': lambda: not_game('Win'),
        'GameOver': lambda: not_game('GameOver'),
        'Game': game
    }

    curses.use_default_colors()
    game_field = GameField(win=32)

    state = 'Init'

    # 状态机开始循环
    while state != 'Exit':
        state = state_actions[state]()


curses.wrapper(main)
