require 'find'
require 'rubygems'
require "guardfilegenerator/version"
require "guardfilegenerator/cli"

module Guardfilegenerator
  def self.get_file_count(extension)
    files = []
    Find.find('.') do |path|
      files << path if path =~ /.*\.#{extension}$/
    end
    return files.length
  end
  def self.get_test_string(extension)
    return extension == 'rb' ? get_ruby_test_string : get_python_test_string
  end
  def self.get_ruby_test_string
    if defined? 'minitest'
      return 'ruby test/*.rb'
    end
    if defined? 'rspec'
      return 'rspec spec'
    end
    if defined? 'rails'
      return 'bundle exec rspec spec'
    end
    installed_gems =  Gem::Specification.sort_by{
      |gem| [gem.name.downcase] }.group_by{ |gem| gem.name }
    raise "Couldn't find test runner in #{installed_gems.keys}"
  end
  def self.get_python_test_string
    requirements = 'requirements.txt'
    if File.file?(requirements)
      dependencies = File.read(requirements).downcase.split(/\n+/)
      case
        when dependencies.index {|s| s.include?('django')}
          return 'python manage.py test'
        when dependencies.index {|s| s.include?('pytest')}
          return 'py.test --color=yes -s test'
        else
          return 'python setup.py test'
      end
    end
    return 'python setup.py test'
  end
  def self.write_guardfile(extension, test_string)
    content = %{
    guard :shell do
      watch /.*.#{extension}/ do
        `#{test_string}`
      end
    end
    }
    File.write('Guardfile', content)
  end
end
