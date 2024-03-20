# practice 1
print("100")
print(100)
print(50+50)
print("50+50") #answer

# practice 2
print('%d / %d= %d' % (5, 10, 5/10))

# practice 3
print("%04d" % 876)
print("%5s" % "CookBook")
print("%1.1f" % 123.45)

# practice 4
print ("{2:d} {0:d} {1:d]".format (111, 222, 333))


# practice 11
# (1) 1011(2진수)
int(0b1011)
# (2) 1A (16진수)
int(0x1A)

# practice 13
# (1) int('1002', 2)   ## 1002 가 2 진수가 아님
# (2) int('1008', 8)   ## 1008 이 8 진수가 아님
# (3) int('AAFG', 16)  ## 16진수 표기법에 알파벳 'G' 존재 없음

# practice 15
num =  12345678
hex_num = hex(num)
oct_num = oct(num)
bin_num = bin(num)
print("10진수 =>", num)
print("16진수 =>", hex_num)
print(" 8진수 =>", oct_num)
print(" 2진수 =>", bin_num)


