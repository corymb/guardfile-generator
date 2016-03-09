import os
import shutil
import unittest

from guardfile_generator import _count_by_extension


class HelperFunctions(object):
    def generate_data(self, extension):
        primary, secondary = ('py', 'rb') if extension == 'py' else ('rb', 'py')
        self.create_files(primary, secondary)

    def create_files(self, primary, secondary):
        os.mkdir(self.directory)
        for i in range(5):
            open('{0}/test_{1}.{2}'.format(self.directory, i, primary), 'w+')
        for i in range(4):
            open('{0}/test_{1}.{2}'.format(self.directory, i, secondary), 'w+')


class EnvironmentDetectorTest(HelperFunctions, unittest.TestCase):

    def setUp(self):
        self.directory = 'test_data'

    def tearDown(self):
        shutil.rmtree(self.directory)

    def test_python_detection(self):
        self.generate_data('py')
        print _count_by_extension('test_data', 'py')

    def test_ruby_detection(self):
        self.generate_data('rb')
        print _count_by_extension('test_data', 'rb')

if __name__ == '__main__':
    unittest.main()
