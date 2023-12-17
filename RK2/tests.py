import unittest
from main import *


class TestOrchestraProgram(unittest.TestCase):
	def setUp(self):
		self.conductors = [
			Conductor(1, 'John Smith', 5000),
			Conductor(2, 'Emily Johnson', 6000),
			Conductor(3, 'Michael Davis', 5500)
		]

		self.orchestras = [
			Orchestra(1, 'Symphony Orchestra', 1),
			Orchestra(2, 'Chamber Orchestra', 2),
			Orchestra(3, 'Philharmonic Orchestra', 3)
		]

		self.conductor_orchestras = [
			ConductorOrchestra(1, 1),
			ConductorOrchestra(2, 2),
			ConductorOrchestra(3, 3),
			ConductorOrchestra(1, 2),
			ConductorOrchestra(2, 1),
			ConductorOrchestra(3, 2),
		]

	def test_join_data(self):
		result = join_data(self.conductors, self.orchestras)
		expected_result = [
			('John Smith', 5000, 'Symphony Orchestra'),
			('Emily Johnson', 6000, 'Chamber Orchestra'),
			('Michael Davis', 5500, 'Philharmonic Orchestra')
		]
		self.assertEqual(result, expected_result)

	def test_calculate_total_salary(self):
		orchestra = self.orchestras[0]  # Symphony Orchestra
		result = calculate_total_salary(orchestra, self.conductors, self.conductor_orchestras)
		expected_result = ('Symphony Orchestra', 11000)
		self.assertEqual(result, expected_result)

	def test_find_conductors_for_symphony(self):
		result = find_conductors_for_symphony(self.orchestras, self.conductors, self.conductor_orchestras)
		expected_result = {'Symphony Orchestra': ['John Smith', 'Emily Johnson']}
		self.assertEqual(result, expected_result)


if __name__ == '__main__':
	unittest.main()
