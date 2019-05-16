3

Thread communication can be as simple as sharing a variable or object bearing in mind that synchronization is required. Interprocess communication is a bit harder and much slower since processes are separated and cannot intervene. For this type of communication you can use named pipes, memory mapped files, msmq, TCP, WCF, file system and other.


什么是线程安全？ 如何保证线程安全？ 什么是锁？死锁？ synchronized的实现原理是什么？ 有了synchronized，还要volatile干什么？ synchronized的锁优化是怎么回事？（锁粗化？锁消除？自旋锁？偏向锁？轻量级锁？） 知道JMM吗？（原子性？可见性？有序性？） Java并发包了解吗？ 那什么是fail-fast？什么是fail-safe？
