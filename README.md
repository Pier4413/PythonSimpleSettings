# PythonSimpleSettings
This is a simple module to wrap ConfigParser and check if the settings exists

To use it you need to call the getInstance as it's implemented from a singleton

Small example below :

```python

from <submodule>.setting import Settings

Settings.getInstance().loadSettings(<file path or absolute>)
print(Settings.getInstance().get(<section>, <key>, <defaultValue>))
```
