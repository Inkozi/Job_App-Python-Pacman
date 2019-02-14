import unittest
import sys
import os.path

# Import application code here ...
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.audition import it_runs  # noqa
from src.pacman import Pacman
from src.level import Dot
from src.level import Wall
from src.level import Floor
from src.main import Theatre


class TestMarkdownPy(unittest.TestCase):

    def test_it_runs(self):
        self.assertTrue(it_runs())

class TestConstructors(unittest.TestCase):

    def test_constructor_pacman(self):
        x = 1
        y = 1
        self.assertIsNotNone(Pacman(x,y), "pacman failed to construct")

    def test_dot_constructor(self):
        self.assertIsNotNone(Dot(), "dot failed to construct")

    def test_wall_constructor(self):
        self.assertIsNotNone(Wall(), "wall failed to construct")

    def test_floor_constructor(self):
        self.assertIsNotNone(Floor(), "floor failed to construct")

class TestRenders(unittest.TestCase):

    def test_pacman_render(self):
        x = 1
        y = 1
        pac = Pacman(x,y)
        self.assertEqual(pac.sprite, pac.render(), "pacman's rendered failed")

    def test_dot_render(self):
        dot = Dot()
        self.assertEqual(dot.sprite, dot.render(), "dot's render failed")

    def test_wall_render(self):
        wall = Wall()
        self.assertEqual(wall.sprite, wall.render(), "wall's render failed")

    def test_floor_render(self):
        floor = Floor()
        self.assertEqual(floor.sprite, floor.render(), "floor's render failed")

class TestPacmanMovement(unittest.TestCase):

    def test_moveUp(self): #default starting position is up.
        x = 1
        y = 1
        pac = Pacman(x,y)
        pac.movement("up")
        self.assertEqual(y-1, pac.posY, "Pacman Failed to moveUp")
    
    def test_moveLeft(self):
        x = 1
        y = 1
        pac = Pacman(x,y)
        pac.movement("left")
        self.assertEqual(pac.sprite, pac.render(), "Pacman Failed to Rotate Left")
        pac.movement("left")
        self.assertEqual(x-1, pac.posX, "Pacman Failed to move Left")

    def test_moveRight(self):
        x = 1
        y = 1
        pac = Pacman(x,y)
        pac.movement("right")
        self.assertEqual(pac.sprite, pac.render(), "Pacman Failed to Rotate Right")
        pac.movement("right")
        self.assertEqual(x+1, pac.posX, "Pacman Failed to move Right")

    def test_moveDown(self):
        x = 1
        y = 1
        pac = Pacman(x,y)
        pac.movement("down")
        self.assertEqual(pac.sprite, pac.render(), "Pacman Failed to Rotate Down")
        pac.movement("down")
        self.assertEqual(y+1, pac.posY, "Pacman Failed to move Down")


class TestCollisions(unittest.TestCase):

    def test_pacman_self_collision(self):
        obj = "pacman"
        x = 1
        y = 1
        pac = Pacman(x,y)
        result = pac.collision(obj)
        self.assertFalse(result, "Pacman failed to miss colliding with himself")

    def test_pacman_wall_collision(self):
        obj = "wall"
        x = 1
        y = 1
        pac = Pacman(x,y)
        result = pac.collision(obj)
        self.assertTrue(result, "Pacman failed to collide with a wall")

    def test_pacman_floor_collision(self):
        obj = "floor"
        x = 1
        y = 1
        pac = Pacman(x,y)
        result = pac.collision(obj)
        self.assertTrue(result, "Pacman failed to collide with a floor")

    def test_pacman_dot_collision(self):
        obj = "dot"
        x = 1
        y = 1
        pac = Pacman(x,y)
        result = pac.collision(obj)
        self.assertTrue(result, "Pacman failed to collide with a dot")


if __name__ == '__main__':
    unittest.main()
