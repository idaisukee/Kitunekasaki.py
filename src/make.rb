alphabet = File.join(File.expand_path(File.dirname(__FILE__)), '../dat/alphabet.dat')
symbol = File.join(File.expand_path(File.dirname(__FILE__)), '../dat/symbol.dat')
monster = File.join(File.expand_path(File.dirname(__FILE__)), '../dat/monster.dat')

gentle = File.readlines(alphabet).reject{ |i| i == "\n" } + File.readlines(symbol).reject{ |i| i == "\n"} 
gentle_array = gentle.map do |line|
	i = line.strip.split(' ')
	qwerty = i[0]
	dvorak = i[1]
	[qwerty, dvorak]
end

monster = File.readlines(monster).reject{ |i| i == "\n"} 
monster_array = monster.map do |line|
	i = line.strip.split(' ')
	qwerty = i[0]
	dvorak = i[1]
	[qwerty, dvorak]
end

gentle_modifiers = [nil, 'Shift-', 'C-', 'M-', 'Win-', 'Shift-C-', 'Shift-M-', 'Shift-Win-', 'C-M-', 'C-Win-', 'M-Win-', 'Shift-C-M-', 'Shift-C-Win-', 'Shift-M-Win-', 'C-M-Win-']
monster_modifiers = gentle_modifiers.reject do |i|
	/Shift/.match i
end

product_lines = ((gentle_modifiers.product gentle_array) + (monster_modifiers.product monster_array)).map do |i|
	modifier = i[0]
	qwerty = i[1][0]
	mod_qwerty = [modifier, qwerty].join('')
	dvorak = i[1][1]
	mod_dvorak = [modifier, dvorak].join('')
	product_line = 	"K(\"#{mod_qwerty}\"): K(\"#{mod_dvorak}\")"
end


puts product_lines.join(",\n")

=begin
array = Array.new
mod = ['C', 'M', 'S']
(0 .. mod.size).each do |i|
	array << mod.combination(i).to_a
end

a =array.map do |i|
	i.map do |j|
		j.join('-')
	end
end.flatten
p a
=end
