from models import Task

def clear_task():
	task_list = Task.select()
	for task in task_list:
		task.delete_instance()


clear_task()
