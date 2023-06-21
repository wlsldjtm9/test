import turtle
import math
import random

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Collision Detection by @TokyoEdtech")
wn.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

# shapes = ["wizard.gif", "goblin.gif", "pacman.gif", "cherry.gif", "bar.gif", "ball.gif", "x.gif"]
shapes = ['pacman.gif', 'goblin.gif', 'x.gif']

for shape in shapes:
    wn.register_shape(shape)
    
class Sprite():
    
    ## 생성자: 스프라이트의 위치, 가로/세로 크기, 이미지 지정

    def __init__(self, x, y, width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image

    ## 스프라이트 메서드

    # 지정된 위치로 스프라이트 이동 후 도장 찍기
    def render(self, pen):
        pen.goto(self.x, self.y)
        pen.shape(self.image)
        pen.stamp()

    # 충돌 감지 방법 1: 두 스프라이트의 중심이 일치할 때 충돌 발생
    def is_overlapping_collision(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    # 충돌 감지 방법 2: 두 스프라이트 사이의 거리가 두 객체의 너비의 평균값 보다 작을 때 충돌 발생
    def is_distance_collision(self, other):
        distance = (((self.x-other.x) ** 2) + ((self.y-other.y) ** 2)) ** 0.5
        if distance < (self.width + other.width)/2.0:
            return True
        else:
            return False

    # 충돌 감지 방법 3: 각각의 스프라이트를 둘러썬 경계상자가 겹칠 때 충돌 발생
    # aabb: Axis Aligned Bounding Box
    def is_aabb_collision(self, other):
        x_collision = (math.fabs(self.x - other.x) * 2) < (self.width + other.width)
        y_collision = (math.fabs(self.y - other.y) * 2) < (self.height + other.height)
        return (x_collision and y_collision)
    
    def ycor(self):
        return self.y
    
    def sety(self, y):
        self.y = y
    
    def setx(self, x):
        self.x = x

class Character(Sprite, turtle.Turtle):
    
        def __init__(self, x, y, width, height, image, jump=False):
            super().__init__(x, y, width, height, image)
            self.jump = jump
                    
        def hop(self, dx, dy):
            if self.jump == True:
                self.dy = dy
                self.dx = dx
                    
        def ycor(self):
            return self.y
        
        def xcor(self):
            return self.x
        
        def sety(self, y):
            self.y = y

        def setx(self, x):
            self.x = x
                    
pacman = Character(0, -300, 128, 128, "pacman.gif", jump=True)

goblin_1 = Sprite(0, 435, 32, 32, "goblin.gif")
goblin_2 = Sprite(250, 435, 32, 32, "goblin.gif")
goblin_3 = Sprite(-250, 435, 32, 32, "goblin.gif")

# 스프라이트 모음 리스트
# sprites = [wizard, goblin, pacman, cherry, bar, ball]
sprites = [pacman, goblin_1, goblin_2, goblin_3]

# 팩맨 왼쪽 이동
def move_pacman_left():
    if pacman.x > -250:
        pacman.x -= 250
    else:
        pacman.x = -250
    

# 팩맨 오른쪽 이동
def move_pacman_right():
    if pacman.x < 250:
        pacman.x += 250
    else:
        pacman.x = 250

# 팩맨 점프
def jump_pacman(dx = 0.9, dy = 1.3):
    pacman.hop(dx, dy)




# 이벤트 처리
wn.listen()
wn.onkeypress(move_pacman_left, "Left")  # 왼쪽 방향 화살표 입력
wn.onkeypress(move_pacman_right, "Right") # 오른쪽 방향 화살표 입력

pacman.dy = 0
pacman.dx = 0
goblin_1.dy = 0
goblin_2.dy = 0
goblin_3.dy = 0
gravity = -0.009
goblin_gravity = -0.00006


val = True
num = random.randint(0, 2)

while True:

    pacman.dy += gravity
    goblin_1.dy += goblin_gravity
    goblin_2.dy += goblin_gravity
    goblin_3.dy += goblin_gravity

    
    if num == 0:
        goblin_y_1 = goblin_1.ycor()
        goblin_y_1 += goblin_1.dy
        goblin_1.sety(goblin_y_1)

        goblin_y_2 = goblin_2.ycor()
        goblin_y_2 += goblin_2.dy
        goblin_2.sety(goblin_y_2)


    if num == 1:
        goblin_y_2 = goblin_2.ycor()
        goblin_y_2 += goblin_2.dy
        goblin_2.sety(goblin_y_2)

        goblin_y_3 = goblin_3.ycor()
        goblin_y_3 += goblin_3.dy
        goblin_3.sety(goblin_y_3) 

    
    if num == 2:
        goblin_y_1 = goblin_1.ycor()
        goblin_y_1 += goblin_1.dy
        goblin_1.sety(goblin_y_1)

        goblin_y_3 = goblin_3.ycor()
        goblin_y_3 += goblin_3.dy
        goblin_3.sety(goblin_y_3) 


    if pacman.ycor() < -300:
        pacman.sety(-300)
        pacman.dy = 0
        pacman.dx = 0

    if goblin_1.ycor() < -400:
        goblin_1.sety(400)
        goblin_1.dy = 0
        val = False

    if goblin_2.ycor() < -400:
        goblin_2.sety(400)
        goblin_2.dy = 0
        val = False

    if goblin_3.ycor() < -400:
        goblin_3.sety(400)
        goblin_3.dy = 0
        val = False


    # 각 스프라이트 위치 이동 및 도장 찍기
    for sprite in sprites:
        sprite.render(pen)
    
        
    if goblin_1.is_aabb_collision(pacman):
        pacman.image = "x.gif"

    if goblin_2.is_aabb_collision(pacman):
        pacman.image = "x.gif"

    if goblin_3.is_aabb_collision(pacman):
        pacman.image = "x.gif"

    if val == False:
        num = random.randint(0, 2)
        val = True
    
        
    wn.update() # 화면 업데이트
    pen.clear() # 스프라이트 이동흔적 삭제