import sys
from spleeter.separator import Separator

def separate_audio(input_path, output_path="output"):
    """
    Разделяет аудио на вокал и инструментал.
    """
    separator = Separator('spleeter:2stems')  # 2 stems: вокал + остальное
    separator.separate_to_file(input_path, output_path)
    print(f"Готово! Результаты в папке: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Использование: python app.py <путь_к_аудио>")
        sys.exit(1)
    input_file = sys.argv[1]
    separate_audio(input_file)
