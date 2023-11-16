import glfw
import pytest as pytest
from rotation import draw_tetrahedron, draw_cone

def test_draw_tetrahedron():
    if not glfw.init():
        assert False, "glfw.init() error"

    window = glfw.create_window(800, 600, "Test Window", None, None)
    if not window:
        glfw.terminate()
        assert False, "glfw.create_window() error"

    glfw.make_context_current(window)
    draw_tetrahedron()
    glfw.terminate()

def test_draw_cone():
    if not glfw.init():
        assert False, "glfw.init() error"

    window = glfw.create_window(800, 600, "Test Window", None, None)
    if not window:
        glfw.terminate()
        assert False, "glfw.create_window() error"

    glfw.make_context_current(window)
    draw_cone()
    glfw.terminate()

if __name__ == "__main__":
    pytest.main([__file__, '-v'])