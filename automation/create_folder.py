from pathlib import Path
from send2trash import send2trash

# desktop = Path.home() / "Desktop" / "4 FACUL"
min_size = 1
max_size = 10
limit = 7  # dafult: 0
directory = 'TESTE'

path = Path.home() / 'Desktop' / directory
folders = range(min_size, max_size + 1)

def create_folder(path, trash='no'):
    
    if not path.exists():
        path.mkdir(parents=True)
        print(f'Folder created: {path}')

    if trash == 'no':
        print('CREATED STRUCTURE')
        for folder in folders:
            if folder >= limit:
                print()
                name_folder0 = f'{folder} SEMESTRE'
                folder0 = path / name_folder0
                folder0.mkdir(exist_ok=True)                
                print(name_folder0)
                
                for sub1_folder in range(0, 5):
                    name_folder1 = f'DISCIPLINA {sub1_folder + 1}'
                    folder1 = folder0 / name_folder1
                    folder1.mkdir(exist_ok=True)
                    print(1*'  ', '└──', name_folder1)
                    
                    for sub2_folder in range(0, 2):
                        name_folder2 = f'BIM { sub2_folder + 1}'
                        folder2 = folder1 / name_folder2
                        folder2.mkdir(exist_ok=True)
                        print(2*'  ', '└──', name_folder2)
                        for sub2 in range(0,2):
                            if sub2 == 0:
                                sub_name = 'Conteudo'
                            else:
                                sub_name = 'Atividade'
                            sub = folder2 / sub_name
                            sub.mkdir(exist_ok=True)
                            print(3*'  ', '└──', sub_name)
    elif trash == 'yes':
        send2trash(path)
        print('Directory sended to trash!')

create_folder(path, trash='no')
