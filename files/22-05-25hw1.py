class Player:
    def __init__(self, health=4, x_pos=0, y_pos=0):
        self.__health = self.__validate_health(health)
        self.__x_pos = self.__validate_x_pos(x_pos)
        self.__y_pos = self.__validate_y_pos(y_pos)
        
    def __validate_health(self, health):
        if not isinstance(health, int):
            raise TypeError("Health must be int")
        if health < 0 or health > 4:
            raise ValueError("Health must be between 0 and 4")
        return health

    def __validate_x_pos(self, x_pos):
        if not isinstance(x_pos, int):
            raise TypeError("X position must be int")
        if x_pos < 0 or x_pos > 1000:
            raise ValueError("X position must be between 0 and 1000")
        return x_pos

    def __validate_y_pos(self, y_pos):
        if not isinstance(y_pos, int):
            raise TypeError("Y position must be int")
        if y_pos < 0 or y_pos > 100:
            raise ValueError("Y position must be between 0 and 100")
        return y_pos

    def move(self, direction):
        direction = direction.lower()
        if direction not in ["left", "right"]:
            raise ValueError("Direction must be 'left' or 'right'")
        
        if direction == "left":
            self.__x_pos = max(0, self.__x_pos - 10)
        else:
            self.__x_pos = min(1000, self.__x_pos + 10)
        print(f"Moved {direction} to x={self.__x_pos}, y={self.__y_pos}")

    def jump(self):
        self.__y_pos = min(100, self.__y_pos + 20)
        print(f"Jumped to y={self.__y_pos}")

    def get_status(self):
        print(f"Health: {self.__health}, Position: x={self.__x_pos}, y={self.__y_pos}")

player = Player(health=4, x_pos=0, y_pos=0)
player.get_status()
player.move("right")
player.get_status()
player.jump()
player.get_status()
player.move("left")
player.get_status()