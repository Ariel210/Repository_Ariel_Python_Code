import sysconfig

var_1 = sysconfig.get_python_version()
print(f"Python Version: {var_1}")

var_2 = sysconfig.get_platform()
print(f"Current Platform: {var_2}")