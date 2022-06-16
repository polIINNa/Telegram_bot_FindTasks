from urllib.request import urlopen
import re


def hello_world():
    print("hello world!!")


def decorator_func(func):
    def wrapper():
        print(f'Получена ф-ция {func} в качестве аргумента')
        func()
    return wrapper()


@decorator_func
def hello_world():
    print("hello world!!")

'''
regx = r'<code>(.*?)</code>'
py_constr = {}
ans = []
html = urlopen('https://stepik.org/media/attachments/lesson/209719/2.html').read().decode('utf-8')
s = str(html)
lst = re.findall(regx, s)
for i in lst:
    if i in py_constr:
        py_constr[i] += 1
    else:
        py_constr[i] = 1
max_val = max(py_constr.values())
for key in py_constr:
    if py_constr[key] == max_val:
        ans.append(key)
print(sorted(ans))
'''

