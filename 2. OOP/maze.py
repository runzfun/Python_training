from collections import deque

class Config:
    def __init__(self):
        self.map, self.start, self.finish = self.loadmap()
        self.optimal_path = self.find_path()
        for el in self.map:
            for i in el:
                if len(str(i)) == 1:
                    print(f'  {i}  ', end='')
                if len(str(i)) == 2:
                    print(f'  {i} ', end='')
                if len(str(i)) == 3:
                    print(f' {i} ', end='')


            print()

    def loadmap(self):

        """ Загружаем лабиринт из файла, определяем старт и финиш координаты """

        file = open('maze.txt', 'r')
        map = [[c for c in line.strip()] for line in file]
        start, finish = None, None
        for indx, elem in enumerate(map):
            if 'F' in elem: finish = (indx, elem.index('F'))
            if 'S' in elem: start = (indx, elem.index('S'))

        print(f'Координаты : \nСтарт:{start}\nФиниш:{finish}')
        return map, start, finish

    def obstacle(self, nx, ny):

        '''Возвращаем True если  x,y в пределах карты и это не стена'''

        in_height = True if nx in range(0, len(self.map)+1) else False
        in_width = True if ny in range(0, len(self.map[0])+1) else False
        notWall = True if self.map[nx][ny] != '*' else False
        result = True if in_height and in_width and notWall else False
        return result

    def find_path(self):
        queue = [self.start]
        delta = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        step = 1
        zx, zy = self.start

        while queue:
            x, y = queue.pop(0)
            if self.map[zx][zy] != self.map[x][y]:
                step += 1

            for dx, dy in delta:
                nx, ny = dx + x, dy + y
                if self.obstacle(nx, ny) and self.map[nx][ny] == '.' or self.map[nx][ny] == 'F':
                    if self.map[nx][ny] == 'F':
                        queue.clear()
                    self.map[nx][ny] = step
                    queue.append((nx, ny))
            zx, zy = x, y



con = Config()
