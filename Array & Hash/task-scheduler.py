class Solution:
    def leastInterval(self, tasks, N):
        task_counts = collections.Counter(tasks).values()
        max_task_counts = max(task_counts)
        num_max_task_counts = list(task_counts).count(max_task_counts)
        
        
        # figure the math trick out if necessary
        return max(len(tasks), (max_task_counts - 1) * (N + 1) + num_max_task_counts)
