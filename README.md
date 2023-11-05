# pysbie

Interact with Sandboxie in Python

## Sandboxie Plus fast start

```python
from sandboxie import SandboxiePlus

sbie_plus = SandboxiePlus(installation_dir='Your Sandboxie Plus installation path')
sbie_plus.create_sandbox('TestBox')
sbie_plus.start('Path to the program to be launched', box='TestBox', wait=True)
sbie_plus.delete_sandbox('TestBox')
```

## SbieIni fast start

```python
from sandboxie import SbieIni

sbieini = SbieIni(installation_dir='Your Sandboxie installation path')
print(sbieini.query(specify=True, boxes=True))
sbieini.set('DefaultBox', 'AutoRecover', 'n')
sbieini.insert('DefaultBox', 'RecoverFolder', r'C:\Downloads')
```