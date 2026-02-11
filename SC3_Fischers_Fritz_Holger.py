# DIFFICULTY: 1
# Mit lediglich dem gegebenen String wollen wir die folgenden
# Outputs erreichen:
#
# 1. ihsrzihf
# 2. sifhrhi
# 3. sche (mit möglichst wenigen Zeichen)
# 4. eci hsr hsfziFseci
# 5. ii i
#
# TASK: Nutze String-Slicing, um die gesuchten Outputs aus dem
#       vorgegebenen String zu extrahieren.

my_string = "Fischers Fritz fischt frische Fische"

print(my_string[1]+my_string[4]+my_string[7]+my_string[10]+my_string[13]+
      my_string[16]+my_string[19]+my_string[22])
print(my_string[2]+my_string[11]+my_string[15]+my_string[19]+my_string[23]+
      my_string[27]+my_string[31])
print(my_string[2:6])
print(my_string[5]+my_string[3]+my_string[1]+my_string[8]+my_string[4]+
      my_string[7]+my_string[6]+my_string[8]+my_string[4]+my_string[2]+
      my_string[15]+my_string[13]+my_string[1]+my_string[0]+my_string[2]+
      my_string[5]+my_string[3]+my_string[1])
print(my_string[1]+my_string[1]+my_string[8]+my_string[1])