print("Lesson 10: Kiểu dữ liệu chuỗi trong Python - Phần 5")
print("----------------------------")
print('''*Overview:
	1. Các phương thức tách chuỗi
	2. Các phương thức tiện ích
	3. Các phương thức xác thực ''')

print("")
print("# 1. Các phương thức tách chuỗi")
print("## 1.1. Phương thức .split():")
print("- Syntax: <chuỗi>.split(separator=None, maxsplit=-1)")
print("- Công dụng: Trả về một list (kiểu dữ liệu sẽ được Kteam giới thiệu ở bài KIỂU DỮ LIỆU LIST) bằng cách chia các phần tử bằng kí tự sep.")
print("\t+ Nếu sep mặc định bằng None thì sẽ dùng kí tự khoảng trắng.")
print("\t+ Nếu maxsplit được mặc định bằng -1, Python sẽ không bị giới hạn việc tách, còn không, Python sẽ tách với số lần được cung cấp thông qua maxsplit.")
print("- Ví dụ:")
string1 = 