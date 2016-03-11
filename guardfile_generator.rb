require 'find'


def get_files(extension)
  files = []
  Find.find('.') do |path|
    files << path if path =~ /.*\.#{extension}$/
  end
  return files
end

puts get_files('rb')
