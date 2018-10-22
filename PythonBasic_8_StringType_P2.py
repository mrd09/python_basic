print("Lesson 8: KIỂU DỮ LIỆU CHUỖI - P2")
print("----------------------------")
print('''*Overview:
	1. Chuỗi trần là gì?
	2. Một số toán tử với chuỗi
	3. Indexing và cắt chuỗi
	4. Ép kiểu dữ liệu
	5. Thay đổi nội dung chuỗi''')
print("\n")
print("# 1. Chuỗi trần là gì")
print("- Nếu in chuỗi string bình thường thì mỗi khi có \"Escape Sequence\" thì python sẽ translate")
print("- Vậy để vô hiệu hóa \"Escape Sequence\" python cho phép sử dụng \"Chuỗi trần\" => Khi đó sẽ ignore được \"Escape Sequence\" ")
print("- Cú pháp: r'nội dung chuỗi'")
print("- Ví dụ 1:")
a = 'Haizz, \neu mot ngay nao do'
b = r'Haizz, \neu mot ngay nao do'
print("\t+ Nếu ko dùng chuỗi trần:", a)
print("\t+ Nếu dùng chuỗi trần:", b)
print("\t+ Dùng chuỗi trần tương đương với dùng \\\"Escape Sequence\"")
print("\n")

print("# 2. Một số toán tử với chuỗi:")
print("## 2.1. Toán tử +: Nối chuỗi")
print("- Cú pháp: A + B (A và B là type string)")
print("- Ví dụ:")

c = 'te' 
d = 'st'
print("c:", c)
print("d:", d) 
print("c + d =",c + d)
print("----------------------------")
print("## 2.2. Toán tử *: Lặp chuỗi")
print("- Cú pháp: A * N ( Với A là một chuỗi, N là một số nguyên dương)")

print("- Ví dụ:")
e = 'a' * 3
print("Tạo ra chuỗi lặp: 'a' * 3 : ", e)
f = 'abc'
f *= 2
print("Tạo ra chuỗi lăp: f = 'abc', f *= 2, kết quả:", f)
f = f * 2
print("Tạo ra chuỗi lăp: f = 'abcabc', f = f * 2, kết quả:", f)

print("- Khi: A * N, trong TH N là: 0 or số nguyên âm:")
f *= 0
print("Tạo ra chuỗi trắng: f *= 0, kết quả là: ' '", f)
f = 'abc'
f *= -2
print("Tạo ra chuỗi trắng: f = 'abc', f *= -2, kết quả:", f)

print("----------------------------")
print("## 2.3. Toán tử in: Kiểm tra sự tồn tại của chuỗi trong chuỗi")
print("- Khi sử dụng toán tử này, bạn chỉ có thể nhận được một trong hai đáp án đó là True hoặc False.")
print("- Cú pháp: s in A (Với s và A là chuỗi)")
print("=> Kết quả sẽ là True nếu chuỗi s xuất hiện trong chuỗi A. Ngược lại sẽ là False. (True và False là kiểu dữ liệu Boolean) ")
print("- Ví dụ:")
h = 'a' in 'abc'
h1 = 'ac' in 'abc'
print("Check tính đúng của sụ xuất hiện: 'a' in 'abc':", h)
print("Check tính đúng của sụ xuất hiện: 'ab' in 'abc':", h1)

print("\n")
print("# 3. Indexing và cắt chuỗi:")
print("## 3.1. Indexing:")
print('''- Kí tự tạo nên một chuỗi sẽ được đánh số từ 0 -> n-1, từ trái -> phải, 
		với n là số kí tự trong chuỗi và n là nguyên
- nếu đánh index theo thứ tự âm: -n -> -1, từ trái -> phải
		''')
print("- Ví dụ:")
i = 'abc xyz'
print("Gọi chuỗi i =", i)
print('''- Số thự tự index trong ví dụ như sau:
	a   b   c       x   y   z
	0   1   2   3	4   5   6
	-7 -6  -5  -4  -3  -2  -1
	''')
print("- Cú pháp: <chuỗi>[vị trí] = value")
print("In ra giá trị index = 2 trong chuỗi i: i[2] =", i[2])
print("In ra giá trị index = 3 trong chuỗi i: i[3] =", i[3])
print('''In ra giá trị index = 7 trong chuỗi i: i[7] 
	=> ko có index thứ 7 => error: IndexError: string index out of range''')

print('''In ra giá trị index = 3.2 trong chuỗi i: i[3.2] =
	=> index phải là sô nguyên => error: TypeError: string indices must be integers''')
print('''In ra giá trị index = '3' trong chuỗi i: i['3'] =
	=> index phải là sô nguyên, ko thể là string => error: TypeError: string indices must be integers''')
print("-----------------------------")
print("- Để in ra được phần tử cuối cùng khi ko biết index cuối cùng là bao nhiêu: dùng hàm len()")
print("- Ví dụ:")
print("Value của kí tự cuối cùng của chuỗi i là: i[len(i) - 1]:", i[len(i) - 1])
print("")

print("## 3.2. Cắt chuỗi từ trái qua phải")
print("-  Dựa trên Indexing, Python cho phép chúng ta cắt chuỗi/slice")
print("- Cú pháp: <chuỗi>[vị trí bắt đầu : vị trí dừng]")
print("- Rule áp dụng cho cả vị trí dương và âm: value của chuỗi cắt sẽ dừng tại index: \"Vị trí dừng\" - 1 ")
print("- Ví dụ:")
print("Cắt chuỗi index từ 1 -> 4: i[1:5] = ", i[1:5])
print("Cắt chuỗi index  từ 0 -> 2: i[0:3] = ", i[0:3])
print("cắt chuỗi có index từ -4 đến -2: i[-4:-1]", i[-4:-1])
print("cắt chuỗi có index từ 1 đến -2: i[1:-1]", i[1:-1])
print("=> Gt:giá trị lớn nhất trong chuỗi cắt tại: index = -2 => đếm ngược lại: index 1 tương ứng với: -6")
print("=> i[1:-1] <=> i[-6:-1]")
print("-----------------------")
print('''- Vậy làm thế nào cắt được 1 chuỗi có value mà index lớn nhất trong chuỗi gốc?
+ Khi mà cắt chuỗi chỉ được vị trí dừng - 1 => Ta có thể dùng \"vị trí dừng\" = tổng số lượng kí tự trong 1 chuỗi
=> Ví dụ: i = 'abc xyz' => i[1:7] = bc xyz
	''')
print("- Dùng cách bt: để \"vị trí dừng\" = tổng số lượng kí tự: i[1:7]", i[1:7])
print("=> Sử dụng index đặc biệt: \"None\" hoặc là \"bỏ trống vị trí dừng\" python sẽ tự hiểu là cắt đến index cuối cùng của chuối")
print("- Ví dụ:")
print("Cắt chuỗi từ index 1 đến index lớn nhất: i[1:None] = ", i[1:None])
print("Cắt chuỗi từ index 3 đến index lớn nhất: i[3:] = ", i[3:])
print("-----------------------")
print('''- Vậy sẽ ra sao nếu để \"None\" hoặc là \"bỏ trống vị trí\" vào \"vị trí bắt đầu\"?
	=>> Hoàn toàn tương tự python sẽ tự hiểu là cắt từ index đầu tiên của chuỗi: i[:4]
	=>> Nếu bỏ trống cả \"vị trí bắt đầu\" và \"vị trí bắt đầu\" thì ta sẽ copy cả chuỗi: i[:]
	''')
print("- Ví dụ:")
print("# lấy các kí tự có vị trí từ 0 đến 3: i[:4] = ", i[:4])
print("# Copy nguyên cả chuỗi i[:] = ", i[:])

print("")
print("## 3.3. Cắt chuỗi từ trái qua phải")
print("- Cú pháp: <chuỗi>[vị trí bắt đầu : vị trí dừng : bước là số dương]")
print("- \"Bước\": chính là thứ để tính được vị trí tiếp theo cách vị trí trước đó bao nhiêu đơn vị.")
print("- Mặc định nếu ko nhập bước thì sẽ là case cắt chuỗi từ trái qua phải với \"bước = 1\"")
print("\t=> Tức là vị trí của kí tự tiếp theo hơn vị trí của kí tự hiện tại 1 đơn vị")
print("- Ví dụ:")
print("\t+ Nhắc lại chuỗi i =", i)
print('''- Số thự tự index trong ví dụ như sau:
	a   b   c       x   y   z
	0   1   2   3	4   5   6''')
print("\t+ Lấy giá trị từ trái qua phải, dùng bước nhảy dương 1: i[2:5:1] =", i[2:5:1])
print("\t+ Mặc định ko nhập bước nhảy: i[2:5] = i[2:5:1] = ", i[2:5])
print("\t+ Lấy giá trị từ trái qua phải, dùng bước nhảy dương 2: i[1:7:2] =", i[1:7:2])

print("")
print("## 3.4. Cắt chuỗi từ phải qua trái")
print("- Cú pháp: <chuỗi>[vị trí bắt đầu : vị trí dừng : bước là số âm]")
print("- Ví dụ:")
print("\t+ Nhắc lại chuỗi i =", i)
print("\t+ Lấy giá trị từ phải qua trái, dùng bước nhảy âm 1: # bắt đầu ở 3 và dừng ở 1. Các vị trí lấy là 3, 2(1- (-1): i[3:1:-1] =", i[3:1:-1])
print("\t+ Lấy giá trị từ phải qua trái, index ngược từ 3 về 1, dùng bước nhảy âm 1: i[3:0:-1] =",i[3:0:-1])
print("\t+ Lấy giá trị từ phải qua trái, index ngược từ 3 về 0, dùng bước nhảy âm 1: i[3::-1] =",i[3::-1])
print("\t+ Lấy cả chuỗi giá trị từ phải qua trái, dùng bước nhảy âm 1: i[::-1] =",i[::-1])
print("\t+ Không thê lấy giá trị từ vị trí số 3 ngược về vị trí dừng số 1 với bước nhảy dương 1: i[3:1] =",i[3:1])

print("")
print("- Lưu ý: bước nhảy luôn khác 0")
print('''\ti[::0]
\tTraceback (most recent call last):
  \tFile "<stdin>", line 1, in <module>
\tValueError: slice step cannot be zero)''')

print("")
print("# 4.Ép kiểu dữ liệu:")
print("- Mờ đầu:")
a = '69'
b = 69
print("\t+ Gọi biến a = '69' type a sẽ là:", type(a))
print("\t+ Gọi biến b = 69 type b sẽ là:", type(b))
print("\t+ Sẽ có khác biệt khi sử dụng toán tử như sau")
print("\t\t-> a * 2 =", a*2)
print("\t\t-> b * 2 =", b*2)
print("- Vậy muốn ép kiểu value từ sring sang int, ta sử dụng cú pháp: int('string sô nguyên')")
print("- Ví dụ:")
print("\t+ Ép kiểu dữ liệu cho string a về int(): int(a) =", int(a))
print("\t+ Tuy là ép kiểu nhưng biến a vẫn giữ là type string: type(a) =", type(a))
c=int(a)
print("\t=> Vậy muốn đổi type ta chỉ còn cách gọi biến mới với value đã được ép kiểu: c=int(a) =",c)
print("\t=> Type của c bây giờ sẽ là type(c) =", type(c))

print("")
print("- Ép kiểu dữ liệu từ số thực sang số nguyên: bỏ đi phần thập phân sau dấu phẩy, cú pháp: int('string số thực') ")
print("- Ví dụ:")
c = 3.1
print("\t+ Gọi biến c = 3.1")
print("\t+ Type của biến c =", type(c))
d = int(c)
print("\t+ Chuyển đổi từ số thực 3.1 sang số nguyên 3: gọi d = int(c) = ", d)
print("\t+ Type của biến d =", type(d))
print("")

print("- Lưu ý: Không thể chuyển đổi từ chuỗi là 1 số thực ví dụ '3.1' sang số nguyên")
print('''\t+ >>> int('3.1')
	Traceback (most recent call last):
  	File "<stdin>", line 1, in <module>
	ValueError: invalid literal for int() with base 10: '3.1' ''')
print("")

print("- Tuy vậy ta có thể chuyển đổi từ chuỗi là 1 số thực sang số thực, Cú pháp: float('string số thực')")
print("- Ví dụ:")
e = '3.1'
print("\t+ Gọi biến e = '3.1'")
print("\t+ Type của biến e =", type(e))
f = float(e)
print("\t+ Chuyển đổi từ string số thực '3.1' sang số thực 3.1: gọi f = float(e) = ", f)
print("\t+ Type của biến f =", type(f))
print("")

print("")
print("# 5.Thay đổi nội dung chuỗi:")
print("- Bạn có nghĩ tới việc thay đổi nội dung chuỗi nhờ Indexing không? Nhưng đáng buồn Python ko cho phép điều đó")
print("- Nhắc lại chuỗi i =", i)
print("\t+ Giá trị tại index 0: i[0] =", i[0])
print("\t+ Thử thay Giá trị tại index 0: i[0] = k")
print(''' => Lập tức bị Lỗi:
		>>> i[0] = ‘k’
		Traceback (most recent call last):
		  File "<stdin>", line 1, in <module>
		TypeError: 'str' object does not support item assignment ''')

print("")
print("- Bạn chỉ có thể thay thế nó một cách gián tiếp giá trị chuỗi mà biến của bạn lưu giữ bằng cách sử dụng việc cắt chuỗi và toán tử + để tạo ra một chuỗi mới và gán lại vào biến của bạn")
print("- Ví dụ:")
i = 'k' + i[1:]
print("\t + Nối chuỗi mới với chuỗi đã cắt: i = 'k' + i[1:] = ", i)
print("")
print("- Ví dụ cho hàm hash 1 giá trị: hash('abc') =", hash('abc'))
print("- hashable object là hằng, một giá trị không bao giờ thay đổi. Và có một vài trường hợp bắt buộc bạn phải sử dụng kiểu dữ liệu là hashable object điển hình như khóa (key) trong kiểu dữ liệu Dict của Python (một kiểu dữ liệu sẽ được Kteam giới thiệu ở bài DICTONARY TRONG PYTHON).")