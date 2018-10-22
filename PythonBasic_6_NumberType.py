# -*- encoding: utf-8 -*-

'''
Overview: Số là gì
- Trong Python cũng hỗ trợ rất nhiều kiểu dữ liệu số. Một số kiểu dữ liệu cơ bản như:
	- số nguyên (integers), 
	- số thực (floating-point), 
	- phân số (fraction), 
	- số phức (complex).
'''

'''
### 1. Số nguyên(integer):
- gồm các số nguyên dương (1, 2, 3, ..), các số nguyên âm (-1, -2, -3) và số 0. 
- Một điểm đáng chú ý trong Python 3.X đó là kiểu dữ liệu số nguyên là vô hạn. 
	=> Điều này cho phép bạn tính toán với những số cực kì lớn, điều mà đa số các ngôn ngữ lập trình khác KHÔNG THỂ.
'''
# Ví dụ:
print("# 1.Số là gì")
a = 4 # gán giá giá trị của biến a là số 4, là một số nguyên
print("type a la", type(a))



'''
### 2. Số thực(float):
- tập hợp các số nguyên và số thập phân 1, 1.4, -123, 69.96,…
'''
# Ví dụ:
print("\n")
print("# 2. Số thực (float)")
f = 1.23 # gán giá trị của biến f là số 1.23, là một số thực
print("type cua f la", type(f))

q = 1.0  # đây là số thực, không phải số nguyên
print("type cua q la", type(q))

t = 10/3
print("- Số thực độ chính xác 15 chữ số:")
print(t)
print('''	Python 2.7: 10/3 = 3
	Python 3.6: 10/3 = 3.3333333333333335 => Số thực độ chính xác 15 chữ số ''')

'''
Python 2.7: 10/3 = 3
Python 3.6: 10/3 = 3.3333333333333335 => Số thực độ chính xác 15 chữ số

Nếu muốn chính xác hơn:
	>>> from decimal import *   # lấy toàn bộ nội dung của thư viện Decimal
	>>> getcontext().prec = 30   # lấy tối đa 30 chữ số phần nguyên và phần thập phân Decimal
	>>> Decimal(10) / Decimal(3)
	Decimal(‘3. 33333333333333333333333333333’)
	>>> type(Decimal(5))   # các số Decimal thuộc lớp Decimal
	<class 'decimal.Decimal'>

=> Tuy Decimal có độ chính xác cao hơn so với float tuy nhiên nó lại khá rườm rà so với float. 
Do đó, hãy cân bằng sự tiện lợi và chính xác để chọn kiểu dữ liệu phù hợp.
'''
# Ví dụ:
from decimal import * # lấy toàn bộ nội dung của thư viện decimal
getcontext().prec = 30 # lấy tối đa 30 chữ số phần thập phân Decimal
e = Decimal(10) / Decimal(3)
st = "- Kết quả của 10/3 dùng decimal với phần thập phân 30 chữ số là:"
print(st); print(e)

## note that sublime text not support for unicode output when Build code
## in Python display unicode normally


''' 
### 3. Phân số:
Tạo một phân số
Để tạo phân số trong python, ta sử dụng hàm Fraction với cú pháp sau
	Fraction(<Tử_số>, <Mẫu_số>)
'''
print("")
print("# 3. Phân số:")
from fractions import * # lấy toàn bộ nội dung của thư viện fraction
g1 = Fraction(1, 4)
g2 = Fraction(3, 9)
print("Gia tri cua g1:", g1)
print("Type g1 la", type(g1))

'''
### 4. Số phức:

Số phức gồm 2 thành phần :
	<Phần thực> + <Phần ảo> j

Trong đó
	<Phần thực> <Phần ảo> là số thực
	j là đơn vị ảo trong toán học với  j2 = -1

Tạo một số phức
Để tạo một số phức, bạn có thể sử dụng hàm complex với cú pháp sau
	complex(<Phần_thực>,<Phần_ảo>)

Gán giá trị số phức cho một biến
	<tên_biến> = <Phần_thực> + <Phần_Ảo>j

Xuất ra từng phần của một biến số phức
Để xuất ra phần thực, ta sử dụng cú pháp:
	<tên_biến>.real

Để xuất ra phần ảo của biến số phức, ta dùng cú pháp:
	<tên_biến>.imag
'''
'''
# Ví dụ:
- Nhập một số số phức sau
	1. 1 + 3j 
	2. Gán biến c có giá trị 2+1j. Xuất ra phần thực và phần ảo của biến c.
	3. 4 +j (sẽ có lỗi vì kiểu dữ liệu nhập vào không đúng).
	4. Tạo số phức có phần thực là 3, phần ảo là 1.
	5. Tạo số phức chỉ có phần thực là 2.
	6. Xuất ra kiểu dữ liệu của số 3+1j.
'''

print("# 4. Số phức")
print("")
print("- Gán giá trị cho biến c là một số phức với phần thực là 2 còn phần ảo là 1")
c = 2 + 1j
print(c)
print("- TH sai: d = 4 + j")
print('''# phần ảo là 1, tuy vậy chúng ta không được phép bỏ số 1 như trong toán
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'j' is not defined''')

e = 4 + 1j
print("- So phuc dung format:")
print(e)
print("Day la phan ao cua so phuc e", c.imag)
print("Day la phan thuc cua so phuc e",c.real)

print("- # dùng hàm complex để tạo một số phức với phần thực là 3, ảo là 1: complex(3 , 1)")
f = complex(3 , 1)
print(f)
print("type la so phuc f", type(f))

print("")
print("# 5. Các toán tử cơ bản với kiểu dữ liệu số trong Python")
print('''- Biểu thức: gồm 2 thành phần
	+ Toán hạng: có thể là một hằng số, biến số (X , Y)\n 	+ Toán tử: xác định cách thức làm việc giữa các toán hạng (+,-,*,/)''')

print('''- Một số biểu thức:
	X + Y	:	Tổng của X và Y
	X - Y	:	Hiệu của X với Y
	X * Y	:	Tích
	X / Y	:	Thương (Kết quả là số phức: vd: 1.03
	X // Y 	:	Thương nguyên (Kết quả luôn < or = X / Y
	X % Y	:	Dư của thương X/Y
	X ** Y	:	Lũy thừa mũ Y với cơ số X''')

print("- Ví dụ")
a = 8
print("a = 8", a)
b = 3
print("b = 3", b)
print("a + b:", a + b)
print("a - b:", a - b)
print("a * b:", a * b)
print("a / b:", a / b)
print("a // b:", a // b)
print("a % b:", a % b)
print("a ** b", a ** b)

print("")
print("# 6. Thư viện math:")
print("- Import thư viện: import <tên_thư_viện>")
print("\t+ Ví dụ: import math")
print("- Muốn sử dụng hàm: <tên_thư_viện>.<tên_hàm>")
print('''- Một số hàm thường dùng:
	.trunc(x)	:	trả về số nguyên là phần nguyên của số x
	.floor(x)	:	trả về số nguyên làm tròn từ số x, kết quả < or = x
	.ceil(x)	:	trả về số nguyên làm tròn từ số x, kết quả > or = x
	.fab(x)		:	trả về số thực là giá trị tuyệt đối của x
	.sqrt(x)	:	trả về số thực là căn bậc 2 của x
	.gcd(x)		:	trả về số nguyên là ước chung lớn nhất của x và y''')

import math
print("- Vi du ham trunc: trunc(3.9) = ", math.trunc(3.9))
print("- Vi du ham fabs: fabs(-3) =", math.fabs(-3))
print("- Vi du ham sqrt: sqrt(16) =", math.sqrt(16))
print("- Vi du ham gcd: gcd(6,4) =", math.gcd(6,4))

print("")
print("# Kết Luận:")
print("- Khi làm việc tính toán nên để ý lớn nhỏ của số âm dương ngược nhau")