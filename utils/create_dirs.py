from pathlib import Path

DIR_PATH = Path(__file__).parent.parent / 'book'

for dir in range(3, 21):
    (DIR_PATH / f'cap{dir}').mkdir(parents=True, exist_ok=True)