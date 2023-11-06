# pysbie

Interact with Sandboxie in Python

## Sandboxie fast start

```python
from sandboxie import Sandboxie

sbie = Sandboxie(installation_dir='Your Sandboxie installation dir path')
sbie.create_sandbox('TestBox')
sbie.start('Path to the program to be launched', box='TestBox', wait=True)
sbie.delete_sandbox('TestBox')
```

## SbieIni fast start

```python
from sandboxie import SbieIni

sbieini = SbieIni(installation_dir='Your Sandboxie installation dir path')
print(sbieini.query(specify=True, boxes=True))
sbieini.set('DefaultBox', 'AutoRecover', 'n')
sbieini.insert('DefaultBox', 'RecoverFolder', r'C:\Downloads')
```