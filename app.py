import platform

def main():
    print("========================================")
    print("🚀 Старт системи автоматизації RPi")
    print(f"💻 Архітектура процесора: {platform.machine()}")
    print(f"🐧 Операційна система: {platform.system()} {platform.release()}")
    print("========================================")
    print("✅ Тест емуляції успішно пройдено!")

if __name__ == "__main__":
    main()
