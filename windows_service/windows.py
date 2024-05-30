try:
    import servicemanager
    import win32con
    import win32event
    import win32evtlog
    import win32evtlogutil
    import win32service
    import win32serviceutil
except ImportError as exc:
    raise OSError("OS Windows is required!") from exc


class _SMWinservice(win32serviceutil.ServiceFramework):
    _svc_name_ = "PythonService"
    _svc_display_name_ = "Python Service"
    _svc_description_ = "Python Service Description"

    def __init__(self, args) -> None:
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)

    @classmethod
    def parse_command_line(cls) -> None:
        win32serviceutil.HandleCommandLine(cls)

    def SvcStop(self) -> None:  # noqa
        self.stop()
        self.ReportServiceStatus(win32service.SERVICE_STOPPED)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self) -> None:  # noqa
        self.start()
        self.ReportServiceStatus(win32service.SERVICE_RUNNING)
        servicemanager.LogMsg(
            servicemanager.EVENTLOG_INFORMATION_TYPE,
            servicemanager.PYS_SERVICE_STARTED,
            (self._svc_name_, ""),
        )
        self.main()

    def start(self) -> None:
        pass

    def stop(self) -> None:
        pass

    def main(self) -> None:
        pass
