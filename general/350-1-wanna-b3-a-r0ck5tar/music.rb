@rocknroll = true
@silence = false
@a_guitar = 19
@tommy = 44
@music = 160
print '> '
__input = $stdin.gets.chomp
@the_music = Float(__input) rescue __input
if @the_music == @a_guitar
  puts ("Keep on rocking!").to_s
  print '> '
__input = $stdin.gets.chomp
@the_rhythm = Float(__input) rescue __input
  if @the_rhythm - @music == nil
    @tommy = 66
    puts (@tommy).to_s
    @music = 79
    @jamming = 78
    puts (@music).to_s
    puts (@jamming).to_s
    @tommy = 74
    puts (@tommy).to_s
    @tommy = 79
    puts (@tommy).to_s
    @rock = 86
    puts (@rock).to_s
    @tommy = 73
    puts (@tommy).to_s
    break
    puts ("Bring on the rock!").to_s
  else
    break
  end
end
