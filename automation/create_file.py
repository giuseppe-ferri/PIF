from pathlib import Path

def create_folder(path: Path) -> Path:
    folder_name = 'backlog itens'
    folder = path / folder_name
    
    if folder.exists():
        print(f'Folder  "{folder_name.upper()}" already exists!')
    else:
        folder.mkdir()
        print(f'Folder  "{folder_name.upper()}" was created successfully!')
    return folder

def create_file(path: Path, total_files: int = 12) -> None:
        
        folder_path = create_folder(path)
        
        for item in range(1, total_files):
            file_name = f'item{item:02d}.txt'
            file_path = folder_path / file_name
            
            if file_path.exists():
                print(f'File    "{file_name.upper()}"    already exists!')
            else:
                file_path.touch()
                file_path.write_text(f'#{file_name[:-4].capitalize()}\n\n' +
                'Título:\n\nDescrição:\n\nCritérios de aceitação:' +
                '\n\t1. \n\t\t1.1. \n\t2. \n\t\t2.1. \n\t\t2.2. \n\t3. \n\t\t3.1. \n\t\t3.2. ' +
                '\n\t4. \n\t\t4.1. \n\t\t4.2. \n\t5. \n\t\t5.1. \n\t\t5.2. \n\n' + 
                'Prioridade:')               
                print(f'File    "{file_name}"    was created successfully!')
                
if __name__ == '__main__':
    path_file = Path.home().joinpath(
        'Desktop',
        '4 FACUL',
        '7 SEMESTRE',
        'ENGENHARIA DE SOFTWARE',
        'BIM 1',
        'Atividade',
    )
    create_file(path=path_file, total_files=12)