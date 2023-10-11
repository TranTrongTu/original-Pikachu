<<<<<<< HEAD
global_variable = 10  # Đây là biến toàn cục

def function1():
    global global_variable  # Sử dụng từ khóa global để tham chiếu đến biến toàn cục
    local_variable = 5  # Đây là biến cục bộ trong hàm function1
    global_variable += 1  # Thay đổi giá trị của biến toàn cục
    print(global_variable)  # Có thể truy cập và in giá trị của biến toàn cục từ trong hàm function1

def function2():
    # Đây là hàm khác và không thể truy cập biến cục bộ của hàm function1
    print(global_variable)  # Có thể truy cập và in giá trị của biến toàn cục từ trong hàm function2

function1()
function2()
=======
global_variable = 10  # Đây là biến toàn cục

def function1():
    global global_variable  # Sử dụng từ khóa global để tham chiếu đến biến toàn cục
    local_variable = 5  # Đây là biến cục bộ trong hàm function1
    global_variable += 1  # Thay đổi giá trị của biến toàn cục
    print(global_variable)  # Có thể truy cập và in giá trị của biến toàn cục từ trong hàm function1

def function2():
    # Đây là hàm khác và không thể truy cập biến cục bộ của hàm function1
    print(global_variable)  # Có thể truy cập và in giá trị của biến toàn cục từ trong hàm function2

function1()
function2()
>>>>>>> b4ad1b8a753ee39e5edc5f4d9156196a0efd2257
