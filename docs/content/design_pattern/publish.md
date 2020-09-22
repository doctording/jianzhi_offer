---
title: "发布订阅"
layout: page
date: 2019-03-20 00:00
---

[TOC]

# 发布订阅

![](../../content/design_pattern/imgs/publish.png)

发布/订阅者模式最大的特点就是实现了松耦合，也就是说你可以让发布者发布消息、订阅者接受消息，而不是寻找一种方式把两个分离的系统连接在一起。当然这种松耦合也是发布/订阅者模式最大的缺点，因为需要中间的代理，增加了系统的复杂度。而且发布者无法实时知道发布的消息是否被每个订阅者接收到了，增加了系统的不确定性。

![](../../content/design_pattern/imgs/cmp.webp)