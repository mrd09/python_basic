print("Lesson 7: KIỂU DỮ LIỆU CHUỖI")
print("----------------------------")
print('''*Overview:
	Trong bài học này, chúng ta sẽ cùng tìm hiểu các vấn đề:
	1.Chuỗi là gì?
	2.Sự khác nhau giữa ‘ ’ và “ ”.
	3.Chuỗi nhiều dòng với ‘’’ và “””. Khái niệm Docstring.
	4.Escape Sequence là gì?
	5.Câu hỏi củng cố''')

print("\n")
print("# 1. Chuỗi là gì?")
print('''- Trong Python, chuỗi là những thứ được đặt trong cặp dấu ' ', hoặc " ",  có thể cũng là trong cặp  \''' \''', """ """. 
	+ Nhưng cơ bản và thường đường sử dụng nhất là cặp '' và "".''')
s = 'how kteam'
print("- gán cho biến s với giá trị là một chuỗi: s =", s)
s1 = "how kteam"
print("- gán cho biến s1 với giá trị là một chuỗi: s =", s1)
print("- Type cua s va s1 la:", type(s))
print("")
print('''# 2. But when to use "" or '':
	+ "" use when string have ' and vice versa use '' when string have " ''')
print("")
print("# 3. Docstring: Chuỗi/chú thích nhiều dòng")
print("- Để in chuỗi/chú thích nhiều dòng, đặt chuỗi/chú thích đó trong cặp dấu ''' or \"\"\" ")
print('''- Sau đây là ví dụ chuỗi nhiều dòng:
	1.A
	2.B''')
print('- Hay xuất hiện ở đầu một file Python, sau một dòng định nghĩa lớp, hàm')
print("""- Ví dụ:)
'''
Đây là những dòng chú thích đầu file
Về việc import các thư viện, module '''

import lungtung
import taolao

def hamvodung():
	'''
	Đây là 1 doctring
	Cho một function:
	là một hàm vô dụng'''
	pass

class vovan:
	'''
	Class ko hề có gì
	ví dụ thôi
	'''
	pass
""")
print("")
print("# 4. Escape Sequence:")
print("- Ví dụ thường dùng nhất: là kí tự xuống dòng '\\n'" )
print("- Escape Sequence là một chuỗi (chính xác là kí tự) đặc biệt trong Python. Bắt đầu với một dấu \\")
print('''- Một số escape sequence hay dùng:
	Alert	:	\\a 	:	Phát ra 1 tiếng bíp
	Backspace	:	\\b 	:	Đưa con trỏ/xóa về lại 1 khoảng trắng
	New line	:	\\n 	:	Đưa con trỏ xuống dòng tiếp theo
	Horizontal tab	:	\\t 	:	In ra 1 tab
	Single quote	:	\\' 	:	In ra kí tự \' 
	Double quote	:	\\" 	:	In ra kí tự " 
	Blackslash		:	\\\\	:	In ra kí tự \\ ''')
print('-----------------------')
print('- Sau day la 1 tieng bip: \a')
print('- Trinh bay xuong dong:\nxuong dong 1\nxuong dong 2')
print('- Trinh bay tab: abc\tdef')
print('- Muon in dau \\')
print('- Muon in dau \'')