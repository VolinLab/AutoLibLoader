import os

def install(package, i):
    print(f'{i}. Install {package}')
    #os.system(f"pip install {package}")

def loader_start():
    with open('requirements.txt', 'r') as f:
        print('The automatic installer will install now the following packages:')
        
        i = 1 # This variable is used as a counter to count the number of installed libraries, ignore it
        
        for line in f:
            install(line, i)
            i += 1
        
        print(f'\n{i - 1} libraries were installed')
