import os
import shutil
import unittest

from guardfile_generator import count_by_extension


class HelperFunctions(object):
    def generate_data(self, extension):
        primary, secondary = ('py', 'rb') if extension == 'py' else ('rb', 'py')
        self.create_files(primary, secondary)

    def create_files(self, primary, secondary):
        primary_count, secondary_count = 5, 4
        os.mkdir(self.directory)
        for i in range(primary_count):
            open('{0}/test_{1}.{2}'.format(self.directory, i, primary), 'w+')
        for i in range(secondary_count):
            open('{0}/test_{1}.{2}'.format(self.directory, i, secondary), 'w+')

        # Sanity check:
        primary_files = [x for x in os.listdir(self.directory) if x.endswith(primary)]
        secondary_files = [x for x in os.listdir(self.directory) if x.endswith(secondary)]
        self.assertEqual(primary_count, len(primary_files))
        self.assertEqual(secondary_count, len(secondary_files))


class EnvironmentDetectorTest(HelperFunctions, unittest.TestCase):

    def setUp(self):
        self.directory = 'test_data'

    def tearDown(self):
        shutil.rmtree(self.directory)

    def test_python_detection(self):
        self.generate_data('py')
        self.assertEqual(count_by_extension('test_data', 'py'), 5)

    def test_ruby_detection(self):
        self.generate_data('rb')
        self.assertEqual(count_by_extension('test_data', 'rb'), 5)

if __name__ == '__main__':
    unittest.main()
