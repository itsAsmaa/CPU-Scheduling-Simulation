# CPU Scheduling Simulation with Multiple Algorithms

## Overview

This project simulates CPU scheduling using different scheduling algorithms, including:
1. **First Come First Served (FCFS)**
2. **Shortest Job First (SJF)**
3. **Shortest Remaining Time First (SRTF)**
4. **Round Robin (RR)**
5. **Preemptive Priority Scheduling**
6. **Non-preemptive Priority Scheduling**

The goal is to simulate these algorithms, generate Gantt charts, and calculate the average waiting time and turnaround time for a given set of processes. The processes are initialized with attributes like arrival time, burst time, priority, and time to come back after completion.

## Requirements

- **Operating System**: Linux/Unix/MacOS or Windows with Python support.
- **Language**: Python (if you choose to rewrite this as a Python project) or any language that supports basic object-oriented programming.
- **Libraries**: 
  - `numpy`: For handling numerical computations (optional if using Python).
  
## Files Included

- **cpu_scheduling_simulation.py**: The main Python file containing the implementation of CPU scheduling algorithms, process classes, and the simulation.
- **README.md**: The documentation file.

## Process Representation

Each process is represented by an instance of the `Process` class, which contains the following attributes:
- **Pid**: Process ID
- **ArrivalTime**: Time when the process arrives.
- **BurstTime**: Time required by the process to complete execution.
- **ComesBackAfter**: Time after which the process comes back to the ready queue.
- **priority**: The priority level of the process.
- **RemainingTime**: Remaining execution time (used in SRTF).
- **inQueue**: Whether the process is in the ready queue or not.
- **Pair**: A list of tuples representing the process's start and end time for Gantt chart visualization.

## Scheduling Algorithms Implemented

### 1. **First Come First Served (FCFS)**
   - Processes are executed in the order they arrive.
   - Simple but may lead to high waiting times, especially for long burst times.

### 2. **Shortest Job First (SJF)**
   - The process with the shortest burst time is selected first for execution.
   - Non-preemptive; once a process starts, it runs to completion.

### 3. **Shortest Remaining Time First (SRTF)**
   - A preemptive version of SJF, where the process with the shortest remaining time is selected.
   - A process can be preempted if a new process with a shorter remaining time arrives.

### 4. **Round Robin (RR)**
   - Each process is assigned a fixed time quantum (e.g., 5 time units).
   - Processes are executed in a cyclic manner, with each process getting an equal chance to execute.

### 5. **Preemptive Priority Scheduling**
   - The process with the highest priority is selected to run next.
   - If a process has the same priority, it will be chosen based on arrival time.

### 6. **Non-preemptive Priority Scheduling**
   - Similar to preemptive priority scheduling but without preemption.
   - Once a process starts executing, it will complete before another process with a higher priority can preempt it.

## Features

- **Gantt Chart Visualization**: The program prints a Gantt chart for each scheduling algorithm.
- **Average Waiting Time**: The average waiting time across all processes is calculated for each algorithm.
- **Average Turnaround Time**: The average turnaround time (completion time minus arrival time) across all processes is calculated for each algorithm.


