require 'guardfilegenerator'
require 'thor'

module Guardfilegenerator
  class Generator < Thor
    desc "guardfile generate", "This will generate the Guardfile"
    long_desc <<-GUARDFILE

    `hello NAME` will print out a message to the person of your choosing.
    `generate` will generate a Guardfile.

    It will inspect your current environment to determine
    which testrunner you are using.

    It also works for Python projects! Currently supports:

    - Django
    - pytest
    - unittest from the standard library


    Nosetests support coming soon.
    GUARDFILE

    def generate
      # puts Guardfilegenerator.get_file_count('rb')
      extension = Guardfilegenerator.get_file_count('rb') < Guardfilegenerator.get_file_count('py') ? 'py' : 'rb'
      test_string = Guardfilegenerator.get_test_string(extension)
      Guardfilegenerator.write_guardfile(extension, test_string)
    end
  end
end
