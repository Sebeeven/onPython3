# Python常用知识
### 列表推导式
```python
nums = [number for number in range(1, 6)]
print(nums)
```

```
OUTPUT:
[1, 2, 3, 4, 5]
```

### 字典推导式
```python
word = 'letters'
letters = {letter: word.count(letter) for letter in word}
print(letters)
```

```
OUTPUT:
{'r': 1, 's': 1, 't': 2, 'e': 2, 'l': 1}
```

### 集合推导式
```python
a_set = {number for number in range(1, 6) if number % 3 == 1}
print(a_set)
```

```
OUTPUT:
{1, 4}
```

### zip()并行迭代
```python
days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']
for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    print(day, ": drink ", drink, " - eat ", fruit, " - enjoy ", dessert)
```

```
OUTPUT:
Monday : drink  coffee  - eat  banana  - enjoy  tiramisu
Tuesday : drink  tea  - eat  orange  - enjoy  ice cream
Wednesday : drink  beer  - eat  peach  - enjoy  pie
```

### split()与join()
```python
friends = "Harry,Henry,Barkley"
friends_list = friends.split(',')
print(friends_list)
joined_str = ','.join(friends_list)
print(joined_str)
```

```
OUTPUT:
['Harry', 'Henry', 'Barkley']
Harry,Henry,Barkley
```

### 函数
+ 位置参数，如：

```python
def menu(wine, entree, dessert):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}
print(menu('chardonnay', 'chicken', 'cake'))
```

+ 关键字参数，如：

```python
print(menu(entree='beef', dessert='bagel', wine='bordeaux'))
```

```
OUTPUT:
{'dessert': 'cake', 'entree': 'chicken', 'wine': 'chardonnay'}
{'dessert': 'bagel', 'entree': 'beef', 'wine': 'bordeaux'}
```

+ args, 使用`*`号收集：

```python
def print_args(*args):
    print('Positional argument tuple: ', args)

print_args(3, 2, 'wait!', 2, 'uh...')

def print_more(required1, required2, *args):
    print('Need this one:', required1)
    print('Need this one too:', required2)
    print('All the rest:', args)

print_more('cap', 2, 'gloves', 'banana', 2*3)
```

```
OUTPUT:
Positional argument tuple:  (3, 2, 'wait!', 2, 'uh...')
Need this one: cap
Need this one too: 2
All the rest: ('gloves', 'banana', 6)
```

+ kwargs, 使用`**`号收集：

```python
def print_kwargs(**kwargs):
    print('Keyword arguments: ', kwargs)
    
print_kwargs(wine='merlot', entree='mutton', dessert='macaroon')
```

```
OUTPUT:
Keyword arguments:  {'wine': 'merlot', 'entree': 'mutton', 'dessert': 'macaroon'}
```

### 装饰器
#### 把一个函数作为输入且返回另外一个函数。需使用如下python技巧
1. `*args`和`**kwargs`
2. 闭包
3. 作为参数的函数

```python
# 定义装饰器
def document_it(func): # 3
    def new_function(*args, **kwargs # 1): # 2
        print('Running function: ', func.__name__)
        print('Positional arguments: ', args)
        print('Keyword arguments: ', kwargs)
        result = func(*args, **kwargs)
        print('Result: ', result)
        return result
    return new_function

# 方式一：人工赋值
def add_ints(a, b):
    return a + b

cooler_add_ints = document_it(add_ints)
cooler_add_ints(3, 5)

# 方式二：在函数定义时添加
@document_it
def add_ints2(a, b):
    return a + b

add_ints2(3, 6)

# 可添加多个装饰器，且任何顺序都会得到相同的最终结果。中间步骤的实现还是有不一样的。
def square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return new_function

print("未交换顺序前：")
@document_it
@square_it
def add_ints3(a, b):
    return a + b

add_ints3(2, 7)


print("交换顺序后：")
@square_it
@document_it
def add_ints4(a, b):
    return a + b

add_ints4(2, 7)
```

```
OUTPUT:
Running function:  add_ints
Positional arguments:  (3, 5)
Keyword arguments:  {}
Result:  8
Running function:  add_ints2
Positional arguments:  (3, 6)
Keyword arguments:  {}
Result:  9
未交换顺序前：
Running function:  new_function
Positional arguments:  (2, 7)
Keyword arguments:  {}
Result:  81
Out[]: 81
交换顺序后：
Running function:  add_ints4
Positional arguments:  (2, 7)
Keyword arguments:  {}
Result:  9
Out[]: 81
```

### 类class
#### 使用属性property对特性attribute进行访问和设置（getter/setter）
```
# 说明，在讨论python类的时候，有几个约定：
# 1.attribute，特性（或属性，要看讨论这部分内容时具体的上下文），数据，类变量，概念相当
# 2.method，方法，函数，类函数，类方法，概念相当
```
```python
class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name
    def get_name(self):
        print('inside the getter')
        return self.hidden_name
    def set_name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name   
    name = property(get_name, set_name) # 这里定义属性property
    
fowl = Duck('Howard')
fowl.name
fowl.get_name()

# 对 name特性赋值时，调用set_name()方法
fowl.name = 'Daffy' # 相当于fowl.set_name('Daffy')
fowl.name
```

```
OUTPUT:
inside the getter
inside the getter
inside the setter
inside the getter
Out[]: 'Daffy'
```

#### 使用修饰符定义属性
#### `@property`指示getter方法, `@属性名.setter`指示setter方法.
```python
class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name
        
    @property
    def name(self):
        print('inside the getter')
        return self.hidden_name
    
    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name
        
fowl = Duck('Howard')
fowl.name
fowl.name = 'Donald'
fowl.name
```

```
OUTPUT:
inside the getter
inside the setter
inside the getter
Out[]: 'Donald'
```

#### 用`__name`代替以上`hidden_name`特性，python对隐藏在类内部的特性有独特的命名规范，`__特性名`，如`__name`
```python
class Duck():
    def __init__(self, input_name):
        self.__name = input_name
        
    @property
    def name(self):
        print('inside the getter')
        return self.__name
    
    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.__name = input_name
        
fowl = Duck('Howard')
# 无法访问__name特性
fowl.__name
# python特有的访问方法： _类名__特性名
fowl._Duck__name
```

```
OUTPUT:
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-1-5b7e179d3eb4> in <module>()
     16 fowl = Duck('Howard')
     17 # 无法访问__name特性
---> 18 fowl.__name
     19 # python特有的访问方法： _类名__特性名
     20 fowl._Duck__name

AttributeError: 'Duck' object has no attribute '__name'
```
```
OUTPUT:
Out[]: 'Howard'
```

### 方法（函数）的类型：
1. 实例方法：以`self`作为第一个参数。调用时把对象作为`self`参数传入。
2. 类方法：用`@classmethod`修饰方法且以`cls`（即`class`）作为第一个参数。作用于整个类，对类作出的任何改变都会对它的所有实例对象产生影响。
3. 静态方法：用`@staticmethod`修饰方法，不需要self和cls参数。即不影响类也不影响类的对象

```python
class A():
    count = 0 # 记录有多少个类A的对象被创建
    
    def __init__(self):
        # self.count += 1 # count永远为1
        A.count += 1 # 这里用A.count，而不是self.count，与以下cls.count作用一样，作为类A的记数。注意，所有对象的count都会一起变化。
    
    def exclaim(self):
        print("I'm an A!")
    
    @classmethod
    def kids(cls):
        print("A has ", cls.count, " little objects.")

A.kids()
easy_a = A()
print("create easy_a of A")
print("easy_a's count: ", easy_a.count)
print("------------")
breezy_a = A()
print("create breezy_a of A")
print("easy_a's count: ", easy_a.count)
print("breezy_a's count: ", breezy_a.count)
print("------------")
wheezy_a = A()
print("create wheezy_a of A")
print("easy_a's count: ", easy_a.count)
print("breezy_a's count: ", breezy_a.count)
print("wheezy_a's count: ", wheezy_a.count)
print("------------")
A.kids()

class CoyoteWeapon():
    @staticmethod
    def commercial():
        print('This CoyoteWeapon has been brought to you by Acme.')

print("------------")
CoyoteWeapon.commercial()
```

```
OUTPUT:
A has  0  little objects.
create easy_a of A
easy_a's count:  1
------------
create breezy_a of A
easy_a's count:  2
breezy_a's count:  2
------------
create wheezy_a of A
easy_a's count:  3
breezy_a's count:  3
wheezy_a's count:  3
------------
A has  3  little objects.
------------
This CoyoteWeapon has been brought to you by Acme.
```

### 闭包、回调
```python
def apply_async(func, *args, callback):
    result = func(*args)   
    callback(result)

def print_result(result):
    print('Got: ', result)
    
def add(x, y):
    return x + y

apply_async(add, 2, 3, callback=print_result)
apply_async(add, 'hello', 'world', callback=print_result)

def make_handler():
    sequence = 0 # （1）
    def handler(result): # handler就是闭包
        nonlocal sequence # 声明此变量作用域不是在handler的范围内，是外部(1)处，即make_handler函数范围内。
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))
    return handler

handler = make_handler()
apply_async(add, 2, 3, callback=handler)
apply_async(add, 'hello', 'world', callback=handler)
```

### 关于正则表达式匹配
#### match/search/findall/sub

```python
import re
source = 'Young Frankenstein'
m = re.match('You', source)
if m:
    print(m.group())
else:
    print("not match")
    
n = re.findall('n', source)
print('Found ', len(n), ' matches')
```

```
OUTPUT:
You
Found  4  matches
```

###关于操纵数据库
#### 对于所有的关系型数据库，SQL是不完全相同的，且python的DB-API仅仅实现共有的那部分，每一种数据库实现的是包含自己特征和哲学的方言。而SQLAlchemy是其中一个著名的用于消除数据库之间差异的跨数据库的python库。