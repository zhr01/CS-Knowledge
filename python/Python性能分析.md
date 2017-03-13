# Python性能分析 - timeit, profile

### timeit - 准确测量小段代码的执行时间

使用命令行界面：

```shell
$ python -m timeit '"-".join(str(n) for n in range(100))'
10000 loops, best of 3: 40.3 usec per loop
$ python -m timeit '"-".join([str(n) for n in range(100)])'
10000 loops, best of 3: 33.4 usec per loop
$ python -m timeit '"-".join(map(str, range(100)))'
10000 loops, best of 3: 25.2 usec per loop
```

在Python下导入模块调用：

```python
import timeit
res = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(res)
res = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
print(res)
res = timeit.timeit('"-".join(map(str, range(100)))', number=10000)
print(res)
```



### cProfile

 **cProfile**：基于lsprof的用C语言实现的扩展应用，运行开销比较合理，适合分析运行时间较长的程序，推荐使用这个模块；

 **profile**：纯Python实现的性能分析模块，接口和cProfile一致。但在分析程序时增加了很大的运行开销。不过，如果你想扩展profiler的功能，可以通过继承这个模块实现

 假设现在有这样一个Python函数，需要测试一下它的运行速度：

```python
def sum_num(max_num):
    total = 0
    for i in range(max_num):
        total += i
    return total
 
 
def test():
    total = 0
    for i in range(40000):
        total += i
 
    t1 = sum_num(100000)
    t2 = sum_num(400000)
 
    return total
 
if __name__ == "__main__":
    test()
```

使用cProfile进行性能分析，你可以在Python脚本中实现，也可以使用命令行执行。使用Python脚本的主函数代码如下：

```python
if __name__ == "__main__":
    import cProfile
 
    # 直接把分析结果打印到控制台
    cProfile.run("test()")
    # 把分析结果保存到文件中
    cProfile.run("test()", filename="result.out")
    # 增加排序方式
    cProfile.run("test()", filename="result.out", sort="cumulative")
```

使用命令行运行的方法基本一致，Bash代码如下:

```python
# 直接把分析结果打印到控制台
python -m cProfile test.py
# 把分析结果保存到文件中
python -m cProfile -o result.out test.py
# 增加排序方式
python -m cProfile -o result.out -s cumulative test.py
```

使用最后一种方式分析的运行结果如下：

```python
 8 function calls in 0.042 seconds
 
   Ordered by: cumulative time
 
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.042    0.042 test.py:5(<module>)
        1    0.002    0.002    0.042    0.042 test.py:12(test)
        2    0.035    0.018    0.039    0.020 test.py:5(sum_num)
        3    0.004    0.001    0.004    0.001 {range}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```

| ncalls                    | 函数的被调用次数                     |
| ------------------------- | ---------------------------- |
| tottime                   | 函数总计运行时间，除去函数中调用的函数运行时间      |
| percall                   | 函数运行一次的平均时间，等于tottime/ncalls |
| cumtime                   | 函数总计运行时间，含调用的函数运行时间          |
| percall                   | 函数运行一次的平均时间，等于cumtime/ncalls |
| filename:lineno(function) | 函数所在的文件名，函数的行号，函数名           |



### 分析工具pstats

使用cProfile分析的结果可以输出到指定的文件中，但是文件内容是以二进制的方式保存的，用文本编辑器打开时乱码。所以，Python提供了一个pstats模块，用来分析cProfile输出的文件内容。它支持多种形式的报表输出，是文本界面下一个较为实用的工具。



### 图形化工具

对于一些比较大的应用程序，如果能够将性能分析的结果以图形的方式呈现，将会非常实用和直观，常见的可视化工具有Gprof2Dot，visualpytune，KCacheGrind等

