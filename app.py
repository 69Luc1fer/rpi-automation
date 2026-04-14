import platform
import os
import psutil

def main():
    print("=== RPi Monitor System (CI/CD Test) ===")
    print(f"OS: {platform.system()} {platform.release()}")
    print(f"Arch: {platform.machine()}")
    print(f"CPU Cores: {os.cpu_count()}")
    print(f"RAM Usage: {psutil.virtual_memory().percent}%")
    print("=======================================")
    print("✅ System monitoring: OK")

if __name__ == "__main__":
    main()
