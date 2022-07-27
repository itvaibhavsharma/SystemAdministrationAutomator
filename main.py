#!/usr/bin/env python3
import os
import sys
import subprocess as s
import time
from simple_term_menu import TerminalMenu
from pyfiglet import Figlet
#f = Figlet(font='slant')
#--------------------------------------global variables----------------------------
import shutil

columns = shutil.get_terminal_size().columns
temp=''
operatingsys=''
metadata={'mainmenu':"this is something"}
user=''
lin_flav=''

def check_requirements():
    global lin_flav
    os.system("clear")
    print("Checking All the System Requirements".center(columns))
    os.system('export $TERM=xterm-256color')
    print("\n")
    print(gen_figlet('Checking'))
    print("Installing GDOWN".center(columns))
    os.system("pip3 install gdown")
    print("Checking the flavour of Linux".center(columns))
    print("Checking for Debian Flavour",end='')
    temp=s.getstatusoutput("apt help")
    if temp[0]==0:
        lin_flav='apt'
        print("✅")
    else:
        print("❌")
        print("Checking for RPM Flavour",end='')
        temp1=s.getstatusoutput("yum help")
        if temp1[0]==0:
            lin_flav='yum'
            print("✅")

#---------------------------browsh-------------------------------------
    print("Checking browsh..",end='')
    temp=s.getstatusoutput("browsh --version")
    if temp[0]==0:
        print("✅")
    else:
        print("❌")
        print("Installing browsh....".center(columns))
        if lin_flav=='apt':
            os.system('wget https://github.com/browsh-org/browsh/releases/download/v1.6.4/browsh_1.6.4_linux_amd64.deb')
            os.system('sudo dpkg -i browsh_1.6.4_linux_amd64.deb')
        elif lin_flav=='yum':
            os.system('wget https://github.com/browsh-org/browsh/releases/download/v1.6.4/browsh_1.6.4_linux_amd64.rpm')
            os.system('rpm -Uvh browsh_1.6.4_linux_amd64.rpm')
        else:
            print("No source Found Please Contact the developer".center(columns))
#-------------------------docker----------------------------------------
    print("Checking Docker..",end='')
    temp=s.getstatusoutput("docker")
    if temp[0]==0:
        print("✅")
    else:
        print("❌")
        print("Installing Docker....".center(columns))
        if lin_flav=='apt':
            os.system('sudo apt-get install docker-ce docker-ce-cli containerd.io')
        elif lin_flav=='yum':
            os.system('sudo yum install -y yum-utils')
            os.system('sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo')
            os.system('sudo yum install docker-ce docker-ce-cli containerd.io -y --nobest')
        else:
            print("No source Found Please Contact the developer".center(columns))


def gen_figlet(argu='*'):
    f = Figlet(font='slant')
    #a=input("Enter:")
    argu=' '*(columns//20)+argu
    figlet_str=f.renderText(argu)
    return figlet_str

def findos():
    global operatingsys,user
    print("Wait while we detect your os....")
    temp=s.getstatusoutput("uname -s")
    if temp[0]==0:
        if temp[1]=='Linux':
            #print("Linux Detected.....")
            operatingsys='Linux'
            user=s.getoutput("whoami")
            #print(user)
            #print(operatingsys)
    else:
        temp=s.getstatusoutput("systeminfo /?")
        if temp[0]==0:
            #print("Windows Detected.....")
            operatingsys='Windows'

def start_exec():
    global user
    #print(user)
    topr="     Welcome "+'\x1b[6;35m'+'  {}'.format(user)+'\x1b[0m'
    print(topr.center(columns//2))
    print( '\x1b[5;33m' + ' {}'.format(gen_figlet(operatingsys)) +'\x1b[0m'+'\t',end='')
    print(" detected".center(columns//3))
    print('\x1b[31m'+"Press Enter to continue".center(columns//2))
    input()
    print('\x1b[0m')
    print('\x1b[5m')
    check_requirements()
    input("Press Enter to Continue") 
    mainmenu_select()

def validate_os():
    findos()
    global operatingsys
    #print(operatingsys)
    if operatingsys=='Linux':
        start_exec()
    elif operatingsys=='Windows':
        print("Support for Windows is yet to be extended")
    else:
        print("Exception Occured Contact the developer now program will exit")

def hdfs(dir,a="none"):
    if a=="none":
        print("creating HDFS File locally")
        os.system("echo '<configuration>' > /etc/hadoop/hdfs-site.xml")
        os.system("echo '<property>' >> /etc/hadoop/hdfs-site.xml")
        os.system("echo '<name>dfs.data.dir</name>' >> /etc/hadoop/hdfs-site.xml")
        os.system("echo '<value>{}</value>' >> /etc/hadoop/hdfs-site.xml".format(dir))
        os.system("echo '</property>' >> /etc/hadoop/hdfs-site.xml")
        os.system("echo '</configuration>' >> /etc/hadoop/hdfs-site.xml")
    
    else:
        print("creating HDFS File at {}".format(a))
        os.system("echo '<configuration>' > hdfs-site.xml")
        os.system("echo '<property>' >> hdfs-site.xml")
        os.system("echo '<name>dfs.data.dir</name>' >> hdfs-site.xml")
        os.system("echo '<value>{}</value>' >> hdfs-site.xml".format(dir))
        os.system("echo '</property>' >> hdfs-site.xml")
        os.system("echo '</configuration>' >> hdfs-site.xml")
        os.system("scp hdfs-site.xml root@{}:/etc/hadoop/hdfs-site.xml".format(a))
def core(ip,a="none"):
    if a=="none":
        print("creating HDFS File locally")
        os.system("echo '<configuration>' > /etc/hadoop/core-site.xml")
        os.system("echo '<property>' >> /etc/hadoop/core-site.xml")
        os.system("echo '<name>fs.default.name</name>' >> /etc/hadoop/core-site.xml")
        os.system("echo '<value>{}:9001</value>' >> /etc/hadoop/core-site.xml".format(ip))
        os.system("echo '</property>' >> /etc/hadoop/core-site.xml")
        os.system("echo '</configuration>' >> /etc/hadoop/core-site.xml")
    else:
        print("creating Core File at {}".format(a))
        os.system("echo '<configuration>' > core-site.xml")
        os.system("echo '<property>' >> core-site.xml")
        os.system("echo '<name>fs.default.name</name>' >> core-site.xml")
        os.system("echo '<value>{}:9001</value>' >> core-site.xml".format(a))
        os.system("echo '</property>' >> core-site.xml")
        os.system("echo '</configuration>' >> core-site.xml")
        os.system("scp core-site.xml root@{}:/etc/hadoop/core-site.xml".format(a))



def mainmenu_select():
    main_menu_title = gen_figlet('Main Menu')
    main_menu_items = [
        "[l] Linux",
        "[d] DOCKER",
        "[w] WEBSERVER",
        "[a] AWS",
        "[e] LVM",
        "[f] HADOOP",
        "[g] NETWORKING",
        "[h] Windows",
        "[i] Connect to Remote Agent",
        "[q] Quit"]
    main_menu_cursor = ">>>*|====================>>>"
    main_menu_cursor_style = ("fg_red", "bold")
    main_menu_style = ("bg_red", "fg_yellow")
    main_menu_exit = False

    main_menu = TerminalMenu(menu_entries=main_menu_items,
                             title=main_menu_title,
                             menu_cursor=main_menu_cursor,
                             menu_cursor_style=main_menu_cursor_style,
                             menu_highlight_style=main_menu_style,
                             cycle_cursor=True,
                             clear_screen=True)



    edit_menu_title = gen_figlet('Linux List')
    edit_menu_items = [
        '[a] Fire a CLI Browser',
        '[c] Launch Apache Server',
        '[d] Start ProxyChains',
        '[e] Install some package',
        '[f] Search a package',
        '[g] Add USER',
        '[h] Change the password',
        '[i] Start the SSH Service',
        '[j] Check if command is present',
        '[k] Checking all the running processes',
        '[l] Check all the adapters',
        '[m] Check all the open ports',
        '[n] Check the process Tree',
        '[o] Open Gparted',
        '[p] Open Snap Store',
        '[q] Check free Space',
        '[r] Edit a File in Gedit',
        '[s] Checks the connectivity to IP',
        '[t] Capture the packets using Wireshark',
        '[u] Get all system overview',
        "[b] Back to Main Menu"]
    edit_menu_back = False
    edit_menu = TerminalMenu(edit_menu_items,
                             edit_menu_title,
                             main_menu_cursor,
                             main_menu_cursor_style,
                             main_menu_style,
                             cycle_cursor=True,
                             clear_screen=True)

    docker_edit_menu_title = gen_figlet('Docker List')
    docker_edit_menu_items = [
        "[a] Check Docker Service",
        "[c] Get Docker Info ",
        "[d] Start Docker Service",
        "[e] Enable Docker on Startup",
        "[f] Check Available Docker Images",
        "[g] Pull Docker image from DockerHub",
        "[h] Check Docker Running Container",
        "[i] List all Docker running/stopped Containers",
        "[j] Run a New Docker Container",
        "[k] Start a existing Docker Container",
        "[l] Attach a Running Docker Container",
        "[m] View Docker help or Run Custom Docker Command",
        "[s] Stop the docker service",
        "[n] Stop the docker container",
        "[o] Launch HTTP Server On Container",
        '[p] Get the IP of the container',
        "[b] Back to Main Menu"]
    #docker_menu_back = False
    docker_menu = TerminalMenu(docker_edit_menu_items,
                             docker_edit_menu_title,
                             main_menu_cursor,
                             main_menu_cursor_style,
                             main_menu_style,
                             cycle_cursor=True,
                             clear_screen=True)

    AWS_edit_menu_title = gen_figlet('AWS List')
    AWS_edit_menu_items = [
        "[l] Login into AWS CLI",
        "[n] Launch a instance",
        "[r] Start a Instance",
        "[o] Stop a Instance",
        "[d] Describe All Instances ",
        "[v] Create a Volume",
        "[a] Attach volume with instance",
        "[p] Partitioning the attached volume",
        "[c] configure Web Server ",
        "[f] Format Partition ",
        "[m] Mount the Web Server to Volume",
        "[i] Install And Download AWS CLI",
        "[b] Back to Main Menu"]
    #AWS_menu_back=False
    AWS_menu = TerminalMenu(AWS_edit_menu_items,
                         AWS_edit_menu_title,
                         main_menu_cursor,
                         main_menu_cursor_style,
                         main_menu_style,
                         cycle_cursor=True,
                         clear_screen=True)  

#------------------------------------------hadoop------------------------------

    hadoop_edit_menu_title = gen_figlet('Hadoop List')
    hadoop_edit_menu_items = [
        "[a] Deploy Hadoop Master on Current System",
        "[c] Deploy Hadoop Master on Remote Client ",
        "[d] Deploy Hadoop Managed Node on Current System",
        "[e] Deploy Hadoop Managed Node on Remote System",
        "[f] Check for Hadoop service status",
        "[g] Perform a HDFS Operation",
        "[h] Execute Custom command",
        "[i] View HDFS and Core Configuration File",
        "[j] View remote HDFS and Core Configuration File ",
        "[k] Stop hadoop service",
        "[b] Back to Main Menu"]
    #hadoop_menu_back = False
    hadoop_menu = TerminalMenu(hadoop_edit_menu_items,
                             hadoop_edit_menu_title,
                             main_menu_cursor,
                             main_menu_cursor_style,
                             main_menu_style,
                             cycle_cursor=True,
                             clear_screen=True)

#------------------------------------------LVM------------------------------

    LVM_edit_menu_title = gen_figlet('LVM List')
    LVM_edit_menu_items = [
        "[c] Create New LogicalVolume(LV)",
        "[a]  All LogicalVolume(LV) Info",
        "[l] Particular LogicalVolume Info",
        "[p]  Create PhysicalVolume(PV)",
        "[i]   All VolumeGroup(VG) Info",
        "[v]  Create VG",
        "[e]  Extend LV ",
        "[b] Back to Main Menu"]
    #LVM_menu_back = False
    LVM_menu = TerminalMenu(LVM_edit_menu_items,
                             LVM_edit_menu_title,
                             main_menu_cursor,
                             main_menu_cursor_style,
                             main_menu_style,
                             cycle_cursor=True,
                             clear_screen=True)
                         
    while not main_menu_exit:
        main_sel = main_menu.show()
#---------------------------Linux---------------------------------
        if main_sel == 0:
            while not edit_menu_back:
                edit_sel = edit_menu.show()
                if edit_sel == 0:
                    print('\x1b[6;32m')
                    print("Press Ctrl+Q to Exit".center(columns))
                    print("Press Ctrl+I to Enter URL".center(columns))
                    os.system("browsh")
                    print('\x1b[6;35m'+'\n\n')
                    print("Press Enter to continue".center(columns))
                    input()
                    print('\x1b[0m')
                elif edit_sel == 1:
                    argum=''
                    srv='apache2'
                    if lin_flav=="yum":
                        srv='httpd'
                    temp=s.getoutput("systemctl status {}".format(srv))
                    if "inactive" in temp:
                        argum=input("{} Daemon is Not Running Do you want to Start it enter Y/y else anything to go back:".format(srv))
                    elif "active" in temp:
                        argum=input("{} Daemon is Running Do you want to Stop it enter Y/y:".format(srv))
                    print('\x1b[6;32m')
                    if argum=="y" or argum=="Y":
                        print("Done =",end='')
                        print(argum)
                        if "inactive" in temp:
                            os.system("systemctl start {}".format(srv))
                        else:
                            os.system("systemctl stop {}".format(srv))
                    print('\x1b[6;35m'+'\n\n')
                    print("Press Enter to continue".center(columns))
                    input()
                    print('\x1b[0m')
                elif edit_sel == 2:
                    print('\x1b[6;32m')
                    program_tt=input("Enter the program to Run through Proxychains:")
                    os.system("proxychains {}".format(program_tt))
                    print('\x1b[6;35m'+'\n\n')
                    print("Press Enter to continue".center(columns))
                    input()
                    print('\x1b[0m')
                elif edit_sel == 3:
                    print('\x1b[6;32m')
                    program_tt=input("Enter the program to be Installed:")
                    os.system("{} install {}".format(lin_flav,program_tt))
                    print('\x1b[6;35m'+'\n\n')
                    print("Press Enter to continue".center(columns))
                    input()
                    print('\x1b[0m')
                elif edit_sel == 4:
                    print('\x1b[6;32m')
                    program_tt=input("Enter the program to be Searched:")
                    os.system("{} search {}".format(lin_flav,program_tt))
                    print('\x1b[6;35m'+'\n\n')
                    print("Press Enter to continue".center(columns))
                    input()
                    print('\x1b[0m')
                elif edit_sel == 5:
                    print('\x1b[6;32m')
                    program_tt=input("Enter the user to be Added:")
                    os.system("useradd {}".format(program_tt))
                    print('\x1b[6;35m'+'\n\n')
                    print("Press Enter to continue".center(columns))
                    input()
                    print('\x1b[0m')
                elif edit_sel == 6:
                    print('\x1b[6;32m')
                    program_tt=input("Enter the user to Change Password:")
                    os.system("sudo passwd {}".format(program_tt))
                    print('\x1b[6;35m'+'\n\n')
                    print("Press Enter to continue".center(columns))
                    input()
                    print('\x1b[0m')
                elif edit_sel == 7:
                    print('\x1b[6;32m')
                    os.system("systemctl start sshd")
                    print('\x1b[6;35m'+'\n\n')
                    print("Press Enter to continue".center(columns))
                    input()
                    print('\x1b[0m')

                elif edit_sel == 8:
                    print('\x1b[6;32m')
                    program_tt=input("Enter the Program Name:")
                    os.system("which {}".format(program_tt))
                    print('\x1b[6;35m'+'\n\n')
                    print("Press Enter to continue".center(columns))
                    input()
                    print('\x1b[0m')

                elif edit_sel == 9:
                    print('\x1b[6;32m')
                    #program_tt=input("Enter the Program Name:")
                    os.system("ps aux")
                    print('\x1b[6;35m'+'\n\n')
                    print("Press Enter to continue".center(columns))
                    input()
                    print('\x1b[0m')

                elif edit_sel == 10:
                    print('\x1b[6;32m')
                    #program_tt=input("Enter the Program Name:")
                    os.system("ip a")
                    print('\x1b[6;35m'+'\n\n')
                    print("Press Enter to continue".center(columns))
                    input()
                    print('\x1b[0m')

                elif edit_sel == 11:
                    print('\x1b[6;32m')
                    #program_tt=input("Enter the Program Name:")
                    os.system("netstat -tunlp")
                    print('\x1b[6;35m'+'\n\n')
                    print("Press Enter to continue".center(columns))
                    input()
                    print('\x1b[0m')

                elif edit_sel == 12:
                    print('\x1b[6;32m')
                    #program_tt=input("Enter the Program Name:")
                    os.system("pstree")
                    print('\x1b[6;35m'+'\n\n')
                    print("Press Enter to continue".center(columns))
                    input()
                    print('\x1b[0m')

                elif edit_sel == 13:
                    print('\x1b[6;32m')
                    #program_tt=input("Enter the Program Name:")
                    os.system("gparted")
                    print('\x1b[6;35m'+'\n\n')
                    print("Press Enter to continue".center(columns))
                    input()
                    print('\x1b[0m')


                elif edit_sel == 14:
                    print("This depends if you have snap package Install due to portability\n we don't want to force Install the package")
                    print('\x1b[6;32m')
                    #program_tt=input("Enter the Program Name:")
                    os.system("snap-store")
                    print('\x1b[6;35m'+'\n\n')
                    print("Press Enter to continue".center(columns))
                    input()
                    print('\x1b[0m')

                elif edit_sel == 15:
                    print('\x1b[6;32m')
                    #program_tt=input("Enter the Program Name:")
                    os.system("df -h")
                    print('\x1b[6;35m'+'\n\n')
                    print("Press Enter to continue".center(columns))
                    input()
                    print('\x1b[0m')

                elif edit_sel == 16:
                    print('\x1b[6;32m')
                    #program_tt=input("Enter the Program Name:")
                    os.system("gedit")
                    print('\x1b[6;35m'+'\n\n')
                    print("Press Enter to continue".center(columns))
                    input()
                    print('\x1b[0m')


                elif edit_sel == 17:
                    print('\x1b[6;32m')
                    program_tt=input("Enter the IP Address:")
                    os.system("ping {}".format(program_tt))
                    print('\x1b[6;35m'+'\n\n')
                    print("Press Enter to continue".center(columns))
                    input()
                    print('\x1b[0m')

                elif edit_sel == 18:
                    print('\x1b[6;32m')
                    #program_tt=input("Enter the IP Address:")
                    os.system("sudo wireshark")
                    print('\x1b[6;35m'+'\n\n')
                    print("Press Enter to continue".center(columns))
                    input()
                    print('\x1b[0m')

                elif edit_sel == 19:
                    print('\x1b[6;32m')
                    #program_tt=input("Enter the IP Address:")
                    os.system("bashtop")
                    print('\x1b[6;35m'+'\n\n')
                    print("Press Enter to continue".center(columns))
                    input()
                    print('\x1b[0m')

                elif edit_sel == 20:
                    edit_menu_back = True
                    print("Back Selected")
            edit_menu_back = False
#-------------------------------docker-------------------------------        
        elif main_sel == 1:
            print("option 2 selected")
            while not edit_menu_back:
                edit_sel = docker_menu.show()
                if edit_sel == 0:
                    print('\x1b[6;32m')
                    print("Checking Docker Service Status\n\n".center(columns))
                    print('\x1b[0m')
                    os.system("systemctl status docker")
                    print('\x1b[6;35m'+'\n\n')
                    print("Press Enter to continue".center(columns))
                    input()
                    print('\x1b[0m')
#-------------------------------docker info-------------------------------        
                elif edit_sel == 1:
                    print('\x1b[6;32m')
                    print("Checking Docker Info\n\n".center(columns))
                    print('\x1b[0m')
                    os.system("docker info")
                    print('\x1b[6;35m'+'\n\n')
                    print("Press Enter to continue".center(columns))
                    input()
                    print('\x1b[0m')

                elif edit_sel == 2:
                    print('\x1b[6;32m')
                    print("Starting Docker Service\n\n".center(columns))
                    print('\x1b[0m')
                    os.system("systemctl start docker")
                    print('\x1b[6;35m'+'\n\n')
                    print("Press Enter to continue".center(columns))
                    input()
                    print('\x1b[0m')

                elif edit_sel == 3:
                    print('\x1b[6;32m')
                    print("Enabling Docker on Startup/Service\n\n".center(columns))
                    print('\x1b[0m')
                    os.system("systemctl enable docker")
                    print('\x1b[6;35m'+'\n\n')
                    print("Press Enter to continue".center(columns))
                    input()
                    print('\x1b[0m')

                elif edit_sel == 4:
                    print('\x1b[6;32m')
                    print("Checking Available Docker Images\n\n".center(columns))
                    print('\x1b[0m')
                    os.system("docker images")
                    print('\x1b[6;35m'+'\n\n')
                    print("Press Enter to continue".center(columns))
                    input()
                    print('\x1b[0m')

                elif edit_sel == 5:
                    print('\x1b[6;32m')
                    print("Pulling Docker Image From Docker Hub\n\n".center(columns))
                    docker_image=input("Enter the docker image to pull\n Specify docker Hub Image name".center(columns))
                    print('\x1b[0m')
                    os.system("docker pull {}".format(docker_image))
                    print('\x1b[6;35m'+'\n\n')
                    print("Press Enter to continue".center(columns))
                    input()
                    print('\x1b[0m')

                elif edit_sel == 6:
                    print('\x1b[6;32m')
                    print("Checking Docker Running Container\n\n".center(columns))
                    print('\x1b[0m')
                    os.system("docker ps")
                    print('\x1b[6;35m'+'\n\n')
                    print("Press Enter to continue".center(columns))
                    input()
                    print('\x1b[0m')

                elif edit_sel == 7:
                    print('\x1b[6;32m')
                    print("Listing all Docker running/stopped Containers\n\n".center(columns))
                    print('\x1b[0m')
                    os.system("docker ps -a")
                    print('\x1b[6;35m'+'\n\n')
                    print("Press Enter to continue".center(columns))
                    input()
                    print('\x1b[0m')

                elif edit_sel == 8:
                    print('\x1b[6;32m')
                    print("Run a New Docker Container\n\n".center(columns))
                    print('\x1b[0m')
                    docker_image=input("Enter the docker image to Launch with version (Use image:latest for latest image)".center(columns))
                    docker_container_name=' '
                    docker_container_name=input("Enter the Container name (Press Enter for Random Name)".center(columns))
                    #print('\x1b[0m')
                    yn=input("Do you want to attach docker terminal N for No else press Enter to attach".center(columns))
                    if docker_container_name==' ':
                        if (yn=='N' or yn=='n'):
                            os.system("docker run {}".format(docker_image))
                            os.system("docker run -it {}".format(docker_image))
                        else:
                            os.system("docker run -it {}".format(docker_image))
                    else:
                        if (yn=='N' or yn=='n'):
                            os.system("docker run --name {} {}".format(docker_container_name,docker_image))
                        else:
                            os.system("docker run -it --name {} {}".format(docker_container_name,docker_image))
                    print('\x1b[6;35m'+'\n\n')
                    print("Press Enter to continue".center(columns))
                    input()
                    print('\x1b[0m')

                elif edit_sel == 9:
                    print('\x1b[6;32m')
                    print("Starting Docker Container\n\n".center(columns))
                    print('\x1b[0m')
                    yn=input("Do you want to View all existing containers (Y/y) else leave empty)".center(columns))
                    if (yn=='Y' or yn =="y"):
                        os.system("docker ps -a")
                    docker_container_name=input("Enter docker Container Name".center(columns))
                    if docker_container_name:
                        os.system("docker start {}".format(docker_container_name))
                    print('\x1b[6;35m'+'\n\n')
                    print("Press Enter to continue".center(columns))
                    input()
                    print('\x1b[0m')

                elif edit_sel == 10:
                    print('\x1b[6;32m')
                    print("Attching Docker Container terminal\n\n".center(columns))
                    print('\x1b[0m')
                    yn=input("Do you want to View all existing containers (Y/y) else leave empty)".center(columns))
                    if yn=='Y' or yn=='y':
                        os.system("docker ps -a")
                    docker_container_name=input("Enter docker Container Name".center(columns))
                    if docker_container_name:
                        os.system("docker attach {}".format(docker_container_name))
                    print('\x1b[6;35m'+'\n\n')
                    print("Press Enter to continue".center(columns))
                    input()
                    print('\x1b[0m')

                elif edit_sel == 11:
                    print('\x1b[6;32m')
                    print("View Docker help or Run Custom Docker Command\n\n".center(columns))
                    print('\x1b[0m')
                    yn=input("Do you want to View Docker Help (Y/y) else leave empty)".center(columns))
                    if yn=='Y' or yn=='y':
                        os.system("docker help")
                    docker_container_name=input("Enter docker Custom Command".center(columns))
                    if "docker" in docker_container_name:
                        os.system("{}".format(docker_container_name))
                    print('\x1b[6;35m'+'\n\n')
                    print("Press Enter to continue".center(columns))
                    input()
                    print('\x1b[0m')

                elif edit_sel == 12:
                    print('\x1b[6;32m')
                    print("Stoping Docker Service\n\n".center(columns))
                    print('\x1b[0m')
                    os.system("systemctl stop docker")
                    print('\x1b[6;35m'+'\n\n')
                    print("Press Enter to continue".center(columns))
                    input()
                    print('\x1b[0m')

                elif edit_sel == 13:
                    print('\x1b[6;32m')
                    print("Stoping Docker Container\n\n".center(columns))
                    print('\x1b[0m')
                    docker_container_name=input("Enter docker Container name".center(columns))
                    os.system("docker stop {}".format(docker_container_name))
                    print('\x1b[6;35m'+'\n\n')
                    print("Press Enter to continue".center(columns))
                    input()
                    print('\x1b[0m')

                elif edit_sel == 14:
                    print('\x1b[6;32m')
                    print("Launching HTTPD over Docker Container\n\n".center(columns))
                    print('\x1b[0m')
                    yn=input("Do you want to View all existing containers (Y/y) else leave empty)".center(columns))
                    if (yn=='Y' or yn =="y"):
                        os.system("docker ps -a")
                    docker_container_name=input("Enter docker Container Name if you want to launch it over it".center(columns))
                    if docker_container_name:
                        temp=s.getstatusoutput("docker exec 'yum help' {}".format(docker_container_name))
                        temp1=s.getstatusoutput("docker exec 'apt help' {}".format(docker_container_name))
                        if temp[0]==0:
                            os.system("docker exec 'yum install httpd {}'".format(docker_container_name))
                            os.system("docker exec '/usr/sbin/httpd' {}".format(docker_container_name))
                            os.system("docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' {}".format(docker_container_name))
                        
                        elif temp1[0]==0:
                            os.system("docker exec 'apt install apache2' {} ".format(docker_container_name))
                            os.system("docker exec /usr/sbin/apache2 {}".format(docker_container_name))
                            os.system("docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' {}".format(docker_container_name))
                        else:
                            print("Some Unknown Os detected".center(columns))
                    print('\x1b[6;35m'+'\n\n')
                    print("Press Enter to continue".center(columns))
                    input()
                    print('\x1b[0m')

                elif edit_sel == 15:
                    print('\x1b[6;32m')
                    print("Getting The Ip of Docker Container\n\n".center(columns))
                    print('\x1b[0m')
                    docker_container_name=input("Enter docker Container name".center(columns))
                    os.system("docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' {}".format(docker_container_name))
                    print('\x1b[6;35m'+'\n\n')
                    print("Press Enter to continue".center(columns))
                    input()
                    print('\x1b[0m')

                elif edit_sel == 16:
                    edit_menu_back = True
                    #print("Press Enter to go back".center(columns))
                    #input()
            edit_menu_back = False
#---------------------------AWSCLI---------------------------------
        elif main_sel == 3:
            print("option 3 selected")
            while not edit_menu_back:
                edit_sel = AWS_menu.show()
                if edit_sel==0:
                    print('\x1b[6;32m')
                    print("Logging into AWSCLI\n\n".center(columns))
                    print(' \x1b[0m')
                    os.system("aws configure")
                    print('\x1b[6;35m'+'\n\n')
                    print("Press Enter to continue".center(columns))
                    input()
                    print('\x1b[0m')
                elif edit_sel == 1:
                    print('\x1b[6;32m')
                    print("Lanching instances\n\n".center(columns))
                    print(' \x1b[0m')
                    print("The Available AMIs are:-\n\
                    AWS Linux 2     ami-007a607c4abd192db\n\
                    RHEL8           ami-09b4418342d60f7aa\n\
                    SuSe Linux      ami-0a782e324655d1cc0\n\
                    Ubuntu 20.4     ami-0885b1f6bd170450c\n\
                    Ubuntu 18.4     ami-00ddb0e5626798373\n\
                    Server 2019     ami-06ba345d99c2958fc")
                    image_id=input("Enter the AMI ID to Launch Instance:".center(columns))
                    security_id=input("Enter Security ID to Launch Instance:".center(columns))
                    key=input("Enter Key Name".center(columns))
                    os.system("aws ec2 run-instances --image-id{} --subnet-id subnet-ba5b5cd2 --instance-type t2.micro --key-name {} --security-group-ids {} --count 1".format(image_id,key,security_id))
                    print('\x1b[6;35m'+'\n\n')
                    print("Press Enter to continue".center(columns))
                    input()
                    print('\x1b[0m')
                elif edit_sel ==2:
                    print('\x1b[6;32m')
                    print("Starting Instance\n\n".center(columns))
                    print(' \x1b[0m')
                    ID=input("Enter instance ID".center(columns))
                    os.system(" aws ec2 stop-instances --instance-id {}".format(ID))
                    print('\x1b[6;35m'+'\n\n')
                    print("Press Enter to continue".center(columns))
                    input()
                    print('\x1b[0m')
                elif edit_sel==3:
                    print('\x1b[6;32m')
                    print("Stopping Instance\n\n".center(columns))
                    print(' \x1b[0m')
                    ID=input("Enter instance ID".center(columns))
                    os.system(" aws ec2 stop-instances --instance-id {}".format(ID))
                    print('\x1b[6;35m'+'\n\n')
                    print("Press Enter to continue".center(columns))
                    input()
                    print('\x1b[0m')
                elif edit_sel==4:
                    print('\x1b[6;32m')
                    print("Describe All Instance\n\n".center(columns))
                    print(' \x1b[0m')
                    os.system("aws ec2 describe-instances")
                    print('\x1b[6;35m'+'\n\n')
                    print("Press Enter to continue".center(columns))
                    input()
                    print('\x1b[0m')
                elif edit_sel==5:
                    print('\x1b[6;32m')
                    print("Create Volume    \n\n".center(columns))
                    print(' \x1b[0m')
                    az=input("Enter availability Zone".center(columns))
                    size=input("Enter size".center(columns))
                    vt=input("Enter volume type:".center(columns))
                    os.system(" aws ec2 create-volume  --availability-zone {} --size {} --volume-type {}".format(az,size,vt))
                    print('\x1b[6;35m'+'\n\n')
                    print("Press Enter to continue".center(columns))
                    input()
                    print('\x1b[0m')
                elif edit_sel==6:
                    print('\x1b[6;32m')
                    print("Attaching volume to instance\n\n".center(columns))
                    print(' \x1b[0m')
                    Id=input("Enter Volume ID".center(columns))
                    i=input("Enter  Instance ID".center(columns))
                    device = input("Enter device : /dev/".center(columns))
                    os.system(" aws ec2 attach-volume --volume-id {} --instance-id {} --device /dev/{} ".format(Id,i,device))
                    print('\x1b[6;35m'+'\n\n')
                    print("Press Enter to continue".center(columns))
                    input()
                    print('\x1b[0m')
                elif edit_sel==7:
                    print('\x1b[6;32m')
                    print("Partitioning the attached volume\n\n".center(columns))
                    print(' \x1b[0m')
                    ip=input("Enter IP ".center(columns))
                    key = input("Enter key".center(columns))
                    device = input("Enter device: /dev/".center(columns))
                    os.system(" ssh -l ec2-user {} -i {}.pem sudo fdisk /dev/{} ".format(ip,key,device))
                    print('\x1b[6;35m'+'\n\n')
                    print("Press Enter to continue".center(columns))
                    input()
                    print('\x1b[0m')
                elif edit_sel==8:
                    print('\x1b[6;32m')
                    print("Configuring Webserver\n\n".center(columns))
                    print(' \x1b[0m')
                    ip=input("Enter IP ".center(columns))
                    key = input("Enter key".center(columns))
                    os.system(" ssh -l ec2-user {} -i {}.pem sudo systemctl start httpd ".format(ip,key))  
                    print('\x1b[6;35m'+'\n\n')
                    print("Press Enter to continue".center(columns))
                    input()
                    print('\x1b[0m')
                elif edit_sel==9:
                    print('\x1b[6;32m')
                    print("Formatting the partition\n\n".center(columns))
                    print(' \x1b[0m')
                    ip=input("Enter IP ".center(columns))
                    key = input("Enter key".center(columns))
                    device = input("Enter device: /dev/".center(columns))
                    os.system(" ssh -l ec2-user {} -i {}.pem sudo mkfs.ext4 /dev/{} ".format(ip,key,device))
                    print('\x1b[6;35m'+'\n\n')
                    print("Press Enter to continue".center(columns))
                    input()
                    print('\x1b[0m')
                elif edit_sel==10:
                    print('\x1b[6;32m')
                    print("Mount the Web Server to Volume\n\n".center(columns))
                    print(' \x1b[0m')
                    ip=input("Enter IP ".center(columns))
                    key = input("Enter key".center(columns))
                    device = input("Enter device: /dev/".center(columns))
                    os.system(" ssh -l ec2-user {} -i {}.pem sudo mount /dev/{} /var/www/html/ ".format(ip,key,device))
                    print('\x1b[6;35m'+'\n\n')
                    print("Press Enter to continue".center(columns))
                    input()
                    print('\x1b[0m')
                elif edit_sel==11:
                    print('\x1b[6;32m')
                    print("Installing  AWS CLI\n\n".center(columns))
                    print(' \x1b[0m')
                    os.system("pip3 install awscli --upgrade --user")
                    print('\x1b[6;35m'+'\n\n')
                    print("Press Enter to continue".center(columns))
                    input()
                    print('\x1b[0m')
                elif edit_sel==12:                                   
                    edit_menu_back = True
            edit_menu_back = False

#------------------------------LVM--------------------------------
        elif main_sel == 4:
            print("option 6 selected")
            while not edit_menu_back:
                edit_sel = LVM_menu.show()
                if edit_sel==0:
                    print('\x1b[6;32m')
                    print("Creating new Logical Volume\n\n".center(columns))
                    print(' \x1b[0m')
                    print("\n\t\t\t\t .......................these are your drive and disk.........................")
                    time.sleep(4)
                    os.system('fdisk -l')
                    #Physical Volume
                    pv= input("Enter your drive for which you want to create PV = ".center(columns))
                    pvcmd = os.system("pvcreate {}".format(pv))
                    print("\n\n")
                    os.system("pvdisplay {}".format(pv))
                    #Volume Group
                    print("\n Now Creating Volume Group".center(columns))
                    vg_name= input("Enter your VG name =".center(columns))
                    pv_name=input(" Enter your PV name =".center(columns))
                    vgcmd = os.system("vgcreate {} {}".format(vg_name, pv_name))
                    print("\n\n")
                    os.system("vgdisplay {}".format(vg_name))
                    #LV
                    print("\n\n Creating Logical Volume".center(columns))
                    lv_name= input("Enter your LV name =".center(columns))
                    lv_size = input("Enter your LV Size =".center(columns))
                    lvcmd = os.system("lvcreate --size {} --name {} {}".format(lv_size, lv_name, vg_name))
                    print("\n\n")
                    os.system("lvdisplay {}/{}".format(vg_name, lv_name))
                    #format for LV
                    print("\n\n  format and mount the LV to your folder".center(columns))
                    format_name= input("Enter your format type=".center(colums))
                    mount_folder = input(" Enter your mount folder name =".center(columns))
                    #format
                    format_cmd = os.system("{} /dev/{}/{}".format(format_name, vg_name, lv_name))
                    print("\n\n")
                    mount_cmd = os.system("mount /dev/{}/{} {}".format(vg_name,lv_name,mount_folder))
                    print("\n\n")
                    print('\x1b[6;35m'+'\n\n')
                    print("Press Enter to continue".center(columns))
                    input()
                    print('\x1b[0m')
                elif edit_sel==1:                   #All LV Info
                    print('\x1b[6;32m')
                    print("All LV Info".center(columns))
                    print(' \x1b[0m')
                    lv_all_cmd = os.system("lvdisplay") 
                    print('\x1b[6;35m'+'\n\n')
                    print("Press Enter to continue".center(columns))
                    input()
                    print('\x1b[0m')          
                elif edit_sel==2:                 #get particular LV info
                    print('\x1b[6;32m')
                    print("Particular LV Info ".center(columns))
                    print(' \x1b[0m')
                    vg_name = input("Enter your Volume Group name = ".center(columns))
                    lv_name = input("\n Eneter your Logical Volume name = ".center(columns))
                    os.system("lvdisplay {}/{}".format(vg_name, lv_name))   
                    print('\x1b[6;35m'+'\n\n')
                    print("Press Enter to continue".center(columns))
                    input()
                    print('\x1b[0m')
                elif edit_sel==3:                   #create PV
                    print('\x1b[6;32m')
                    print("Create PV ".center(columns))
                    print(' \x1b[0m')
                    cprint("\n these are your drive and disk", "green")
                    time.sleep(4)
                    os.system('fdisk -l')
                    #Physical Volume
                    pv= input(" Enter your drive which you want to create PV =  ".center(columns))
                    os.system("pvcreate {}".format(pv))
                    print('\x1b[6;35m'+'\n\n')
                    print("Press Enter to continue".center(columns))
                    input()
                    print('\x1b[0m')
                elif edit_sel==4:                   
                    print('\x1b[6;32m')
                    print(" All VG info".center(columns))
                    print(' \x1b[0m')
                    os.system("vgdisplay")
                    os.system("pvcreate {}".format(pv))
                    print('\x1b[6;35m'+'\n\n')
                    print("Press Enter to continue".center(columns))
                    input()
                    print('\x1b[0m')
                elif edit_sel==4:                   #all VG info       
                    print('\x1b[6;32m')
                    print(" All VG info".center(columns))
                    print(' \x1b[0m')                 
                    os.system("vgdisplay")           
                    print('\x1b[6;35m'+'\n\n')
                    print("Press Enter to continue".center(columns))
                    input()
                    print('\x1b[0m')       
                elif edit_sel==5:                   #Create VG       
                    print('\x1b[6;32m')
                    print(" Creating VG".center(columns))
                    print(' \x1b[0m')      
                    vg_name= input("Enter your VG name = ".center(colums))
                    pv_name = input("Enter your PV name = ".center(columns))
                    vgcmd = os.system("vgcreate {} {}".format(vg_name, pv_name))
                    print("\n\n")
                    os.system("vgdisplay {}".format(vg_name))
                    print('\x1b[6;35m'+'\n\n')
                    print("Press Enter to continue".center(columns))
                    input()
                    print('\x1b[0m')  
                elif edit_sel==6:                   #Extend LV       
                    print('\x1b[6;32m')
                    print(" Resizing LV".center(columns))
                    print(' \x1b[0m')
                    os.system("lvdisplay")
                    os.system("vgdisplay")  
                    lv_name= input("Enter your LV name =".center(columns))
                    vg_name= input(" Enter your VG name =".center(columns))
                    lv_size = input("Enter your LV ReSize(+G/-G) =".center(columns))
                    lvcmd = os.system("lvextend --size {} /dev/{}/{}".format(lv_size, vg_name, lv_name))
                    os.system("resize2fs /dev/{}/{}".format(vg_name, lv_name))
                    print('\x1b[6;35m'+'\n\n')
                    print("Press Enter to continue".center(columns))
                    input()
                    print('\x1b[0m')  
                elif edit_sel == 7:
                    edit_menu_back = True
            edit_menu_back = False   

#------------------------------Hadoop--------------------------------
        elif main_sel == 5:
            print("option 3 selected")
            while not edit_menu_back:
                edit_sel = hadoop_menu.show()
                if edit_sel==0:
                    print('\x1b[6;32m')
                    if lin_flav=="yum":
                        print("Checking for java ".center(columns))
                        temp=s.getstatusoutput("jps")
                        if temp[0]==0:
                            print("Checking for Hadoop".center(columns))
                            temp=s.getstatusoutput("hadoop version")
                            if temp[0]==0:
                                print("Hadoop and Java Already Present")
                            else:
                                print("Installing Hadoop".center(columns))
                                os.system("gdown --id 1541gbFeGZZJ5k9Qx65D04lpeNBw87rM5")
                                
                        else:
                            print("Downloading jdk".center(columns))
                            temp=s.getstatusoutput("gdown --id 17UWQNVdBdGlyualwWX4Cc96KyZhD-lxz")
                            print("Checking for Hadoop".center(columns))
                            temp=s.getstatusoutput("hadoop version")
                            if temp[0]==0:
                                print("Hadoop Already Present")
                            else:
                                print("Installing Hadoop".center(columns))
                                os.system("gdown --id 1541gbFeGZZJ5k9Qx65D04lpeNBw87rM5")
#--------------------------------Configuring the Core-HDFS
                        dir='mn'
                        dir=input("Enter the Directory to use For HDFS (only enter the name):")
                        ip=os.system("ip -o -4 route get 1 | awk '/src/ {print $7}'")
                        os.system("mkdir /{}".format(dir))
                        hdfs(dir)
                        core(ip)
                        print("Formating the HDFS".center(columns))
                        os.system("hadoop namenode -format")
                        os.system('hadoop-daemon.sh start namenode')
                        print("Setup Complete".center(columns))
                        print(' \x1b[0m')
                        print('\x1b[6;35m'+'\n\n')
                        print("Press Enter to continue".center(columns))
                        input()
                        print('\x1b[0m')
                    else:
                        print("Please Install Debian packages for saftey Feature Restricted")

                elif edit_sel == 1:
                    print('\x1b[6;32m')
                    remoteip=input("Enter the remote IP:")
                    print("Follow the process to create ssh key".center(columns))
                    os.system('ssh-keygen')
                    print("Copying the SSH-KEY enter your password for remote client".center(columns))
                    os.system('ssh-copy-id root@{}'.format(remoteip))
                    if lin_flav=="yum" or lin_flav=='apt':
                        print("Checking for java ".center(columns))
                        temp=s.getstatusoutput("ssh root@{} jps".format(remoteip))
                        if temp[0]==0:
                            print("Checking for Hadoop".center(columns))
                            temp=s.getstatusoutput("ssh root@{} hadoop version".format(remoteip))
                            if temp[0]==0:
                                print("Hadoop and Java Already Present")
                            else:
                                print("Installing Hadoop".center(columns))
                                os.system("ssh root@{} gdown --id 1541gbFeGZZJ5k9Qx65D04lpeNBw87rM5".format(remoteip))
                                
                        else:
                            print("Downloading jdk".center(columns))
                            temp=s.getstatusoutput("ssh gdown --id 17UWQNVdBdGlyualwWX4Cc96KyZhD-lxz".format(remoteip))
                            print("Checking for Hadoop".center(columns))
                            temp=s.getstatusoutput("ssh root@{} hadoop version".format(remoteip))
                            if temp[0]==0:
                                print("Hadoop Already Present")
                            else:
                                print("Installing Hadoop".center(columns))
                                os.system("ssh root@{} gdown --id 1541gbFeGZZJ5k9Qx65D04lpeNBw87rM5".format(remoteip))
                    else:
                        print("Currently blocked for debian based system")
#--------------------------------Configuring the Core-HDFS
                    dir='mn'
                    dir=input("Enter the Directory to use For HDFS (only enter the name):")
                    ip=os.system("ssh root@{}".format(remoteip) + " ip -o -4 route get 1 | awk '/src/ {print $7} '")
                    os.system("ssh root@{} mkdir /{}".format(remoteip,dir))
                    hdfs(dir,remoteip)
                    core(ip,remoteip)
                    print("Formating the HDFS".center(columns))
                    os.system("ssh root@{} hadoop namenode -format".format(remoteip))
                    os.system('ssh root@{} hadoop-daemon.sh start namenode'.format(remoteip))
                    print("Setup Complete".center(columns),end='')
                    print("Over Ip {}".format(remoteip))
                    print(' \x1b[0m')
                    print('\x1b[6;35m'+'\n\n')
                    print("Press Enter to continue".center(columns))
                    input()
                    print('\x1b[0m')

#-------------------------------------------------------
                if edit_sel==2:
                    print('\x1b[6;32m')
                    if lin_flav=="yum":
                        print("Checking for java ".center(columns))
                        temp=s.getstatusoutput("jps")
                        if temp[0]==0:
                            print("Checking for Hadoop".center(columns))
                            temp=s.getstatusoutput("hadoop version")
                            if temp[0]==0:
                                print("Hadoop and Java Already Present")
                            else:
                                print("Installing Hadoop".center(columns))
                                os.system("gdown --id 1541gbFeGZZJ5k9Qx65D04lpeNBw87rM5")
                                
                        else:
                            print("Downloading jdk".center(columns))
                            temp=s.getstatusoutput("gdown --id 17UWQNVdBdGlyualwWX4Cc96KyZhD-lxz")
                            print("Checking for Hadoop".center(columns))
                            temp=s.getstatusoutput("hadoop version")
                            if temp[0]==0:
                                print("Hadoop Already Present")
                            else:
                                print("Installing Hadoop".center(columns))
                                os.system("gdown --id 1541gbFeGZZJ5k9Qx65D04lpeNBw87rM5")
#--------------------------------Configuring the Core-HDFS
                        dir='mn'
                        dir=input("Enter the Directory to use For HDFS (only enter the name):")
                        ip=os.system("ip -o -4 route get 1 | awk '/src/ {print $7}'")
                        os.system("mkdir /{}".format(dir))
                        hdfs(dir)
                        core(ip)
                        print("Formating the HDFS".center(columns))
                        #os.system("hadoop namenode -format")
                        os.system('hadoop-daemon.sh start datanode')
                        print("Setup Complete".center(columns))
                        print(' \x1b[0m')
                        print('\x1b[6;35m'+'\n\n')
                        print("Press Enter to continue".center(columns))
                        input()
                        print('\x1b[0m')
                    else:
                        print("Please Install Debian packages for saftey Feature Restricted")

                elif edit_sel == 3:
                    print('\x1b[6;32m')
                    remoteip=input("Enter the remote IP:")
                    print("Follow the process to create ssh key".center(columns))
                    os.system('ssh-keygen')
                    print("Copying the SSH-KEY enter your password for remote client".center(columns))
                    os.system('ssh-copy-id root@{}'.format(remoteip))
                    if lin_flav=="yum":
                        print("Checking for java ".center(columns))
                        temp=s.getstatusoutput("ssh root@{} jps".format(remoteip))
                        if temp[0]==0:
                            print("Checking for Hadoop".center(columns))
                            temp=s.getstatusoutput("ssh root@{} hadoop version".format(remoteip))
                            if temp[0]==0:
                                print("Hadoop and Java Already Present")
                            else:
                                print("Installing Hadoop".center(columns))
                                os.system("ssh root@{} gdown --id 1541gbFeGZZJ5k9Qx65D04lpeNBw87rM5".format(remoteip))
                                
                        else:
                            print("Downloading jdk".center(columns))
                            temp=s.getstatusoutput("ssh gdown --id 17UWQNVdBdGlyualwWX4Cc96KyZhD-lxz".format(remoteip))
                            print("Checking for Hadoop".center(columns))
                            temp=s.getstatusoutput("ssh root@{} hadoop version".format(remoteip))
                            if temp[0]==0:
                                print("Hadoop Already Present")
                            else:
                                print("Installing Hadoop".center(columns))
                                os.system("ssh root@{} gdown --id 1541gbFeGZZJ5k9Qx65D04lpeNBw87rM5".format(remoteip))
                    else:
                        print("Please Install Debian packages for saftey Feature Restricted")
                    
#--------------------------------Configuring the Core-HDFS
                    dir='mn'
                    dir=input("Enter the Directory to use For HDFS (only enter the name):")
                    ip=os.system("ssh root@{} ip -o -4 route get 1 | awk '/src/ {print $7}'".format(remoteip))
                    os.system("ssh root@{} mkdir /{}".format(dir,remoteip))
                    hdfs(dir,a=remoteip)
                    core(ip,a=remoteip)
                    print("Formating the HDFS".center(columns))
                    #os.system("ssh root@{} hadoop namenode -format".format(remoteip))
                    os.system('ssh root@{} hadoop-daemon.sh start datanode'.format(remoteip))
                    print("Setup Complete".center(columns))
                    print(' \x1b[0m')
                    print('\x1b[6;35m'+'\n\n')
                    print("Press Enter to continue".center(columns))
                    input()
                    print('\x1b[0m')

                elif edit_sel==4:
                    rip=input("Is system on remote IP if yes input IP else N for local:")
                    print('\x1b[6;32m')
                    print("Checking for Hadoop service status".center(columns))
                    print(' \x1b[0m')
                    if rip=="N":
                        os.system("jps")
                    else:
                        os.system("ssh root@{} jps".format(rip))
                    print('\x1b[6;35m'+'\n\n')
                    print("Press Enter to continue".center(columns))
                    input()
                    print('\x1b[0m')
                
                elif edit_sel==5:
                    print('\x1b[6;32m')
                    prt='''
                               [-ls <path>]
           [-lsr <path>]
           [-du <path>]
           [-dus <path>]
           [-count[-q] <path>]
           [-mv <src> <dst>]
           [-cp <src> <dst>]
           [-rm [-skipTrash] <path>]
           [-rmr [-skipTrash] <path>]
           [-expunge]
           [-put <localsrc> ... <dst>]
           [-copyFromLocal <localsrc> ... <dst>]
           [-moveFromLocal <localsrc> ... <dst>]
           [-get [-ignoreCrc] [-crc] <src> <localdst>]
           [-getmerge <src> <localdst> [addnl]]
           [-cat <src>]
           [-text <src>]
           [-copyToLocal [-ignoreCrc] [-crc] <src> <localdst>]
           [-moveToLocal [-crc] <src> <localdst>]
           [-mkdir <path>]
           [-setrep [-R] [-w] <rep> <path/file>]
           [-touchz <path>]
           [-test -[ezd] <path>]
           [-stat [format] <path>]
           [-tail [-f] <file>]
           [-chmod [-R] <MODE[,MODE]... | OCTALMODE> PATH...]
           [-chown [-R] [OWNER][:[GROUP]] PATH...]
           [-chgrp [-R] GROUP PATH...]
           [-help [cmd]]
                    '''
                    print("Some of the Hadoop file system commands are:".center(columns))
                    print(prt)
                    print(' \x1b[0m')
                    temp=input("Enter the hadoop fs Command:")
                    if "hadoop fs" in temp:
                        os.system("{}".format(temp))
                    print('\x1b[6;35m'+'\n\n')
                    print("Press Enter to continue".center(columns))
                    input()
                    print('\x1b[0m')

                elif edit_sel==6:
                    print('\x1b[6;32m')
                    print("Execute Custom command".center(columns))
                    print(' \x1b[0m')
                    temp=input("Enter the Command:")
                    if "hadoop" in temp:
                        os.system("{}".format(temp))
                    print('\x1b[6;35m'+'\n\n')
                    print("Press Enter to continue".center(columns))
                    input()
                    print('\x1b[0m')
                
                elif edit_sel==7:
                    print('\x1b[6;32m')
                    print("Displaying the files".center(columns))
                    print(' \x1b[0m')
                    print("------------Core file--------".center(columns))
                    os.system("cat /etc/hadoop/core-site.xml")
                    print('\x1b[6;32m')
                    print("------------HDFS file--------".center(columns))
                    print(' \x1b[0m')
                    os.system("cat /etc/hadoop/hdfs-site.xml")
                    print('\x1b[6;35m'+'\n\n')
                    print("Press Enter to continue".center(columns))
                    input()
                    print('\x1b[0m')

                elif edit_sel==8:
                    print('\x1b[6;32m')
                    print("Displaying the Remote system files".center(columns))
                    print(' \x1b[0m')
                    ip=input("Enter the IP of remote System:")
                    print('\x1b[6;32m')
                    print("------------Core file--------".center(columns))
                    print(' \x1b[0m')
                    os.system("ssh root@{} cat /etc/hadoop/core-site.xml".format(ip))
                    print('\x1b[6;32m')
                    print("------------HDFS file--------".center(columns))
                    print(' \x1b[0m')
                    os.system("ssh root@{} cat /etc/hadoop/hdfs-site.xml".format(ip))
                    print('\x1b[6;35m'+'\n\n')
                    print("Press Enter to continue".center(columns))
                    input()
                    print('\x1b[0m')               

                elif edit_sel==9:
                    print('\x1b[6;32m')
                    print("Stopping the Hadoop services".center(columns))
                    print(' \x1b[0m')
                    ip='local'
                    node='namenode'
                    node=input('Enter what to stop datanode and namenode=default:')
                    ip=input("Enter the IP of remote System:")
                    print('\x1b[6;32m')
                    print("------------Core file--------".center(columns))
                    print(' \x1b[0m')
                    os.system("ssh root@{} cat /etc/hadoop/core-site.xml".format(ip))
                    print('\x1b[6;32m')
                    print("------------HDFS file--------".center(columns))
                    print(' \x1b[0m')
                    if ip=='local':
                        os.system('hadoop-daemon.sh stop {}'.format(node))
                    else:
                        os.system('ssh root@{} hadoop-daemon.sh stop {}'.format(ip,node))
                    print('\x1b[6;35m'+'\n\n')
                    print("Press Enter to continue".center(columns))
                    input()
                    print('\x1b[0m')    

                elif edit_sel==10:                                   
                    edit_menu_back = True
            edit_menu_back = False        
              
#----------------------------------------7------------------------------------
        elif main_sel == 6:
            print("Networking Option is under construction selected")
            input()
        elif main_sel == 7:
            print("Windows Option is not supported now")
            input()

        elif main_sel == 8:
            print("Running the same program on Remote Host".center(columns))
            remoteip=input('Enter the remote Ip of the system:')
            remoteuser=input('Enter the remote agent  port followed by name:')
            remotepass=input('Enter the remote agent passwd var followed by password log in:')
            os.system("curl -X POST http://{}:{}{}".format(remoteip,remoteuser,remotepass))
        elif main_sel == 9:
            main_menu_exit = True
            print("Quit Selected")


validate_os()
