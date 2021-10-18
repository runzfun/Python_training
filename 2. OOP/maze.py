import os.path
import colorama
from colorama import Back
colorama.init(autoreset=True)


class Maze:
    def __init__(self):
        self.map, self.start, self.finish = self.loadmap()
        self.optimal_path = self.find_path()

        for x, elemlist in enumerate(self.map):
            for y, elem in enumerate(elemlist):
                curpos = (x, y)
                if elem == '*':
                    color = Back.BLACK
                elif elem == 'S':
                    color = Back.CYAN
                elif curpos in self.optimal_path:
                    color = Back.GREEN
                else:
                    color = Back.LIGHTBLACK_EX

                if len(str(elem)) == 1:
                    print(f'{color}  {elem}  ', end='')
                if len(str(elem)) == 2:
                    print(f'{color}  {elem} ', end='')
                if len(str(elem)) == 3:
                    print(f'{color} {elem} ', end='')

            print()
    def loadmap(self):
        """ Загружаем лабиринт из файла, определяем старт и финиш координаты """
        save_path = '/save/save.json'
        if not(os.path.exists(save_path)):

            file = open('maze.txt', 'r')
            map = [[c for c in line.strip()] for line in file]
            start, finish = None, None
            for indx, elem in enumerate(map):
                if 'F' in elem: finish = (indx, elem.index('F'))
                if 'S' in elem: start = (indx, elem.index('S'))

            print(f'Координаты : \nСтарт:{start}\nФиниш:{finish}')
        return map, start, finish

    def not_obstacle(self, nx, ny):

        '''Возвращаем True если  x,y в пределах карты и это не стена'''

        curPos = self.map[nx][ny]
        in_height = True if nx in range(0, len(self.map) + 1) else False
        in_width = True if ny in range(0, len(self.map[0]) + 1) else False
        notWall = True if curPos != '*' else False
        notFinish = True if curPos != 'F' else False
        result = True if in_height and in_width and notWall and notFinish else False
        return result

    def find_path(self):
        queue = [self.start]
        zx, zy = self.start
        delta = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        step = 0

        while queue:
            x, y = queue.pop(0)
            if self.map[zx][zy] != self.map[x][y]:
                step += 1
            for dx, dy in delta:
                nx, ny = dx + x, dy + y
                if self.not_obstacle(nx, ny) and self.map[nx][ny] == '.':
                    self.map[nx][ny] = step
                    queue.append((nx, ny))
                if self.map[nx][ny] == 'F':
                    self.map[nx][ny] = step
                    queue.clear()
            zx, zy = x, y

        path = []
        zx, zy = self.finish
        done = False
        while not done:
            for dx, dy in delta:
                nx, ny = dx + zx, dy + zy
                if self.not_obstacle(nx, ny) and type(self.map[nx][ny]) == int and self.map[zx][zy] > self.map[nx][ny]:
                    path.append((nx, ny))
                    zx, zy = nx, ny
                    done = True if self.map[zx][zy] == 0 else False

        return path[::-1]

class PlayerController:
    pass
con = Maze()
print(input('Dd'))
