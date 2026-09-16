---
author: "Anish Goyal"
title: "CPU Scheduling"
description: "We want max CPU utilization when doing multiprogramming"
tags:
  - "notes"
  - "computer-science"
  - "operating-systems"
date: 2025-09-21T15:29:04
modified: 2025-11-29T19:22:49
readingtime: "8"
course: "Operating System Concepts Essentials (Silberschatz)"
course_slug: "operating-systems"
subject: "computer-science"
kind: "lecture"
ordinal: 6
weight: 60
slug: "cpu-scheduling"
links: []
sources:
  - "Course slides: CPU Scheduling"
  - "Practice 6 solutions"
  - "Silberschatz, Galvin & Gagne, Operating System Concepts Essentials"
generated: true
---

## Basic Concepts {#basic-concepts}
- We want max CPU utilization when doing multiprogramming
	- This is achieved via the CPU-I/O Burst Cycle: processes execute by alternating a cycle of CPU burst and I/O wait
- I/O wait is because peripheral devices have slower access time than the CPU
- The distribution of the CPU burst is important, since you don't want the cores to be too spread out (there will be too much overhead)

## CPU Scheduler {#cpu-scheduler}
- **Short-term scheduler**: select from processes in ready queue and allocate CPU to one
	- Queue is handled with several algorithms
- CPU scheduling decisions can occur only when a process is switching states:
	- Running -> Wait
	- Running -> Ready
	- Waiting -> Ready
	- Running -> Terminated
- Circumstances 1 and 4 is nonpreemptive/cooperative, since the process decides when it gives up the CPU
- Circumstances 2 and 3 are preemptive, since the OS is forcibly taking away the CPU from the process
- A ready program must run before it can wait (it has to be dispatched by the scheduler first)
- A waiting program must become ready before it can run (it has to wait for I/O or event completion first)
- For $n$ states, you have $n(n-1)$ possible edges

<a class="zoom" href="/notes/img/process-states.png"><img src="/notes/img/process-states.png" alt="process states" loading="lazy"></a>

## Dispatcher {#dispatcher}
- Component of the scheduler that switches the CPU from one process to another
	- Saves address space of process (suspend)
	- Switch to user mode
	- Jump to proper location in user program and resume that program
- **Dispatch latency:** time for dispatcher to stop a process and start another; this is pure overhead
- You don't want to dispatch processes too often; too frequent means the overhead of switching is not doing any useful work from any user POV, and too infrequent will cause programs to hang (usually its a few ms)

## Scheduling Criteria {#scheduling-criteria}
- **CPU utilization:** % of time CPU is busy; keep the CPU as busy as possible
- **Throughput:** number of processes completing execution per time unit
- **Turnaround time:** time for a process to fully execute, from instantiation to termination
- **Waiting time:** time a process spends in ready queue (not to be confused with the waiting state)
	- Total waiting time would be the sum of the I/O burst times
	- The waiting time for a particular process would be the sum of the waiting times for all the processes before that one
- **Response time:** time from when a request is submitted until the first response is produced (new -> ready and in queue -> running)
	- Includes the waiting time
	- The period that the process actually spends waiting to run (from launch to run)
- The goal with CPU scheduling algorithms is to max cpu utilization/throughput and min turnaround time/waiting time/response time

## Scheduling Algorithms {#scheduling-algorithms}
- A Gantt Chart is a diagram that puts processes in a block for their execution time
	- Generally, we assume that all the processes arrive at time 0
	- And all the process time blocks are contiguous in the Gantt chart, since we are assuming negligible context switching overhead

### First-Come-First Served {#first-come-first-served}
- Processes are scheduled in the order that they arrive
- When the shorter burst time processes go later than long burst process, the average waiting time is much higher due to the **Convoy effect**
	- This is undesirable since you don't want to schedule long process first

<a class="zoom" href="/notes/img/fcfs-scheduling.png"><img src="/notes/img/fcfs-scheduling.png" alt="fcfs scheduling" loading="lazy"></a>

### Shortest-Job-First {#shortest-job-first}
- Associate with each process the length of its next CPU burst, and schedule the process with the shortest CPU burst time first
- Optimal because is gives the minimum average waiting time for a given set of process
	- Difficulty: how to know the length of next CPU burst?
	- Maybe we can ask the user?

<a class="zoom" href="/notes/img/sjf-scheduling.png"><img src="/notes/img/sjf-scheduling.png" alt="sjf scheduling" loading="lazy"></a>

### Shortest-Remaining-Time-First (Preemptive SJF) {#shortest-remaining-time-first-preemptive-sjf}
- Still finding the process with the shortest burst time, but now you have to account for processes that are not arriving at the same time
	- Instead of comparing total burst time, we compute *remaining* burst time
- It's called "Preemptive SJF" because you're preemptively pausing and resuming the process via the kernel
- We assume the process' creation time is equal to its arrival time

<a class="zoom" href="/notes/img/preemptive-sjf-scheduling.png"><img src="/notes/img/preemptive-sjf-scheduling.png" alt="preemptive sjf scheduling" loading="lazy"></a>

### Priority Scheduling {#priority-scheduling}
- A priority number is associated with each process
	- Smallest integer is highest priority
- The CPU is allocated to the process with the highest priority
	- Preemptive approach: unfinished low priority processes may be preempted by newly arrived high priority processes
	- Nonpreemptive: just let the process finish first
- **Starvation problem:** Low priotiy processes may never execute
	- Solution: *Process aging*; increase the priority of waiting processes as time progresses

<a class="zoom" href="/notes/img/priority-scheduling.png"><img src="/notes/img/priority-scheduling.png" alt="priority scheduling" loading="lazy"></a>

### Round Robin {#round-robin}
- The waiting time for each process is *quantized* by the fundamental unit, a quantum, which has a fixed time length
- Each process gets one quantum of time of CPU burst
	- If the process has not finished execution within that time, it must wait $(n-1)q$ time units before it is scheduled again
- The timer will interrupt at the end of every quantum to schedule the next process
- Performance:
	- $q$ very large: essentially becomes FCFS or FIFO
	- $q$ very small: very inefficient, since the quantum time is small with regard to the context switch time
	- The best heuristics keep $q$ small but not too small
	- Typically higher turnaround time than SJF, but better response time overall

<a class="zoom" href="/notes/img/round-robin-scheduling.png"><img src="/notes/img/round-robin-scheduling.png" alt="round robin scheduling" loading="lazy"></a>

## Time Formulas {#time-formulas}
- Notation: $A_i$ arrival time, $C_i$ completion time, $B_i$ burst time, $S_i$ start time, $n$ total number of processes
- All times can be read directly from the Gantt chart

### Turnaround Time {#turnaround-time}
- Time from process arrival to completion
- Per process: $TAT_i = C_i - A_i$
	- If all processes arrive at $t = 0$, this simplifies to $TAT_i = C_i$
- Average turnaround time:

$$
\overline{TAT} = \frac{1}{n}\sum_{i=1}^{n} C_i - A_i
$$

### Waiting Time {#waiting-time}
- Total time spent in the ready queue (not running)
- Per process: $WT_i = TAT_i - B_i$
	- If the zeroth process finishes execution in a single burst, it has a waiting time of zero
	- This could apply to the other processes as well, but only if they begin execution at their arrival time
- Average waiting time:

$$
\overline{WT} = \frac{1}{n}\sum_{i=1}^{n} TAT_i - B_i
$$

### Response Time {#response-time}
- Time from arrival until the process first gets the CPU
- Per process: $RT_i = S_i - A_i$
	- For all processes arriving at $t = 0$, $RT_i = S_i$
- For nonpreemptive algorithms (such as FCFS, SJF, and Priority), the response time equals the waiting time, since the processes do not stop between execution once they have started
- Average response time:

$$
\overline{RT} = \frac{1}{n}\sum_{i=1}^{n} S_i - A_i
$$

## Multilevel Queue {#multilevel-queue}
- Ready queue is split into separate queues, each with its own scheduling policy
	- Foreground queue: interactive processes (use Round Robin)
	- Background queue: batch processes (use FCFS)
- Each process is permanently assigned to one queue
- Scheduling between queues:
	- Fixed priority scheduling: one queue always runs before the other (may cause starvation)
	- Time slicing: each queue gets a portion of CPU time (e.g. 80% to foreground, 20% to background)
- Advantage: separates short, interactive tasks from long batch tasks for better responsiveness
- Disadvantage: inflexible; once assigned, a process cannot move to another queue

### Multilevel Feedback Queue {#multilevel-feedback-queue}
- Processes can move between queues based on their behavior
	- For example, a CPU-bound process moves to a lower-priority queue
	- An I/O-bound or newly arriving process may move to a higher-priority queue
- Parameters of the scheduler:
	- Number of queues
	- Scheduling algorithm for each queue
	- Rules for entering and moving between queues
	- Upgrade policy: determines when to move a process to a higher queue
	- Demotion policy: determines when to move a process to a lower queue
- Aging is implemented by moving long-waiting processes up the queues
- Used by general-purpose OS kernels to balance throughput and responsiveness

## Multiple-Processor Scheduling {#multiple-processor-scheduling}
- Scheduling is more complex when multiple CPUs are available
- **Asymmetric multiprocessing:**
	- One processor handles all scheduling and system data structures
	- Simpler design but may cause a bottleneck
- **Symmetric multiprocessing (SMP):**
	- Each processor is self-scheduling
	- Either a common ready queue or a private queue per processor
	- Most modern OS use SMP
- **Processor affinity:**
	- Processes tend to run on the same CPU to maximize cache reuse
		- *Soft affinity:* OS tries to keep process on the same CPU
		- *Hard affinity:* process is bound to a specific CPU
	- Processor sets allow grouping CPUs for load distribution
- Load balancing is necessary to avoid idle processors while others are overloaded
- SMP improves throughput but introduces synchronization and data consistency challenges

## References {#references}
- <span class="cite cite-embed">Source: Silberschatz, Galvin &amp; Gagne, <em>Operating System Concepts Essentials</em>, p.&nbsp;291</span>
- <span class="cite cite-ref">Course slides: CPU Scheduling</span>
- <span class="cite cite-ref">Practice 6 solutions</span>
