import os

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pyperclip
import requests
import webbrowser
vr = ["1.8.9", "1.16.5"]
version="1.0"
run=1
import threading
def fetch_github_file(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверка на ошибки
        return response.text
    except:
        if messagebox.askyesno("ezzLauncher", "Ошибка чтения файла возможно у вас нет интернета повторить?"):
            compare_content()
        else:
            main()


def compare_content():
    github_content = fetch_github_file("https://raw.githubusercontent.com/pashtet0612/ezzLauncher/refs/heads/main/version")
    try:
        if github_content is not None:
            if github_content.strip() == version.strip():
                main()
            else:
                if messagebox.askyesno("ezzzLauncher",f"Найдено обновление {github_content} установить?"):
                    webbrowser.open("https://github.com/pashtet0612/ezzLauncher",new=2)
                    exit()
                else:
                    main()

        else:
            exit()

    except:
        exit()


def main():
    def rw():
        if messagebox.askyesno("ezzzLauncher","Click yes for copy ip"):
            pyperclip.copy("mc.reallyworld.ru")

    def ac():
        if messagebox.askyesno("ezzzLauncher", "Click yes for copy ip"):
            pyperclip.copy("agerapvp.club")

    def rn():
        if messagebox.askyesno("ezzzLauncher", "Click yes for copy ip"):
            pyperclip.copy("revage.net")

    def mh():
        if messagebox.askyesno("ezzzLauncher", "Click yes for copy ip"):
            pyperclip.copy("mc.metahvh.space")

    def ft():
        if messagebox.askyesno("ezzzLauncher", "Click yes for copy ip"):
            pyperclip.copy("funtime.su")

    def se():
        pass


    def hw():
        if messagebox.askyesno("ezzzLauncher","Click yes for copy ip"):
            pyperclip.copy("mc.holyworld.ru")


    def bt():
        if messagebox.askyesno("ezzzLauncher", "Click yes for copy ip"):
            pyperclip.copy("2b2t.org.ru")

    def lw():
        if messagebox.askyesno("ezzzLauncher", "Click yes for copy ip"):
            pyperclip.copy("mc.politmine.ru")


    def start():
        ram=en1.get()
        name=en.get()
        argjava="java"
        getver=cb.get()
        java=en2.get()
        pathnow=os.getcwd()
        try:

            if name=="":
                messagebox.showerror("ezzLauncher","Place enter your nickname")
                return
            if java != "java":
                argjava = "\"" + java + "\""
        except:
            messagebox.showerror("ezzzLauncher","Error                           \n0ezz000001")
            return
        try:
            def st():
                if getver == "1.8.9":
                    if cb.get() == "True":
                        os.system(f'{argjava} -Xmx{ram}M -Dlog4j.configurationFile={pathnow}/assets/log_configs/patched-variant-2.0.xml -Dfml.ignoreInvalidMinecraftCertificates=true -Dfml.ignorePatchDiscrepancies=true -Djava.net.useSystemProxies=true -XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump "-Dos.name=Windows 10" -Dos.version=10.0 -Djava.library.path={pathnow}/versions/1.8.9/natives -Dminecraft.launcher.brand=java-minecraft-launcher -Dminecraft.launcher.version=1.6.84-j -Dminecraft.client.jar={pathnow}/versions/1.8.9/1.8.9.jar -cp {pathnow}/libraries/com/turikhay/ca-fixer/1.0/ca-fixer-1.0.jar;{pathnow}/libraries/ru/tlauncher/patchy/1.0.0/patchy-1.0.0.jar;{pathnow}/libraries/oshi-project/oshi-core/1.1/oshi-core-1.1.jar;{pathnow}/libraries/net/java/dev/jna/jna/3.4.0/jna-3.4.0.jar;{pathnow}/libraries/net/java/dev/jna/platform/3.4.0/platform-3.4.0.jar;{pathnow}/libraries/com/ibm/icu/icu4j-core-mojang/51.2/icu4j-core-mojang-51.2.jar;{pathnow}/libraries/net/sf/jopt-simple/jopt-simple/4.6/jopt-simple-4.6.jar;{pathnow}/libraries/com/paulscode/codecjorbis/20101023/codecjorbis-20101023.jar;{pathnow}/libraries/com/paulscode/codecwav/20101023/codecwav-20101023.jar;{pathnow}/libraries/com/paulscode/libraryjavasound/20101123/libraryjavasound-20101123.jar;{pathnow}/libraries/com/paulscode/librarylwjglopenal/20100824/librarylwjglopenal-20100824.jar;{pathnow}/libraries/com/paulscode/soundsystem/20120107/soundsystem-20120107.jar;{pathnow}/libraries/io/netty/netty-all/4.0.23.Final/netty-all-4.0.23.Final.jar;{pathnow}/libraries/com/google/guava/guava/17.0/guava-17.0.jar;{pathnow}/libraries/org/apache/commons/commons-lang3/3.3.2/commons-lang3-3.3.2.jar;{pathnow}/libraries/commons-io/commons-io/2.4/commons-io-2.4.jar;{pathnow}/libraries/commons-codec/commons-codec/1.9/commons-codec-1.9.jar;{pathnow}/libraries/net/java/jinput/jinput/2.0.5/jinput-2.0.5.jar;{pathnow}/libraries/net/java/jutils/jutils/1.0.0/jutils-1.0.0.jar;{pathnow}/libraries/com/google/code/gson/gson/2.2.4/gson-2.2.4.jar;{pathnow}/libraries/by/ely/authlib/3.11.49.2/authlib-3.11.49.2.jar;{pathnow}/libraries/com/mojang/realms/1.7.59/realms-1.7.59.jar;{pathnow}/libraries/org/apache/commons/commons-compress/1.8.1/commons-compress-1.8.1.jar;{pathnow}/libraries/org/apache/httpcomponents/httpclient/4.3.3/httpclient-4.3.3.jar;{pathnow}/libraries/commons-logging/commons-logging/1.1.3/commons-logging-1.1.3.jar;{pathnow}/libraries/org/apache/httpcomponents/httpcore/4.3.2/httpcore-4.3.2.jar;{pathnow}/libraries/org/apache/logging/log4j/log4j-api/2.0-beta9/log4j-api-2.0-beta9.jar;{pathnow}/libraries/org/apache/logging/log4j/log4j-core/2.0-beta9/log4j-core-2.0-beta9.jar;{pathnow}/libraries/org/lwjgl/lwjgl/lwjgl/2.9.4-nightly-20150209/lwjgl-2.9.4-nightly-20150209.jar;{pathnow}/libraries/org/lwjgl/lwjgl/lwjgl_util/2.9.4-nightly-20150209/lwjgl_util-2.9.4-nightly-20150209.jar;{pathnow}/libraries/tv/twitch/twitch/6.5/twitch-6.5.jar;{pathnow}/versions/1.8.9/1.8.9.jar -Xss2M net.minecraft.client.main.Main --username {name} --version {getver} --gameDir {pathnow} --assetsDir {pathnow}/assets --assetIndex 1.8 --uuid a1227148e64331e780412b80c4d1d412 --accessToken a1227148e64331e780412b80c4d1d412  --userType legacy --width 925 --height 530 --demo True')
                    else:
                        os.system(f'{argjava} -Xmx{ram}M -Dlog4j.configurationFile={pathnow}/assets/log_configs/patched-variant-2.0.xml -Dfml.ignoreInvalidMinecraftCertificates=true -Dfml.ignorePatchDiscrepancies=true -Djava.net.useSystemProxies=true -XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump "-Dos.name=Windows 10" -Dos.version=10.0 -Djava.library.path={pathnow}/versions/1.8.9/natives -Dminecraft.launcher.brand=java-minecraft-launcher -Dminecraft.launcher.version=1.6.84-j -Dminecraft.client.jar={pathnow}/versions/1.8.9/1.8.9.jar -cp {pathnow}/libraries/com/turikhay/ca-fixer/1.0/ca-fixer-1.0.jar;{pathnow}/libraries/ru/tlauncher/patchy/1.0.0/patchy-1.0.0.jar;{pathnow}/libraries/oshi-project/oshi-core/1.1/oshi-core-1.1.jar;{pathnow}/libraries/net/java/dev/jna/jna/3.4.0/jna-3.4.0.jar;{pathnow}/libraries/net/java/dev/jna/platform/3.4.0/platform-3.4.0.jar;{pathnow}/libraries/com/ibm/icu/icu4j-core-mojang/51.2/icu4j-core-mojang-51.2.jar;{pathnow}/libraries/net/sf/jopt-simple/jopt-simple/4.6/jopt-simple-4.6.jar;{pathnow}/libraries/com/paulscode/codecjorbis/20101023/codecjorbis-20101023.jar;{pathnow}/libraries/com/paulscode/codecwav/20101023/codecwav-20101023.jar;{pathnow}/libraries/com/paulscode/libraryjavasound/20101123/libraryjavasound-20101123.jar;{pathnow}/libraries/com/paulscode/librarylwjglopenal/20100824/librarylwjglopenal-20100824.jar;{pathnow}/libraries/com/paulscode/soundsystem/20120107/soundsystem-20120107.jar;{pathnow}/libraries/io/netty/netty-all/4.0.23.Final/netty-all-4.0.23.Final.jar;{pathnow}/libraries/com/google/guava/guava/17.0/guava-17.0.jar;{pathnow}/libraries/org/apache/commons/commons-lang3/3.3.2/commons-lang3-3.3.2.jar;{pathnow}/libraries/commons-io/commons-io/2.4/commons-io-2.4.jar;{pathnow}/libraries/commons-codec/commons-codec/1.9/commons-codec-1.9.jar;{pathnow}/libraries/net/java/jinput/jinput/2.0.5/jinput-2.0.5.jar;{pathnow}/libraries/net/java/jutils/jutils/1.0.0/jutils-1.0.0.jar;{pathnow}/libraries/com/google/code/gson/gson/2.2.4/gson-2.2.4.jar;{pathnow}/libraries/by/ely/authlib/3.11.49.2/authlib-3.11.49.2.jar;{pathnow}/libraries/com/mojang/realms/1.7.59/realms-1.7.59.jar;{pathnow}/libraries/org/apache/commons/commons-compress/1.8.1/commons-compress-1.8.1.jar;{pathnow}/libraries/org/apache/httpcomponents/httpclient/4.3.3/httpclient-4.3.3.jar;{pathnow}/libraries/commons-logging/commons-logging/1.1.3/commons-logging-1.1.3.jar;{pathnow}/libraries/org/apache/httpcomponents/httpcore/4.3.2/httpcore-4.3.2.jar;{pathnow}/libraries/org/apache/logging/log4j/log4j-api/2.0-beta9/log4j-api-2.0-beta9.jar;{pathnow}/libraries/org/apache/logging/log4j/log4j-core/2.0-beta9/log4j-core-2.0-beta9.jar;{pathnow}/libraries/org/lwjgl/lwjgl/lwjgl/2.9.4-nightly-20150209/lwjgl-2.9.4-nightly-20150209.jar;{pathnow}/libraries/org/lwjgl/lwjgl/lwjgl_util/2.9.4-nightly-20150209/lwjgl_util-2.9.4-nightly-20150209.jar;{pathnow}/libraries/tv/twitch/twitch/6.5/twitch-6.5.jar;{pathnow}/versions/1.8.9/1.8.9.jar -Xss2M net.minecraft.client.main.Main --username {name} --version {getver} --gameDir {pathnow} --assetsDir {pathnow}/assets --assetIndex 1.8 --uuid a1227148e64331e780412b80c4d1d412 --accessToken a1227148e64331e780412b80c4d1d412  --userType legacy --width 925 --height 530')

                elif getver == "1.16.5":
                    if cb1.get()=="True":
                        os.system(
                        f'{argjava}  -Xmx{ram}M  -XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump -Djava.library.path={pathnow}/versions/1.16.5/natives -Dminecraft.launcher.brand=java-minecraft-launcher -Dminecraft.launcher.version=1.6.84-j -cp {pathnow}/libraries/com/turikhay/ca-fixer/1.0/ca-fixer-1.0.jar;{pathnow}/libraries/ru/tlauncher/patchy/1.0.0/patchy-1.0.0.jar;{pathnow}/libraries/oshi-project/oshi-core/1.1/oshi-core-1.1.jar;{pathnow}/libraries/net/java/dev/jna/jna/4.4.0/jna-4.4.0.jar;{pathnow}/libraries/net/java/dev/jna/platform/3.4.0/platform-3.4.0.jar;{pathnow}/libraries/com/ibm/icu/icu4j/66.1/icu4j-66.1.jar;{pathnow}/libraries/com/mojang/javabridge/1.0.22/javabridge-1.0.22.jar;{pathnow}/libraries/net/sf/jopt-simple/jopt-simple/5.0.3/jopt-simple-5.0.3.jar;{pathnow}/libraries/io/netty/netty-all/4.1.25.Final/netty-all-4.1.25.Final.jar;{pathnow}/libraries/com/google/guava/guava/21.0/guava-21.0.jar;{pathnow}/libraries/org/apache/commons/commons-lang3/3.5/commons-lang3-3.5.jar;{pathnow}/libraries/commons-io/commons-io/2.5/commons-io-2.5.jar;{pathnow}/libraries/commons-codec/commons-codec/1.10/commons-codec-1.10.jar;{pathnow}/libraries/net/java/jinput/jinput/2.0.5/jinput-2.0.5.jar;{pathnow}/libraries/net/java/jutils/jutils/1.0.0/jutils-1.0.0.jar;{pathnow}/libraries/com/mojang/brigadier/1.0.17/brigadier-1.0.17.jar;{pathnow}/libraries/com/mojang/datafixerupper/4.0.26/datafixerupper-4.0.26.jar;{pathnow}/libraries/com/google/code/gson/gson/2.8.0/gson-2.8.0.jar;{pathnow}/libraries/by/ely/authlib/3.11.49.2/authlib-3.11.49.2.jar;{pathnow}/libraries/org/apache/commons/commons-compress/1.8.1/commons-compress-1.8.1.jar;{pathnow}/libraries/org/apache/httpcomponents/httpclient/4.3.3/httpclient-4.3.3.jar;{pathnow}/libraries/commons-logging/commons-logging/1.1.3/commons-logging-1.1.3.jar;{pathnow}/libraries/org/apache/httpcomponents/httpcore/4.3.2/httpcore-4.3.2.jar;{pathnow}/libraries/it/unimi/dsi/fastutil/8.2.1/fastutil-8.2.1.jar;{pathnow}/libraries/org/apache/logging/log4j/log4j-api/2.8.1/log4j-api-2.8.1.jar;{pathnow}/libraries/org/apache/logging/log4j/log4j-core/2.8.1/log4j-core-2.8.1.jar;{pathnow}/libraries/org/lwjgl/lwjgl/3.2.2/lwjgl-3.2.2.jar;{pathnow}/libraries/org/lwjgl/lwjgl-jemalloc/3.2.2/lwjgl-jemalloc-3.2.2.jar;{pathnow}/libraries/org/lwjgl/lwjgl-openal/3.2.2/lwjgl-openal-3.2.2.jar;{pathnow}/libraries/org/lwjgl/lwjgl-opengl/3.2.2/lwjgl-opengl-3.2.2.jar;{pathnow}/libraries/org/lwjgl/lwjgl-glfw/3.2.2/lwjgl-glfw-3.2.2.jar;{pathnow}/libraries/org/lwjgl/lwjgl-stb/3.2.2/lwjgl-stb-3.2.2.jar;{pathnow}/libraries/org/lwjgl/lwjgl-tinyfd/3.2.2/lwjgl-tinyfd-3.2.2.jar;{pathnow}/libraries/com/mojang/text2speech/1.11.3/text2speech-1.11.3.jar;{pathnow}/versions/1.16.5/1.16.5.jar -Xss2M net.minecraft.client.main.Main --username Lut14_08_23 --version 1.16.5 --gameDir {pathnow} --assetsDir {pathnow}/assets --assetIndex 1.16 --uuid a1227148e64331e780412b80c4d1d412 --accessToken a1227148e64331e780412b80c4d1d412 --userType legacy --versionType release --width 925 --height 530 --demo True')
                    else:
                        os.system(
                            f'{argjava}  -Xmx{ram}M  -XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump -Djava.library.path={pathnow}/versions/1.16.5/natives -Dminecraft.launcher.brand=java-minecraft-launcher -Dminecraft.launcher.version=1.6.84-j -cp {pathnow}/libraries/com/turikhay/ca-fixer/1.0/ca-fixer-1.0.jar;{pathnow}/libraries/ru/tlauncher/patchy/1.0.0/patchy-1.0.0.jar;{pathnow}/libraries/oshi-project/oshi-core/1.1/oshi-core-1.1.jar;{pathnow}/libraries/net/java/dev/jna/jna/4.4.0/jna-4.4.0.jar;{pathnow}/libraries/net/java/dev/jna/platform/3.4.0/platform-3.4.0.jar;{pathnow}/libraries/com/ibm/icu/icu4j/66.1/icu4j-66.1.jar;{pathnow}/libraries/com/mojang/javabridge/1.0.22/javabridge-1.0.22.jar;{pathnow}/libraries/net/sf/jopt-simple/jopt-simple/5.0.3/jopt-simple-5.0.3.jar;{pathnow}/libraries/io/netty/netty-all/4.1.25.Final/netty-all-4.1.25.Final.jar;{pathnow}/libraries/com/google/guava/guava/21.0/guava-21.0.jar;{pathnow}/libraries/org/apache/commons/commons-lang3/3.5/commons-lang3-3.5.jar;{pathnow}/libraries/commons-io/commons-io/2.5/commons-io-2.5.jar;{pathnow}/libraries/commons-codec/commons-codec/1.10/commons-codec-1.10.jar;{pathnow}/libraries/net/java/jinput/jinput/2.0.5/jinput-2.0.5.jar;{pathnow}/libraries/net/java/jutils/jutils/1.0.0/jutils-1.0.0.jar;{pathnow}/libraries/com/mojang/brigadier/1.0.17/brigadier-1.0.17.jar;{pathnow}/libraries/com/mojang/datafixerupper/4.0.26/datafixerupper-4.0.26.jar;{pathnow}/libraries/com/google/code/gson/gson/2.8.0/gson-2.8.0.jar;{pathnow}/libraries/by/ely/authlib/3.11.49.2/authlib-3.11.49.2.jar;{pathnow}/libraries/org/apache/commons/commons-compress/1.8.1/commons-compress-1.8.1.jar;{pathnow}/libraries/org/apache/httpcomponents/httpclient/4.3.3/httpclient-4.3.3.jar;{pathnow}/libraries/commons-logging/commons-logging/1.1.3/commons-logging-1.1.3.jar;{pathnow}/libraries/org/apache/httpcomponents/httpcore/4.3.2/httpcore-4.3.2.jar;{pathnow}/libraries/it/unimi/dsi/fastutil/8.2.1/fastutil-8.2.1.jar;{pathnow}/libraries/org/apache/logging/log4j/log4j-api/2.8.1/log4j-api-2.8.1.jar;{pathnow}/libraries/org/apache/logging/log4j/log4j-core/2.8.1/log4j-core-2.8.1.jar;{pathnow}/libraries/org/lwjgl/lwjgl/3.2.2/lwjgl-3.2.2.jar;{pathnow}/libraries/org/lwjgl/lwjgl-jemalloc/3.2.2/lwjgl-jemalloc-3.2.2.jar;{pathnow}/libraries/org/lwjgl/lwjgl-openal/3.2.2/lwjgl-openal-3.2.2.jar;{pathnow}/libraries/org/lwjgl/lwjgl-opengl/3.2.2/lwjgl-opengl-3.2.2.jar;{pathnow}/libraries/org/lwjgl/lwjgl-glfw/3.2.2/lwjgl-glfw-3.2.2.jar;{pathnow}/libraries/org/lwjgl/lwjgl-stb/3.2.2/lwjgl-stb-3.2.2.jar;{pathnow}/libraries/org/lwjgl/lwjgl-tinyfd/3.2.2/lwjgl-tinyfd-3.2.2.jar;{pathnow}/libraries/com/mojang/text2speech/1.11.3/text2speech-1.11.3.jar;{pathnow}/versions/1.16.5/1.16.5.jar -Xss2M net.minecraft.client.main.Main --username Lut14_08_23 --version 1.16.5 --gameDir {pathnow} --assetsDir {pathnow}/assets --assetIndex 1.16 --uuid a1227148e64331e780412b80c4d1d412 --accessToken a1227148e64331e780412b80c4d1d412 --userType legacy --versionType release --width 925 --height 530 ')



            th1=threading.Thread(target=st)
            th1.start()

        except:
            messagebox.showerror("ezzzLauncher","Error                           \n0ezz000001")

    root = Tk()
    root.geometry("500x470")
    dm=["True","False"]
    root.title("ezzzLauncher")
    root.resizable(False,False)

    bt1 = Button(root, text="mc.reallyworld.ru", command=rw)
    bt1.place(x=30, y=80, width=200, height=30)
    bt2 = Button(root, text="agerapvp.club", command=ac)
    bt2.place(x=30, y=120, width=200, height=30)
    bt3 = Button(root, text="revage.net", command=rn)
    bt3.place(x=30, y=160, width=200, height=30)
    bt4 = Button(root, text="mc.metahvh.space", command=mh)
    bt4.place(x=30, y=200, width=200, height=30)
    bt5 = Button(root, text="funtime.su", command=ft)
    bt5.place(x=240, y=80, width=200, height=30)
    bt6 = Button(root, text="mc.holyworld.ru", command=hw)
    bt6.place(x=240, y=120, width=200, height=30)
    bt7 = Button(root, text="2b2t.org.ru", command=bt)
    bt7.place(x=240, y=160, width=200, height=30)
    bt8 = Button(root, text="politmine.ru", command=lw)
    bt8.place(x=240, y=200, width=200, height=30)
    bt9 = Button(root, text="site", command=se)
    bt9.place(x=420, y=535, width=100, height=50)

    lb4 = Label(root, text="Version:")
    lb4.place(x=200, y=310, width=100, height=30)
    cb = ttk.Combobox(root, values=vr, state="readonly")
    cb.place(x=280, y=310, width=100, height=30)
    cb.set(vr[1])

    lb4 = Label(root, text="Demo:")
    #lb4.place(x=300, y=350, width=60, height=30)
    cb1 = ttk.Combobox(root, values=dm, state="readonly")
    #cb1.place(x=360, y=350, width=100, height=30)
    cb1.set(dm[1])

    bt = Button(root, text="Play", command=start,font=("Arial",20))
    bt.place(x=25, y=400, width=450, height=40)

    lb1 = Label(root, text="Nickname:")
    lb1.place(x=10, y=350, width=60, height=30)
    en = Entry(root)
    en.place(x=80, y=350, height=30, width=200)

    lb3 = Label(root, text="Java path (type java for auto):")
    lb3.place(x=10, y=270, width=160, height=30)

    en2 = Entry(root)
    en2.place(x=180, y=270, height=30, width=250)
    en2.insert(0, "java")

    lb = Label(root, text="ezzzLauncher",font=("Arial",30))
    lb.place(x=50, y=10, width=400, height=70)

    lb2 = Label(root, text="RAM:")
    lb2.place(x=10, y=310, width=30, height=30)
    en1 = Entry(root)
    en1.place(x=60, y=310, height=30, width=100)
    en1.insert(0, "2048")

    root.mainloop()


if __name__=="__main__":
    if run==1:
        run=2
        compare_content()
    else:
        exit()
