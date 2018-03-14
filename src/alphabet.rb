file = File.join(File.expand_path(File.dirname(__FILE__)), '../dat/alphabet.dat')
lines = File.readlines(file)
product_lines = lines.map do |line|
	array = line.strip.split(' ')
	qwerty = array[0]
	dvorak = array[1]
	'K("' + qwerty + '"): ' + 'K("' + dvorak + '")'
end + lines.map do |line|
	array = line.strip.split(' ')
	qwerty = array[0].upcase
	dvorak = array[1].upcase
	'K("' + qwerty + '"): ' + 'K("' + dvorak + '")'
end	

puts product_lines.join(",\n")
