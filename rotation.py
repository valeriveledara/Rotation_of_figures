import glfw
from OpenGL.GL import *
from OpenGL.GLU import *

# Параметры для тетраэдра
tetrahedron_vertices = [
    (0.5, -0.5, -0.5),
    (-0.5, -0.5, -0.5),
    (0, 0.5, -0.5),
    (0, 0, 0.5)
]
tetrahedron_faces = [
    (0, 1, 2),
    (0, 1, 3),
    (1, 2, 3),
    (2, 0, 3)
]

# Параметры для конуса
cone_radius = 0.25
cone_height = 0.5
cone_slices = 30
cone_stacks = 1
cone_quadric = gluNewQuadric()

# Углы для вращения
rotation_x = 0
rotation_y = 0
rotation_z = 0

"""
     Функция draw_tetrahedron() отвечает за отрисовку фигуры тетраэдр. 
     В функции определяются треугольники и их вершины, используется смешивание цветов с прозрачностью. 
     RGBA-цвета треугольников устанавливаются с помощью glColor(). 
     Значения координат каждой вершины умножаются на 0.5 для уменьшения размера тетраэдра в окне.
"""
def draw_tetrahedron():
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glBegin(GL_TRIANGLES)
    glColor4f(0.5, 0.8, 0.7, 0.5)

    for face in tetrahedron_faces:
        for vertex_index in face:
            glVertex3fv([coord * 0.5 for coord in tetrahedron_vertices[vertex_index]])
    glEnd()

"""
     Функция draw_cone() преднаначена для отображения конуса с плавными нормалями,
     текстурированием и частичной прозрачностью в окне OpenGL.
     В функции создается объект quadric, используемый для отрисовки геометрических примитивов.
     RGBA-цвета треугольников устанавливаются с помощью glColor().  
"""
def draw_cone():
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    gluQuadricNormals(cone_quadric, GLU_SMOOTH)
    gluQuadricTexture(cone_quadric, GL_TRUE)
    glColor4f(1.0, 0.0, 1.0, 0.5)
    glTranslatef(0, 0, -0.5)
    gluCylinder(cone_quadric, 0, cone_radius, cone_height, cone_slices, cone_stacks)
    glTranslatef(0, 0, cone_height)
    gluDisk(cone_quadric, 0, cone_radius, cone_slices, 1)
    glDisable(GL_BLEND)

"""
     Функция display() используется для отображения графики в окне OpenGL.
     Эта функция отрисовывает тетраэдр и конус в соответствии с установленными 
     углами вращения и цветами для каждой из фигур.
"""
def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glRotatef(rotation_x, 1, 0, 0)
    glRotatef(rotation_y, 0, 1, 0)
    glRotatef(rotation_z, 0, 0, 1)

    glColor3f(1.0, 0.0, 0.0)
    draw_tetrahedron()

    glColor3f(0.0, 0.0, 1.0)
    draw_cone()

    glfw.swap_buffers(window)

"""
     Функция key_callback() обрабатывает события нажатия клавиш для вращения сцены, 
     в частности, изменяет углы вращения в зависимости от нажатой клавиши.
"""
def key_callback(_, key, __, action, ___):
    global rotation_x, rotation_y, rotation_z

    if action == glfw.PRESS or action == glfw.REPEAT:
        if key == glfw.KEY_UP:
            rotation_x += 5
        elif key == glfw.KEY_DOWN:
            rotation_x -= 5
        elif key == glfw.KEY_LEFT:
            rotation_y -= 5
        elif key == glfw.KEY_RIGHT:
            rotation_y += 5
        elif key == glfw.KEY_Z:
            rotation_z += 5
        elif key == glfw.KEY_X:
            rotation_z -= 5

def main():
    global window
    if not glfw.init():
        return

    window = glfw.create_window(800, 600, "Пересечение тетраэдра и конуса", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (800 / 600), 0.1, 50.0)
    glTranslatef(0, 0, -5)
    glfw.set_key_callback(window, key_callback)

    while not glfw.window_should_close(window):
        glfw.poll_events()
        display()

    glfw.terminate()

if __name__ == "__main__":
    main()
