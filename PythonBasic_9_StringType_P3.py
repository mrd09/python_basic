print("Lesson 9: KIỂU DỮ LIỆU CHUỖI - P3")
print("----------------------------")
print('''*Overview:
	1. Giới thiệu về định dạng chuỗi trong Python
	2. Định dạng bằng toán tử %
	3. Định dạng bằng chuỗi f (f-string)
	4. Định dạng bằng phương thức format ''')

print("")
print("# 2. Định dạng bằng toán tử %")
print("- Syntax: <định_dạng_1, định_dạng_2, ... > % (giá trị 1, giá trị 2, ... giá trị n)")
print('''- 1 số toán tử % cơ bản:
  		'd'		Signed integer decimal.	 
		'i'		Signed integer decimal.
		'f'		Floating point decimal format.
		's'		String (converts any Python object using str()).
		'r'		String (converts any Python object using repr()).''')

print("")
string1 = 'test1 %s', 'Escape sequence new line: \n'
string2 = 'test2 %r', 'Escape sequence new line: \n'
a = '%s %s' % (string1)
b = '%r %r' % (string2)
print("- Ví dụ về dùng %s: format string: a = '%s %s' % ('test1 %s', 'Escape sequence new line: \\n') =", a)
print("- Ví dụ về dùng %r: format string: b = '%r %r' % ('test2 %r', 'Escape sequence new line: \\n') =", b)
print('''=> Từ ví dụ ta thấy:
		%s 		:invoke method str() sẽ in ra content của giá trị
		%r 		:invoke method repre() sẽ parse giá trị thành str object bỏ qua escape sequence ''')

print("")
list1 = [1, 2, 3]
d = '%s' % (list1)
tuple1 = (1, 2, 3)
d2 = '%s' % (tuple1,)
print("- Ví dụ về dùng %s: format string: Kiểu dữ liệu list: d = '%s' % ([1, 2, 3]) =", d)
print("\t=> Kiểu dữ liệu của d =", type(d))
print("- Ví dụ về dùng %s: format string: Kiểu dữ liệu tuple: d = '%s' % ((1, 2, 3),) =", d2)
print("\t=> Kiểu dữ liệu của d =", type(d2))

print('''=> Tuple vs list 
		Tuple thường được sử dụng cho các kiểu dữ liệu không đồng nhất (khác nhau) và 
		List thường sử dụng cho các kiểu dữ liệu (đồng nhất) giống nhau.
		Vì tuple không thể thay đổi, việc lặp qua các phần tử của tuple nhanh hơn so với list. ''')

print("")
integer1 = 2
float1 = 3.9
float2 = 3.56342
float3 = 3.99999

d3 = '%d' % (integer1)
d4 = '%d' % (float1)
d5 = '%f' % (float1)
d6 = '%f' % (integer1)
d7 = '%.2f' % (float2)
d8 = '%.3f' % (float3)

print("- Ví dụ về dùng %d: format integer number: Kiểu dữ liệu số nguyên: d = '%d' % (2) = ", d3)
print("\t=> Kiểu dữ liệu của d =", type(d3))
print('''- Ví dụ về dùng %d: format integer number: cho string se bị lỗi: d = '%d' % ('2'):
	=> TypeError: %d format: a number is required, not str ''')
print("- Ví dụ về dùng %d: format integer number: cho kiểu dữ liệu số thực: d = '%d' % (3.9) = ", d4)
print("\t=> Kiểu dữ liệu của d =", type(d4))
print("\t=> %d không phù hợp cho số thực, đó là lí do ta có %f")

print("")
print("- Ví dụ về dùng %f: format float number: Kiểu dữ liệu số thực: d = '%f' % (3.9) = ", d5)
print("\t=> Kiểu dữ liệu của d =", type(d5))
print("- Format float number: cũng yêu cầu input là 1 số, ngoài ra sẽ lỗi")
print("- Ví dụ về dùng %f: format float number: cho Kiểu dữ liệu số nguyên: d = '%f' % (2) = ", d6)
print("- Ví dụ về dùng %f: format float number: cho Kiểu dữ liệu số thực, lấy 2 số phần thập phân: d = '%.2f' % (3.56342) = ", d7)
print("- Ví dụ về dùng %f: format float number: cho Kiểu dữ liệu số thực, cũng có khả năng làm tròn: d = '%.3f' % (3.99999) = ", d8)

print("")
print("# 3. Định dạng bằng chuỗi f (f-string)")
print("- Syntax: f'giá trị trong chuỗi'")
print("- Nếu so với định dạng thường thì ko khác mấy")
print("- Khác khi dùng trong TH gọi value từ tên biến")
print("- Ví dụ:")
a1 = 1
b1 = 2
c = f'a1: {a1}, b1: {b1}'

print("\t+ Khởi tạo a1 = 1, b1 = 2, khi đó gọi biến c dùng chuỗi f: c = f'a1: {a1}, b1: {b1}', kết quả: c =", c)
print("\t=> biến trong dấu ngoặc nhọn {} đã được thay thế vứi giá trị tương ứng")

print("")
print("- Ví dụ: dùng chuỗi f với biến chưa được khởi tạo:")
print(''' f’{variable_2}’  # chưa khởi tạo biến có tên variable_2
	=> lối như sau: Traceback (most recent call last):
	  				File "<stdin>", line 1, in <module>
					NameError: name ' variable_2' is not defined''')

f = 3
f2 = f'{{f1}}, {f}'
print("- Nếu muốn escape thay giá trị của biến dấu ngoặc {}: cú pháp như sau: {{variable_name}}")
print("- Ví dụ:")
print("\t+ Gọi biến f = 3, f1 chưa định nghĩa, ta sẽ viết được như sau: f2 = f'{{f1}}, {f}' = ", f2)

print("")
print("# 4. Định dạng bằng phương thức format:")
print("- Cách định dạng này cho phép Python định dạng chuỗi một cách tuyệt vời, không chỉ tốt về mặt nội dung mà còn về thẩm mĩ:")
print("- Ví dụ về dùng format tương đương với cách dùng %:")
f3 = 'a: {}, b: {}, c: {}'.format(1, 2, 3)
print("\t+ Gọi f3 = 'a: {}, b: {}, c: {}'.format(1, 2, 3) = ", f3)
f4 = 'a: %d, b: %d, c: %d' % (1, 2, 3)
print("\t+ Gọi f4 = 'a: %d, b: %d, c: %d' % (1, 2, 3) = ", f4), print("\t=> Kết quả Tương đương với nhau")

print("")
print("- Sự khác biệt đó là khi dung format có thể chỉ định vị trí của giá trị tùy biến theo index chỉ định")
f5 = 'a: {2}, b:{1}, c:{0}'.format('one', 'two', 'three')
print("\t+ f5 = 'a: {2}, b:{1}, c:{0}'.format('one vị trí là 0', 'two vị trí là 1', 'three vị trí là 2')", f5)
print("- Nếu các vị trí đánh số còn chưa đủ rõ ràng, và bạn có khả năng bị nhầm lẫn. Phương thức format vẫn chiều lòng được bạn.")
print(''' >>> ‘1: {one}, 2: {two}’.format(one=111, two=222)
	‘1: 111, 2: 222’''')

print("")
print('''- Đặc biệt nhất, Dưới đây là 3 cách căn lề cơ bản của phương thức format: 
			Căn lề trái	:	{:(c)>n}
			Căn lề phải	:	{:(c)<n}
			Căn lề giữa	:	{:(c)^n}

			Trong đó với: c: kí tự sẽ thay thế vào khoảng trắng
						  n: số kí tự dùng để căn lề = số kí tự format() + c ''')
print("")
print("- Ví dụ:")
f_right = 'a: {:<10}, check căn lề'.format('aaaa')
f_left = 'a: {:>10}, check căn lề'.format('aaaa')
f_center = 'a: {:^10}, check căn lề'.format('aaaa')
f_right_rp = 'a: {:*<10}, check căn lề'.format('aaaa')
f_left_rp = 'a: {:*>10}, check căn lề'.format('aaaa')
f_center_rp = 'a: {:*^10}, check căn lề'.format('aaaa')
print("\t+ Check căn lề phải: f_right = 'a: {:<10}, check căn lề'.format('aaaa') = ", f_right)
print("\t+ Check căn lề trái: f_left = 'a: {:>10}, check căn lề'.format('aaaa') = ", f_left)
print("\t+ Check căn lề giữa: f_center = 'a: {:^10}, check căn lề'.format('aaaa') = ", f_center)
print("\t+ Check căn lề phải, thay thế khoẳng trắng với dấu *: f_right = 'a: {:<10}, check căn lề'.format('aaaa') = ", f_right_rp)
print("\t+ Check căn lề trái, thay thế khoẳng trắng với dấu *: f_left = 'a: {:>10}, check căn lề'.format('aaaa') = ", f_left_rp)
print("\t+ Check căn lề giữa, thay thế khoẳng trắng với dấu *: f_center = 'a: {:^10}, check căn lề'.format('aaaa') = ", f_center_rp)

print("")
print("- Ví dụ format ra 1 table: ")
row_1 = '+ {:-<6} + {:-^15} + {:->10} +'.format('', '', '')
row_2 = '| {:<6} | {:^15} | {:>10} |'.format('ID', 'Ho va ten', 'Noi sinh')
row_3 = '| {:<6} | {:^15} | {:>10} |'.format('123', 'Yui Hatano', 'Japanese')
row_4 = '| {:<6} | {:^15} | {:>10} |'.format('6969', 'Sunny Leone', 'Canada')
row_5 = '+ {:-<6} + {:-^15} + {:->10} +'.format('', '', '')
# phần xuất kết quả
print(row_1)
print(row_2)
print(row_3)
print(row_4)
print(row_5)

print("")
print(len('Elements with a matching tag name (case insensitive;'))
print("- Table 1: Selenium: Find element")
row_6 = '+ {:-^50} + {:-^55} +'.format('','')
print(row_6)
row_6_1 = '+ {:^50} + {:^55} +'.format('method name','WebElement object/list returned')
print(row_6_1)
row_6 = '+ {:-^50} + {:-^55} +'.format('','')
print(row_6)

row_7 = '| {:<50} | {:^55} |'.format('browser.find_element_by_class_name(name)','Elements that use the CSS class name')
print(row_7)
row_8 = '| {:<50} | {:^55} |'.format('browser.find_elements_by_class_name(name)','')
print(row_8)
print(row_6)

row_9 = '| {:<50} | {:^55} |'.format('browser.find_element_by_css_selector(selector)','Elements that match the CSS selector')
print(row_9)
row_10 = '| {:<50} | {:^55} |'.format('browser.find_element_by_css_selector(selector)','')
print(row_10)
print(row_6)

row_10 = '| {:<50} | {:^55} |'.format('browser.find_element_by_id(id)','Elements with a matching id attribute value')
print(row_10)
row_11 = '| {:<50} | {:^55} |'.format('browser.find_elements_by_id(id)','')
print(row_11)
print(row_6)

row_12 = '| {:<50} | {:^55} |'.format('browser.find_element_by_link_text(text)','<a> elements that completely match the text provided')
print(row_12)
row_13 = '| {:<50} | {:^55} |'.format('browser.find_elements_by_link_text(text)','')
print(row_13)
print(row_6)

row_14 = '| {:<50} | {:^55} |'.format('browser.find_element_by_partial_link_text(text)','<a> elements that contain the text provided')
print(row_14)
row_15 = '| {:<50} | {:^55} |'.format('browser.find_elements_by_partial_link_text(text)','')
print(row_15)
print(row_6)

row_16 = '| {:<50} | {:^55} |'.format('browser.find_element_by_name(name)','Elements with a matching name attribute value')
print(row_16)
row_17 = '| {:<50} | {:^55} |'.format('browser.find_elements_by_name(name)','')
print(row_17)
print(row_6)

row_18 = '| {:<50} | {:^55} |'.format('browser.find_element_by_tag_name(name)','Elements with a matching tag name (case insensitive;')
print(row_18)
row_19 = '| {:<50} | {:^55} |'.format('browser.find_elements_by_tag_name(name)',"an <a> element is matched by 'a'  and 'A' )")
print(row_19)
print(row_6)

row_20 = '| {:^108} |'.format('Except for the *_by_tag_name() methods, the arguments to all the methods are case sensitive. ')			
print(row_20)
print(row_6)

row_21 = '| {:<108} |'.format('If no elements exist => selenium module raises a NoSuchElement exception')			
print(row_21)
row_22 = '| {:<108} |'.format('If you do not want this exception to crash your program, add try')			
print(row_22)
row_23 = '| {:<108} |'.format('and except statements to your code.')			
print(row_23)
print(row_6)

print("")
print("- Table 2: Selenium: Action")
row_6 = '+ {:-^15} + {:-^55} +'.format('','')
print(row_6)
row_6_1 = '+ {:^15} + {:^55} +'.format('Method name','Action in Webpage')
print(row_6_1)
row_6 = '+ {:-^15} + {:-^55} +'.format('','')
print(row_6)

row_24 = '| {:^15} | {:^55} |'.format('send_keys()',"Sending keystrokes to text fields on a web page")
print(row_24)
row_25 = '| {:<15} | {:^55} |'.format('',"of finding the <input> or <textarea> element ")
print(row_25)
print(row_6)

row_26 = '| {:^15} | {:^55} |'.format('submit()',"Same result as clicking the Submit button for the form")
print(row_26)
print(row_6)

print("")
print("- Table 3: Selenium: Action")
row_6 = '+ {:-^15} + {:-^55} +'.format('','')
print(row_6)
row_6_1 = '+ {:^15} + {:^55} +'.format('Method name','Action in Webpage')
print(row_6_1)
row_6 = '+ {:-^15} + {:-^55} +'.format('','')
print(row_6)

row_27 = '| {:^15} | {:^55} |'.format('click()',"simulates a mouse click on that element")
print(row_27)
print(row_6)
