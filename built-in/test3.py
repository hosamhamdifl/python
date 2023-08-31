from platform import (processor, python_implementation, python_version_tuple,
                      system, version)

print(processor())

print(system())
print(version())

print(python_implementation())

for atr in python_version_tuple():
    print(atr)
