## Windows Service in Python

This GitHub repository serves as a comprehensive guide and demonstration for creating a functional Windows Service using Python. 

A Windows Service is a specialized application that runs in the background on a Windows operating system, typically without a user interface. 
Unlike standard applications, services are designed to start automatically during system boot and run independently, providing essential functionality without requiring user interaction.

Here's how a Windows Service works:

1. **Installation**: To deploy a Windows Service, it needs to be installed on the system. This is typically done using a service installer, which registers the service with the Windows Service Control Manager (SCM).
2. **Configuration**: Services often come with configuration settings that determine their behavior. These settings can be defined during installation or stored in configuration files.
3. **Start and Stop Control**: The Windows Service Control Manager is responsible for starting, stopping, and managing services. Users can control services through tools like the Services Management Console, the sc command, or programmatically through APIs.
4. **Lifecycle**: A Windows Service goes through various states during its lifecycle.
5. **Logging**: Windows Services often utilize logging mechanisms to record events, errors, and other relevant information. This is crucial for troubleshooting and monitoring the service's behavior.
6. **Error Handling**: Robust error handling is essential for Windows Services. Services should be designed to handle unexpected errors gracefully, log relevant information, and, if possible, recover without requiring manual intervention.
7. **Security**: Windows Services run with specific user credentials and permissions. Proper security measures must be implemented to ensure the service has the necessary access rights and that potential security vulnerabilities are mitigated.

## Installation and running

Install repository using Poetry:

```
python -m pip install poetry
python -m poetry install
```

Installation of Windows Service to SCM:

```
# Standard installation
python -m poetry run python -m windows_service.main install

# Installation with autostart after reboot
python -m poetry run python -m windows_service.main --startup=auto install
```

Starting Windows Service:

```
python -m poetry run python -m windows_service.main start
```

After this, you should see the service running. You can check using PowerShell:

```
Get-Service
```

Stopping Windows Service:

```
python -m poetry run python -m windows_service.main stop
```

Uninstalling Windows Service:

```
python -m poetry run python -m windows_service.main remove
```

You can also build EXE file using PyInstaller and install it as binary:

```
python -m poetry run pyinstaller windows_service/main.py --copy-metadata windows-service --hiddenimport win32timezone --onefile -n Example_Win_Service
dist/Example_Win_Service.exe install
dist/Example_Win_Service.exe start
```

## Author

[Aleph Null s.r.o.](https://alephnull.sk)
