# Software Requirements Specification / Design Document: GolfScore

**Company:** MSSE Software, Inc.  
**Revision:** 1.1  
**Author:** Neil Bitzengolfer (with all due respect to Edward Kit)  
**Date:** July 18, 2017  

---

## Table of Contents
1. Scope
   - 1.1 Objective
   - 1.2 Identification
   - 1.3 System Architecture
2. Functional Requirements
   - 2.1 Program Description
   - 2.2 Calling GolfScore
   - 2.3 Program Functionality
     - 2.3.1 Tournament Assumptions
     - 2.3.2 Scoring
   - 2.4 Data Input
     - 2.4.1 Course Records
     - 2.4.2 Delimiter Record
     - 2.4.3 Golfer Records
     - 2.4.4 Delimiter Record
   - 2.5 Data Output
     - 2.5.1 Tournament Ranking Report (`trank.rep`)
     - 2.5.2 Golfer Report (`golfer.rep`)
     - 2.5.3 Course Report (`course.rep`)
   - 2.6 Error Handling
     - 2.6.1 Input Parameter Errors
     - 2.6.2 Input Data Errors
     - 2.6.3 Errors on Output
3. Deliverables
4. Performance Requirements

---

## 1. Scope

### 1.1 Objective
This document specifies the functional requirements and high-level design for GolfScore Release 1.1. The purpose of the program is to process scores from a golf tournament and produce reports showing who won the tournament and how the golfers performed on each course played.

### 1.2 Identification
GolfScore Release 1.1. The program displays its title and revision number on screen at execution time.

### 1.3 System Architecture
Written in C or C++, running on PC Windows 2000 or later as a stand-alone command-line application (no GUI).

---

## 2. Functional Requirements

### 2.1 Program Description
GolfScore reads a formatted text input file containing course and golfer records, processes tournament scores, and generates up to 3 output text reports formatted for printing.

### 2.2 Calling GolfScore
Command Syntax:
```bash
golf <options> <filename> <output-directory>
```

**Options:**
- `-h`: Display help information on screen.
- `-c`: Generate Course Report (`course.rep`).
- `-t`: Generate Tournament Ranking Report (`trank.rep`).
- `-g`: Generate Golfer Report (`golfer.rep`).
- Options can be combined (e.g., `-cg` or `-ct`).

**Examples:**
- `golf -h` -> Display help
- `golf -ct c:\in.txt c:\golfout` -> Read `in.txt` and generate Course and Tournament Ranking reports in `c:\golfout`.

---

## 2.3 Program Functionality

### 2.3.1 Tournament Assumptions
- Number of golf courses: 1 to 5.
- Number of golfers: 2 to 12.
- Each course has 18 holes; Par for each hole is 3, 4, or 5 strokes.
- Each golfer plays each course once.

### 2.3.2 Scoring System

| Stroke Count vs Par | Score Earned |
| :--- | :---: |
| Over par | 0 |
| Par | 1 |
| 1 under par | 2 |
| 2 under par | 4 |
| 3 or more under par | 6 |

- Golfer stroke count = sum of strokes on 18 holes.
- Golfer score = sum of scores earned on 18 holes. Lower stroke count yields higher score.

---

## 2.4 Data Input

Formatted text file with records terminated by end-of-line:
1. **Course Records:** 1 record per course. Column 1: Blank; Cols 2-19: Course name; Col 20: 1-char course ID; Cols 21-38: Par for holes 1-18 (3, 4, or 5).
2. **Delimiter Record:** Col 1 Non-blank.
3. **Golfer Records:** 1 record per golfer per course. Col 1: Blank; Col 2: Course ID; Cols 3-9: Ignored; Cols 10-29: Golfer name; Col 30: Ignored; Cols 31-48: Stroke counts for 18 holes.
4. **Delimiter Record:** Col 1 Non-blank (ends input file).

---

## 2.5 Data Output

1. **Tournament Ranking Report (`trank.rep`):** Golfer name, score per course, total score, and final rank (1st, 2nd, etc.) in descending order of score. Alphabetical on ties.
2. **Golfer Report (`golfer.rep`):** Same as Tournament Ranking Report, but sorted alphabetically by last name.
3. **Course Report (`course.rep`):** Section for each course listing golfers, hole-by-hole stroke count, and total course score in descending order.

---

## 2.6 Error Handling

### 2.6.1 Input Parameter Errors
Invalid options, missing input file, or non-existent output directory stop execution with an explanatory error message. Additional arguments beyond output-directory are ignored.

### 2.6.2 Input Data Errors
- Non-numeric data where numbers are expected -> Stop with error message.
- Par values outside {3, 4, 5} -> Stop with error message.
- Duplicate golfer records for same course -> Ignore duplicates, display warning, continue.

### 2.6.3 Output Errors
If an output report file already exists, prompt user: `"File <file> already exists. Do you want to overwrite it? (Y/N)"`.

---

## 3. Deliverables
- `GolfScore` executable file.

---

## 4. Performance Requirements
Completes processing within one minute of execution.
