# Setting up PyCharm and Python (W10)
For those who are lazy and want to keep their software updated there is quite an easy way to setup not only PyCharm. With the Windows Package Manager 'Chocolatey' it's quite easy. It requires an administrative powershell for installation and updates.

```powershell
Set-ExecutionPolicy AllSigned
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```
For TS4 Python 3.7 is needed and it shouldn't be upgraded. Pinning a version prevents this:
```cmd
choco install python3 --version 3.7
choco pin add -n python3
```
The PyCharm installation is also straightforward:
```cmd
choco install pycharm-community
```

Verify the installation:
```cmd
choco list --localonly
```
### Weekly updates
Update PyCharm to the latest version (may be done weekly, the effort to keep the software updated like this is really small):
```cmd
choco upgrade all
```

##### Cheat Sheet

Show Upgrades: 'choco upgrade all --noop'
Upgrade automatically: 'choco upgrade all -y'

A small list of programs which can be installed:
Launcher: 'choco install epicgameslauncher steam ubisoft-connect' # eol: origin uplay
Tools: 'choco install 7zip kdiff3 notepadplusplus vscode procmon psexec rufus OpenOffice discord'
Security: 'choco install keepass veracrypt openssl'
Image: 'choco install gimp XnView'
Video: 'choco install obs-studio ffmpeg gpac 4k-video-downloader'
Java: 'choco install git TortoiseGit svn tortoisesvn eclipse openjdk8'
IDEs: 'choco install eclipse intellijidea-community pycharm-community'
Network: 'choco install git curl Wget winscp putty openvpn wireshark onionshare'
Servers & Databases: 'choco install apache-httpd nginx Tomcat Glassfish mariadb mysql mongodb neo4j-community'

Available Packages Overview: 'choco search >c:\choco.packages.txt'
Open the file with a user without admin permissions.
