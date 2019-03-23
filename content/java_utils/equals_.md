---
title: "==,equals"
layout: page
date: 2018-11-24 00:00
---

[TOC]

# 操作符`==`,对象的`equals`方法

1. 作用于基本数据类型的变量，则直接比较其存储的`值`是否相等

基本数据类型 | 包装类
-|-
byte   | Byte
short  | Short
int | Integer
long  |  Long
char   |     Char
float   |     Float
double  |   Double
boolean  | Boolean

2. 作用于引用类型的变量，则比较的是所指向的对象的地址

程序验证

```java
int a = 1;
int b = 1;
Integer ia = new Integer(a);
Integer ib = new Integer(b);
//  true
System.out.println(a == b);
// false
System.out.println(ia == ib);
```

```java
String s0 = "helloworld";
String s1 = "helloworld";
String s2 = "hello" + "world";
// true s0跟s1是指向同一个对象,字符串常量
System.out.println(s0==s1);
// true s2也指向同一字符串常量
System.out.println(s0==s2);
String s3 = new String(s0);
String s4 = new String(s0);
// false s3, s4是不同的对象，地址不同, 只是内容相同
System.out.println(s3==s4);
// true
System.out.println(s3.equals(s4));
```