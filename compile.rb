require 'erb'
require 'json'

width = (97 / 2).to_i - 1
height = 27

Dir['*.erb.conf'].each do |input|
  base = input.chomp('.erb.conf')
  output = base + '.gen.conf'
  compiled = ERB.new(File.read(input)).result(binding)
  File.write(output, compiled)
end

system '/src/start.sh', "#{height}"

