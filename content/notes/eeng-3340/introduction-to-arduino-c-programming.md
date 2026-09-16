---
author: "Anish Goyal"
title: "Introduction to Arduino C Programming"
description: "Arduino C programs run continuously after executing in the main loop"
tags:
  - "notes"
  - "electrical-engineering"
  - "eeng-3340"
date: 2025-05-21T08:59:16
modified: 2025-05-24T23:31:19
readingtime: "3"
course: "EENG 3340"
course_slug: "eeng-3340"
subject: "electrical-engineering"
kind: "lecture"
ordinal: 1
weight: 10
slug: "introduction-to-arduino-c-programming"
links: []
sources: []
generated: true
---

## Program Structure {#program-structure}
- Arduino C programs run continuously after executing in the main loop
	- The only way to stop the program is by resetting the microcontroller or loading a new program
- 3 basic sections:
	- Variable Declaration
	- `setup()`
	- `loop()`

### Variable Declaration {#variable-declaration}
- These variables are global, since they're declared at the top of the C program (*i.e.,* outside of the `setup()` and `loop()` functions
- It's typically recommended to use local variables, since global variables can be modified anywhere in a program

### Setup {#setup}
- Declarations that are only executed at the beginning of the program
- Initialize I/O pins and ports
- Initialize serial communication channel speed

### Loop {#loop}
- Main program instructions
- Repeats continuously

### Boilerplate {#boilerplate}

```c
// declare global variables here

void setup()

{  
  // put your setup code here, to run once:  
}  
  
void loop() {  
  // put your main code here, to run repeatedly:  
}
```

## Program Development {#program-development}
- Several steps when developing a program:
	1. Creating/Editing the program
	2. Preprocess
	3. Compile
	4. Link
	5. Load
	6. Execute

### Creating the Program {#creating-the-program}
- Can use any text editor to create a C program, but Arduino IDE is the best
- Programs in the Arduino environment are called sketches with the extension `.ino`

### Preprocessing {#preprocessing}
- Automated syntax checking
- This occurs without even needing to compile (*i.e.,* colors in the text will change if an instruction is reserved or unrecognized)

<a class="zoom" href="/notes/img/preprocessing-arduino-c.png"><img src="/notes/img/preprocessing-arduino-c.png" alt="preprocessing arduino c" loading="lazy"></a>

### Compilation {#compilation}
- The program is translated into object code
- Syntax errors not found at the preprocessing stage will appear
- Any other errors will also appear

<a class="zoom" href="/notes/img/compilation-arduino-c.png"><img src="/notes/img/compilation-arduino-c.png" alt="compilation arduino c" loading="lazy"></a>

### Linking {#linking}
- The object code contains placeholders and offsets that need to be completed by the linker
- The linker uses the libraries referenced in the program to fill in these placeholders

<a class="zoom" href="/notes/img/importing-library-example.png"><img src="/notes/img/importing-library-example.png" alt="importing library example" loading="lazy"></a>

### Loading {#loading}
- The program needs to be loaded into memory before it can be executed

<a class="zoom" href="/notes/img/loading-program-arduino-ide.png"><img src="/notes/img/loading-program-arduino-ide.png" alt="loading program arduino ide" loading="lazy"></a>

- Ensure the correct board and serial port is selected in the Tools menu

<a class="zoom" href="/notes/img/serial-port-and-board-selection.png"><img src="/notes/img/serial-port-and-board-selection.png" alt="serial port and board selection" loading="lazy"></a>

- Programs are loaded in Arduino IDE using the Upload arrow
	- This will reset the Arduino and upload the code into the board's flash (non-volatile) memory

### Execution {#execution}
- The code starts running as soon as the program has been uploaded into the microcontroller

<a class="zoom" href="/notes/img/c-code-to-executable.png"><img src="/notes/img/c-code-to-executable.png" alt="c code to executable" loading="lazy"></a>

## Program Execution and Control {#program-execution-and-control}

### Program Sequencing {#program-sequencing}
- Instructions are always executed sequentially in the same order that they appear in the program, known as top-to-bottom execution
	- The exception to this is if a jump to another part of the program is explicitly defined

<a class="zoom" href="/notes/img/top-to-bottom-execution.png"><img src="/notes/img/top-to-bottom-execution.png" alt="top-to-bottom execution" loading="lazy"></a>

### Program Structure {#program-structure-1}

#### Jumping Structure {#jumping-structure}
- Branching allows decision-making in programs
- Too many branches makes debugging nontrivial

## References {#references}
- 
