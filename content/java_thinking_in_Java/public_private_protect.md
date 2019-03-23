---
title: "《Java编程思想》第6章：访问权限控制"
layout: page
date: 2018-12-12 00:00
---

[TOC]

# 访问权限控制

## 访问权限修饰词

Java访问控制符的含义和使用情况(默认是default)

- | 类内部 | 本包 | 子类 | 外部包
- | -| - | - | -
public | ✓ | ✓ | ✓ | ✓
protect | ✓ | ✓ | ✓ | x
default | ✓ | ✓ | x | x
private | ✓ | x | x | x

* package

* public: 接口访问权限

* private: 你无法访问

* protect: 继承访问权限

## 接口和实现

访问权限的控制常被称为是具体实现的隐藏。把数据和方法包装进类中，以及具体实现的隐藏，常共同被称作是**封装**。其结果是一个同时带有特征和行为的数据类型。

1. 设定客户端程序员可以使用和不可以使用的界限
2. 接口和具体实现进行分离