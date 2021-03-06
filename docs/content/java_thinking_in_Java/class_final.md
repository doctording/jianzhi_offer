---
title: "《Java编程思想》第7章：复用类"
layout: page
date: 2018-12-12 00:00
---

[TOC]

Java中问题的解决是围绕`类`展开的

* 组合 `has-a`
* 继承(extends，super) `is-a`
* 代理

## protected 继承 与 权限

包，类，子类

```java
package com.test;

/**
 * @Author mubi
 * @Date 2019/2/11 6:53 PM
 */
public class Bowl {
    private int a;

    public Bowl(int _a) {
        a = _a;
    }

    protected void set(int _a){
        this.a = _a;
    }

    @Override
    public String toString() {
        return "Bowl{" +
                "a=" + a +
                '}';
    }
}
```

```java
package com.test;

/**
 * @Author mubi
 * @Date 2019/2/11 6:54 PM
 */
public class BowlSon extends Bowl{
    int b;

    public BowlSon(int _a, int _b) {
        super(_a);
        this.b = _b;
    }

    public void change(int _a, int _b){
        // 子类方法能够访问基类的set方法，因为set方法在子类中是protected
        set(_a);
        this.b = _b;
    }

    @Override
    public String toString() {
        return "BowlFa{" +
                "b=" + b +
                '}' + super.toString();
    }
}
```

```java
package com.other;

import com.test.Bowl;
import com.test.BowlSon;

/**
 * @Author mubi
 * @Date 2019/2/11 6:57 PM
 */
public class MainOther {
    public static void main(String[] args) throws Exception {
        Bowl b1 = new Bowl(1);
        BowlSon bowlSon = new BowlSon(1,2);
        bowlSon.change(3,4);
        System.out.println(b1);
        System.out.println(bowlSon);
    }
}
```

## 向上转型

如下：`Wind`继承`Instrument`,将`Wind`转换成`Instrument`引用的动作，称为**向上转型**； 同理：向下转型

```bash
Instrument
    ^
    |
  Wind
```

继承和组合的选择： 如果需要从新类到基类的向上转型，那么继承是必要的，否则需要考虑用继承还是用组合

## final（无法改变的）- 设计或效率

final 数据认识

```java

import java.util.Random;

class Value{
    int i;

    public Value(int i) {
        this.i = i;
    }
}

public class FinalData{
    private static Random rand = new Random(47);
    private String id;

    public FinalData(String id) {
        this.id = id;
    }
    // can be compile-time constants
    private final int valueOne = 9;
    private static final int VALUE_TWO = 99;
    // Typical public constant
    // final 说明是个常量， static 强调只有一份 （编译期常量）
    public static final int VALUE_THREE = 39;
    // can not be compile-time constants
    // 不能因为是final，就认为在编译时可以知道它的值； 在运行时使用随机生产的数值来初始化
    private final int i4 = rand.nextInt(20);
    // 装载时已经初始化了，而不是每次创建一个对象时都初始化
    static final int INT_5 = rand.nextInt(20);
    private Value v1 = new Value(11);
    private final Value v2 = new Value(22);
    private static final Value VAL_3 = new Value(33);
    // Arrays
    private final int[] a = {1,2,3,4,5};

    @Override
    public String toString() {
        return "id:" + id + " i4:" + i4 + " INT_5:" + INT_5;
    }

    public static void main(String[] args) throws Exception {
        FinalData fd1 = new FinalData("fd1");

//        fd1.valueOne++; // error: cannot change value
        fd1.v2.i ++; //Object is not constant
        fd1.v1 = new Value(9); // ok , not final
        for(int i=0;i<fd1.a.length;i++){
            fd1.a[i] ++; // Object is not constant
        }
//        fd1.v2 = new Value(0); //error, can not， 无法将v2再指向其它对象引用，v2是final类型的
//        fd1.VAL_3 = new Value(1); // change reference，error同上
//        fd1.a = new int[3]; // 数组也一样， error同上
        System.out.println(fd1);
        System.out.println("Creating new FinalData");
        FinalData fd2 = new FinalData("fd2");
        System.out.println(fd1);
        System.out.println(fd2);
    }
}
/* output
 id:fd1 i4:15 INT_5:18
 Creating new FinalData
 id:fd1 i4:15 INT_5:18
 id:fd2 i4:13 INT_5:18
 */
```

* `final` 和 `static final` 的区别

static属于类，不属于实例，静态区域

### final 参数

在参数列表中以声明的方式将参数指明为final, 这意味着你无法在方法中更改参数引用所指向的对象

```java
void with(final int a){
    a = 10; // illegal, a is final
}
```

### final 方法

* final 方法的使用的两个原因

1. 将方法锁定，以防止任何继承类修改它的含义
2. 效率：Java早期实现中，如果将一个方法指明为final, 就是同意编译器将针对该方法的所有调用都转为内嵌调用，以代码副本代替方法调用，可能消除方法调用的开销。如果一个方法很大，则程序代码就会膨胀，可能看不到内嵌带来的任何性能提高，因为，所带来的性能提高会话费于防范诶的时间量而被压缩。（最近的Java版本已经优化此过程）

private 由于无法使用，所以 private 加上 final 修饰词，并没有实际的意义

```java
class WithFinalMethod {
    final void f() {}
}
public class E21_FinalMethod extends WithFinalMethod {
    void f() {} // 报错,final方法无法override
    public static void main(String[] args) {}
}
```

### final 类

不允许继承，不能有子类

## 初始化及类的加载

* 加载类的动作仅发生一次

* 类的第一个实例的创建或者对static成员的访问都有可能引起加载

* 定义为static的东西，只会被初始化一次

```java
class LoadTest {
    // The static clause is executed
    // upon class loading:
    static {
        System.out.println("Loading LoadTest");
    }
    static void staticMember() {}
}

public class MainTest {
    public static void main(String args[]) {
        System.out.println("Calling static member");
        LoadTest.staticMember();
        System.out.println("Creating an object");
        new LoadTest();
    }
}
/*output

Calling static member
Loading LoadTest
Creating an object
 */
```

巩固学习：[第5章，总结一个对象的创建过程](./05.md)

```java
class LoadTest {
    public LoadTest(){
        System.out.println("LoadTest constructor");
    }
    static {
        System.out.println("Loading LoadTest");
    }
    static void staticMember() {}
}

public class MainTest {
    public static void main(String args[]) {
        System.out.println("Calling static member");
        LoadTest.staticMember();
        System.out.println("Creating an object");
        new LoadTest();
        new LoadTest();
    }
}
/*output

Calling static member
Loading LoadTest
Creating an object
LoadTest constructor
LoadTest constructor
 */
```
