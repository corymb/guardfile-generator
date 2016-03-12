require 'find'
require 'rubygems'

def get_file_count(extension)
  files = []
  Find.find('.') do |path|
    files << path if path =~ /.*\.#{extension}$/
  end
  return files.length
end

def write_guardfile(extension, test_string)
content = %{
guard :shell do
  watch /.*.#{extension}/ do
    `#{test_string}`
  end
end
}
  File.write('Guardfile_dev', content)
end

def get_test_string(extension)
  return extension == 'rb' ? get_ruby_test_string : get_python_test_string
end

def get_ruby_test_string
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

def get_python_test_string
  puts 'Python'
end

extension = get_file_count('rb') < get_file_count('py') ? 'py' : 'rb'
test_string = get_test_string(extension)
puts test_string
write_guardfile(extension, test_string)
