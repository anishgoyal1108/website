---
author: "Anish Goyal"
title: "ISA and MIPS"
description: "Instruction set architecture"
tags:
  - "notes"
  - "electrical-engineering"
  - "eeng-5342"
date: 2025-08-27T19:40:43
modified: 2025-10-08T14:52:50
readingtime: "7"
course: "EENG 5342"
course_slug: "eeng-5342"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 2
weight: 20
slug: "isa-and-mips"
links: []
sources:
  - "Course handout, MIPS reference sheet"
  - "Course slides, chapter 2"
generated: true
---

## ISA {#isa}
- Instruction set architecture
- Different CPUs have different ISAs, though they share many of the same paradigms
- Using the MIPS ISA for this course
	- Big Endian: MSB at the least address of a word

## Register Operations {#register-operations}
- Operations between two CPU registers that are stored in a destination register 
- MIPS has a 32x32-bit register file (32 registers with 32 bits each)
	- Since each register can store up to 32 bits, we designate 32 bits as the fundamental unit, or *WORD*, for this architecture
	- Nearly all MIPS data types have sizes of one or more words 
- Assembler names
	- `$t0, $t1, ..., $t9` reserved for temp values
	- `$s0, $s1, ..., $s7` for saved variables
- The primitive arithmetic operations (`add/sub/mult/div`) are register operations because they only use registers as operands

## Memory Operations {#memory-operations}
- Operations that move data between registers and memory locations
- Why RAM is needed
	- Data that is not immediately needed in a program can be stored in RAM to free a register
	- Data larger than a word can be stored in RAM rather than distributed across registers
		- Arrays, structs, dynamic data	
- Memory addresses identify a memory location corresponding to a single byte
	- *Word-alignment:* MIPS requires that data with a size of one word (or multiples of one word) be instantiated at addresses that are multiples of 4
- The use of memory operations introduces overhead
	- Registers have faster access time than RAM architecture-wise
	- Require additional instructions (`lw/sw`) to move data between registers and RAM 
	- The programmer should only store values in RAM when absolutely necessary

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="02.1">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 02.1</span>.</div></div>
<div class="callout-content">

Memory Storing/Loading into Register

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/01-isa-and-mips-2025-08-27-20-20-12.svg"><img src="/notes/excalidraw/01-isa-and-mips-2025-08-27-20-20-12.svg" alt="01 ISA and MIPS 2025-08-27 20.20.12" loading="lazy"></a></figure>

</div>
</div>

## Immediate Operations {#immediate-operations}
- Operations between a register and 16-bit immediate (constant) value that are stored in a register
- Faster than register operations since immediate is encoded within the instruction itself
	- This avoids the use of `lw` to load a value from memory into a register, or even the use of a register altogether
- The immediate is *sign-extended* to 32 bits so that the operation can be performed with a register
- There is no immediate `sub` instruction, but you can use negative constants
- `addi` using 0 effectively copies one register to another

<div class="callout theorem-callout theorem-callout-example theorem-callout-en theorem-callout-mathwiki" data-callout="example" data-theorem-index="02.2">
<div class="callout-title"><div class="callout-icon"><svg class="svg-inline--fa" viewBox="0 0 576 512"><use href="#cicon-fa-anchor"/></svg></div><div class="callout-title-inner"><span class="theorem-callout-main-title">Example 02.2</span>.</div></div>
<div class="callout-content">

Immediate Operand Subtraction

<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/01-isa-and-mips-2025-08-27-20-53-18.svg"><img src="/notes/excalidraw/01-isa-and-mips-2025-08-27-20-53-18.svg" alt="01 ISA and MIPS 2025-08-27 20.53.18" loading="lazy"></a></figure>

</div>
</div>

## Zero Constant Register {#zero-constant-register}
- `$zero` 
- Cannot be overwritten
- Can be used with `add` to copy registers
	- Same efficiency as using `addi` with `imm 0` to copy registers
	- It is best to remain consistent with the method you use for enhanced program readability
- Can be used to load a constant: `addi $reg1, $zero, imm`

## Signed Integers {#signed-integers}

### Two's Complement {#two-s-complement}
- Binary expansion of a number, but with the MSB negated
- If the MSB is zero, the number must be positive
	- Therefore, the Two's Complement of a positive number is equivalent to its unsigned representation
- Range is $[-2^{n-1}, 2^{n-1}-1]$
	- The additive inverse of $-2^{n-1}$ is out of range, so $-(-2^{n-1})$ cannot be performed
- Identities:
	- $x + \overline{x} = -1$
	- $\overline{x} + 1 = -x$
		- This is used to negate binary numbers

### Sign Extension {#sign-extension}
- Preserves the numeric value of $x$ but with more bits
- `addi` is the easiest way to do this, since it sign-extends any value to one word by default
- Can use `lb, lh` to load a byte/halfword at a memory location to a register
	- This effectively sign-extends the data to one word so it can be stored in the register
- `beq` and `bne` internally use sign extension to word-align 16-bit immediate offsets with the current instruction reference in the program counter (so that it can be added/subtracted)

## Representing Instructions {#representing-instructions}
- All instructions are binary machine code
- MIPS instructions are fixed-length words
	- There are various instruction formats that encode different information depending on the use case
- Register numbers
	- `$t0 - $t7`: 8-15 
	- `$t8 - $t9`: 24-25
	- `$s0 - $s7`: 16-23

### R-Format {#r-format}
- Generic format used by a lot of instructions
- op: opcode
- rs: first register number
- rt: second register number
- rd: destination register number
- shamt: shift amount
- funct: function code

<a class="zoom" href="/notes/img/r-format.png"><img src="/notes/img/r-format.png" alt="r format" loading="lazy"></a>

### I-Format {#i-format}
- Immediate arithmetic, load/store, and branching
- rt: second/destination register number (instruction-specific)
- constant/address: an offset for a branching instruction or constant for an immediate instruction
- Question: how does the assembler know whether it's in i-format or r-format based on shamt/funct alone?

## Logical Operations {#logical-operations}
- Useful for extracting/inserting groups of bits

<a class="zoom" href="/notes/img/logical-operations.png"><img src="/notes/img/logical-operations.png" alt="logical operations" loading="lazy"></a>

### Logical Shifts {#logical-shifts}
- `sll` multiplies by $2^n$ and `srl` divides by $2^n$

### AND {#and}
- Useful for bit masking

### OR {#or}
- Useful for setting some bits to 1, and leaving others unchanged

### NOR {#nor}
- Logical NOT if one register is `$zero`

## Conditional Branches {#conditional-branches}
- Branch to a label if a condition is true

## Basic Blocks {#basic-blocks}
- A sequence of instructions that:
	- Contains no branches (except at the end)
	- Contains no branch targets (except at the beginning)
- Compilers identify basic blocks for optimization

## Conditional Operations {#conditional-operations}
- Sets result to 1 if a condition is true and 0 otherwise
- There are signed and unsigned comparisons

## Procedure Calling {#procedure-calling}
1. Place parameters in registers
2. Transfer control to procedure
3. Acquire storage for proceduer
4. Perform procedure operations
5. Place result in register for caller
6. Return to call location

### Register Convention {#register-convention}
- `$a0 - $a3`: arguments (4-7)
- `$v0, $v1`: results (2-3)
- `$t0-$t9`: temporary registers to be overwritten by the procedure call
- `$s0-$s7`: must be saved and restored before and after procedure
	- This means the procedure must save all the values in the `s` registers on the stack, and restore them after finishing!
- `$gp`: global pointer for static data (28)
- `$sp`: stack pointer (29)
- `$fp`: frame pointer (30)
- `$ra`: return address (31)

### Calling a Procedure {#calling-a-procedure}
- Jump and link `jal ProcedureLabel`
	- Address of the following instruction is put into `$ra`
	- Jumps to the address in `ProcedureLabel`
- Procedure return: `jr $ra`
	- Copies `$ra` to program counter
	- Can also be used for switch cases or computed jumps 

## Branch Addressing {#branch-addressing}
- Branch instructions use i-format
	- Need to specify opcode, 2 registers, and target address
- PC-relative addressing
	- Target address = PC + 4 * offset 
	- The reason why the offset is multiplied by 4 is a very interesting optimization by the MIPS assembler that allows for a range of $2^{18}-1$ instead of $2^{16} - 1$ addresses. Essentially, since memory addresses are word-aligned, you know those addresses are divisible by 4, which means their values must end in 00 in their binary representation. This means that you only have to enter the first 16 bits of the address, even if your final address ends up being 18 bits

## Jump Addressing {#jump-addressing}
- Jump targets can be anywhere in the text section
	- The full address is encoded in the instruction because the first 4 bits of the next instruction address plus the extra 2-bit optimization equals 32 bits
		- Therefore, you only have to enter bits 5-30 in the address
		- Technically, this means you can only select from $2^{28}-1$ addresses surrounding the instruction pointer since you're hardcoding the first four bits, but this is equivalent to ~256 MiB, which is greater than the size of text section in the address space

<a class="zoom" href="/notes/img/jump-instruction-format.png"><img src="/notes/img/jump-instruction-format.png" alt="jump instruction format" loading="lazy"></a>

## References {#references}
- <span class="cite cite-ref">Course slides, chapter 2</span>
- <span class="cite cite-ref">Course handout, <em>MIPS reference sheet</em></span>
