import os

if os.getenv('TERRAGEN_PATH'):
    print('variable exist')
    print(os.getenv('TERRAGEN_PATH'))
else:
    if os.path.exists('C:\Program Files\Planetside Software\Terragen 4'):
        os.environ['TERRAGEN_PATH'] = 'C:\Program Files\Planetside Software\Terragen 4'
    else:
        print('Non esiste')