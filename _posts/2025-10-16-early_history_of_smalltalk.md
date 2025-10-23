---
title: The Early History Of Smalltalk
date: 2025-10-16
url: https://worrydream.com/EarlyHistoryOfSmalltalk/
tags:
  - smalltalk
---

## Abstract

绝大多数想法来自之前已有的想法。

Smalltalk是新思想的完整实现，计算机是个人学习、思考与表达的工具，而不是更强的计算机器。

## Introduction

Smalltalk是更大的被称为个人计算(personal computing)的追求的一部分。

编程语言可以分成两类，一类是特性拼凑`agglutination of features`，另一类是风格结晶`crystallization of style`。后者有清晰的核心思想，而前者没有。前者通常由委员会设计，而后者由一个人主导。

Smalltalk的设计是基于我们所有可以描述和呈现的事物都可以通过一种行为构建块的递归组合来表示。状态和过程被隐藏在块内，对块的交互只通过消息交换。

哲学上说，Smalltalk的对象和莱布尼兹的单子比较接近。同时，Smalltalk的类也是对象，这和柏拉图的理念论比较接近，类型本身也有类型Mateclass,这个类则是自己表示自己的。

Smalltalk的每一个对象都像是一个小型的计算机。开始先确定接口，对实现的关注可以推迟。

Smalltalk的贡献是面向对象的设计范式。

## 1960-66—Early OOP and other formative ideas of the sixties

OOP的两个核心动力：

- 寻找一个对于复杂系统更优的模块结构，允许隐藏实现细节
- 寻找一个更灵活版本的指派

新思想的接受过程，包括内部和外部。

1961年，对文件进行特殊处理，包含三个部分，第一部分是运行指令的指针，第二部分是各个运行部分，第三部分是任意尺寸和形式的数据。

分段存储系统。调用函数接口而不是直接操作指针。

### Sketchpad and Simula

ARPA组织和Utah的主要目标是解决3d图像的隐藏线问题。

计划`Sketchpad: A man-machine graphical communication system`，其中的巨大的想法，发明了现代交互式计算机图像，图像使用`master painting`绘制`instance drawing`，提供限制。

Simula语言。和Sketchpad类似，也有对象的概念，但是使用命令式的方式控制对象。

命令控制对象的想法改变了一切。

## 1967-69—The FLEX Machine, a first attempt at an OOP-based personal computer

个人电脑，FLEX machine，面向非计算机专业的用户，类似JOSS和Wirth的EULER。特点是动态模拟和动态拓展。

借鉴EULER，使用byte-code执行，简化Simula。

### Doug Engelbart and NLS

个人计算`personal computing`。Doug Engelbart提出计算机是强化人类智能的工具。FLEX机器接受了这些观点。

人机交互的概念和摩尔定律的结合产生了震撼的效果。给多数人使用的设备是颠覆性的概念。

NLS的一个特点是用户界面是参数化的，准确的说是语法化的。

同时有了一些基于Sketchpad的新想法，窗口并不是全部，而只是一个观察口，只是虚拟世界的一部分。

从赋值到对象，FLEX的对象包含一个主指针和一个实例指针，对于传统的左值和右值，对于复杂对象，比如赋值给数组一个默认值这种情况，应该被忽略，但是传统的方法不可避免地会创建一个冗余的对象。对于赋值运算，可以将其视为是一个发给对象的消息，运算符也只是消息的一个部分。对象应该内部管理它的行为，对象是某种值和行为的映射。Rudolf Carnap的逻辑著作提供了哲学层面的支持，类型定义是一种内涵定义，通过定义性质和规则来定义。

ref: Rudolf Carnap

Simula中使用了协程控制结构来挂起和恢复对象。循环的控制结构中也使用了协程。这些部分在Smalltalk中得到了继承和强化。

FLEX中还有一个when的控制结构，是一种事件驱动的软中断。when之中的逻辑，只会对变化的变量进行重新计算，这使得其变得高效。但是对应的，when也带来了复杂性，上下文的控制。

原始的一些FLEX的`proto-object`的想法可以实现。

Marvin Minsky提到了构建主义学习理论，重新构建教育，基于心理学和认知科学。

Alan kay见到了平板显示器。

Alan kay见到了系统GRAIL，提供了和FLEX完全不同的交互形式。

Alan Kay见到了LOGO小组，计算机并不是个人工具，而是个人媒介。

以上种种见闻最终让Alan Kay明白了个人电脑应该是的样子。

IMP语言支持对语言中的任何部分定义含义和行为。Alan Kay借鉴了这部分概念，实现了直接解释器，并随后发展成了每个对象都是对消息的解释并执行。

ref:[The Reactive Engine by Alan Curtis Kay 1969](https://www.chilton-computing.org.uk/inf/pdfs/kay.htm)

AI系统，Carl Hewitt的PLANNER系统和Pat Winston的概念形成系统

CAL-TSS系统中，对象的内部状态被禁止访问。

Lisp的核心是`eval`和`apply`。Lisp在实践中变得不再纯粹，同时它也是不纯粹的函数式。Alan Kay的设计原则：把最难、最深刻的事情做到极致，然后从它构建出其他一切。

## 1970-72—Xerox PARC: The KiddiKomp, miniCOM, and Smalltalk-71

KiddiKomp的新版本并不理想。

`观点胜过80点智力`。

`预测未来的最好方式就是创造未来`。

头脑风暴不能取代冷静持续的思考。

KiddiKomp精炼为了miniCOM，其中包含了Smalltalk。

Smalltalk-71是一种带有对象附加功能的解析器，可以直接执行代码。求值是直接的模式匹配。

如何将对象描述为通用计算机。

Dave Fisher给出了更通用的控制环境，反射式设计。关键在于只需处理模块之间调用的机制，而不用关心模块内部的细节。

美在面向对象设计中的含义。

Alan Kay认为在这里更契合的美是从受精卵发展成复杂生物体的特化过程，并且细胞膜是一个很独特的设计，兼顾了拓展性和一致性。

Alan Kay发明了桌面和窗口系统。

字符生成器。

## 1972-76—The first real Smalltalk (-72), its birth, applications, and improvements

打赌smalltalk可以在一页纸中定义出来。

但是碰到了问题：

- 基于循环实现解释器
- 解析和消息接收交织在一起
- 发送和接收需要如何项目协作

此时smalltalk的六个主要思想：

- Everything is an object
- Objects communicate by sending and receiving messages (in terms of objects)
- Objects have their own memory (in terms of objects)
- Every object is an instance of a class (which must be an object)
- The class holds the shared behavior for its instances (in the form of objects in a program list)
- To eval a program list, control is passed to the first object and the remainder is treated as its message

### Development of the Smalltalk-72 System and Applications

Interim Dynabook上的实现过程，键盘交互，重叠窗口，绘图海龟，所见即所得的编辑器，按实例检索，音乐合成，实时乐谱采集系统，动画系统，编程环境。

### The Evolution of Smalltalk-72

Smalltalk-74。OOZE，虚拟内存系统。

## "Object-oriented" Style

面向对象编程风格和抽象数据类型(abstract data types, ADT)。

对象可以取代掉那些赋值操作，但这个部分没有被坚持下去。

OOP是一种后期绑定策略，可以运行时决定行为。

## Smalltalk and Children

与儿童合作。

孩子们自己创造交互式工具。

黑客现象：对任何给定的追求，特定的5%的人会自然而然的投入其中。

孩子学习的关键是系统是否直观。

有一些概念需要了解了才会发现。

需要一种表达思想的中间媒介，设计模板。

更进一步的技术是继承，在更专业的架构基础上进行由孩子进行构建。编程和写作的相似性，需要多年循序渐进的学习。

同时，学习编程可能并不会让一个人得到提升，甚至可能相反。

要认识世界，必须构建世界。

关键是流畅性和将知识作为隐喻。

计算机包含着特殊的思考方式，增强了我们理解世界的能力。

## 1976-80—The first modern Smalltalk (-76), its birth, applications, and improvements

需要重新开始。Alan kay和Dan走向了不同的方向。

工具会反过来重塑我们，smalltalk本身的范式在工具中不断重复着，而抹去了工具中的新想法。

### Inheritance

委托式继承。

### The Smalltalk User Interface

### Smalltalk-76

Smalltalk的推式被拉式所取代。

## 1980-83—The release version of Smalltalk (-80)

Smalltalk的一些特点被去除以适应分发。

## Coda

硬件其实就是软件的早期结晶。底层技术和过度优化阻碍了程序设计的进步。

软件进步可以被看作是寻找后期绑定的方法，然后将这些方法统一硬件。

面向对象的一些优化其实也需要硬件支持。

从晚绑定到智能计算。

一种正确的方式是，培养对自己作品的深度不满足感，同时不把不满足等同于自我否定。
