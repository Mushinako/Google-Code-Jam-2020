# Parenting Partnering Returns: Analysis

## My Approach

It's much easier to allocate tasks when they're in chronological order. Therefore, the tasks are first sorted, with their original positions noted. Then, each task is sorted chronologically.

To assign tasks, the end times of each person's last tasks are kept track of. The start time of the new task is compared to the two people's end times.

* If the start time of the new task is no earlier than Cameron's end time, assign it to Cameron.
* If the start time of the new task is earlier than Cameron's end time but no earlier than Jamie's end time, assign it to Jamie.
* If the task fits neither's schedule, then a schedule cannot be reached.
