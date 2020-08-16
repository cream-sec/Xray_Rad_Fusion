import subprocess
#rad路径(建议使用相对路径)
radPath="./Rad/rad.exe"
#xray路径(建议使用相对路径)
xrayPath="./Xray/xray_windows_amd64.exe"
#xray代理地址
xrayProxy="127.0.0.1:7777"
def Scan(target,startxray):
	cmd = [radPath,"-t",target,"-http-proxy",xrayProxy]
	rsp=subprocess.Popen(cmd,start_new_session=True)
	rsp.communicate()
with open("target.txt","r") as targats:
	xrayShell = [xrayPath, "webscan", "--listen", xrayProxy, "--html-output", "result.html"]
	startxray = subprocess.Popen(xrayShell)
	while targat :=targats.readline().strip("\n"):
		Scan(targat,startxray)