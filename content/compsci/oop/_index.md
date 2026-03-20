---
title: 面向对象程序设计
date: 2026-03-19
type: docs
---
### References and Pointer

No references to references.\
No pointers to references `int&\*p`, but reference to pointer is ok `int\*&p`.\
No array of references.

| References                                                                   | Pointer                                     |
| ---------------------------------------------------------------------------- | ------------------------------------------- |
| can't be null                                                                | can be set to null                          |
| can't change to a new "address" location                                     | can change to point to a different address  |
| are dependent on an existing variable. <br>they are an alias for an variable | pointer is independent of existing objects. |

It's safe to apply delete to the null pointer (nothing happens).\
Don't mix-use new/delete and malloc/free.

`delete` 的时候如果忘了 `[]` 就只会析构第一个元素。

| new          | delete      |
| ------------ | ----------- |
| new int;     | delete p;   |
| new Stash;   | delete[] p; |
| new int[10]; |             |
### Const Qualifier

A const in C++ defaults to internal linkage.\
The compiler tries to avoid creating storage for a const,\
holds the value in its symbol table.\
extern forces storage to be allocated.\
const value can be exploited.

It's possible to use const for aggregates. but storage will be allocated. In these situations. const means "a piece of storage that cannot be changed." However, the value cannot be used at compile time because the compiler is not required to know the contents of the storage at compile time.

```C++
int * const p=a; // p  is const
const int * p=a; // *p is const
char* s="Hello, world"; // s is a pointer initialized to a string const
char s[]="Hello, world";// s is an array
```
can always treat a non-const value as const.\
cannot treat a constant object as non-constant without an explicit cast.
### Constructors Destructors

A default constructor is one that can be called with no arguments.\
The destructor is named after the name of the class with a leading tilde. The destructor never has any arguments.\
The only evidence for a destructor call is the closing brace of the scope that surrounds the object.

对于同一花括号内的类，析构函数的调用顺序与构造函数的调用顺序相反（栈）\
The compiler allocates all the storage for a scope at the opening brace of scope.\
可能会存在 `goto` 跳过构造函数但后来调用析构函数导致错误的问题

如果已经定义了构造函数，就不能使用聚合类进行构造\
If and only if there are no constructors for a class (struct or class), the compiler will automatically create one for you.

Initializer list: Order of initialization is order of declaration, not the order in the list. Destroyed in the reverse order.

Local variables are defined inside a method, have a scope limited to the method to which they belong.

`this` is a hidden parameter for all member functions, with the type of the struct.

declare member of functions const, programmer declares member functions to be safe.

```C++
void Date::set_day(int d){
	day=d; // Legal
}

int Date::get_day()const{
	day++; // Illegal
	set_day(12);// Illegal
	return day; // Legal
}
```

类中的常量只能通过 Initializer list 进行构造，不可在构造函数内部进行赋值

```C++
class HasArray{
	const int size;
	int array[size]; // Illegal
}
static const int size=100; // Legal
const int size=100; // Illegal
enum {size=1000}; // Legal
```
### Inline Functions

An inline function is expanded in place, like preprocessor macro in C, so the overhead of the function call is eliminated. 

Much safer than macro, it checks the types of the parameters and has no dangerous side effect.

The definition of an inline function should be put in a header file.

An inline function definition may not generate any code in  `.obj` file.
It is declaration rather than definition.

Any function you define inside a class declaration is automatically an inline.
### Inheritance Basics

All embedded objects must be initialized. The default constructor is called if you don't supply the arguments, and there is a default constructor.

If you redefine a member function in the derived class, all other overloaded functions in the base class are inaccessible.

not inherited: constructor, destructor, assignment operation, private data is hidden but still present.

|               | public    | protected | private |
| ------------- | --------- | --------- | ------- |
| **public**    | public    | protected | private |
| **protected** | protected | protected | private |
| **private**   | private   | private   | private |
### Friend Functions

friends to explicitly grant access to a function that isn't a member of structure.
The class itself controls which code has access to its members.

Can declare a global function as a friend, as well as a member function of another class, or even an entire class, as a friend.

先构造父类再构造子类，析构顺序与之相反。存储中先存父类再存子类的新内容
A是B的友元类，B不一定是A的友元类
### Virtual Functions

Upcasting is the act of converting from a derived reference or pointer to a base class reference or pointer.

由于生成了 virtual table ，实际上类的大小需要 +8 ，在头部位置

If you override an overloaded function, you should  override all of the variants.

Never redefine an inherited non-virtual function.
Never redefine an inherited parameter value.
### Abstract Classes

An abstract base class has pure virtual functions.
Abstract base classes cannot be instantiated.

```C++
virtual void render()=0; // 纯虚函数
```

C++ builds a copy ctor for you if you don't provide one, copies each member variable, copies each pointer, data may become shared.
### Operator Overloading

不允许重载的运算符：`.` `.*` （成员指针访问运算符） `::` `?:` `sizeof` `typeid` `static_cast` `dynamic_cast` `const_cast` `reinterpret_cast`

不能用 `friend` 重载的运算符：`=` `()` `[]` `->` `->*`

```C++
const Integer& operator++();   // prefix++
const Integer operator++(int); // postfix++
const Integer& operator--();   // prefix--
const Integer operator--(int); // postfix--
```

### Type Casting

构造函数前加 `explicit` 来防止隐式转换，强制显式构造

1. `static_cast<type>()` explicit type conversion instead of implicit type conversion.is not safe when it is used to cast object pointer (not check)
2. `dynamic_cast<type>()` checks whether a downcast of object pointer is safe. If not safe , will return a null pointer.
3. `const_cast<type>()` is used to modify the const or volatile property.
4. `reinterperet_cast<type>()` is used to convert pointers or reference into integer or backforth. Cannot be used for converting between non-pointer variables of the same type (int to int).

### Stream I/O

stream random access on file, but not on `std::cin/cout`

|                   | input         | output        | header        |
| ----------------- | ------------- | ------------- | ------------- |
| generic           | istream       | ostream       | \<iostream\>  |
| file              | ifstream      | ofstream      | \<fstream\>   |
| C string (legacy) | istrstream    | ostrstream    | \<strstream\> |
| C++ string        | istringstream | ostringstream | \<sstream\>   |

`cin` - standard input
`cout` - standard output
`cerr` - unbuffered error (debugging) output
`clog` - buffered error (debugging) output
### Templates

Template instantiation (实例化) generating a definition from a template class/function and template arguments.

A template function is an instantiation of a function template.
No conversion operations are applied.

overloading rules:
* Check first unique function match
* Then check for unique function template match
* Then implicit conversions on regular functions

```C++
template <class T>
void foo(){/* ... */}
foo<int>() // type T is int
foo<float>() // type T is float
```

class template
* Abstract operations from the types being operated upon
* Define potentially infinite set of classes
* Another step towards reuse
