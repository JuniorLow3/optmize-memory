import psutil
import time
import threading

def monitor_memory(interval=1, event=None):
    while not event.is_set():
        memory_info = psutil.virtual_memory()
        print(f"Total Memory: {memory_info.total / (1024 ** 3):.2f} GB")
        print(f"Available Memory: {memory_info.available / (1024 ** 3):.2f} GB")
        print(f"Used Memory: {memory_info.used / (1024 ** 3):.2f} GB")
        print(f"Percentage Used: {memory_info.percent}%")
        
        # Pausar pelo intervalo especificado antes de atualizar novamente
        time.sleep(interval)

def start_monitoring(interval=1):
    stop_event = threading.Event()
    monitor_thread = threading.Thread(target=monitor_memory, args=(interval, stop_event))
    monitor_thread.daemon = True  # Define a thread como daemon para terminar quando o programa principal terminar
    monitor_thread.start()
    return stop_event, monitor_thread
