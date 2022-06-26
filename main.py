from tkinter import *
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os, psutil

window = Tk()
window.title("PC Tools")

# Application open

def CPUWATCH():
    os.system('pythonw CPUWatcher.py')

def DisplayCPU():
    return messagebox.showinfo('PC Tools', f'Your current CPU usage is {str(psutil.cpu_percent())}%')

def CFV():
    okF = ['addins', 'appcompat', 'apppatch', 'AppReadiness', 'assembly', 'bcastdvr', 'bfsvc.exe', 'Boot', 'bootstat.dat', 'Branding', 'CbsTemp', 'ChangeLang_Done.tag', 'comsetup.log', 'Containers', 'Core.xml', 'CSUP.txt', 'Cursors', 'debug', 'diagerr.xml', 'diagnostics', 'DiagTrack', 'diagwrn.xml', 'DigitalLocker', 'Downloaded Program Files', 'DPINST.LOG', 'DtcInstall.log', 'ELAMBKUP', 'en-US', 'explorer.exe', 'Firmware', 'Fonts', 'GameBarPresenceWriter', 'Globalization', 'Help', 'HelpPane.exe', 'hh.exe', 'IdentityCRL', 'IME', 'ImmersiveControlPanel', 'INF', 'InputMethod', 'Installer', 'L2Schemas', 'LanguageOverlayCache', 'LiveKernelReports', 'Logs', 'Media', 'mib.bin', 'Microsoft.NET', 'Migration', 'ModemLogs', 'NAPP_Dism_Log', 'notepad.exe', 'NvContainerRecovery.bat', 'NvTelemetryContainerRecovery.bat', 'OCR', 'oem', 'Offline Web Pages', 'Panther', 'Patch.log', 'Performance', 'PFRO.log', 'PLA', 'PolicyDefinitions', 'Prefetch', 'PrintDialog', 'Provisioning', 'rescache', 'Resources', 'RtlExUpd.dll', 'SchCache', 'schemas', 'security', 'ServiceProfiles', 'ServiceState', 'servicing', 'Setup', 'setupact.log', 'setuperr.log', 'ShellComponents', 'ShellExperiences', 'SKB', 'SoftwareDistribution', 'Speech', 'Speech_OneCore', 'splwow64.exe', 'System', 'system.ini', 'System32', 'SystemApps', 'SystemResources', 'SystemTemp', 'SysWOW64', 'TAPI', 'Tasks', 'Temp', 'TextInput', 'tracing', 'twain_32', 'twain_32.dll', 'Vss', 'WaaS', 'Web', 'win.ini', 'WindowsShell.Manifest', 'WindowsUpdate.log', 'winhlp32.exe', 'WinSxS', 'WMSysPr9.prx', 'write.exe']
    myFil = os.listdir("C:\\Windows")
    for i in range(len(myFil)):
        if myFil[i] not in okF:
            return messagebox.showinfo('PC Tools', f'Your PC Has A Virus')
        else:
            return messagebox.showinfo('PC Tools', f'Your PC Does Not Have A Virus')

def DisplayMemory():
    return messagebox.showinfo('PC Tools', f'Your Current Memory usage is {str(psutil.virtual_memory()[2])}%')

def CC():
    try:
        os.system("control update")
    except:
        return messagebox.showinfo('PC Tools', "Your PC is at its latest version!")

# All The Actions
Lb = Label(window, text="PC Tools", font=("Times New Roman", 25), bg='#121212',fg='white')
Lb.place(x=180, y=30)

CPUWatcher = Button(window, text="CPU Watcher", font=("Times New Roman", 11), bg="#121212",fg='white',bd=0, command=CPUWATCH)
CPUWatcher.place(x=195, y=100)

CPUDisplayer = Button(window, text="CPU Displayer", font=("Times New Roman", 11), bg="#121212", fg='white', bd=0, command=DisplayCPU)
CPUDisplayer.place(x=192, y=150)

MemoryDisplays = Button(window, text="Memory Display", font=("Times New Roman", 11), bg="#121212", fg="white", bd=0, command=DisplayMemory)
MemoryDisplays.place(x=187,y=200)

VirusChecker = Button(window, text="Virus Detector", font=('Times New Roman', 11), bg="#121212", fg='white', bd=0, command=CFV)
VirusChecker.place(x=192, y=250)

ClearCache = Button(window, text="Update PC", font=('Times New Roman', 11), bg="#121212", fg="white", bd=0, command=CC)
ClearCache.place(x=203, y=300)

window.configure(bg='#323232')
window.geometry("500x750")
window.mainloop()
