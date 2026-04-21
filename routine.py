import json
import schedule
import time

class DailyRoutineManager:
    def __init__(self):
        self.schedule = {}

    def add_task(self, task_name, task_time):
        self.schedule[task_name] = task_time
        schedule.every().day.at(task_time).do(self.reminder, task_name)
        print(f"Task '{task_name}' added to schedule at {task_time}.")

    def reminder(self, task_name):
        print(f"Reminder: It's time to {task_name}!")

    def save_schedule(self, file_path='schedule.json'):
        with open(file_path, 'w') as f:
            json.dump(self.schedule, f)
        print("Schedule saved.")

    def load_schedule(self, file_path='schedule.json'):
        try:
            with open(file_path, 'r') as f:
                self.schedule = json.load(f)
            print("Schedule loaded.")
        except FileNotFoundError:
            print("No saved schedule found.")

    def run(self):
        while True:
            schedule.run_pending()
            time.sleep(1)

if __name__ == '__main__':
    manager = DailyRoutineManager()
    manager.add_task('Eat breakfast', '08:00')
    manager.add_task('Study', '10:00')
    manager.add_task('Work', '12:00')
    manager.add_task('Watch videos', '15:00')
    manager.run()