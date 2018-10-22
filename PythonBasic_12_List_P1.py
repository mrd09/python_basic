print("Lesson 12 : Kiểu dữ liệu List trong Python - Phần 1")
print("----------------------------")
print('''*Overview:
	Container. Đặt vấn đề và cách giải quyết
	Giới thiệu về List trong Python
	Cách khởi tạo List
	Một số toán tử với List trong Python
	Indexing và cắt List trong Python
	Thay đổi nội dung List trong Python
	Ma trận
	Vấn đề cần lưu tâm khi sử dụng List ''')

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
print(list_a, list_b, list_c, list_d, empty_list)