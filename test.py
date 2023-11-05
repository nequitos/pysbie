from sandboxie import SandboxiePlus


sbie_plus = SandboxiePlus(installation_dir=r'C:\Program Files\Sandboxie-Plus')
sbie_plus.create_sandbox('TestBox')
sbie_plus.start(r'C:\Program Files (x86)\Steam\steam.exe', 'TestBox', wait=True)