# -----> File: process_tasks.py <-----
def main(available_time, tasks, people, available_times):
    # Simulate task distribution logic
    task_list = tasks.split(", ")
    num_tasks = len(task_list)
    tasks_per_person = available_time // num_tasks if num_tasks > 0 else 0
    
    result = f"Each task will take approximately {tasks_per_person} hours. Assigned to: {people} with times: {available_times}."
    return result