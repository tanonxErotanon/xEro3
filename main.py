import os

def create_files(num_files):
    for i in range(1, num_files + 1):
        filename = f"file{i}.txt"
        with open(filename, 'w') as f:
            f.write(f"Это файл номер {i}. Он был создан программой на Python.\n")
        print(f"Файл {filename} успешно создан.")

def main():
    num_files = int(input("Введите количество файлов для создания: "))
    create_files(num_files)

if __name__ == "__main__":
    main()

