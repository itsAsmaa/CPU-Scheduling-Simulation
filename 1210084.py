import numpy as np

# Define the process class
class Process:
    def __init__(self, Pid, ArrivalTime, BurstTime, ComesBackAfter, priority):
        # Initialize process attributes
        self.id = Pid
        self.ArrivalTime = ArrivalTime
        self.BurstTime = BurstTime
        self.ComesBackAfter = ComesBackAfter
        self.priority = priority
        self.RemainingTime = BurstTime
        self.ActualArrival = ArrivalTime
        self.inQueue = False  # Does the process exist in the ready queue or not
        self.Pair = []

    def AddPair(self, start, end):
        # Helper method to add start-end pairs to the process for Gantt chart
        self.Pair.append((start, end))

    def BackToDefault(self):
        # Helper method to reset process attributes to default values
        self.RemainingTime = self.BurstTime
        self.ActualArrival = self.ArrivalTime
        self.inQueue = False
        self.Pair = []


# Represent each process with its attributes
p1 = Process(1, 0, 10, 2, 3)
p2 = Process(2, 1, 8, 4, 2)
p3 = Process(3, 3, 14, 6, 3)
p4 = Process(4, 4, 7, 8, 1)
p5 = Process(5, 6, 5, 3, 0)
p6 = Process(6, 7, 4, 6, 1)
p7 = Process(7, 8, 6, 9, 2)

# List to hold all processes instances
AllProcesses = [p1, p2, p3, p4, p5, p6, p7]

totalnum = len(AllProcesses)

def calculate_average_waiting_time(GanttChart, AllProcesses):
    total_waiting_time = 0
    for process in AllProcesses:
        WaitingTime = 0
        inQueue = False
        for task in GanttChart:
            if task[0] == process.id:
                if not inQueue:
                    inQueue = True
                else:
                    WaitingTime = task[1] - process.ArrivalTime
        total_waiting_time += WaitingTime
    return total_waiting_time / totalnum


def calculate_average_turnaround_time(GanttChart, AllProcesses):
    total_turnaround_time = 0
    for process in AllProcesses:
        turnaround_time = 0
        for task in GanttChart:
            if task[0] == process.id:
                turnaround_time = task[2] - process.ArrivalTime
        total_turnaround_time += turnaround_time
    return total_turnaround_time / totalnum


# FCFS implementation
def FCFS():
    # Initialize needed variables
    current_time = 0
    ready_queue = []
    waiting_queue = []
    GanttChart = []

    # Simulation loop, it runs until simulation time reaches 200 time units
    while current_time < 200:
        # Check for processes that are ready to be added to the ready queue
        for process in AllProcesses:
            if process.ArrivalTime <= current_time and not process.inQueue:
                ready_queue.append(process)
                process.inQueue = True

        # Sort processes in the ready queue according to their arrival times
        ready_queue.sort(key=lambda x: x.ActualArrival)

        # If there are processes in the ready queue
        if ready_queue:
            current_process = ready_queue.pop(0)
            # Get the process with the earliest arrival time from the queue
            start_time = max(current_time, current_process.ActualArrival)
            end_time = min(start_time + current_process.BurstTime, 200)
            # Calculate process start time
            current_process.AddPair(start_time, end_time - start_time)
            # Append the process to the gantt chart
            GanttChart.append((current_process.id, start_time, end_time))
            # Update the current time to be the previous process end time
            current_time = end_time
            current_process.ActualArrival = (
                current_time + current_process.ComesBackAfter
            )
            # Append the completed process to the waiting queue
            waiting_queue.append(current_process)

        for process in waiting_queue:
            # Check if the process in the waiting queue are ready to be added to the ready queue
            if current_time >= process.ActualArrival:
                ready_queue.append(process)
                waiting_queue.remove(process)

    # Print the Gantt Chart for FCFS algorithm
    print("FCFS Gantt Chart:")
    for task in GanttChart:
        print(f"p{task[0]}: {task[1]} -> {task[2]}")

    # Reset process data to default values
    for process in AllProcesses:
        process.BackToDefault()

    # Calculate and print average waiting time and average turnaround time
    AvgWaitingTime = calculate_average_waiting_time(GanttChart, AllProcesses)
    AvgTurnaroundTime = calculate_average_turnaround_time(GanttChart, AllProcesses)
    print(f"Average Waiting Time (FCFS): {AvgWaitingTime}")
    print(f"Average Turnaround Time (FCFS): {AvgTurnaroundTime}")

    print("\n*********************************************************************************************************")


# SJF implementation
def SJF():
    # Initialize needed variables
    current_time = 0
    ready_queue = []
    waiting_queue = []
    GanttChart = []

    # Do not exceed the 200 time units
    while current_time < 200:
        # Check for processes arriving at the current time and add them to the ready queue
        for process in AllProcesses:
            if process.ArrivalTime <= current_time and not process.inQueue:
                ready_queue.append(process)
                process.inQueue = True

        # Sort the ready queue based on burst time (shortest job first)
        ready_queue.sort(key=lambda x: x.BurstTime)

        # If there is a process in the ready queue
        if ready_queue:
            # Get the process with the shortest burst time from the ready queue
            current_process = ready_queue.pop(0)
            start_time = max(current_time, current_process.ActualArrival)
            end_time = min(start_time + current_process.BurstTime, 200)

            # Update the process details and Gantt chart
            current_process.AddPair(start_time, end_time - start_time)
            GanttChart.append((current_process.id, start_time, end_time))
            # The current time is the previous process end time
            current_time = end_time
            current_process.ActualArrival = (
                current_time + current_process.ComesBackAfter
            )
            # Append the completed process to the waiting queue
            waiting_queue.append(current_process)

        # Check for processes in the waiting queue that can move to the ready queue
        for process in waiting_queue:
            if current_time >= process.ActualArrival:
                ready_queue.append(process)
                waiting_queue.remove(process)

    # Display the Gantt chart for the SJF algorithm
    print("\nSJF Gantt Chart:")
    for task in GanttChart:
        print(f"p{task[0]}: {task[1]} -> {task[2]}")

    # Reset process data to default
    for process in AllProcesses:
        process.BackToDefault()

    # Calculate and print average waiting time and average turnaround time
    AvgWaitingTime = calculate_average_waiting_time(GanttChart, AllProcesses)
    AvgTurnaroundTime = calculate_average_turnaround_time(GanttChart, AllProcesses)
    print(f"Average Waiting Time (SJF): {AvgWaitingTime}")
    print(f"Average Turnaround Time (SJF): {AvgTurnaroundTime}")

    print("\n*********************************************************************************************************")


# SRTF implementation
def SRTF():
    # Initialize needed variables
    current_time = 0
    ready_queue = []
    waiting_queue = []
    GanttChart = []
    start_time = 0
    previous_process = None

    while current_time < 200:
        # Check for processes arriving at the current time and add them to the ready queue
        for process in AllProcesses:
            if process.ArrivalTime <= current_time and not process.inQueue:
                ready_queue.append(process)
                process.inQueue = True

        # Sort the ready queue based on remaining time (shortest remaining time first)
        ready_queue.sort(key=lambda x: x.RemainingTime)

        if ready_queue:
            # Get the process with the shortest remaining time from the ready queue
            current_process = ready_queue[0]

            # If there was a previous process and it's not the same as the current one, update its end time
            if previous_process and previous_process != current_process:
                end_time = current_time
                previous_process.AddPair(start_time, end_time - start_time)
                GanttChart.append((previous_process.id, start_time, end_time))
                start_time = max(current_time, current_process.ActualArrival)

            # Decrement the remaining time for the current process
            current_process.RemainingTime -= 1
            current_time += 1
            # Set the previous process to the current process
            previous_process = current_process

            if current_process.RemainingTime == 0:
                current_process.ActualArrival = (
                    current_time + current_process.ComesBackAfter
                )
                current_process.RemainingTime = current_process.BurstTime
                waiting_queue.append(current_process)
                ready_queue.remove(current_process)

        # Check for processes in the waiting queue that can move to the ready queue
        for process in waiting_queue:
            if current_time >= process.ActualArrival:
                ready_queue.append(process)
                waiting_queue.remove(process)

    # Display the Gantt chart for the SRTF algorithm
    print("\nSRTF Gantt Chart:")
    for task in GanttChart:
        print(f"p{task[0]}: {task[1]} - {task[2]}")

    # Reset process data to default for future simulations
    for process in AllProcesses:
        process.BackToDefault()

    # Calculate and print average waiting time and average turnaround time
    AvgWaitingTime = calculate_average_waiting_time(GanttChart, AllProcesses)
    AvgTurnaroundTime = calculate_average_turnaround_time(GanttChart, AllProcesses)
    print(f"Average Waiting Time (SRTF): {AvgWaitingTime}")
    print(f"Average Turnaround Time (SRTF): {AvgTurnaroundTime}")

    print("\n*********************************************************************************************************")


# Round Robin implementation
def RoundRobin():
    # Initialize needed variables
    current_time = 0
    ready_queue = []
    waiting_queue = []
    GanttChart = []
    qu = 5

    # Do not exceed the 200 time unit
    while current_time < 200:
        # Check for processes arriving at the current time and add them to the ready queue
        for process in AllProcesses:
            if process.ArrivalTime <= current_time and not process.inQueue:
                ready_queue.append(process)
                process.inQueue = True
        # Sort processes according to their actual arrival time
        ready_queue.sort(key=lambda x: x.ActualArrival)

        if ready_queue:
            # Get the process from the front of the ready queue
            current_process = ready_queue[0]
            ready_queue.remove(current_process)
            start_time = max(current_time, current_process.ActualArrival)
            end_time = min(
                start_time + qu, start_time + current_process.RemainingTime
            )
            current_process.RemainingTime -= end_time - start_time
            current_process.AddPair(start_time, end_time - start_time)
            GanttChart.append((current_process.id, start_time, end_time))
            current_time = end_time

            if current_process.RemainingTime == 0:
                current_process.ActualArrival = (
                    current_time + current_process.ComesBackAfter
                )
                current_process.RemainingTime = current_process.BurstTime
                waiting_queue.append(current_process)
            else:
                ready_queue.append(current_process)
                current_process.ActualArrival = current_time

        # Check for processes in the waiting queue that can move to the ready queue
        for process in waiting_queue:
            if current_time >= process.ActualArrival:
                ready_queue.append(process)
                waiting_queue.remove(process)

    # Display the Gantt chart for the Round Robin algorithm
    print("\nRR Gantt Chart:")
    for task in GanttChart:
        print(f"p{task[0]}: {task[1]} -> {task[2]}")

    # Reset process data to default
    for process in AllProcesses:
        process.BackToDefault()

    # Calculate and print average waiting time and average turnaround time
    AvgWaitingTime = calculate_average_waiting_time(GanttChart, AllProcesses)
    AvgTurnaroundTime = calculate_average_turnaround_time(GanttChart, AllProcesses)
    print(f"Average Waiting Time (Round Robin): {AvgWaitingTime}")
    print(f"Average Turnaround Time (Round Robin): {AvgTurnaroundTime}")

    print("\n*********************************************************************************************************")

# Preemptive Priority implementation
def PreemptivePriority():
    # Initialize needed variables
    current_time = 0
    ready_queue = []
    waiting_queue = []
    GanttChart = []

    while current_time < 200:
        # Check for processes arriving at the current time and add them to the ready queue
        for process in AllProcesses:
            if process.ArrivalTime <= current_time and not process.inQueue:
                ready_queue.append(process)
                process.inQueue = True
        ready_queue.sort(key=lambda x: (x.priority, x.ActualArrival))

        if ready_queue:
            # Get the process with the highest priority from the front of the ready queue
            current_process = ready_queue[0]
            ready_queue.remove(current_process)
            # Caclculate the start and time for the process
            start_time = max(current_time, current_process.ActualArrival)
            end_time = min(start_time + 1, start_time + current_process.RemainingTime)
            current_process.RemainingTime -= end_time - start_time
            current_process.AddPair(start_time, end_time - start_time)
            GanttChart.append((current_process.id, start_time, end_time))
            current_time = end_time

            if current_process.RemainingTime == 0:
                current_process.ActualArrival = (
                    current_time + current_process.ComesBackAfter
                )
                current_process.RemainingTime = current_process.BurstTime
                waiting_queue.append(current_process)
            else:
                ready_queue.append(current_process)
                current_process.ActualArrival = current_time

        # Check for processes in the waiting queue that can move to the ready queue
        for process in waiting_queue:
            if current_time >= process.ActualArrival:
                ready_queue.append(process)
                waiting_queue.remove(process)

    # Display the Gantt chart for the Preemptive Priority algorithm
    print("\nPreemptive Priority Gantt Chart:")
    for task in GanttChart:
        print(f"p{task[0]}: {task[1]} -> {task[2]}")


    # Reset process data to default
    for process in AllProcesses:
        process.BackToDefault()

    # Calculate and print average waiting time and average turnaround time
    AvgWaitingTime = calculate_average_waiting_time(GanttChart, AllProcesses)
    AvgTurnaroundTime = calculate_average_turnaround_time(GanttChart, AllProcesses)
    print(f"Average Waiting Time (Preemptive Priority): {AvgWaitingTime}")
    print(f"Average Turnaround Time (Preemptive Priority): {AvgTurnaroundTime}")



# Non-Preemptive Priority implementation
def NonPreemptivePriority():
    current_time = 0
    ready_queue = []
    waiting_queue = []
    GanttChart = []
    # Simulation loop, it runs until simulation time reaches 200 time units
    while current_time < 200:
        # Check for precosses that are ready to be added to the ready queue
        for process in AllProcesses:
            if process.ArrivalTime <= current_time and not process.inQueue:
                ready_queue.append(process)
                process.inQueue = True

        # Sort processes in the ready queue according to their arrival times
        ready_queue.sort(key=lambda x: (x.priority, x.ActualArrival))

        # If there are processes in the ready queue
        if ready_queue:
            current_process = ready_queue.pop(0)
            # Get the process with the earliest arrival time from the queue
            start_time = max(current_time, current_process.ActualArrival)
            end_time = min(start_time + current_process.BurstTime, 200)
            # Calculate process start time
            current_process.AddPair(start_time, end_time - start_time)
            # Append the process to the gantt chart
            GanttChart.append((current_process.id, start_time, end_time))
            # Update the current time to be the previous process end time
            current_time = end_time
            current_process.ActualArrival = (
                current_time + current_process.ComesBackAfter
            )
            # Append the completed process to the waiting queue
            waiting_queue.append(current_process)

        for process in waiting_queue:
            # Check if the process in the waiting queue are ready to be added to the ready queue
            if current_time >= process.ActualArrival:
                ready_queue.append(process)
                waiting_queue.remove(process)

    # Display the Gantt chart for the Non-Preemptive Priority algorithm
    print("\nNon-Preemptive Priority Gantt Chart:")


    
    for task in GanttChart:
        print(f"p{task[0]}: {task[1]} -> {task[2]}")
     

    # Reset process data to default
    for process in AllProcesses:
        process.BackToDefault()

    # Calculate and print average waiting time and average turnaround time
    AvgWaitingTime = calculate_average_waiting_time(GanttChart, AllProcesses)
    AvgTurnaroundTime = calculate_average_turnaround_time(GanttChart, AllProcesses)
    print(f"Average Waiting Time (Non-Preemptive Priority): {AvgWaitingTime}")
    print(f"Average Turnaround Time (Non-Preemptive Priority): {AvgTurnaroundTime}")



    print("\n*********************************************************************************************************")


# Simulate different scheduling algorithms
FCFS()
SJF()
SRTF()
RoundRobin()
PreemptivePriority()
NonPreemptivePriority()
