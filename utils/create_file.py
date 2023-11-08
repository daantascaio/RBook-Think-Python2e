from pathlib import Path

FILE_PATH = Path(__file__).parent.parent / 'book'

for file in range(3, 21):
    file_path = FILE_PATH / f'cap{file}'
    
    # Create notes.md in each directory
    (file_path / 'notes.md').touch()
    
    # Create e_0xx in each directory
    (file_path / f'e_{str(file).zfill(3)}.py').touch()