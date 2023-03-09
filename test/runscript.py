import subprocess, sys, platform
user_inp = input("What do you wanna say?")
if platform.system().lower() == "windows":
    print("windows yall")
    print(subprocess.Popen(["pwsh","-File","./script.ps1",user_inp],stdout=sys.stdout))
elif platform.system().lower() == "linux":
    print("linux yall")
    print(subprocess.run(["./script.sh",user_inp], shell=True))
else:
    print(f"{platform.system()} is not supported")
