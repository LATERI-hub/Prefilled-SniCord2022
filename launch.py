import os
try:
    os.system('pip install -r requirements.txt')
except Exception as e:
    print(e)
input('you can now run main.py')