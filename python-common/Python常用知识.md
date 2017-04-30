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

### map/reduce/filter/lambda函数使用
```python
from functools import reduce

def add(x):
    return x + 100

nums = [1, 2, 4, 5, 6, 11, 22, 33]

print("----map----")
print(list(map(add, nums)))

print("----map None----")
print(map(None, nums))

def add2(x, y):
    return x + y

print("----reduce----")
print(reduce(add2, nums))

def is_odd(n):
    return n % 2 == 1

print("----filter----")
print(list(filter(is_odd, nums)))

print("----lambda----")
print(list(map(lambda x: x*2, nums)))
```

```
OUTPUT:
----map----
[101, 102, 104, 105, 106, 111, 122, 133]
----map None----
<map object at 0x11119dc50>
----reduce----
84
----filter----
[1, 5, 11, 33]
----lambda----
[2, 4, 8, 10, 12, 22, 44, 66]
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


### 新式类与经典类
#### 在python3.x中，经典类写法与新式类写法都默认继承object类，即python3.x中默认都是新式类，可不必显式继承object类。而python 2.x中默认都是经典类，只有显式继承了object才是新式类。
```python
class CC: #经典类写法
    def __init__(self):
        pass

class CCN(object): #新式类写法
    def __init__(self):
        pass
    
c1 = CC()
c2 = CCN()
```

#### 比较实例对象的type和__class__，如果x是一个新式类的实例，那么type(x)和x.__class__是一样的结果。
```python
print(c1.__class__)
print(type(c1))
print(c2.__class__)
print(type(c2))
```
```
OUTPUT:
<class '__main__.CC'>
<class '__main__.CC'>
<class '__main__.CCN'>
<class '__main__.CCN'>
```

### 关于经典类与新式类的类继承写法及效果的差异
```python
# 经典类的继承
class A:
    def __init__(self):
        print "enter A"
        print "leave A"

class B(A):
    def __init__(self):
        print "enter B"       
        A.__init__(self)  # ** 这里是非绑定的类方法（用父类名A来调用）
        print "leave B"
    
b = B()
```
#### 注意，非绑定的类方法，是用父类来调用并在参数列表中，引入待绑定的子类对象（self），从而达到调用父类方法的目的。但这样做的缺点是，当子类B的父类A发生变化时（如类B的父类由A变为C时），必须遍历整个类定义，把所有的通过非绑定的方法的类名全部替换过来。
```python
class B(C):    # A 变成 C，这里要改
    def __init__(self):
        print "enter B"
        C.__init__(self)  # A 变成 C， 这里也要改
        print "leave B"
```

```python
# 新式类的继承(以下写法在python2x和python3x中都可以)
class A(object):
    def __init__(self):
        print "enter A"  # python3x中，请改成 print("enter A")
        print "leave A"

class B(A):     # 即使B的父类由A变成C，只需要改这里。
    def __init__(self):
        print "enter B"
        super(B, self).__init__() #这里使用了super()。
        print "leave B"
```

### 关于类继承的顺序MRO
#### 以下是反面例子，混合使用了非绑定的类方法和super()方法，出现了类A和类D的初始化函数被重复调用了2次的情况。
```python
class A(object):
    def __init__(self):
        print("enter A")
        print("leave A")
        
class B(object):
    def __init__(self):
        print("enter B")
        print("leave B")
        
class C(A):
    def __init__(self):
        print("enter C")
        super(C, self).__init__()  # 这里使用了super()方法
        print("leave C")
        
class D(A):
    def __init__(self):
        print("enter D")
        super(D, self).__init__()  # 这里使用了super()方法
        print("leave D")
        
class E(B, C):
    def __init__(self):
        print("enter E")
        B.__init__(self)  # 这里使用了非绑定的类方法
        C.__init__(self)  # 这里使用了非绑定的类方法
        print("leave E")
        
class F(E, D):
    def __init__(self):
        print("enter F")
        E.__init__(self)  # 这里使用了非绑定的类方法
        D.__init__(self)  # 这里使用了非绑定的类方法
        print("leave F")
        
f = F()
```

```
OUTPUT:
enter F
enter E
enter B
leave B
enter C
enter D
enter A
leave A
leave D
leave C
leave E
enter D
enter A
leave A
leave D
leave F
```

#### 只使用super()方法
```python
class A(object):
    def __init__(self):
        print("enter A")
        super(A, self).__init__()  # 增加super()
        print("leave A")
        
class B(object):
    def __init__(self):
        print("enter B")
        super(B, self).__init__()  # 增加super()
        print("leave B")
        
class C(A):
    def __init__(self):
        print("enter C")
        super(C, self).__init__()  # 不变
        print("leave C")
        
class D(A):
    def __init__(self):
        print("enter D")
        super(D, self).__init__()  # 不变
        print("leave D")
        
class E(B, C):
    def __init__(self):
        print("enter E")
        super(E, self).__init__()  # 这里删掉反例中使用的非绑定的类方法 B.__init__(self) 和 C.__init__(self) 改成super()方法
        print("leave E")
        
class F(E, D):
    def __init__(self):
        print("enter F")
        super(F, self).__init__()  # 这里删掉反例中使用的非绑定的类方法 E.__init__(self) 和 D.__init__(self) 改成super()方法
        print("leave F")
        
f = F()
print(f.__class__.__mro__)
```

```
OUTPUT:
enter F
enter E
enter B
enter C
enter D
enter A
leave A
leave D
leave C
leave B
leave E
leave F
(<class '__main__.F'>, <class '__main__.E'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.D'>, <class '__main__.A'>, <class 'object'>)
```
#### 初始化顺序为 F -> E -> B -> C -> D -> A -> object
#### MRO拓扑图如下：
```
      object
      /    \
     /      A
    /     /   \
   B     C     D
    \   /     /
      E      /
        \   /
          F
```
#### 小结:
1. Python的多继承类是通过mro的方式来保证各个父类的函数被逐一调用，而且保证每个父类函数只调用一次（如果每个类都使用super）；
2. 混用super()和非绑定的函数是一个危险行为，这可能导致应该调用的父类函数没有调用或者一个父类函数被调用多次。
3. super()是一个函数方法，只是返回的类型是一个类对象。

### 剖析super()方法和MRO(Method Resolution Order)
#### 虽然直接用非绑定的类方法（用父类名来调用）在使用单继承的时候没问题，但是如果使用多继承，将会涉及到查找顺序（MRO）、重复调用（钻石继承）等种种问题。super()是用来专门解决多重继承问题的。
#### python中super()的定义如下
```
def super(cls, inst):
    mro = inst.__class__.mro()
    return mro[mro.index(cls) + 1]
```
#### 参数 cls 和 inst 分别做了两件事： 
1. inst 即类对象实例，通过__class__.mro()方法生成 MRO 的列表。
2. 通过 cls 定位当前 MRO 中的 index, 并返回 mro[index + 1]即下一个位置的类。

#### 以上两件事就是 super() 的实质。
#### 通过以上例子`f.__class__.__mro__`可打印出mro路径。
#### 在 MRO 中，基类永远出现在派生类后面，如果有多个基类，基类的相对顺序保持不变。
#### 注意：以上super()和MRO都是针对新式类的，如果不是新式类，只能老老实实用父类的类名去调用函数了。

#### 对于有参数的情况，也是类似的，写法如下
```python
class A(object):
    def __init__(self, strName, *args):
        self.name = strName
        super(A, self).__init__(*args)
            
class B(object):
    def __init__(self, id):
        self.id = id
        
class C(A, B):
    def __init__(self, *args):
        super(C, self).__init__(*args)
```

####  另外，如果没有复杂的继承结构，super 作用不大。而复杂的继承结构本身就是不良设计。对于多重继承的用法，现在比较推崇 Mixin 的方式，也就是:
1. 普通类多重继承只能有一个普通父类和若干个 Mixin 类（保持主干单一）
2. Mixin 类不能继承普通类（避免钻石继承）
3. Mixin 类应该单一职责

#### 如果按照上述标准，只使用 Mixin 形式的多继承，那么不会有钻石继承带来的重复方法调用，也不会有复杂的查找顺序 ，此时super()是可有可无的，用不用全看个人喜好。

### 关于`__new__`, `__init__`, `__call__`
1. `__new__(cls, *args, **kwargs)`  创建对象时调用，返回当前对象的一个实例，这里的第一个参数是`cls`即`class`本身。
2. `__init__(self, *args, **kwargs)`  在创建完对象后调用，对当前对象实例的一些初始化，无返回值，即在调用`__new__`之后，根据返回的实例初始化，这里的第一个参数是`self`即对象本身。
3. `__call__(self,  *args, **kwargs)`  如果类实现了这个方法，相当于把这个类的对象当作函数来使用，相当于 重载了括号`()`运算符。

```python
class A(object):
    def __init__(self, *args, **kwargs):
        print("init and self: ", self)
        super(A, self).__init__(*args, **kwargs)
    def __new__(cls, *args, **kwargs):
        print("new and cls: ", cls)
        return super(A, cls).__new__(cls, *args, **kwargs)
    def __call__(self,  *args, **kwargs):
        print("call and self: ", self)
        
aa = A()
print("---------------")
aa()
```

```
OUTPUT:
new and cls:  <class '__main__.A'>
init and self:  <__main__.A object at 0x00000000045850B8>
---------------
call and self:  <__main__.A object at 0x00000000045850B8>
```