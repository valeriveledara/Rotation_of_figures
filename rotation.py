import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import math

# Parameters for the tetrahedron
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

# Parameters for the cone (replacing the cylinder)
cone_radius = 0.25
cone_height = 0.5
cone_slices = 30
cone_stacks = 1  # Adjusted stacks for a cone
cone_quadric = gluNewQuadric()

# Rotation angles
x = 0
y = 0
z = 0

def draw_tetrahedron():
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glBegin(GL_TRIANGLES)
    glColor4f(0.0, 0.0, 1.0, 0.3)
    for face in tetrahedron_faces:
        for vertex_index in face:
            glVertex3fv([coord * 0.5 for coord in tetrahedron_vertices[vertex_index]])
    glEnd()

def draw_cone():
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    gluQuadricNormals(cone_quadric, GLU_SMOOTH)
    gluQuadricTexture(cone_quadric, GL_TRUE)
    glColor4f(1.0, 0.0, 1.0, 0.3)
    gluCylinder(cone_quadric, 0, cone_radius, cone_height, cone_slices, cone_stacks)
    glTranslatef(0, 0, cone_height)
    gluDisk(cone_quadric, 0, cone_radius, cone_slices, 1)
    glDisable(GL_BLEND)

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glRotatef(x, 1, 0, 0)
    glRotatef(y, 0, 1, 0)
    glRotatef(z, 0, 0, 1)

    glColor3f(1.0, 0.0, 0.0)
    draw_tetrahedron()

    glColor3f(0.0, 0.0, 1.0)
    glTranslatef(0, 0, -cone_height / 2)  # Adjust for cone
    draw_cone()

    glfw.swap_buffers(window)

def key_callback(_, key, __, action, ___):
    global x, y, z

    if action == glfw.PRESS or action == glfw.REPEAT:
        if key == glfw.KEY_UP:
            x += 5
        elif key == glfw.KEY_DOWN:
            x -= 5
        elif key == glfw.KEY_LEFT:
            y -= 5
        elif key == glfw.KEY_RIGHT:
            y += 5
        elif key == glfw.KEY_Z:
            z += 5
        elif key == glfw.KEY_X:
            z -= 5

def main():
    global window
    if not glfw.init():
        return

    window = glfw.create_window(800, 600, "Intersection of Tetrahedron and Cone", None, None)
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
