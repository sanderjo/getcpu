import platform, subprocess, os


def getcpu():
    # find the CPU name (which needs a different method per OS), and return it
    # return None if none found
    # works on Linux, MacOS (aka OSX), Windows, FreeBSD

    cputype = None

    try:
        if platform.system() == "Windows":
            import _winreg as winreg    # needed on Python 2
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"Hardware\Description\System\CentralProcessor\0")
            cputype = winreg.QueryValueEx(key, "ProcessorNameString")[0]
            winreg.CloseKey(key)

        elif platform.system() == "Darwin":
            cputype = subprocess.check_output(['sysctl', "-n", "machdep.cpu.brand_string"]).strip()

        elif platform.system() == "Linux":
            for myline in open("/proc/cpuinfo"):
                if myline.startswith(('model name')):
                    # Typical line:
                    # model name      : Intel(R) Xeon(R) CPU           E5335  @ 2.00GHz
                    cputype = myline.split(":", 1)[1]   # get everything after the first ":"
                    break # we're done

        elif platform.system() == "FreeBSD":
            myline = os.popen('sysctl hw.model').readline().strip()
            # Typical line:
            # hw.model: Intel(R) Core(TM) i3 CPU       M 370  @ 2.40GHz
            cputype = myline.split(":", 1)[1]   # get everything after the first ":"

    except:
        # An exception, maybe due to a subprocess call gone wrong
        cputype = "Exception happened"
        pass

    if cputype:
        # remove unnneeded space:
        cputype = " ".join(cputype.split())
    return cputype

print getcpu()
