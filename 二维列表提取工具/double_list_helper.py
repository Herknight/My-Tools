class Vector2:
    """
        二维向量
        可以表示位置/方向
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def left():
        return Vector2(0, -1)

    @staticmethod
    def right():
        return Vector2(0, 1)

    @staticmethod
    def up():
        return Vector2(-1, 0)

    @staticmethod
    def down():
        return Vector2(1, 0)


class DoubleListHelper:
    @staticmethod
    def get_elements(target, vect_pos, vect_dir, count):
        """
            在二维列表中获取指定位置，指定方向，指定数量的元素.
        :param target: 二维列表
        :param vect_pos: 指定位置
        :param vect_dir: 指定方向
        :param count: 指定数量
        :return: 列表
        """
        list_result = []
        for i in range(count):
            vect_pos.x += vect_dir.x
            vect_pos.y += vect_dir.y
            element = target[vect_pos.x][vect_pos.y]
            list_result.append(element)
        return list_result