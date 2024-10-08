---
title: 现代C++语言核心特性解析
date: 2024-10-01
---

- [新基础类型（C++11～C++20）](#新基础类型c11c20)
  - [整数类型long long](#整数类型long-long)
  - [新字符类型char16\_t和char32\_t](#新字符类型char16_t和char32_t)
  - [char8\_t字符类型](#char8_t字符类型)
- [内联和嵌套命名空间（C++11～C++20）](#内联和嵌套命名空间c11c20)
- [auto占位符（C++11～C++17）](#auto占位符c11c17)
  - [auto推导规则](#auto推导规则)
  - [什么时候使用auto](#什么时候使用auto)
- [decltype说明符（C++11～C++17）](#decltype说明符c11c17)
  - [decltype推导规则](#decltype推导规则)
- [函数返回类型后置（C++11）](#函数返回类型后置c11)
- [右值引用（C++11 C++17 C++20）](#右值引用c11-c17-c20)
  - [值类别](#值类别)
  - [将左值转换为右值](#将左值转换为右值)
  - [万能引用](#万能引用)
- [lambda表达式（C++11～C++20）](#lambda表达式c11c20)
  - [捕获列表](#捕获列表)
  - [lambda表达式的实现原理](#lambda表达式的实现原理)
  - [广义捕获](#广义捕获)
- [非静态数据成员默认初始化（C++11 C++20）](#非静态数据成员默认初始化c11-c20)
- [列表初始化（C++11 C++20）](#列表初始化c11-c20)
- [默认和删除函数（C++11）](#默认和删除函数c11)
- [非受限联合类型（C++11）](#非受限联合类型c11)
- [委托构造函数（C++11）](#委托构造函数c11)
- [继承构造函数（C++11）](#继承构造函数c11)
- [强枚举类型（C++11 C++17 C++20）](#强枚举类型c11-c17-c20)
- [扩展的聚合类型（C++17 C++20）](#扩展的聚合类型c17-c20)

## 新基础类型（C++11～C++20）

### 整数类型long long

在C++中应该尽量少使用宏，用模板取而代之是明智的选择。使用模板可以得到指定类型的最大最小值。

```cpp
std::numeric_limits<long long>::max()
```

### 新字符类型char16_t和char32_t

C++11标准还为3种编码提供了新前缀用于声明3种编码字符和字符串的字面量，它们分别是UTF-8的前缀u8、UTF-16的前缀u和UTF-32的前缀U。wchar_t的前缀是L。

字符类型转换，包含在cuchar库当中。

|   名称   |      作用      |
| :------: | :------------: |
| mbrtoc16 | 多字节转UTF-16 |
| c16rtomb | UTF-16转多字节 |
| mbrtoc32 | 多字节转UTF-32 |
| c32rtomb | UTF-32转多字节 |

通过以下方式可以在字符串中使用新字符类型。

```cpp
using u16string = basic_string;
using u32string = basic_string;
using wstring = basic_string;
```

### char8_t字符类型

c++20引入，用于解决char类型处理UTF-8的问题。

## 内联和嵌套命名空间（C++11～C++20）

内联命名空间能够把空间内函数和类型导出到父命名空间中，这样即使不指定子命名空间也可以使用其空间内的函数和类型了。主要用于无缝升级库代码。

嵌套命名空间可以简化命名空间中类的声明。C++20引入了嵌套形式的内联命名空间。

## auto占位符（C++11～C++17）

- 当用一个auto关键字声明多个变量的时候，编译器遵从由左往右的推导规则，以最左边的表达式推断auto的具体类型。
- 当使用条件表达式初始化auto声明的变量时，编译器总是使用表达能力更强的类型。
- 虽然C++11标准已经支持在声明成员变量时初始化，但是auto却无法在这种情况下声明非静态成员变量。
- 按照C++20之前的标准，无法在函数形参列表中使用auto声明形参（注意，在C++14中，auto可以为lambda表达式声明形参）

### auto推导规则

- 如果auto声明的变量是按值初始化，则推导出的类型会忽略const和volatile限定符。
- 使用auto声明变量初始化时，目标对象如果是引用，则引用属性会被忽略。
- 使用auto和万能引用声明变量时，对于左值会将auto推导为引用类型。(涉及到引用折叠)
- 使用auto声明变量，如果目标对象是一个数组或者函数，则auto会被推导为对应的指针类型
- 当auto关键字与列表初始化组合时。若直接使用列表初始化，列表中必须为单元素，否则无法编译，auto类型被推导为单元素的类型。若用等号加列表初始化，列表中可以包含单个或者多个元素，auto类型被推导为`std::initializer_list<T>`，其中T是元素类型。(列表中元素类型需要相同)

### 什么时候使用auto

- 当一眼就能看出声明变量的初始化类型的时候可以使用auto。
- 对于复杂的类型，例如lambda表达式、bind等直接使用auto。

把auto写到lambda表达式的形参中，这样就得到了一个泛型的lambda表达式

c++17允许auto作为非类型模板形参占位符。

## decltype说明符（C++11～C++17）

### decltype推导规则

- 如果e是一个未加括号的标识符表达式（结构化绑定除外）或者未加括号的类成员访问，则decltype(e)推断出的类型是e的类型T。如果并不存在这样的类型，或者e是一组重载函数，则无法进行推导。
- 如果e是一个函数调用或者仿函数调用，那么decltype(e)推断出的类型是其返回值的类型。
- 如果e是一个类型为T的左值，则decltype(e)是T&。
- 如果e是一个类型为T的将亡值，则decltype(e)是T&&。
- 除去以上情况，则decltype(e)是T。

decltype(auto)是使用decltype的推导规则来推导auto，但是它必须单独声明，不能结合指针、引用和cv限定符。

c++17也允许decltype(auto)作为类型模板形参占位符

## 函数返回类型后置（C++11）

auto作为占位符，在->声明返回类型。

传统函数声明语法无法将函数指针类型作为返回类型直接使用，需要使用typedef将函数指针类型创建别名，再使用别名作为返回类型。使用后置返回类型则不需要这样。

可以使用decltype推导函数模板返回类型。

`std::declval`函数模板声明

## 右值引用（C++11 C++17 C++20）

左值一般是指一个指向特定内存的具有名称的值（具名对象），它有一个相对稳定的内存地址，并且有一段较长的生命周期。而右值则是不指向稳定内存地址的匿名值（不具名对象），它的生命周期很短，通常是暂时性的。能取到内存地址的值为左值，否则为右值。通常字面量都是一个右值，除字符串字面量以外。

非常量左值的引用对象很单纯，它们必须是一个左值。对常量左值引用的特性显得更加有趣，它除了能引用左值，还能够引用右值。

右值引用是一种引用右值且只能引用右值的方法。右值引用的特点之一是可以延长右值的生命周期，并且减少对象复制，提升程序性能。

移动语义，它可以帮助我们将临时对象的内存移动到左值对象中，以避免内存数据的复制。

复制构造函数和移动构造函数：复制构造函数使用常量左值引用作为参数，移动构造函数使用右值引用作为参数，通过转移实参对象的数据以达成构造对象的目的。对于右值编译器会优先选择使用移动构造函数去构造目标对象。当移动构造函数不存在的时候才会退而求其次地使用复制构造函数。移动构造函数和移动赋值运算符等价。

移动语义的风险：异常会导致无法预测的结果，可以使用noexcept说明符限制该函数。

### 值类别

c++11将表达式区分为左值（lvalue）、纯右值（prvalue）和将亡值（xvalue）。表达式首先被分为了泛左值（glvalue）和右值（rvalue），其中泛左值被进一步划分为左值和将亡值，右值又被划分为将亡值和纯右值。

泛左值是具名对象。纯右值是能够用于初始化对象和位域，或者能够计算运算符操作数的值的表达式。

从本质上说产生将亡值的途径有两种，第一种是使用类型转换将泛左值转换为该类型的右值引用。第二种在C++17标准中引入，我们称它为临时量实质化，指的是纯右值转换到临时对象的过程，在C++17标准之前临时变量是纯右值，只有转换为右值引用的类型才是将亡值。

### 将左值转换为右值

在C++11标准中可以在不创建临时值的情况下显式地将左值通过static_cast转换为将亡值。值得注意的是，由于转换的并不是右值，因此它依然有着和转换之前相同的生命周期和内存地址。这可以让左值使用移动语义。

无论一个函数的实参是左值还是右值，其形参都是一个左值，即使这个形参看上去是一个右值引用。在C++11的标准库中还提供了一个函数模板std::move帮助我们将左值转换为右值。

### 万能引用

所谓的万能引用是因为发生了类型推导。在这个推导过程中，初始化的源对象如果是一个左值，则目标对象会推导出左值引用；反之如果源对象是一个右值，则会推导出右值引用，不过无论如何都会是一个引用类型。

引用折叠规定了在不同的引用类型互相作用的情况下应该如何推导出最终类型，当模板类型为左值引用时，只有实际类型为右值引用，推导得到的才会是右值引用，否则就是左值引用。

万能引用最典型的用途被称为完美转发。std::forward函数模板可以帮助完成转发。

c++针对局部变量和右值引用的隐式移动操作进行了优化。

## lambda表达式（C++11～C++20）

语法定义：`[ captures ] ( params ) specifiers exception -> ret { body }`

- [ captures ] —— 捕获列表，它可以捕获当前函数作用域的零个或多个变量，变量之间用逗号分隔。
- ( params ) —— 可选参数列表.
- specifiers —— 可选限定符，C++11中可以用mutable，它允许我们在lambda表达式函数体内改变按值捕获的变量，或者调用非const的成员函数。
- exception —— 可选异常说明符，我们可以使用noexcept来指明lambda是否会抛出异常。
- ret —— 可选返回值类型，不同于普通函数，lambda表达式使用返回类型后置的语法来表示返回类型，如果没有返回值（void类型），可以忽略包括->在内的整个部分。
- { body } —— lambda表达式的函数体。

### 捕获列表

被捕获的变量必须是自动存储类型，及非静态的局部变量。捕获变量可以是捕获值或是捕获引用。捕获值的变量默认无法被修改，除非添加mutable，而lambda表达式中的捕获值的变量类似静态局部变量，会记忆修改，并且不会和外部作用域的值同步。

### lambda表达式的实现原理

lambda表达式类似函数对象。在编译器由编译器自动生成一个闭包类，在运行时由这个闭包类产生一个对象，我们称它为闭包。

无状态的lambda表达式可以隐式转换为函数指针。

### 广义捕获

简单捕获：

- [this] —— 捕获this指针，捕获this指针可以让我们使用this类型的成员变量和函数。
- [=] —— 捕获lambda表达式定义作用域的全部变量的值，包括this。
- [&] —— 捕获lambda表达式定义作用域的全部变量的引用，包括this。

初始化捕获支持捕获表达式结果以及自定义捕获变量名。

c++17添加constexpr关键字，以及捕获this指针，在捕获列表中直接使用this纸箱对象的成员。

c++20加入[=, this]，以区分[=, *this]

c++20中添加模板对lambda的支持`[]<typename T>(T t) {}`。

C++20标准允许了无状态lambda表达式类型的构造和赋值。

## 非静态数据成员默认初始化（C++11 C++20）

C++11标准提出了新的初始化方法，即在声明非静态数据成员的同时直接对其使用=或者{}初始化。在初始化的优先级上有这样的规则，初始化列表对数据成员的初始化总是优先于声明时默认初始化。

在C++20中我们可以对数据成员的位域进行默认初始化。

## 列表初始化（C++11 C++20）

C++11标准引入了列表初始化，它使用大括号{}对变量进行初始化，和传统变量初始化的规则一样，它也区分为直接初始化和拷贝初始化。它支持隐式调用多参数的构造函数。也可以使用列表初始化对标准容器进行初始化。

std::initializer_list简单地说就是一个支持begin、end以及size成员函数的类模板。只需要添加一个以std::initializer_list为形参的构造函数就可以支持列表初始化。

注意事项：

- 隐式缩窄转换报错
- 列表初始化的优先级问题：std::initializer_ list为参数的构造函数优先

C++20标准中引入了指定初始化的特性，允许指定初始化数据成员的名称，从而使代码意图更加明确。

## 默认和删除函数（C++11）

编译器会为类添加默认的构造函数。像这样有特殊待遇的成员函数一共有6个：

- 默认构造函数。
- 析构函数。
- 复制构造函数。
- 复制赋值运算符函数。
- 移动构造函数（C++11新增）。
- 移动赋值运算符函数（C++11新增）。

问题：

- 声明任何构造函数都会抑制默认构造函数的添加。
- 一旦用自定义构造函数代替默认构造函数，类就将转变为非平凡类型。

c++11引入=default和=delete表示显式默认和显示删除。=default可以添加到类内部函数声明，也可以添加到类外部。它可以让我们在不修改头文件里函数声明的情况下，改变函数内部的行为。=delete必须添加在类内部的函数声明中。显式删除特定类的new运算符可以阻止该类在堆上动态创建对象。

## 非受限联合类型（C++11）

过去的C++标准规定，联合类型的成员变量的类型不能是一个非平凡类型，也就是说它的成员类型不能有自定义构造函数。

>当面对一个可能被滥用的功能时，语言的设计者往往有两条路可走，一是为了语言的安全性禁止此功能，另外则是为了语言的能力和灵活性允许这个功能，C++的设计者一般会采用后者。但是联合类型的设计却与这一理念背道而驰。这种限制完全没有必要，去除它可以让联合类型更加实用。

在C++11中如果有联合类型中存在非平凡类型，那么这个联合类型的特殊成员函数将被隐式删除，也就是说我们必须自己至少提供联合类型的构造和析构函数。比较推荐让联合类型的构造和析构函数为空，也就是什么也不做，并且将其成员的构造和析构函数放在需要使用联合类型的地方。可以使用placement new的技巧进行初始化，在使用完成后手动调用对象的析构函数。如果开发环境支持C++17标准，则大部分情况下我们可以使用std::variant来代替联合体。

## 委托构造函数（C++11）

一个类有多个不同的构造函数会包含重复的代码，并且使得代码的重复变得困难。若把数据成员的初始化放到一个函数中，会因为对成员及逆行两次操作导致额外的性能开销。某个类型的一个构造函数可以委托同类型的另一个构造函数对对象进行初始化。委托构造函数会将控制权交给代理构造函数，在代理构造函数执行完之后，再执行委托构造函数的主体。

注意：

- 每个构造函数都可以委托另一个构造函数为代理。特殊构造函数也能成为委托构造函数。
- 递归循环委托会导致未定义的行为，例如栈内存用尽。建议使用委托构造函数时，通常只指定一个代理构造函数即可，其他的构造函数都委托到这个代理构造函数，尽量不要形成链式委托，避免出现循环递归委托。
- 如果一个构造函数为委托构造函数，那么其初始化列表里就不能对数据成员和基类进行初始化。
- 委托构造函数的执行顺序是先执行代理构造函数的初始化列表，然后执行代理构造函数的主体，最后执行委托构造函数的主体。
- 如果在代理构造函数执行完成后，委托构造函数主体抛出了异常，则自动调用该类型的析构函数。

委托模板构造函数是指一个构造函数将控制权委托到同类型的一个模板构造函数，简单地说，就是代理构造函数是一个函数模板。这样做的意义在于泛化了构造函数，减少冗余的代码的产生。

## 继承构造函数（C++11）

当父类中存在大量的构造函数时，子类中也需要定义同样多的构造函数来转发构造参数。可以使用using关键字将父类的函数引入子类，c++11允许使用using关键字将父类的构造函数引入到子类中，`using Base::Base`这可以让编译器自己生成转发到基类的构造函数。

注意

- 派生类是隐式继承基类的构造函数，所以只有在程序中使用了这些构造函数，编译器才会为派生类生成继承构造函数的代码。
- 派生类不会继承基类的默认构造函数和复制构造函数。执行派生类默认构造函数之前一定会先执行基类的构造函数。同样的，在执行复制构造函数之前也一定会先执行基类的复制构造函数。
- 继承构造函数不会影响派生类默认构造函数的隐式声明，也就是说对于继承基类构造函数的派生类，编译器依然会为其自动生成默认构造函数的代码。
- 在派生类中声明签名相同的构造函数会禁止继承相应的构造函数。
- 派生类继承多个签名相同的构造函数会导致编译失败。
- 继承构造函数的基类构造函数不能为私有。

## 强枚举类型（C++11 C++17 C++20）

大多数情况下，我们说C++是一门类型安全的强类型语言，但是枚举类型在一定程度上却是一个例外。

- 枚举类型可以隐式转换为整型
- 枚举类型会把其内部的枚举标识符导出到枚举被定义的作用域。

将枚举类型变量封装成类私有数据成员，保证无法被外界访问。访问枚举类型的数据成员必须通过对应的常量静态对象。

- 无法指定枚举类型的底层类型。因此，不同的编译器对于相同枚举类型可能会有不同的底层类型，甚至有无符号也会不同。

如果代码中有需要表达枚举语义的地方，还是应该使用枚举类型。

C++11添加强枚举类型，在enum之后加上class关键字。

- 枚举标识符属于强枚举类型的作用域，在访问时必须加上枚举类型名，否则会编译失败。
- 枚举标识符不会隐式转换为整型。
- 能指定强枚举类型的底层类型，底层类型默认为int类型。使用:符号指定。
- 强枚举类型不允许匿名。

C++17对有底层类型的枚举类型对象可以直接使用列表初始化。

C++17的枚举类型是一个完美的新整数类型。std::byte就是这样实现的。

C++20可是使用using打开强枚举类型的命名空间:`using enum EnumName;`，也可以只引入特定的枚举标识符:`using EnumName:Enum;`

## 扩展的聚合类型（C++17 C++20）

C++17规定从基类公开且非虚继承的类也可能是一个聚合。

派生类是聚合类型的条件

- 没有用户提供的构造函数。但是可以声明默认构造函数，在C++20中禁止。
- 没有私有和受保护的非静态数据成员。
- 没有虚函数。
- 必须是公开的基类，不能是私有或者受保护的基类。
- 必须是非虚继承。

`<type_traits>`中有`is_aggregate`来判定是否是聚合类型。

可以简化对聚合类型的初始化，只需要删除派生类中用户提供的构造函数，就可以直接初始化(直接使用聚合大括号初始化即可)。总是假设基类是一种在所有数据成员之前声明的特殊成员，如果派生类存在多个基类，那么其初始化的顺序与继承的顺序相同。

C++20规定聚合类型对象的初始化可以用小括号列表来完成，其最终结果与大括号列表相同。
