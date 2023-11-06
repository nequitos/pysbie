from sandboxie import Sandboxie


sbie_plus = Sandboxie(installation_dir=r'C:\Program Files\Sandboxie-Plus')
sbie_plus.create_sandbox('TestBox')
sbie_plus.start(r'notepad.exe', 'TestBox', wait=True, shell=True)
