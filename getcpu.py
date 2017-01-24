import platform, subprocess


def getcpu():
    # find the CPU name (which needs a different method per OS), and return it
    # return None if none found

    try:
        if platform.system() == "Windows":
            import _winreg as winreg	# Python 2
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"Hardware\Description\System\CentralProcessor\0")
            processor_brand = winreg.QueryValueEx(key, "ProcessorNameString")[0]
            winreg.CloseKey(key)
            return processor_brand

        elif platform.system() == "Darwin":
            return subprocess.check_output(['sysctl', "-n", "machdep.cpu.brand_string"]).strip()

        elif platform.system() == "Linux":
            for myline in open("/proc/cpuinfo"):
                if myline.startswith(('model name')):
                    # Typical line:
                    # model name      : Intel(R) Xeon(R) CPU           E5335  @ 2.00GHz
                    return myline.split(":", 1)[1]	# get everything after the first ":"

    except:
        # An exception could happen due to a subprocess call
        pass

    # we couldn't determine the processor name, due to
    # an exception, or
    # not Windows, nor Darwin, nor Linux, so possibly BSD, SUN, ...
    return None



print getcpu()

