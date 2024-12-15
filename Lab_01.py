import subprocess
import threading
import time


def start_process():
    try:
        process = subprocess.Popen(["notepad.exe"])
        print(f"Процес запущено з PID: {process.pid}")
        return process
    except FileNotFoundError:
        print("Програма не знайдена!")
        return None


def wait_for_process(process):
    try:
        process.wait()
        print("Процес завершено.")
    except Exception as e:
        print(f"Помилка при очікуванні завершення: {e}")


def monitor_process(process, timeout):
    def terminate():
        if process.poll() is None:
            print("Процес працює занадто довго. Завершуємо...")
            process.terminate()

    timer = threading.Timer(timeout, terminate)
    timer.start()

    wait_for_process(process)
    timer.cancel()


def main():
    print("Запуск програми...")
    process = start_process()
    if process:
        monitor_process(process, timeout=10)
    print("Програма завершена.")

if __name__ == "__main__":
    main()
