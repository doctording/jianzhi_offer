---
title: "布隆过滤器"
layout: page
date: 2020-04-14 18:00
---

[TOC]

# 布隆过滤器

<a href="https://en.wikipedia.org/wiki/Bloom_filter" target="_blank">/wiki/Bloom_filter</a>

本质上布隆过滤器是一种数据结构，比较巧妙的概率型数据结构（probabilistic data structure），特点是高效地插入和查询，可以用来告诉你 “某样东西**一定不存在**或者**可能存在**”。

讲述布隆过滤器的原理之前，我们先思考一下，通常你判断某个元素是否存在用的是什么？通常想到 HashMap，确实可以将值映射到 HashMap 的 Key，然后可以在`O(1)`的时间复杂度内返回结果，效率奇高。但是 HashMap 的实现也有缺点，例如存储容量占比高，考虑到负载因子的存在，通常空间是不能被用满的，而一旦你的值很多例如上亿的时候，那 HashMap 占据的内存大小就变得很可观了。

## 算法过程

1. 首先需要k个hash函数，每个函数可以把key散列成为1个整数
2. 初始化时，需要一个长度为n比特的数组，每个比特位初始化为0
3. 某个key加入集合时，用k个hash函数计算出k个散列值，并把数组中对应的比特位置为1
4. 判断某个key是否在集合时，用k个hash函数计算出k个散列值，并查询数组中对应的比特位，如果所有的比特位都是1，认为在集合中。

优点：

1. 不需要存储key，节省空间

缺点：

1. 算法判断key在集合中时，有一定的概率key其实不在集合中
2. 无法删除
3. 随着数据的增加，误判率随之增加；只能判断数据是否一定不存在，而无法判断数据是否一定存在。

主要命令

```java
bf.add 添加元素
bf.exists 查询元素是否存在
bf.madd 一次添加多个元素
bf.mexists 一次查询多个元素是否存在
```
