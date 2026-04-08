def filter_tasks_by_priority(tasks, priority):
    result = []
    for task in tasks:
        if task.get("priority", "").lower() == priority.lower():
            result.append(task)
    return result
