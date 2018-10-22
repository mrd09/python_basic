# -*- coding: utf-8 -*-

'''
Over view:
- Variable là gì?
- Why need variable
- Variable init
- Cách kiểm tra dữ liệu của variable
'''

'''
1. Biến là gì?
- Variable là tên của một vùng trong bộ nhớ RAM, được sử dụng để lưu trữ thông tin.
- Bạn có thể gán thông tin cho một biến, và có thể lấy thông tin đó ra để sử dụng. 
- Khi một biến được khai báo, một vùng trong bộ nhớ sẽ dành cho các biến.
'''

'''
2. Tại sao lại cần biến?
Biến giúp chúng ta lưu trữ các dữ liệu và cho phép chúng ta lấy các dữ liệu của chúng để tính toán được thuận tiện và chính xác hơn.
'''

'''
3. Khơi tạo biến
- Tên của biến không được bắt đầu bằng số
- Tên biến không được trùng với các từ khóa của Python: [URL](https://doc-14-2s-docs.googleusercontent.com/docs/securesc/74l2tiutvrrfff5qhfh9nv9pg59hrbtq/o72rtn59t7gbvmtoqihcus12d5tljo90/1533290400000/02133430087311516622/05437506637140307374/0B203s9OfQJZcVGI0MFJSOG1lX1E)
- Tên của biến chỉ chứa các chữ cái, số và ‘_’
- Syntax:
	<tên biến> = <giá trị của biến>
'''
#Vi du:

tuoi = 17 # biến thứ nhất lấy giá trị biến thứ nhất
ten = "Bài giảng thuộc về How Kteam" # biến thứ hai lấy giá trị biến thứ hai
PI = 3.14 # biến thứ ba lấy giá trị biến thứ ba

'''
4. Kiểm tra dữ liệu của biến:
- Syntax:
	type(<tên biến>)
'''
#Ví dụ:
print("tuoi:", tuoi)
print("type tuoi:", type(tuoi))
print("ten:", ten)
print("type ten:", type(ten))
print(PI)
print("type PI:", type(PI))

