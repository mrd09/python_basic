print("Lesson 12 : Kiểu dữ liệu List trong Python - Phần 1")
print("----------------------------")
print('''*Overview:
	1. Container. Đặt vấn đề và cách giải quyết
	2. Giới thiệu về List trong Python + Cách khởi tạo List
		2.1. Sử dụng List Comprehension
		2.2. Sử dụng constructor list
			2.2.1. Constructor là gì?
			2.2.2. Python Non Parameterized vs Python Parameterized Constructor?
			2.2.3. Constructor List
	3. Một số toán tử với List trong Python
		3.1. Toán tử +
		3.2. Toán tử *
		3.3. Toán tử in
	4. Indexing và cắt List trong Python
	5. Thay đổi nội dung List trong Python
	6. Ma trận
	7. Vấn đề cần lưu tâm khi sử dụng List ''')


print("")
print("# 1. Container. Đặt vấn đề và cách giải quyết")
print('''- Các bạn đã biết đến BIẾN (đã giới thiệu trong bài BIẾN TRONG PYTHON),
		 đó là một container cho phép ta lưu trữ các dữ liệu và lấy ra khi cần, thay đổi khi ta cần cập nhật giá trị hoặc sửa chữa.''')
print('''- Khả năng của biến vẫn bị giới hạn, không thể lưu hai giá trị một lúc''')
print('''	=> Cần đến container có khả năng lưu trữ nhiều giá trị cùng một lúc 
			=> Vì thế, Python có rất nhiều các container cho phép ta lưu trữ nhiều các giá trị, đối tượng cùng một lúc, 
			hỗ trợ cho chúng ta trong việc truy xuất, tính toán, thay đổi
			=> Trong bài này ta học list, 
			Trong các ngôn ngữ lập trình khác, những container chứa được nhiều giá trị cùng một lúc thường được gọi là ARRAY (mảng).''')

print("")
print("# 2. Giới thiệu về List + Khởi tạo 1 list")
print('''- Cú pháp: [<giá trị thứ nhất>, <giá trị thứ hai>, .., <giá trị thứ n – 1>, <giá trị thứ n>]
		 => LIST là một container gồm các yếu tố sau:
		 	+ Được giới hạn bởi cặp ngoặc [ ], tất cả những gì nằm trong đó là những phần tử của List.
		 	+ Các phần tử List phân cách nhau = dấu ','
		 	+ List có khả năng chứa mọi giá trị, đối tượng trong Python. Và bao gồm chứa chính nó!  ''')

print("- Ví dụ:")
list_a = [1, 2, 3, 4, 5]
list_b = ['a', 'b', 'c', 'd']
list_c = [[1, 2], [3, 4]]
list_d = [1, 'two', [3, 4]]
empty_list = []
print("list_a =", list_a, ", list_b =", list_b, ", list_c =", list_c, ", list_d =", list_d, ", empty_list =", empty_list)

print("# 2.1. Sử dụng List Comprehension")
print("- Sử dụng vòng lặp for để tạo ra list value:")
print("- Ví dụ:")

a = [kteam for kteam in range(3)]
print("\t+ Dùng vòng lặp for để tạo giá trị list a = [kteam for kteam in range(3)] =",a)
b = [[n, n * 1, n * 2] for n in range(1, 4)]
print("\t+ Ví dụ 2: b = [[n, n * 1, n * 2] for n in range(1, 4)] =", b)

print('# 2.2. Sử dụng constructor')
print('''- Cú pháp: list(iterable)
		 - Có rất nhiều đối tượng chúng ta có thể sử dụng vòng lặp for. Những đối tượng đó gọi là những đối tượng "iterable". 
		 => Và thao tác duyệt qua những đối tượng này gọi là iteration
		 => 2 iterable đã được biết là string và List
		 => Ngoài ra còn có các dạng dữ liệu khác cũng iterable: tuple: (1, 2, 3), dictionary: {'one': 1, 'two': 2, 'three': 3}
		 => When we say "dictionary is iterable," iteration over a dictionary means iteration over the keys of the dictionary. ''')

print('''# 2.2.1. Constructor là gì:
	- Constructor - Phương thức khởi tạo là một phương thức đặc biệt ở trong class, phương thức này mặc định sẽ được gọi khi chúng ta khởi tạo class đó.
	- 1 class sẽ gồm các thuộc tính (các phương thức) miêu tả về Object nào đó
	- Vậy thì constructor trong 1 class sẽ có nhiệm vụ: 
		+ Nó thường được dùng để khởi tạo các thuộc tính, xử lý phương thức 
		+ Hoặc là dùng để nhận các tham số truyền vào class khi khởi tạo
	
	- Cú pháp: def __init__(self) ''')

print('''2.2.2. Python Non Parameterized vs Python Parameterized Constructor? 
	A. Constructor Non Parameterized:  def __init__(self):
	- Example:
		class Student:  
	    # Constructor - non parameterized  
    		def __init__(self):  
        		print("This is non parametrized constructor")  
    		def show(self,name):  
        		print("Hello",name)  
		
		student = Student()  
		student.show("irfan") # we pass the parameter when we call the property(method inside classs) ''')
print("\t- Result:")
print("--------------------")
class Student:
	# Constructor - non parameterized 
	def __init__(self):
		print("This is non parametrized constructor")
	def show(self, name):
		print("Hello", name)

student = Student()
student.show("Mr.D")
print("--------------------")

print('''\tB. Constructor with Parameterized:  def __init__(self, para1, para2, ...): 
	- Example:
		class Student:  
		    # Constructor - parameterized  
		    def __init__(self, name):  # we pass the parameter when we init the class
		        print("This is parametrized constructor")  
		        self.name = name  
		    def show(self):  
		        print("Hello",self.name)  
		student = Student("irfan")  
		student.show()    
	''')
print("\t- Result:")
print("--------------------")
class StudentP:
	# Constructor - parameterized 
	def __init__(self, name):
		print("This is parameterized constructor")
		self.name = name
	def show(self):
		print("Hello", self.name)
student = StudentP("Mr.D")
student.show()
print("--------------------")

print(''' 2.2.3. Constructor List:
	- Cú pháp: list()
	- Ví dụ:''')
lst = list([1, 2, 3])
print("\t\t+ list([1, 2, 3] =", lst)
str_list = list('HowKTeam')
print("\t\t+ list('HowKTeam') =", str_list)
print('''\t+ list(1)
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	TypeError: 'int' object is not iterable''')

print("")
print("# 3. Một số toán tử với List trong Python:")
print("## 3.1 Toán tử +:")
print('''- Cộng list vs list:
	+ lst = [1, 2, 3]
	+ lst += ['one', 'two']''')
lst = [1, 2, 3]
lst += ['one', 'two']
print("=> Result: List mới là: ", lst)

print('''- Cộng list vs chuỗi:
	+ lst = [1, 2, 3, 'one', 'two']
	+ lst += 'abc' ''')
lst += 'abc'
print("=> Result: List mới là: ", lst)

print('''- Ngược lại Chuỗi + List thì ko được phép:
	>>> 'abc' + [1, 2]  
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	TypeError: must be str, not list  ''')

print('## 3.2. Toán tử * :')
print('- Ví dụ:')
lst = list('MrD') * 2 
print("\t+ lst = list('MrD')*2 = ",lst)
print('- Ví dụ 2:')
lst = [1, 2, 3] * 2
print("\t+ lst = [1, 2, 3]*2 = ",lst)

print('## 3.3. Toán tử in :')
print('- Ví dụ:')
a = 'a' in [1, 2, 3]
print("\t+ Kiểm tra tính đúng của: a = 'a' in [1, 2, 3] =", a)
a = 'a' in ['a', 2, 3]
print("\t+ Kiểm tra tính đúng của: a = 'a' in ['a', 2, 3] =", a)
a = 'a' in [[a], 2, 3]
print("\t+ Kiểm tra tính đúng của: a = 'a' in [[a], 2, 3] =", a)

print("")
print("# 4. Indexing và cắt List trong Python")
print('''- Như đã đề cập, List với chuỗi giống nhau rất nhiều điểm, và phần Indexing và cắt List này hoàn toàn giống với Indexing và cắt chuỗi.''')
lst = [1, 2, 'a', 'b', [3, 4]]
print("- Ví dụ: lst = [1, 2, 'a', 'b', [3, 4]]")
print("\t + lst[0] = ", lst[0])
print("\t + lst[-1] = ", lst[-5])