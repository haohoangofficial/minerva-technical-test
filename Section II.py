"""
Section 2: Coding Challenge
1. Write code to solve the below problem:
A string is said to be beautiful if each letter in the string appears at most as many times as the
previous letter in the alphabet within the string; I.e: b occurs no more times than a; c occurs no more
times than b; etc. Note that letter a has no previous letter. Given a string, check whether it is beautiful.
"""
def is_beautiful_string(string):
    # Chuyển kí tự sang lowercase
    string = string.lower()
    # Kiểm tra độ dài của chuỗi kí tự
    if len(string) < 3 or len(string) > 50:
        return False
    # Kiểm tra kí tự có thuộc a-z hay không
    for c in string:
        if ord(c) < 97 or ord(c) > 122:
            return False
    # khởi tạo dictionary chứa tần số của từng kí tự
    f = {}
    for i in string:
        if i in f:
           f[i] += 1
        else:
            f[i] = 1
    # Lọc dữ liệu theo thứ tự anphabet
    d = dict(sorted(f.items()))
    # Khởi tạo biến previous bằng giá trị giới hạn max len(string)
    previous = 50
    for j in d.items():
        if j[1] > previous:
            return False
        else:
            previous = j[1]
    return True
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    string = 'AAAABB!'
    print(is_beautiful_string(string))