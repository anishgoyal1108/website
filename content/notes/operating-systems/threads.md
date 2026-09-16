---
author: "Anish Goyal"
title: "Threads"
description: "Processes with multiple threads can perform different tasks simultaneously"
tags:
  - "notes"
  - "computer-science"
  - "operating-systems"
date: 2025-09-21T09:26:20
modified: 2025-09-21T15:25:27
readingtime: "9"
course: "Operating System Concepts Essentials (Silberschatz)"
course_slug: "operating-systems"
subject: "computer-science"
kind: "lecture"
ordinal: 4
weight: 40
slug: "threads"
links: []
sources:
  - "Course slides: Processes Threads"
  - "Practice 4 solutions"
  - "Silberschatz, Galvin & Gagne, Operating System Concepts Essentials"
generated: true
---

## Motivation {#motivation}
- Processes with multiple threads can perform different tasks simultaneously
	- This allows specialization of work in applications
	- There can be an "overarching" thread/process coordinating the other threads
	- Switching threads is quicker than switching between processes, since they share the same address space
- Used in web/RPC servers to address multiple client requests; previously, servers created one process per client request
	- Now, an overarching thread is used to listen for client requests and the server will create a separate thread to service each request
	- This allows the server to resume listening to requests and address ongoing requests at the same time
- Kernels are multithreaded, and each thread performs a specific task necessary for the system

## Multicore Programming {#multicore-programming}
- Multicore systems can execute application threads in parallel
- Parallelism vs Concurrency
	- Parallel computation: the CPU performs different tasks simultaneously
	- Concurrent system: the CPU supports different tasks making progress, but not necessarily simultaneously
	- Parallelism implies concurrency, but not the other way around!
		- Systems with only one CPU can provide the illusion of parallelism via rapid process switching; such systems are concurrent but not parallel

### Multicore Programming Challenges {#multicore-programming-challenges}
- When developing an application, the programmer must ask:
	- Which tasks can be performed independently of one another (and thus run in parallel)?
	- What is the hierarchy of task contributions for the application? 
		- For example, it is less than ideal to dedicate a core to a job if it has a minor contribution to the application
	- How will the data be accessed and manipulated (essentially "divided") among tasks running on separate cores?
		- If multiple tasks need access to the same data, the programmer must ensure those tasks are synchronized in execution so that each task does not overwrite any information that another task may need (or alternatively, the tasks are not writing to the same data simultaneously)

### Types of Parallelism {#types-of-parallelism}
- **Data parallelism:** distributing subsets of data across cores and performing the same operation on each core
- **Task parallelism**: distributing tasks (threads) across cores, each of which is performing a unique operation

## Multithreading Models {#multithreading-models}
- Threads support is provided at the user and kernel level
	- User threads: supported above the kernel layer and managed without kernel support
	- Kernel threads: managed directly by the kernel, used for syscalls

### Many-to-One Model {#many-to-one-model}
- Maps many user threads to one kernel thread
- Management is performed by the thread library in user space
- Disadvantages:
	- The entire process must wait if a thread makes a blocking syscall
	- Only one thread can access the kernel at a time, so they can't run in parallel

### One-to-One Model {#one-to-one-model}
- Maps each user thread to a kernel thread
- Parallelism and concurrency support
	- Although, the developer must not to create too many threads, since the system could spend more time managing the threads (context switches, memory, scheduling) than doing work
- Most modern OSes use this model 
	- However, they restrict the number of available threads due to the overhead of creating a kernel thread for every user thread
- Still has the thread-specific disadvantage of having to wait on kernel thread to perform syscall, but at least other user threads can continue running on the remaining kernel threads

### Many-to-Many Model {#many-to-many-model}
- User thread pool is multiplexed to a smaller or equal kernel thread pool
- The size of the kernel thread pool is fixed, while the application can create an arbitrarily large thread pool without incurring a proportional kernel overhead
- Parallelism and concurrency is fully supported
	- Additionally, you can oversubscribe user threads relative to kernel threads and let the thread library schedule them efficiently
- Still has the thread-specific disadvantage of having to wait on kernel thread to perform syscall, but at least other user threads can continue running on the remaining kernel threads
- **Two-level model:** two discrete sets of user-kernel thread pairings, one set is many-to-many and the other set is one-to-one

## Thread Libraries {#thread-libraries}
- **Thread library:** API for creating/managing threads
- Two ways to implement a thread library:
	1. All function calls, code, and data structures reside in user space, and there is no kernel support
	2. Implement a kernel-level library in which function calls cause syscalls
- Most common APIs
	- POSIX Pthreads
	- Windows
	- Java (cross-platform; implicitly uses PThreads or Windows)
- Global data is shared among all threads
	- In Java (which lacks global variables), you would have to declare a static variable outside the `Thread` class
- Strategies for creating threads:
	- Asynchronous threading
		- The parent resumes execution on child creation and they execute concurrently
		- The parent need not know when the child terminates
		- Useful when no data is shared/aggregated
	- Synchronous threading
		- Resume execution only when all children terminate; the children operate concurrently
		- Each child finishes its job and joins with the parent
		- Useful when there is significant data sharing/aggregation of data

### Java Threads {#java-threads}
- Two methods of instantiation
	1. Create a subclass of `Thread` and override the `run()` method
	2. Create a class that implements the `Runnable` interface below:

```java
public interface Runnable 
{ 
	public abstract void run(); 
}
```

- Threads are not created until the `start()` method is called
	- We never call `run()` directly
- The `start()` method performs two tasks:
	1. Allocates memory initializes new thread
	2. Calls `run()`

#### Examples of Instantiation {#examples-of-instantiation}
```java
// Method 1
class MyThread extends Thread {
	public void run() {
		// Code goes here
    }
}

// Method 2
class MyRunnable implements Runnable {
	public void run() {
	    // Code goes here
    }
}
```

## Implicit Threading {#implicit-threading}
- Tasking threading to the compiler and runtime libraries rather than the programmer

### Thread Pools {#thread-pools}
- **Thread Pools:** Create threads at process startup that sit in a pool and wait for a work assignment
	- Once a thread completes its assignment, it is placed back
- Benefits:
	- Allocating threads once at runtime is faster than creating them dynamically
	- Limits the number of threads that can exist (which is especially pertinent in the one-to-one case)
	- Programmers no longer have to worry about how to create and manage threads; they can focus on implementing the task to provide to the pool

## Threading Issues {#threading-issues}

### `fork()` And `exec()` Syscalls {#fork-and-exec-syscalls}
- If a thread calls `fork()`, does the entire process clone just that thread or all threads?
	- There are two implementations for each case
- If a thread calls `exec()`, it can only be applicable to the entire process just due to the nature of how `exec()` works
	- For this reason, it's slightly optimal to fork just the one thread instead of all threads if you plan on calling `exec()`

### Signal Handling {#signal-handling}
- A **signal** is used to notify a process that an event occurred
- Follows a pattern
	1. Signal is generated by the occurrence of the event
	2. The signal is delivered to the process
	3. The process handles the signal
- Synchronous signals originate within the process and vice-versa for asynchronous signals
- Every signal has a *default* signal handler ran by the kernel, which may be overridden by a *user-defined* signal handler
- For multithreaded programs, these options exist:
	1. Deliver the signal to the thread that is responsible
	2. Deliver the signal to every thread
	3. Deliver the signal to certain threads
	4. Assign a thread to receive all signals
- Synchronous signals must be delivered to the thread that caused the signal
- Deliver an asynchronous signal based on pid and signal number: `kill(pid_t pid, int signal)`
- Pthreads function to deliver an asynchronous signal to a thread: `pthread_kill(pthread_t tid, int signal)`
	- The signal will go to the first nonblocking thread
- In POSIX, an asynchronous signal sent with `kill()` or `pthread_kill()` is considered *delivered* once the kernel enqueues it to the target process or thread
	- There is no built-in acknowledgment that the handler actually ran; the sender only knows that the signal was queued successfully, not that it was handled
- Signal handlers are installed process-wide, but each thread maintains its own signal mask
	- This means some threads may handle certain signals while others won't, since the kernel only delivers one instance of a signal to a single eligible (unblocked) thread, which is then subsequently executed in that thread's context

### Thread Cancellation {#thread-cancellation}
- **Thread cancellation:** Terminating a thread before completion
	- The thread to be canceled is the *target thread*
	- Example use case: when you find the result from a distributed search 
- Occurs in two ways:
	- **Asynchronous cancellation:** one thread immediately terminates the target thread
		- Need to be careful, since it may not free a necessary system-wide resource
	- **Deferred cancellation:** the target thread periodically checks if it should terminate, allowing for controlled behavior before termination
		- The function that runs is called the *cleanup handler*

### Thread-Local Storage {#thread-local-storage}
- **Thread-local storage:** each thread needs its own copy of some data
	- Example use case: unique IDs for each transaction in a shopping application, which the corresponding thread holds (one thread per transaction)
- Similar to `static` data, but unique to each thread

### Scheduler Activations {#scheduler-activations}
- Some kind of coordination is needed to dynamically adjust the number of kernel threads
- Systems using the many-to-many/two-level models place a **lightweight process (LWP)** between user threads and kernel threads
	- The LWP is a "virtual processor" that the application can use to schedule user threads
- Each LWP is attached to a kernel thread, so you would need $n$ LWPs for $n$ concurrent syscalls

## Threads Programming Model {#threads-programming-model}
- **Pipeline Model:** Specialized threads form stages that depend on one another
- **Master-Slave Model:** Master thread does no work, it assigns work to slave threads and waits for them to finish
	- Possibly collects results returned from slaves
- **Equal-Worker Model:** All threads do the same type of task
	- Each pulls work from a shared pool
	- No fixed order or dependency
	- The focus is on dividing similar tasks evenly

## References {#references}
- <span class="cite cite-embed">Source: Silberschatz, Galvin &amp; Gagne, <em>Operating System Concepts Essentials</em>, p.&nbsp;185</span>

- <div class="transclusion missing"><span class="missing-media">(embedded note unavailable: 04 Threads)</span></div>

- <span class="cite cite-ref">Course slides: Processes Threads</span>
- <span class="cite cite-ref">Practice 4 solutions</span>
