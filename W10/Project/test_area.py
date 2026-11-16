import unittest
import area

class MyTestCase(unittest.TestCase):

	def test_Circles(self):
		self.assertRaises(ValueError, area.circle, "B")
		self.assertRaises(ValueError, area.circle, "a")
		# Negative
		self.assertRaises(TypeError, area.circle, -2)
		# Zero
		self.assertRaises(TypeError, area.circle, 0)
		# Reg
		self.assertAlmostEqual(3.14159, area.circle(1), 5)
		self.assertAlmostEqual(3.14159, area.circle(1.0), 5)
		# Additional regular cases
		self.assertAlmostEqual(12.56637, area.circle(2), 5)
		self.assertAlmostEqual(78.53982, area.circle(5), 5)

	def testSquares(self):
		self.assertRaises(ValueError, area.square, "A")
		# Neg
		self.assertRaises(TypeError, area.square, -2)
		# Zero
		self.assertRaises(TypeError, area.square, 0)
		# Reg
		self.assertEqual(1, area.square(1))
		self.assertEqual(1, area.square(1.0))
		self.assertEqual(400, area.square(20))
		self.assertAlmostEqual(2745.76, area.square(52.4), 2)
		# Additional regular cases
		self.assertEqual(4, area.square(2))
		self.assertEqual(100, area.square(10))
		self.assertAlmostEqual(0.25, area.square(0.5), 5)
		self.assertAlmostEqual(0.0001, area.square(0.01), 7)

	def testRect(self):
		self.assertRaises(ValueError, area.rectangle, "a", "b")
		self.assertRaises(ValueError, area.rectangle, "a", 2)
		self.assertRaises(ValueError, area.rectangle, 2, "b")
		# Neg
		self.assertRaises(TypeError, area.rectangle, -1, -1)
		self.assertRaises(TypeError, area.rectangle, -1, 1)
		self.assertRaises(TypeError, area.rectangle, 1, -1)
		# Zero
		self.assertRaises(TypeError, area.rectangle, 0, 0)
		self.assertRaises(TypeError, area.rectangle, 0, 1)
		self.assertRaises(TypeError, area.rectangle, 1, 0)
		# Reg
		self.assertEqual(2, area.rectangle(1.0, 2.0))
		self.assertEqual(2, area.rectangle(1, 2))
		self.assertEqual(303.5136, area.rectangle(24.32, 12.48))
		self.assertEqual(2000, area.rectangle(10, 200))
		# Additional regular cases
		self.assertEqual(0.5, area.rectangle(0.5, 1))
		self.assertEqual(0.5, area.rectangle(1, 0.5))
		self.assertEqual(100, area.rectangle(10, 10))
		self.assertEqual(6, area.rectangle(2, 3))

	def testTriangles(self):
		self.assertRaises(ValueError, area.triangle, "B", "u")
		self.assertRaises(ValueError, area.triangle, 2, "g")
		self.assertRaises(ValueError, area.triangle, "f", 1)
		# Neg
		self.assertRaises(TypeError, area.triangle, -1, -1)
		self.assertRaises(TypeError, area.triangle, -1, 1)
		self.assertRaises(TypeError, area.triangle, 1, -1)
		# Zero
		self.assertRaises(TypeError, area.triangle, 0, 0)
		self.assertRaises(TypeError, area.triangle, 0, 1)
		self.assertRaises(TypeError, area.triangle, 1, 0)
		# Reg
		self.assertEqual(5, area.triangle(1, 10))
		self.assertEqual(5.0, area.triangle(1.0, 10.0))
		self.assertAlmostEqual(1012.5, area.triangle(45, 45),1)
		self.assertAlmostEqual(50660339770305.73, area.triangle(56486.35, 1793719713.5345345), 5)
		self.assertAlmostEqual(1.5, area.triangle(1.5, 2), delta=4)
		self.assertAlmostEqual(2.3, area.triangle(2,2.3), delta=4)
		# Additional regular cases
		self.assertEqual(6, area.triangle(3, 4))
		self.assertEqual(50, area.triangle(10, 10))
		self.assertEqual(0.5, area.triangle(1, 1))
		self.assertAlmostEqual(0.00005, area.triangle(0.01, 0.01), 7)

if __name__ == '__main__':
	unittest.main()
