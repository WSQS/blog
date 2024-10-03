---
title: Refactoring Improving the Design of Existing Code
date: 2024-10-03
---

- [Preface](#preface)
  - [What is Refactoring](#what-is-refactoring)
  - [What’s in This Book?](#whats-in-this-book)
  - [Who Should Read This Book?](#who-should-read-this-book)
- [Refactoring: A First Example](#refactoring-a-first-example)
  - [The Starting Point](#the-starting-point)
  - [Comments on the Starting Program](#comments-on-the-starting-program)
  - [The First Step in Refactoring](#the-first-step-in-refactoring)
  - [Decomposing the statement Function](#decomposing-the-statement-function)
    - [Removing the play Variable](#removing-the-play-variable)
    - [Removing the format Variable](#removing-the-format-variable)
    - [Removing Total Volume Credits](#removing-total-volume-credits)
  - [Splitting the Phases of Calculation and Formatting](#splitting-the-phases-of-calculation-and-formatting)
  - [Reorganizing the Calculations by Type](#reorganizing-the-calculations-by-type)
    - [Moving Functions into the Calculator](#moving-functions-into-the-calculator)
    - [Making the Performance Calculator Polymorphic](#making-the-performance-calculator-polymorphic)
  - [Final Thoughts](#final-thoughts)
- [Principles in Refactoring](#principles-in-refactoring)
  - [Defining Refactoring](#defining-refactoring)
  - [The Two Hats](#the-two-hats)
  - [Why Should We Refactor?](#why-should-we-refactor)
    - [Refactoring Improves the Design of Software](#refactoring-improves-the-design-of-software)
    - [Refactoring Makes Software Easier to Understand](#refactoring-makes-software-easier-to-understand)
    - [Refactoring Helps Me Find Bugs](#refactoring-helps-me-find-bugs)
    - [Refactoring Helps Me Program Faster](#refactoring-helps-me-program-faster)
  - [When Should We Refactor?](#when-should-we-refactor)
    - [Preparatory Refactoring—Making It Easier to Add a Features](#preparatory-refactoringmaking-it-easier-to-add-a-features)
    - [Comprehension Refactoring: Making Code Easier to Understand](#comprehension-refactoring-making-code-easier-to-understand)
    - [Litter-Pickup Refactoring](#litter-pickup-refactoring)
    - [Planned and Opportunistic Refactoring](#planned-and-opportunistic-refactoring)
    - [Long-Term Refactoring](#long-term-refactoring)
    - [Refactoring in a Code Review](#refactoring-in-a-code-review)
    - [What Do I Tell My Manager?](#what-do-i-tell-my-manager)
    - [When Should I Not Refactor?](#when-should-i-not-refactor)
  - [Problems with Refactoring](#problems-with-refactoring)
    - [Slowing Down New Features](#slowing-down-new-features)
    - [Code Ownership](#code-ownership)
    - [Branches](#branches)
    - [Testing](#testing)
    - [Legacy Code](#legacy-code)
    - [Databases](#databases)
  - [Refactoring, Architecture, and Yagni](#refactoring-architecture-and-yagni)
  - [Refactoring and the Wider Software Development Process](#refactoring-and-the-wider-software-development-process)
  - [Refactoring and Performance](#refactoring-and-performance)
  - [Where Did Refactoring Come From?](#where-did-refactoring-come-from)
  - [Automated Refactorings](#automated-refactorings)
  - [Going Further](#going-further)
- [Bad Smells in Code](#bad-smells-in-code)
  - [Mysterious Name](#mysterious-name)
  - [Duplicated Code](#duplicated-code)
  - [Long Function](#long-function)
  - [Long Parameter List](#long-parameter-list)
  - [Global Data](#global-data)
  - [Mutable Data](#mutable-data)
  - [Divergent Change](#divergent-change)
  - [Shotgun Surgery](#shotgun-surgery)
  - [Feature Envy](#feature-envy)
  - [Data Clumps](#data-clumps)
  - [Primitive Obsession](#primitive-obsession)
  - [Repeated Switches](#repeated-switches)
  - [Loops](#loops)
  - [Lazy Element](#lazy-element)
  - [Speculative Generality](#speculative-generality)
  - [Temporary Field](#temporary-field)
  - [Message Chains](#message-chains)
  - [Middle Man](#middle-man)
  - [Insider Trading](#insider-trading)
  - [Large Class](#large-class)
  - [Alternative Classes with Different Interfaces](#alternative-classes-with-different-interfaces)
  - [Data Class](#data-class)
  - [Refused Bequest](#refused-bequest)
  - [Comments](#comments)
- [Building Tests](#building-tests)
  - [The Value of Self-Testing Code](#the-value-of-self-testing-code)
  - [Sample Code to Test](#sample-code-to-test)
  - [A First Test](#a-first-test)
  - [Add Another Test](#add-another-test)
  - [Modifying the Fixture](#modifying-the-fixture)
  - [Probing the Boundaries](#probing-the-boundaries)
  - [Much More Than This](#much-more-than-this)
- [Introducing the Catalog](#introducing-the-catalog)
  - [Format of the Refactorings](#format-of-the-refactorings)
- [Reference](#reference)

It's my note of *Refactoring Improving the Design of Existing Code*

## Preface

Programmer and project manager have different understand to refactoring.

### What is Refactoring

> Refactoring is the process of changing a software system in a way that does not alter the external behavior of the code yet improves its internal structure.

- 保留外部行为
- 优化内部结构

> Improving the design of the code after it has been written.

先前的观点：设计先于编程，随后代码逐渐从工程沦为被破解。重构于此相反，通过修改使得代码不会衰退。通过重构，设计在编程中持续的存在。

### What’s in This Book?

> My aim is to show you how to do refactoring in a controlled and efficient manner.

- 章节结构
  - 第一章：一个例子
  - 第二章：重构原则
  - 第三章：审查代码
  - 第四章：构建测试
  - 后续：重构的目录

书使用JavaScript作为示例语言

### Who Should Read This Book?

目标读者是专业的程序员和架构师

阅读方法：完全阅读前四章，对后续内容需要知道都包含些什么

## Refactoring: A First Example

困境：一个重构的例子太复杂将会使读者难以理解，反之，若是太简单则会让无法体现重构的价值，显得重构的操作是不值得的。

### The Starting Point

例子：话剧社数据处理

演出数据和账单数据都以Json文件提供，需要同时需要计算信用点数

### Comments on the Starting Program

> When you have to add a feature to a program but the code is not structured in a convenient way, first refactor the program to make it easy to add the feature, then add the feature.

在试图添加新特性之前，需要考虑重构已有代码以使后续工作更加容易

- 引入变化
  - 以HTML格式输出：需要在每个输出结果的语句哪里添加条件性判断
    - 可能的解决方案：复制方法并使其输出HTML，这会导致逻辑修改需要同时对两个函数更新
  - 添加戏剧种类

重构的原因：需求在后续过程中会产生变化而需要人去理解代码并做修改

### The First Step in Refactoring

> Before you start refactoring, make sure you have a solid suite of tests. These tests must be self-checking.

重构的第一步是对将要重构的部分构建足够的测试集，测试的关键是结果能够自动比对，而不需要手动检查。

可以考虑使用现代测试框架。这是一种双重检查。

### Decomposing the statement Function

寻找行为整体中的区分点，根据对其的理解将其转变为函数，这被称为提取函数(Extract Function)。

- 提取函数的过程
  - 查找在原本代码的上下文中需要的变量，将其设置为参数或者是返回值
  - 在代码原本的位置改为调用提取的函数
  - 编译并测试程序是否有错误

> Refactoring changes the programs in small steps, so if you make a mistake, it is easy to find where the bug is.

重构的过程：微小的修改和测试相继进行。这可以有效避免进去debug的混乱当中。

- 重命名变量，使其更加清楚
  - 将返回值重命名为result
  - 在动态类型语言中，命名中包含类型名
  - 若没有特殊信息，则使用不定冠词

> Any fool can write code that a computer can understand. Good programmers write code that humans can understand.

重命名变量可以有效澄清代码

#### Removing the play Variable

play 变量是从performance当中计算得到的，因此并不需要传入。这是用计算替换查询(Replace Temp with Query)。

将计算封装为一个函数，将该变量替换为该函数，这是内联变量(Inline Variable)。

- 改变函数声明(Change Function Declaration)
  - 在其他函数中也将参量替换为函数
  - 移除输入的参量

注：这样的重构操作会对性能产生影响

#### Removing the format Variable

移除本地变量可以使得提取函数变得更加容易，可以在提取函数之前先进行移除本地变量

临时函数变量使用声明函数替换，使用更改函数声明(Change Function Declaration)

#### Removing Total Volume Credits

分割循环(Split Loop)将不同的两个功能在两个循环当中进行

滑动声明(Slide Statements)在循环前声明

随后可以再使用计算替换查询

> The performance of software usually depends on just a few parts of the code, and changes anywhere else don't make an appreciable difference.

重构带来的性能损失通常是可以忽略的，而即使重构会影响性能，重构代码也是值得考虑的，因为这会使得优化代码变得更为容易。通常最终会得到一个又简洁又高效的代码

一小步一小步的修改，每一次修改之后都进行测试

### Splitting the Phases of Calculation and Formatting

重构中，第一步通常是将任务分解，随后是一些功能性的考量。在新的功能中重用代码。

划分阶段(Split Phase):将逻辑划分为多个部分，首先使用提取函数将各个部分抽象成独立的函数，随后在阶段之间添加中介的数据结构，随后将其余参数和相关的计算代码逐步移动到中介数据结构中去。

> I prefer to treat data as immutable as much as I can—mutable state quickly becomes something rotten.

将原始输入数据进行拷贝并随后用之前的函数对其成员进行处理，将后一部分的代码中的对应数据转换为该成员。最终生成这一数据结构的函数会成为独立地一个部分。

使用流程替换for循环(Replace Loop with Pipeline)，这是利用了JavaScript的reduce方法。

> Brevity is the soul of wit, but clarity is the soul of evolvable software.

清晰在重构中比简洁更重要。

> When programming, follow the camping rule: Always leave the code base healthier than when you found it.

### Reorganizing the Calculations by Type

多态(polymorphism)

用多态替换条件(Replace Conditional with Polymorphism)

#### Moving Functions into the Calculator

将函数移动到Calculator类中。

#### Making the Performance Calculator Polymorphic

将代码替换为子类(Replace Type Code with Subclasses)，首先需要创建子类，为了得到正确的子类，用工厂函数替换构造函数(Replace Constructor with Factory Function)，在这个函数中决定返回具体类。随后可以将条件替换为多态，在具体类中覆写基类中的函数，同时可以考虑在基类中添加对具体类报错的逻辑。也可以在基类实现较为普遍的算法，在具体类中实现特殊的算法。在函数中可以返回中间数据结构，也可以返回计算器(生成器)。

### Final Thoughts

- 目前重构的三个阶段:
  - 将原本的函数分解为一组内聚的函数
  - 使用分离阶段划分出计算阶段和渲染阶段
  - 使用多态实现计算器
- 重构的常规过程:
  - 阅读代码
  - 获得洞见
  - 使用重构在代码中实现洞见

对代码的重构可以更容易的获得更深的洞见。

> The true test of good code is how easy it is to change it.

这是超越代码风格的标准

关键是掌握重构的节奏：每次改动一点点

## Principles in Refactoring

### Defining Refactoring

> Refactoring (noun): a change made to the internal structure of software to make it easier to understand and cheaper to modify without changing its observable behavior.
> Refactoring (verb): to restructure software by applying a series of refactorings without changing its observable behavior.
> If someone says their code was broken for a couple of days while they are refactoring, you can be pretty sure they were not refactoring.

重构是一种清理代码(clean up code)的技法，特点是每次只改动一点点。重组(restructuring)是一个更宽泛的清理代码的概念。

重构需要维持不变的是用户可观察到的程序的表现，这和程序实际运行的逻辑存在差异。

重构和性能优化类似，都对代码进行操作，但是不影响到程序整体的功能。区别在于目的，重构是为了让代码更容易理解和更改，这可能提升或降低性能，性能优化则专注于提升性能，并且可能会留下难以理解的代码。

### The Two Hats

程序开发中包含两个不同的过程：添加功能和重构。需要明确自己在某一时刻是在做什么，不能两个过程同时进行。

### Why Should We Refactor?

#### Refactoring Improves the Design of Software

减少重复的代码，可以使得修改更为容易。

#### Refactoring Makes Software Easier to Understand

> Programming is all about saying exactly what I want.
> A little time spent on refactoring can make the code better communicate its purpose—say more clearly what I want.
> I make a point of trying to put everything I should remember into the code so I don’t have to remember it.

减少对代码的记忆，减轻心智负担。

#### Refactoring Helps Me Find Bugs

> I’m not a great programmer; I’m just a good programmer with great habits.

#### Refactoring Helps Me Program Faster

> Every new feature requires more and more time to understand how to fit it into the existing code base, and once it's added, bugs often crop up that take even longer to fix.

已有的代码是一种负担，并随着修改的不断进行，新的修改会越来越难以进行。

> [Design Stamina Hypothesis](https://martinfowler.com/bliki/DesignStaminaHypothesis.html): By putting our effort into a good internal design, we increase the stamina of the software effort, allowing us to go faster for longer.

### When Should We Refactor?

> The Rule of Three:Three strikes, then you refactor.

重复到第三次的时候进行重构。

#### Preparatory Refactoring—Making It Easier to Add a Features

最适合重构的时间是在需要在代码当中添加新特性之前。

参数化函数(Parameterize Function)

> When people are pushing you to just go straight there, sometimes you need to say, ‘Wait, I need to check the map and find the quickest route.’ The preparatory refactoring does that for me.

这是一种准备性的重构。在修复bug时也是同样的情况。

#### Comprehension Refactoring: Making Code Easier to Understand

> Whenever I have to think to understand what the code is doing, I ask myself if I can refactor the code to make that understanding more immediately apparent.

重构将理解移动到代码当中。

#### Litter-Pickup Refactoring

在代码过程中或代码结束之后简单的进行修改。

#### Planned and Opportunistic Refactoring

大多数重构的工作能够和其他工作一同进行。

> You have to refactor when you run into ugly code—but excellent code needs plenty of refactoring too.

已有代码中的权衡随着情况的变化需要重新考量。

> for each desired change, make the change easy (warning: this may be hard), then make the easy change -- Kent Beck

添加新特性的最快方法是让代码更容易去添加。

大多数的重构还是应该随着工作的展开伺机进行。

试图将新特性的代码和重构的代码区分开是一个有待检验的部分，二者通常纠缠在一起，没有了新特性的语境，重构的代码将会更加难以理解。

#### Long-Term Refactoring

相比起直接进行一个长期、大型的重构，一个更好的方法是在对应的问题上逐步解决，这可以避免重构会破坏代码。

用抽象分支(Branch By Abstraction)

#### Refactoring in a Code Review

代码审查可以帮助有经验的开发者向更没有经验的开发者传递知识。重构可以帮助代码审查的进行。重构嵌入代码审查的最佳实践是结对编程。

#### What Do I Tell My Manager?

> A schedule-driven manager wants me to do things the fastest way I can; how I do it is my responsibility.

对于不明智的管理者可以选择不告诉他们，因为选择如何进行我的工作是我的责任。

#### When Should I Not Refactor?

对于不需要修改的糟糕的代码，那就不需要重构。对于可以作为API调用的代码可以保留。另一种情况是相比起重构代码，重写是更简单的时候，这是一个棘手的判断。

### Problems with Refactoring

#### Slowing Down New Features

> The whole purpose of refactoring is to make us program faster, producing more value with less effort.

重构并不是某种为了让代码干净的精神洁癖，而是产生显示经济效益的编程技法。

#### Code Ownership

对于暴露出去的接口，进行重构还需要维持已有的接口不变。不建议采用细粒度的强代码所有权，更应该是团队对代码的所有权，团队的所有人都可以修改整个团队的代码，甚至可以是跨团队的代码。

#### Branches

使用特性分叉的方式保证主分支干净，而在各个分支上实现具体特性并在完成时合并进主分支。但是这会在合并时导致困难，并且这样的困难会随着分支存在的时间的延长显著的增加，特性分支应该越短越好。持续整合(Continuous Integration, CI)用实践去保证主干是健康的，可以有效减少分支合并的困难。将新特性进行分解，并对正在进行的特性添加特性触发器(feature toggles)。CI和重构的结合可以有效避免特性分支合并的困难。

#### Testing

为了快速的发现错误，需要自测试代码。除此之外，如果开发环境当中有自动化的重构工具，可以使用它们并且不需要做测试。另外，可以利用一些语言的特殊技法来做安全的重构，例如[C++中的提取方法](http://jay.bazuzi.com/Safely-extract-a-method-in-any-C++-code/)

#### Legacy Code

重构可以有效处理遗留代码，但是遗留代码缺少测试用例会使得重构难以进行。推荐阅读《Working Effectively with Legacy Code》，按照上面的说明进行，要点是找到程序的接缝，并在那里添加测试，但是添加测试本身就是危险的。并不需要对遗留代码进行彻底的重构，只需要将其分解为多个小部分，并在每次遇到的时候将其变得更好一点。

#### Databases

对于数据库重构，可以参考[evolutionary database design](https://martinfowler.com/articles/evodb.html)和[database refactoring](https://martinfowler.com/books/refactoringDatabases.html)，本质是同时修改数据库的结构和使用数据迁移代码。对于数据库的修改，可以考虑使用同步修改(parallel change)的方法在多个版本之间逐步的进行替换。

### Refactoring, Architecture, and Yagni

重构可以构建一个能够应对需求变化的的代码设计。其中一个方法是将灵活性机制引入到软件中，但是这需要对参数的准确处理和引入，而实际上这是难以做到的，并且会减弱应对改变的能力。不同的是，重构只是使得程序适合当前的需求，只在必要的时候才引入参数，这被称为yagni(you aren't going to need it)。只有在重构的基础上，才可以接受结构和设计。关于架构可以参考《Building Evolutionary Architectures》。

### Refactoring and the Wider Software Development Process

极限编程(Extreme Programming, XP)是最早的[敏捷开发方法(agile software methods)](https://martinfowler.com/articles/newMethodology.html)。重构的首个基础是自动测试代码(self-testing code)。在团队协作中重构的重点是每个成员可以在不干涉他人工作的情况下进行重构，这依赖于CI和自动测试代码。自动测试代码、CI和重构可以产生有力的协同作用，同时重构和yagni也可以产生协同作用。在此基础上，持续交付(Continuous Delivery)可以减少风险，并且满足商业需要，减少一个想法成为现实的时间。

### Refactoring and Performance

快速软件的秘密是首先写出可优化的软件随后再进行优化。有三种方式去制造出性能优良的软件。在硬实时系统中使用的时间预算(time budgeting)，对各个组件分配时间，并限制各个组件的资源，它关注于硬件运行时间。第二种方法是持续关注(constant attention)，这会受到个人的观点的影响。

> Even if you know exactly what is going on in your system, measure performance, don’t speculate. You’ll learn something, and nine times out of ten, it won’t be that you were right!

人们对程序是如何运作的总是存在误解。

程序运行的大多数时间都是花费在代码的一小部分上，对其余部分的优化只是白白浪费了代码的可读性。第三种方法通过运行时分析找到代码中花费时间的点，并对对应的部分进行优化。同时对对应的修改需要在完成之后进行性能测试，如果没有改善就应该回滚修改。

### Where Did Refactoring Come From?

Smalltalk社区当中Ward Cunningham和Kent Beck认识到了重构的重要性。Ralph Johnson和Bill Opdyke对重构的架构进行了研究。John Brant和Don Roberts构建了第一个重构工具。

### Automated Refactorings

如今的IDE可以使用语法树来进行重构，这是更安全的。对于反射的重构IDE可能有点力不从心。所以即使使用了工具进行重构，也需要在重构之后进行测试。现在又语言服务器(Language Servers)可以为文本编辑器提供与IDE类似的功能。

### Going Further

《Refactoring Workbook》更适合学习重构的过程，其中包含练习。《Refactoring to Patterns》结合了重构和设计模式。对具体的领域，有《Refactoring Databases》和《Refactoring HTML》

## Bad Smells in Code

>If it stinks, change it. — Grandma Beck, discussing child-rearing philosophy

需要知道何时开始和结束重构，这是比具体的重构操作更加难以理解的，特别是如果希望为它提供一个坚实的基础的时候。能知道的是有问题可以通过重构来解决，随后就可以更具目录和表格跳转到书上对应的重构的内容。

### Mysterious Name

重命名是重构当中最常做的事情，也是最难做的事情之一，但是好的名字可以有效地让代码容易理解。难以命名同时也意味着代码本身的功能是混杂的，有待重构的。

### Duplicated Code

重复意味着对各个重复的地方需要仔细地阅读来比较其中的差异，在修改时也需要对每一个副本进行修改。处理重复最简单的方法是将重复的代码封装为函数，如果代码只是相似而非完全相同，那么可以使用滑动声明(Slide Statements)，将相似的部分收集在一起进行提取。在子类当中的重复代码可以使用提升方法(Pull Up Method)。

### Long Function

短函数的更容易维护。旧的编程语言因为常见的调用不适合短函数，而现代编程语言则仍然需要在各种文件中进行跳转来阅读函数的作用，函数的良好命名可以缓解这一问题。应该主动的去分解函数，每当我们考虑去写下评论，我们就应该将其转化为函数，并用其意图命名。关键不是函数的长度，而是方法做了什么和它如何实现的语义距离。对于有大量参数和临时变量的函数，可以将临时变量转化为查询。对于大量的参数，可以考虑引入参数对象(Introduce Parameter Object)和保留整个对象(Preserve Whole Object)。如果还是由大量临时变量和参数，可以使用将函数替换为指令(Replace Function with Command)。可以使用评论来找到需要被提取的代码块，如果一行代码需要解释，那就需要被提取。条件和循环也是进行提取的信号，使用分解条件(Decompose Conditional)来应对条件判断，大的switch需要被提取成一个函数，如果对同一个条件判断，有多个switch存在，可以考虑用多态替换条件，对于循环当中的函数，也可以考虑提取成一个方法，如果方法难以命名可以能需要把循环拆开。

### Long Parameter List

将变量作为函数参数传入优于作为全局变量，但是函数参数过多也是一个问题。可以将参数变为查询，可以保留原本的数据结构，可以将若干个变量组织成对象，可以移除标志参数。类型可以有效减少参数链表的尺寸，特别是多个函数共享共同的参数时，可以使用将函数结合为类(Combine Functions into Class)。

### Global Data

全局数据有最强的代码坏味。它可以被任何地方的代码修改，并且难以被发现，它包括全局对象、类对象和单例。可以使用封装变量(Encapsulate Variable)来应对，尽可能限制其被修改的范围。

### Mutable Data

数据的变化通常会导致未预料的结果和棘手的问题。所以函数式编程会要求数据永不改变，更改数据结构将会得到一个包含修改的崭新副本，而保留旧的数据。可以将变量都封装起来，暴露出受监督的接口。如果一个变量被更新来存储不同的值，使用分解变量(Split Variable)来分别存储它们，避免危险的更新。使用查询替换给出变量(Replace Derived Variable with Query)来避免变量参与计算。尽量显示能够对变量进行修改的范围。

### Divergent Change

分叉的变化是指一个模块因为不同的原因向不同的方向进行改变。如果两个功能前后相连，可以用一个中介数据结构分割二者。如果模块中包含向前向后调用，可以使用移动函数(Move Function)来区分两个过程。如果模块是类型，可以使用提取类型(Extract Class)。

### Shotgun Surgery

Shotgun Surgery和变化分叉相反，每当试图做一些修改，需要对很多类做一些小修改，可以将这些共同的函数统一到一个类中来。可以使用内容重构(inlining refactorings)将分开的逻辑放到一起，再将它们分解开。

### Feature Envy

代码应该是高内聚低耦合的，如果一个模块当中的一个方法大量调用了另一个模块的方法，那么它应该被移动到那个模块当中去。如果一个方法使用了多个模块的特性，那么它应该在最多的那个模块当中，也可以将函数进行分解来分开处理。会有一些复杂的设计模式破坏了这个方法，关键在于将一同变化的事物放到一起，数据和设计数据的表现通常一同更改，当有例外时，需要将表现进行移动。

### Data Clumps

一组数据在代码当中一再的出现。可以首先将数据组织成对象，随后通过引入参数对象和保留整个对象来削减参数列表。可以通过从对象当中删除成员变量来测试这个成员变量是否是多余的。使用类可以帮助将一些方法移动到类中来，这可以有效避免复制并且加速未来的开发。

### Primitive Obsession

使用原生类标识特定数据会导致语义信息的缺失，使用对象替换原生类(Replace Primitive with Object)，使用子类来替换类型代码( Replace Type Code with Subclasses)，并随后使用多态。一组原生类可以组成具体的类型。

### Repeated Switches

并不应该无条件的反对条件判断。重点在于重复的switch语句，问题在于，每当要做修改，要在两个地方一同进行修改。可以使用多态对此进行替换。

### Loops

使用流水线替换循环(Replace Loop with Pipeline)，可以使用过滤器和map去替代一些循环的工作。

### Lazy Element

有时一些结构是不需要的。可以使用内联函数和内联类。对于继承，可以使用压缩结构(Collapse Hierarchy)。

### Speculative Generality

一些不需要的逻辑处理，需要被去除。去除函数中无用的参数。当一个函数或类只在测试时被使用时，移除测试用例并应用移除无用代码(Remove Dead Code)。

### Temporary Field

一个只在特定情况下使用的变量是难以理解的。使用提取类型来封装变量，并使用特殊类型(Introduce Special Case)来去除条件判断。

### Message Chains

消息链中，客户为了得到一个对象查询另一个对象，这意味着客户和这样的结构产生了耦合。内部结构的变化会导致客户也必须进行变化。可以使用隐藏代理(Hide Delegate)，或者使用提取函数和移动函数来缩短链条，或者找到都被访问的某个对象，在其上添加方法。

### Middle Man

代理可能导致中间人的出现，一个类当中多数的方法都是在委托给另一个类，可以使用移除中间人(Remove Middle Man)，也可以使用内联函数。如果有额外的行为，可以使用将父类替换为代理(Replace Superclass with Delegate)或是替换子类为代理(Replace Subclass with Delegate)，来折叠中间人。

### Insider Trading

模块之间数据交流需要被抑制，首先使用移动函数和移动区域来限制调用的需要，如果模块对同一个变量有关，可以创建一个第三方模块来有约束的管理那些共同的变量。或者使用隐藏代理将另一个模块作为一个中间人。

### Large Class

当一个类拥有太多的职责，它会拥有很多的成员，同时包含重复的代码。可以结合一部分变量去组成类，又或者是提取子类，变量的前缀和后缀可以作为判断的依据。

### Alternative Classes with Different Interfaces

类的重要特点是可以用子类替代父类实现多态，但是这依赖它们有共同的接口，需要更改函数声明来实现这一点。

### Data Class

只包含数据和set、get方法的类是数据类，它暴露了太多的细节给外部，需要将所有暴露的成员变量都封装起来。试着将行为移动到数据类中去，数据类意味着行为处在错误的位置上，但是这有例外，例如在分割阶段之后的中间数据结构，它的特点是它是不可修改的，不可修改的成员变量并不需要封装。

### Refused Bequest

子类可能并不会重写所有父类的方法，但是只有在会导致误解和问题的情况下才应该考虑将不需要的父类功能下放到同级的子类中去。如果子类不支持父类的一些接口，这个问题更加的严重，可以考虑用代理替换掉子类或父类。这违背了设计模式中“子类必须能够替换它们的基类(IS-A)”的原则。

### Comments

注释是好的，它可以缓解代码的坏味，但是它通常被用作除臭剂，它引导我们看到坏味代码。如果有评论可以考虑将代码提取成函数，或是重命名函数，又或是使用断言(Introduce Assertion)。

> When you feel the need to write a comment, first try to refactor the code so that any comment becomes superfluous.

重构之后，注释应该成为多余的。在不知道该做什么时，应该添加注释，注释说明了你不确定，又或者是解释了你为什么这么做。

## Building Tests

为了顺利进行测试，需要构建坚实的测试用例。

### The Value of Self-Testing Code

写代码只占了很少的一部分时间，绝大部分时间都在debug，在解决bug时，总是有可能会引入新的bug。

> Make sure all tests are fully automatic and that they check their own results.

在两次测试之间发现bug可以有效的定位到所在的位置，自动测试代码成为了bug检测器。在添加新特性之后立刻对其进行测试。

> A suite of tests is a powerful bug detector that decapitates the time it takes to find bugs.

写下测试最合适的时间是在开始编程之前。通过编写测试用例，可以明确什么需要被添加到函数中，更加专注于接口而非实现。

这随后被Kent Beck完善为测试驱动开发。

### Sample Code to Test

可以对数据处理的逻辑和渲染的逻辑分别处理。

### A First Test

为了测试需要选择测试框架，在这里选择的是Mocha。测试包含两个部分，设定一些固定之物，随后检验固定之物的一些特性。测试的名字可以只是区分是什么测试。

> Always make sure a test will fail when it should.

在编写测试用例时，需要修改代码来保证测试用例会失败。

> Run tests frequently. Run those exercising the code you're working on at least every few minutes; run all tests at least daily.

### Add Another Test

检查类中所有代码，并在任何可能失败的情况下进行测试。测试应该是风险驱动的，没必要去测试一些只是读和写的方法，应该测试最可能出错的部分。

> It is better to write and run incomplete tests than not to run complete tests.

在测试代码当中的重复代码也是需要去重构的，但是测试用例之间不应该相互交互。

### Modifying the Fixture

测试的常规流程是setup-exercise-verify。exercise当中会对固定之物进行更改。

### Probing the Boundaries

对于代码的边界，对于异常情况的检测也是测试的重要环节，例如输入为空或者为0和负数。

> Think of the boundary conditions under which things might go wrong and concentrate your tests there.

如果是异常状态的测试会在重构中被修改，这是可以接受的，因为重构只需要保证可观测的行为不变。

> Don’t let the fear that testing can’t catch all bugs stop you from writing tests that catch most bugs.

编写测试用例是收益递减的，应该关注于风险，并在重构的过程中不断添加测试用例。

### Much More Than This

测试用例当中也会存在问题，需要不断地进行修改。

> When you get a bug report, start by writing a unit test that exposes the bug.

## Introducing the Catalog

### Format of the Refactorings

书中的重构由这些部分组成：

- 名字
- 草图
- 动机
- 机制
- 示例

## Reference

[Web Edition of this Book](https://informit.com)

[Bibliography](https://martinfowler.com/books/refactoring-bibliography.html)

other web data:

[Refactoring Website](https://refactoring.com/)

[martin fowler's Website](https://martinfowler.com/)

Kent Beck. Extreme Programming Explained. Addison-Wesley, 2005. ISBN: 0321278658

Michael Feathers. Working Effectively with Legacy Code. Prentice Hall, 2004. ISBN: 0131177052

Neal Ford, Rebecca Parsons, and Patrick Kua. Building Evolutionary Architectures. O'Reilly, 2017. ISBN: 1491986360

William C. Wake. Refactoring Workbook. Addison-Wesley, 2003. ISBN: 0321109295

Joshua Kerievsky. Refactoring to Patterns. Addison-Wesley, 2004. ISBN: 0321213351
