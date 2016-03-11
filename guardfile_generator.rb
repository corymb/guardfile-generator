require 'find'


def get_file_count(extension)
  files = []
  Find.find('.') do |path|
    files << path if path =~ /.*\.#{extension}$/
  end
  return files.length
end

def write_guardfile(extension, test_string)
end

project_type = get_file_count('rb') < get_file_count('py') ? 'py' : 'rb'
puts project_type
