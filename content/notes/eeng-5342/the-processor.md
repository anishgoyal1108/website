---
author: "Anish Goyal"
title: "The Processor"
description: "All instructions are stored in the memory"
tags:
  - "notes"
  - "electrical-engineering"
  - "eeng-5342"
date: 2025-10-22T18:57:53
modified: 2025-11-05T23:10:02
readingtime: "4"
course: "EENG 5342"
course_slug: "eeng-5342"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 4
weight: 40
slug: "the-processor"
links: []
sources:
  - "Course slides, chapter 4"
generated: true
---

## Instruction Execution {#instruction-execution}
- All instructions are stored in the memory
- The program counter points to instruction memory; it fetches an instruction, which is 4 bytes of machine code, and increments by 4
- The memory bus has three ports: address line (input), data line (input), and data line (output)
	- There is a select for Read (which is basically a load) at the top and a select for Write at the bottom (which is basically a store)
- All of the register numbers point to a register file, or the read registers
- Depending on the instruction format
	- Use ALU to calculate arithmetic result, memory address of load/store, or branch target address
	- Necessary loads and stores are performed to access data memory
	- PC is set to the target address or incremented by 4

## Datapath {#datapath}
- Elements that process data and addresses in the CPU
	- Consists of registers, ALUs, multiplexers, memory

### Instruction Fetch {#instruction-fetch}
<a class="zoom" href="/notes/img/instruction-fetch-datapath.png"><img src="/notes/img/instruction-fetch-datapath.png" alt="instruction fetch datapath" loading="lazy"></a>

### R-Formatting {#r-formatting}
- Read from two registers
- Perform an arithmetic/logical operation
- Write the result

<a class="zoom" href="/notes/img/r-formatting-datapath.png"><img src="/notes/img/r-formatting-datapath.png" alt="r formatting datapath" loading="lazy"></a>

### Load/Store {#load-store}
- Read from register
- Calculate address with 16-bit offset
	- Uses ALU and sign-extends to 32-bits
- Load: Reads memory and updates register
- Store: Write register value to memory

<a class="zoom" href="/notes/img/load-store-datapath.png"><img src="/notes/img/load-store-datapath.png" alt="load store datapath" loading="lazy"></a>

### Branching Instructions {#branching-instructions}
- Read from registers
- Subtract operands using ALU and check Zero flag
- Calculate target address
	- Sign-extend displacement
	- Shleft 2 (word alignment)
	- Add to PC + 4
		- Should've already been calculated by intruction fetcher

<a class="zoom" href="/notes/img/branch-instructions-datapath.png"><img src="/notes/img/branch-instructions-datapath.png" alt="branch instructions datapath" loading="lazy"></a>

### Composing Elements of Datapath {#composing-elements-of-datapath}
- First-cut datapath performs each instruction in one clock cycle
	- Each datapath element can only perform one function at a time
	- Therefore, need to separate instruction and data memory
- Use muxes where alternate data sources can be used for different instructions

### R-Type/Load/Store Datapath {#r-type-load-store-datapath}
<a class="zoom" href="/notes/img/r-type-load-store-dp.png"><img src="/notes/img/r-type-load-store-dp.png" alt="r-type load store dp" loading="lazy"></a>

### Full Datapath {#full-datapath}
<a class="zoom" href="/notes/img/full-dp.png"><img src="/notes/img/full-dp.png" alt="full dp" loading="lazy"></a>

## Controlling the ALU {#controlling-the-alu}
- ALU is used for
	- Load/Store: Function = add
	- Branch: Function = subtract
	- R-type: Function depends on funct field

<a class="zoom" href="/notes/img/alu-control-table.png"><img src="/notes/img/alu-control-table.png" alt="alu control table" loading="lazy"></a>

- There is a 2-bit ALUop that is derived from the opcode
	- This is achieved with combinational logic

## Main Control Unit {#main-control-unit}
- The control signals are derived from the instruction

<a class="zoom" href="/notes/img/main-control-unit-dp.png"><img src="/notes/img/main-control-unit-dp.png" alt="main control unit dp" loading="lazy"></a>

## Datapath With Control {#datapath-with-control}
<a class="zoom" href="/notes/img/dp-with-control.png"><img src="/notes/img/dp-with-control.png" alt="dp with control" loading="lazy"></a>

### Control Lines {#control-lines}
<a class="zoom" href="/notes/img/dp-control-lines.png"><img src="/notes/img/dp-control-lines.png" alt="dp control lines" loading="lazy"></a>

## Problems With Current Approach {#problems-with-current-approach}
- Problem: the longest instruction in the datapath determines the clock period
	- The critical path for the overall datapath is `lw`
		- IM -> REG -> ALU -> DM -> MUX -> REG
- It's not feasible to vary the period for different instructions
- We want the common case to be fast
- We can incorporate a design that expedites the execution time of the processor via pipelining

## Pipelining Analogy {#pipelining-analogy}
- Pipelined laundry: overlap the executions
	- Parallelism improves the overall performance
	- Shouldn't introduce any conflicts, as long as each roommate is in different stages!

### Pipelining in MIPS {#pipelining-in-mips}
- Five stages:
	1. Instruction fetch
	2. Instruction decode and register read
	3. Execute operation/calculate address
	4. Access memory operand
	5. Write back to register

## Hazards {#hazards}
- Situations that prevent starting the next instructions in the next cycle
- Types
	- Structure
		- When a required resource is busy
		- More than one instruction is trying to use the same component
			- Q: This shouldn't be the case for a pipeline, though... so isn't this a contradiction since we assume mutual exclusivity?
			- A: Unfortunately, it can still occur, even with distinct components. You could have a memory conflict in the IM/DM if the read/write bits are set at the same time
			- Ex: You shouldn't have an instruction writing to the IM/DM while there's another instruction fetching a memory instruction
			- This isn't really a huge issue on modern architectures, since modern systems *do* guarantee mutual exclusivity of r/w to instruction and data memory
	- Data (most common)
		- An instruction depends on the completion of data access by a previous instruction
		- Can be eliminated entirely if you have a good enough data path or architecture
	- Control hazard
		- Deciding on control action depending on previous instruction
		- Solution: something to do with half-cycles? Not really sure wasn't paying attention

## References {#references}
- <span class="cite cite-ref">Course slides, chapter 4</span>
