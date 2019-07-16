# (`0123456789abcdef`)

# Input: n (Integer)
# Output: Str (Hex representation)
# Example:
# 0 => '0'
# 1 => '1'
# 2 => '2'
# 3 => '3'
# 4 => '4'

# 9 => '9'
# 10 => 'a'
# 11 => 'b'

# 15 => 'f'
# 16 => '10'

# 30 => '1e'
# 31 => '1f'
# 32 => '20'
# 33 => '21'



# ###
# 255 => 'ff'
# 256 => '100'

def intToHexa(n):
  hexa = '0123456789abcdef'
  if(n < 16):
    return hexa[n]

  print(abs(n//16))
  return intToHexa(abs(n//16)) + hexa[n % 16]


print(intToHexa(256))