import subprocess

message = "hello this developed by Joshuakingstech and this was the CEO's idea - noah"
subprocess.Popen(f'cmd /k title info && echo {message}', shell=True)