# 🐸 Python 速查表 | Python Cheatsheet

> **由 [HoppyPy](https://www.hoppypy.com) 精心整理** — 收藏这份速查表，随时查阅！

[English](#english) | [中文](#中文)

---

## English

### 📝 Variables & Data Types

```python
# Strings
name = "Hoppy"
multiline = """Hello
World"""

# Numbers
age = 5                  # int
pi = 3.14                # float

# Boolean
is_cool = True           # True / False

# None
nothing = None

# Type checking
type(name)               # <class 'str'>
isinstance(age, int)     # True
```

### 📋 Lists

```python
fruits = ["apple", "banana", "cherry"]

fruits.append("date")          # Add to end
fruits.insert(1, "avocado")    # Insert at index
fruits.remove("banana")        # Remove by value
fruits.pop()                   # Remove last
fruits[0]                      # First item
fruits[-1]                     # Last item
fruits[1:3]                    # Slice
len(fruits)                    # Length
sorted(fruits)                 # Sort (new list)

# List comprehension ⚡
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]
```

### 📖 Dictionaries

```python
person = {"name": "Hoppy", "age": 5, "lang": "Python"}

person["name"]                 # Get value
person.get("email", "N/A")    # Safe get with default
person["level"] = 10           # Add/update
del person["age"]              # Delete key
person.keys()                  # All keys
person.values()                # All values
person.items()                 # Key-value pairs

# Dict comprehension
squared = {x: x**2 for x in range(5)}
```

### 🔄 Control Flow

```python
# If / Elif / Else
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"

# Ternary
status = "pass" if score >= 60 else "fail"

# For loop
for item in ["a", "b", "c"]:
    print(item)

for i, val in enumerate(["a", "b", "c"]):
    print(f"{i}: {val}")

for i in range(5):        # 0, 1, 2, 3, 4
    print(i)

# While loop
while condition:
    do_something()
    if exit_condition:
        break
```

### 🔧 Functions

```python
# Basic function
def greet(name: str) -> str:
    """Say hello to someone."""
    return f"Hello, {name}!"

# Default arguments
def power(base: int, exp: int = 2) -> int:
    return base ** exp

# *args and **kwargs
def flexible(*args, **kwargs):
    print(args)      # Tuple of positional args
    print(kwargs)    # Dict of keyword args

# Lambda
double = lambda x: x * 2
```

### 📁 File Handling

```python
# Read
with open("file.txt", "r") as f:
    content = f.read()

# Write
with open("file.txt", "w") as f:
    f.write("Hello!")

# Read lines
with open("file.txt") as f:
    lines = f.readlines()
```

### ⚠️ Error Handling

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Unexpected: {e}")
else:
    print("Success!")      # Only if no exception
finally:
    print("Always runs")   # Always executes
```

### 🧰 Useful Built-ins

```python
len([1, 2, 3])              # 3
range(5)                     # 0, 1, 2, 3, 4
enumerate(["a", "b"])        # (0, "a"), (1, "b")
zip([1, 2], ["a", "b"])     # (1, "a"), (2, "b")
map(str, [1, 2, 3])         # "1", "2", "3"
filter(bool, [0, 1, "", 2]) # 1, 2
sorted([3, 1, 2])           # [1, 2, 3]
reversed([1, 2, 3])         # 3, 2, 1
any([False, True, False])   # True
all([True, True, False])    # False
```

### 🎯 String Methods

```python
s = "hello world"

s.upper()          # "HELLO WORLD"
s.lower()          # "hello world"
s.title()          # "Hello World"
s.strip()          # Remove whitespace
s.split(" ")       # ["hello", "world"]
s.replace("o", "0")  # "hell0 w0rld"
s.startswith("he") # True
s.endswith("ld")   # True
f"{'hi':>10}"      # "        hi"  (right-aligned)
f"{'hi':^10}"      # "    hi    "  (centered)
```

---

## 中文

### 📝 变量和数据类型

```python
# 字符串
name = "Hoppy"
multiline = """多行
字符串"""

# 数字
age = 5                  # 整数
pi = 3.14                # 浮点数

# 布尔值
is_cool = True           # True / False

# 空值
nothing = None

# 类型检查
type(name)               # <class 'str'>
isinstance(age, int)     # True
```

### 📋 列表

```python
fruits = ["苹果", "香蕉", "樱桃"]

fruits.append("枣")             # 末尾添加
fruits.insert(1, "牛油果")      # 指定位置插入
fruits.remove("香蕉")           # 按值删除
fruits.pop()                    # 删除最后一个
fruits[0]                       # 第一个元素
fruits[-1]                      # 最后一个元素
fruits[1:3]                     # 切片
len(fruits)                     # 长度
sorted(fruits)                  # 排序（新列表）

# 列表推导式 ⚡
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]
```

### 📖 字典

```python
person = {"名字": "Hoppy", "年龄": 5, "语言": "Python"}

person["名字"]                   # 获取值
person.get("邮箱", "无")         # 安全获取，有默认值
person["等级"] = 10              # 添加/更新
del person["年龄"]               # 删除键
person.keys()                    # 所有键
person.values()                  # 所有值
person.items()                   # 键值对

# 字典推导式
squared = {x: x**2 for x in range(5)}
```

### 🔄 流程控制

```python
# 条件判断
if score >= 90:
    grade = "优秀"
elif score >= 80:
    grade = "良好"
else:
    grade = "加油"

# 三元表达式
status = "通过" if score >= 60 else "不通过"

# for 循环
for item in ["a", "b", "c"]:
    print(item)

for i, val in enumerate(["a", "b", "c"]):
    print(f"{i}: {val}")

# while 循环
while condition:
    do_something()
    if exit_condition:
        break
```

### 🔧 函数

```python
# 基本函数
def greet(name: str) -> str:
    """向某人打招呼"""
    return f"你好, {name}!"

# 默认参数
def power(base: int, exp: int = 2) -> int:
    return base ** exp

# 可变参数
def flexible(*args, **kwargs):
    print(args)      # 位置参数（元组）
    print(kwargs)    # 关键字参数（字典）

# Lambda 匿名函数
double = lambda x: x * 2
```

### ⚠️ 异常处理

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"错误: {e}")
except Exception as e:
    print(f"意外错误: {e}")
else:
    print("成功!")        # 仅在无异常时执行
finally:
    print("总是执行")     # 无论如何都执行
```

---

<p align="center">
  <b>想要互动式学习这些内容？</b><br/>
  <a href="https://www.hoppypy.com">
    <img src="https://img.shields.io/badge/🐸_开始学习-hoppypy.com-00ff88?style=for-the-badge&labelColor=0a0e17" alt="Start"/>
  </a>
</p>

<p align="center">
  <sub>⭐ 觉得有用？Star 这个仓库帮助更多人发现它！</sub>
</p>
