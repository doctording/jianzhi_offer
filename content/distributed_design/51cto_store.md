---
title: "分布式存储系统基础"
layout: page
date: 2019-06-07 00:00
---

[TOC]

# 分布式存储系统基础

**来源：51CTO,分布式存储系统视频课程**

----

## 大数据对分布式存储对需求

问题引入：对 1PB 数据排序，我们需要怎么样的存储系统

1. 存储容量大
2. 高吞吐量
3. 提高数据可靠性（应对数据规模的增长）

4. 服务高可用（容错）

量化下：每年只有几个小时不可用

5. 高效运维

* 将日常硬件处理作为常态，做成流程化
* 对于监控，告警等机制也要有非常完善的支持

6. 低成本

* 保证数据安全，正确服务稳定的前提下，降低成本

## 小概率故障

大规模集群

1. 磁盘出错

2. 机器宕机

怎么把程序平滑的移到其它机器上

怎么把慢节点绕开

3. Raid卡故障

4. 网络故障

5. 电源故障

6. 数据错误

7. 系统错误

网络，内存分配出错

热点

8. 软件缺陷

设计缺陷

9. 误操作

## 常见分布式系统

1. HDFS

nameNode 单节点

2. Ceph

3. Pangu (阿里云)

Checksum
数据多备份
异常会否机制
回收站
数据聚簇
流控和优先级
热点和满盘规避
混合存储
安全访问认证
配额管理和审计
磁盘自动上下线
热升级
动态扩容/缩容
在线监控离线分析

4. 其它如（GPFS, Lustre MooseFS）

## 分布式系统设计要点

* 读写流程

慢节点，热节点
* Qos(服务质量)
* CheckSum(数据正确性)
* Replication
磁盘损坏，宕机，还能服务
* Rebalacne（平横）
* GC
* Erasure Coding(成本)

## 写入流程

### 链式写入流程

![](https://raw.githubusercontent.com/doctording/sword_at_offer/master/content/distributed/imgs/lian.png)

写入，某个节点有错误的情况

数据安全性/数据成功率

### 主从模式

![](https://raw.githubusercontent.com/doctording/sword_at_offer/master/content/distributed/imgs/master.png)

### 总结

数据写入方法 | 优点 | 不足
-|-|-
链式写入 | 每个节点的负载和流量比较均衡 | 链条过长，出现异常时诊断和修复过程比较复杂
主从写入 | 总路径较短，管理逻辑由主从节点负责 | 主节点有可能成为负载和流量瓶颈



异常处理方式| 优点 | 不足
-|-|-
重写修复 | 能最大程度保留之前写入的数据 | - 直接剔除异常节点会导致后续写入的replica数降低 - 如果补充新的replica进来，需要补齐之前写入的数据，给新的replica
Seal and New | 简单快速，可以绕过异常节点 | Chunk长度不固定，需要更多的meta管理

## 读取流程

![](https://raw.githubusercontent.com/doctording/sword_at_offer/master/content/distributed/imgs/read_error.png)

* Backup Read

![](https://raw.githubusercontent.com/doctording/sword_at_offer/master/content/distributed/imgs/read_2.png)

* 满节点规避

client从Master获取每个节点大概的返回时间

![](https://raw.githubusercontent.com/doctording/sword_at_offer/master/content/distributed/imgs/read_3.png)

### 总结

多个副本分布方式：

* 可读取任意的有效副本
* 副本出现异常时，尝试其它副本
* Backup Read可以减少读取延迟
* 选取最优副本访问

## Qos

用户分优先级，分组

IO量（IO量大的拒绝访问）

多个用户访问一个分布式文件系统能都占到IO带宽

## CheckSum

* 全链路CheckSum

* 数据： buffer length CRC

* 网络分包

* 数据和CRC是否存储在一起？验证效率和出错情况

## Replication

* 为防止机器顺坏或磁盘顺坏时，拷贝份数不够造成数据丢失

* 快速恢复

* 流量控制

## Rebalance（数据均衡）

* 充分利用多台机器的带宽

* 复制要有优先级

* 流量控制要严格

## GC

### 垃圾回收场景

* 数据被删除的时候

异步删除

* 数据写入失败，脏数据留在磁盘上

数据版本控制

* 宕机

## Erasure Coding（？）

存储效率和安全性

## 元数据管理的高可用

* 高可用

多个备份： 在故障时快速切换， 保证状态一致性

* 可扩展性

元数据容量可线性扩展

元数据的服务能力可线性扩展

### 高可用方案

* 主从模式

一主多从

数据一致性通过共享存储

* 分布式协议

Paxos/Raft协议

### HDFS NameNode (主从模式)

### Pangu Metadata Server

* 使用Paxos一致性协议，保证高可用和快速切换

* 不依赖外部贡献存储和互斥锁服务，独立自包含

### Ceph Metadata Server

* 自身具备共享存储能力

* 用心跳代替分布式锁

* 做到独立自包含

### Paxos 协议

### Raft协议

## 元数据管理的可扩展性

* HDFS NameNode

* Ceph Metadata Server

## 数据的混合存储

* 不存存储截介质的特性

- | 磁盘 | SSD | 内存
-|-|-|-
容量 | 1-4TB | 400-800GB | 24 -128GB
延迟 | 10ms | 50-75pm | 100nm
吞吐 | 100-200MB/s | 400MB/s | 20GB/s
成本 | 低 | 中 | 高

### RAMCloud内存存储