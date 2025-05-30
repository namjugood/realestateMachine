import os
import sys
import django
from django.core.management import execute_from_command_line
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Django 프로젝트 경로 설정
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.config.settings')
django.setup()

class DjangoReloader(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith('.py'):
            print(f"File changed: {event.src_path}")
            print("Reloading Django server...")
            os.execv(sys.executable, ['python'] + sys.argv)

if __name__ == "__main__":
    print("Starting Django development server with auto-reload...")
    event_handler = DjangoReloader()
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=True)
    observer.start()
    
    try:
        execute_from_command_line(['manage.py', 'runserver'])
    except KeyboardInterrupt:
        observer.stop()
        print("\nStopping server...")
    observer.join() 