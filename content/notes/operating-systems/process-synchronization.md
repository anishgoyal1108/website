---
author: "Anish Goyal"
title: "Process Synchronization"
description: "Cooperating processes can"
tags:
  - "notes"
  - "computer-science"
  - "operating-systems"
date: 2025-09-21T15:28:24
modified: 2025-10-21T12:02:57
readingtime: "16"
course: "Operating System Concepts Essentials (Silberschatz)"
course_slug: "operating-systems"
subject: "computer-science"
kind: "lecture"
ordinal: 5
weight: 50
slug: "process-synchronization"
links: []
sources:
  - "Course slides: ProcessSynchronization"
  - "Practice 5 solutions"
  - "Silberschatz, Galvin & Gagne, Operating System Concepts Essentials"
generated: true
---

## Background {#background}
- Cooperating processes can
	- Share a logical address space (code and data) via threads
	- Share data via files/IPC
- The use of threads to share data for concurrently executing processes creates problems with data inconsistency, since different, asynchronous threads have r/w control over the same blocks of memory

### Bounded Buffer {#bounded-buffer}
- The original implementation of the bounded buffer shared memory algorithm discussed in chapter three has a pitfall
	- Since the buffer is a ring, and the full condition is `(in + 1) % BUFFER_SIZE == out` (so the current memory accessed would be the second-to-last in the buffer), then the last memory index is never used
	- Therefore, only `BUFFER_SIZE - 1` slots are used out of `BUFFER_SIZE`
- The solution: an extra shared variable `counter`
	- Incremented whenever a new item to the buffer is added vice-versa
- However, this implementation introduces a **race condition** between the producer and consumer
	- If they both read the same value from `counter`, then `counter` will equal whoever writes last
	- If one reads from `counter` after the other has already written to `counter`, then this will not be an issue
- To guard against race condition, you must ensure:
	- A thread reads a shared variable only after another thread has finished writing to it
	- A thread writes to a shared variable only after other threads have finished reading or modifying it

## The Critical-Section Problem {#the-critical-section-problem}
- Every process has a **critical section** of code in which the process is changing common variables, updating a table, writing a file, etc.
- The OS must ensure no two processes are executing in their critical sections concurrently---this is known as the "Critical-section problem"
	- The solution: design a shared protocol that processes use to cooperate with one another
	- Each process must request permission to enter its own critical section
		- The section of code to implement this request is called the **entry section**; this will cause the process to wait for selection
	- The critical section may have an **exit section** after it is finished executing (so that the program knows how to handle the exiting of the critical section)
	- Everything else is basically the **remainder section**
- Solutions to the critical-section problem must satisfy the following:
	1. *Mutual exclusion:* No processes can be in their critical section simultaneously
	2. *Progress:* Only processes that are not in their remainder sections (*i.e.,* in their critical/entry/exit sections) may decide which processes can enter their critical sections. This decision cannot pend indefinitely.
		- Q: Why would we want to discriminate between processes that are in the critical/entry/exit sections and ones that are in the remainder section?
		- A: Since processes in the remainder section are not competing for the critical section, including them in the decision could potentially introduce overhead by blocking processes that are pending. In other words, we only want *active contenders* to decide on who gets to participate next. Furthermore, it just wouldn't make sense for regularly executing processes to dictate how other processes should be ran, since all processes in the remainder processes are expected to just focus on their own operation, and this could also introduce some cybersecurity problems
		- Q: What about the edge case where all the processes are in their remainder sections, and a process makes a request to enter the critical section?
		- A: That means there is no processes that are currently trying to enter. Therefore, there will be no contention and the process will be allowed to enter the critical section
	3. *Bounded waiting:* There is a finite bound on the number of times other processes may enter their critical sections before a process's request to enter its critical section is granted
		- In practice, this is known as *process starvation.* The algorithm still enforces mutual exclusion, but some processes might never get a turn, even though they keep waiting. 
		- In a certain sense, the solution could still be "bounded," but the bound is so large that this requirement is effectively not met

### Kernel Preemption {#kernel-preemption}
- Nonpreemptive kernels allow kernel-mode processes to run until they voluntarily close, block, or exit kernel mode
	- "Block" means waiting for some event to occur
- Preemptive kernels allow the preemption of a kernel-mode process
	- Trade-off: hard to design for SMP architectures, since you can have two kernel-mode processes on two different architectures (need to account for race conditions)
	- Can be more responsive, since there's less risk that a kernel-mode process will hang before relinquishing the CPU
	- More suitable for real-time programming, since any real-time process can preempt a kernel process

## Peterson's Solution {#peterson-s-solution}
* Two-process algorithm for mutual exclusion using `flag[2]` and `turn` to coordinate entry into the critical section

* Satisfies mutual exclusion by allowing at most one process in the critical section when the other’s flag and the `turn` selection disagree in the waiting loop

* Provides progress because selection depends only on the two contenders and the `turn` value so if one is not interested the other proceeds

* Bounded waiting holds because `turn` alternates preference after a contender leaves so a process is not postponed indefinitely

* Not safe on modern hardware without proper memory ordering because compilers and CPUs reorder reads and writes unless guarded by atomic operations or memory fences

## Synchronization Hardware {#synchronization-hardware}

* Disabling interrupts is a primitive used in early uniprocessors to make a critical sequence atomic but it fails on multiprocessors and delays timekeeping and device handling

* Hardware supplies atomic read–modify–write instructions like Test-and-Set or Compare-and-Swap to build higher level locks and semaphores safely in presence of preemption and concurrency

* Busy waiting appears when a thread spins on a condition using such primitives which wastes CPU on single cores yet can be acceptable for short holds on multicore systems

* Atomicity of wait and signal is mandatory because if either operation interleaves mid update mutual exclusion can be violated and invariants on semaphore counts can break

* System libraries expose these hardware primitives via OS constructs like spinlocks mutex locks and condition variables on Windows Linux and Solaris to control shared data safely

## Mutex Locks {#mutex-locks}

* A mutex provides mutual exclusion for one holder at a time and is the simplest lock to protect a critical section

* Java exposes implicit locking with `synchronized` on methods or blocks and explicit locks via `java.util.concurrent.locks.Lock` and `ReentrantLock` for structured acquire and release

* Correct usage pattern is acquire the lock execute the critical section then release the lock and never block or return while holding the lock to avoid stalls

* Deadlock can occur if multiple locks are acquired in inconsistent orders by different threads which creates a circular wait among mutexes as demonstrated in textbook code

* A common prevention rule is a global lock ordering or try lock with backoff to break cycles so threads never wait in a cycle on mutex resources

## Semaphores {#semaphores}

* A semaphore maintains a nonnegative integer used for signaling among threads using two atomic operations wait P and signal V only accessible through these primitives

* Counting semaphores track availability of multiple instances while binary semaphores act like a mutex to allow at most one holder in a critical section

* `wait` decrements the value and blocks when the value becomes negative while `signal` increments and wakes a blocked waiter when the value is now nonpositive

* Busy waiting is not required because blocked waiters sleep on a queue and are awakened by signal which prevents spinning and reduces CPU waste

* In Java use `java.util.concurrent.Semaphore` with `acquire` and `release` to implement counting or binary control of access to finite resources with fairness when configured

### Semaphores, Usage {#semaphores-usage}

* Use a counting semaphore to represent a pool like N buffer slots or N connections with `empty` initialized to N and `full` to 0 to synchronize producers and consumers

* Use a binary semaphore or mutex to provide mutual exclusion around the buffer or shared state to serialize updates in the critical region

* Order operations to prevent races for producer `wait(empty)` then `wait(mutex)` then add item then `signal(mutex)` then `signal(full)` matching consumer’s inverse order

* Prefer blocking semaphores over spin based waiting for long or unpredictable waits to avoid CPU waste on single core systems as taught in the chapter summary

* Ensure `wait` and `signal` are atomic in implementation because non atomic updates can break mutual exclusion and cause lost wakeups as noted in the exercises

### Semaphores, Implementation {#semaphores-implementation}

* Kernel or runtime maintains a count and a FIFO or priority queue of blocked threads plus atomic code paths for `wait` and `signal` to update count and queue state

* `wait` performs an atomic decrement then blocks and enqueues if count is now negative which defers CPU to other runnable threads without busy waiting

* `signal` performs an atomic increment then dequeues and wakes one blocked thread if the new count is less than or equal to zero to hand off the resource

* Binary semaphore values are constrained to 0 or 1 while counting semaphores track general availability so choice depends on whether you serialize or meter access

* Java maps P and V to `acquire` and `release` and supports permits to initialize N so code aligns with textbook pseudo code and bounded buffer examples

### Semaphores, Deadlocks and Starvation {#semaphores-deadlocks-and-starvation}

* Deadlock is possible if threads hold one semaphore and wait for another while a cycle of waits exists across threads which satisfies all Coffman conditions

* Starvation can occur if semaphore `signal` always wakes the same class of waiters like readers over writers or if scheduling never runs a particular waiting thread

* Avoid starvation by using fair semaphores or by layering admission policies like FIFO queues or reader writer preference rules where fairness is required

* Prevent deadlock with lock ordering or by never waiting while holding unrelated resources so hold and wait is eliminated at design time

* Timeouts and try acquire with backoff reduce indefinite waiting and allow recovery strategies when contention patterns lead to cyclic waits

## The Classic Problems of Synchronization {#the-classic-problems-of-synchronization}

### Bounded Buffer Problem {#bounded-buffer-problem}

* Two processes producer and consumer share N single item buffers with semaphores `mutex` `empty` and `full` controlling access and counts

* Producer code calls `wait(empty)` then `wait(mutex)` inserts the item then `signal(mutex)` and `signal(full)` to publish availability

* Consumer code calls `wait(full)` then `wait(mutex)` removes the item then `signal(mutex)` and `signal(empty)` then consumes outside the critical section

* The `mutex` protects buffer indices and counters while `empty` and `full` enforce the invariant that the number of items stays within 0 to N inclusive

* Incorrect ordering of waits causes deadlock while omitting `mutex` causes race conditions on shared indices and counters as shown in lecture examples

### Readers-Writers Problem {#readers-writers-problem}

* Readers may share access but writers require exclusive access to avoid inconsistent updates of the shared structure

* A common semaphore solution uses `rw_mutex` to exclude writers and a `mutex` to protect `read_count` which tracks active readers

* The first reader acquires `rw_mutex` and the last reader releases `rw_mutex` so writers gain exclusive access only when no readers are inside

* Reader writer locks generalize this with explicit read and write modes allowing many readers or one writer and can reduce contention when readers dominate

* Starvation policies vary first readers writers favors readers or writers and fair versions alternate to bound waiting for both classes

### Dining Philosophers Problem {#dining-philosophers-problem}

* Five philosophers alternate between thinking and eating where eating requires two adjacent chopsticks modeled as shared resources

* A naive solution uses one semaphore per chopstick but can deadlock if each philosopher picks up the left then waits forever on the right

* Deadlock prevention options include allowing at most four to sit at once or forcing one philosopher to pick up in opposite order to break circular wait

* Starvation must be considered because a philosopher could be perpetually bypassed so fair resource allocation or monitors with condition variables are used

* Monitor based solutions serialize entry and use conditions for picking up and putting down chopsticks which simplifies correctness reasoning

## Monitors {#monitors}

### Monitor Usage {#monitor-usage}

* A monitor encapsulates shared state procedures and condition variables so only one thread is active inside at a time which provides mutual exclusion by design

* Condition variables support `wait` and `signal` allowing a thread to sleep until a predicate holds and to release the monitor during wait then reenter when signaled

* Monitors eliminate manual pairing of semaphore operations and localize synchronization to the abstract data type methods making invariants easier to enforce

* Languages or libraries implement monitors via `synchronized` blocks with object intrinsic conditions or with explicit locks paired with condition objects

* Choice between Hoare or Mesa semantics changes whether a signal hands off immediately or merely wakes a waiter which affects where to recheck predicates

### Dining-Philosophers Solution Using Monitors {#dining-philosophers-solution-using-monitors}

* The monitor holds philosopher states and a condition per philosopher to test and signal when neighbors are not eating consistent with textbook guidance

* `pickup(i)` waits while either neighbor is eating then marks `i` as eating and `putdown(i)` marks thinking and signals neighbors to re test their conditions

* Monitor mutual exclusion prevents races on state arrays so only one thread computes eligibility at a time ensuring correct transitions

* This approach avoids deadlock because at least one eligible philosopher proceeds when conditions allow and prevents livelock by decisive signaling order

* Starvation is avoided by signaling neighbors on putdown and by testing eligibility consistently so any waiting philosopher eventually eats

### Implementing Monitors Using Semaphores {#implementing-monitors-using-semaphores}

* A monitor can be built from a mutex semaphore to protect entry and a semaphore per condition variable to block and wake waiters as in classical constructions

* `wait` on a condition releases the monitor lock then blocks on the condition semaphore and reacquires the lock upon wakeup before returning to the caller

* `signal` increments the condition semaphore and may transfer control to a waiting thread depending on semantics which requires a queue to retain order

* Careful sequencing is required to avoid both lost wakeups and races between releasers and acquirers when switching ownership on signal

* This mapping shows monitors are higher level abstractions over semaphores which reduces error surface by encoding patterns correctly

### Resuming Processes Within a Monitor {#resuming-processes-within-a-monitor}

* Under Hoare semantics the signaled thread runs immediately while the signaller waits which simplifies reasoning but needs an extra queue for signallers

* Under Mesa semantics `signal` only makes the waiter ready so it must retest the predicate on wake which is the model used by Java conditions

* Spurious wakeups and scheduler reorderings require always checking the condition in a loop around `wait` to ensure safety on resume

* Fairness demands policies on which waiting condition to signal first such as FIFO or priority to prevent starvation in heavy contention cases

* Correct resumption is verified by re establishing monitor invariants after each state change before leaving or before signaling a waiting condition

## Deadlocks {#deadlocks}

### System Model {#system-model}

* Processes compete for instances of resource types and request hold and release resources according to an allocation discipline managed by the OS

* A directed resource allocation graph models processes and resource types with request edges from process to resource and assignment edges back to the process

* A deadlock state occurs when processes wait indefinitely for events that only the waiting processes can cause which halts part of the system’s progress

* Multiple instances per resource type complicate detection because cycles can exist without deadlock when an external release can satisfy a pending request

* The model underlies prevention avoidance and detection methods used to manage deadlocks across OS resources and in user level locking libraries

### Deadlock Characterization {#deadlock-characterization}

* Four necessary Coffman conditions are mutual exclusion hold and wait no preemption and circular wait and all must hold for a deadlock to arise

* Circular wait implies hold and wait so the conditions are not entirely independent but the set remains necessary for characterization and prevention design

* Resource allocation graphs help reason about existence of cycles and whether they imply deadlock depending on resource multiplicity and pending releases

* Violating any one of the four conditions through policy prevents deadlock by construction which guides safe lock acquisition and resource management

* Example mutex order inversion across two threads demonstrates practical circular wait using ordinary locks in concurrent programs

### Resource-Allocation Graph {#resource-allocation-graph}

* Vertices partition into processes P1 to Pn and resource types R1 to Rm with edges representing requests and assignments which encode current wait relations

* A cycle in a single instance system implies deadlock while in multiple instance systems a cycle may or may not be deadlock depending on availability and releases

* Analysis includes checking whether some process can finish by receiving required instances which breaks cycles by freeing other resources for neighbors

* The graph is a teaching tool and a basis for algorithms though production OS often rely on simpler locking disciplines and application level protocols

* Graph examples show how one external release can let another acquire and proceed which dissolves apparent cycles that are not deadlocked

### Methods for Handling Deadlocks {#methods-for-handling-deadlocks}

* Prevention constrains requests so that at least one Coffman condition never holds such as enforcing a strict lock ordering to break circular wait

* Avoidance requires advance knowledge of maximum demands and uses safe state checks like Bankers style decisions before granting each request

* Detection and recovery allow deadlocks to occur then run algorithms to find cycles and preempt or abort processes to break the deadlock and resume service

* Many OS ignore deadlocks across general resources and push correctness to applications while providing primitives to build safe policies

* Practical recovery options include terminating one or more participants or rolling back to a checkpoint and reclaiming resources to restore a safe state

---

## Practical Checklist for Your Code {#practical-checklist-for-your-code}

* Use `synchronized` or `ReentrantLock` to guard every shared mutable variable that is read by one thread and written by another or written by two threads

* Prefer lock ordering or a single lock per structure to avoid circular wait and audit all nested acquisitions to match the global order every time

* Use `Semaphore` to model finite resources or producer consumer buffers with explicit `empty` and `full` counts matching textbook patterns

* Choose monitor style with conditions to replace ad hoc flag polling and always recheck predicates after wakeup to handle Mesa style semantics safely

* When in doubt write a resource graph of your locks and semaphores to see possible cycles and restructure to remove any circular acquisition paths

## References {#references}
- <span class="cite cite-embed">Source: Silberschatz, Galvin &amp; Gagne, <em>Operating System Concepts Essentials</em>, p.&nbsp;225</span>
- <span class="cite cite-ref">Course slides: ProcessSynchronization</span>
- <span class="cite cite-ref">Practice 5 solutions</span>
