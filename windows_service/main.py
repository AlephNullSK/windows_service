import sys
import time

try:
    import servicemanager
    import win32serviceutil
except ImportError:
    print("Windows only!")
    sys.exit(1)

from .windows import _SMWinservice, write_to_event_log


def cli():
    if sys.argv[1] == "shell":
        shell()
    else:
        print("Standard CLI functionality")


def shell():
    import code
    code.interact()


class ExampleWindowsService(_SMWinservice):
    _svc_name_ = "Example_Windows_Service"
    _svc_display_name_ = "Example Windows Service in Python"
    _svc_description_ = "Running standard Windows Service as Python script"

    def main(self) -> None:
        while True:
            write_to_event_log(
                "Example_Windows_Service",
                0,
                1,
                "It works!"
            )
            time.sleep(15)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(ExampleWindowsService)
        servicemanager.StartServiceCtrlDispatcher()
    elif len(sys.argv) >= 2 and sys.argv[1] == "cli":
        if len(sys.argv) > 2:
            sys.argv = sys.argv[:1] + sys.argv[2:]
        else:
            sys.argv = sys.argv[:1]

        cli()
    else:
        win32serviceutil.HandleCommandLine(ExampleWindowsService)
