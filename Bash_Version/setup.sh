echo "What is your CLIP username?"
read
user=$REPLY
desktop=$(xdg-user-dir DESKTOP) # /home/user/Desktop/
home=$HOME # /home/user

bash_file="vpn.sh"
bash_script="#!/bin/bash\necho \"RUNNING NOVA FCT VPN\"\nsudo snx-rs -s vpn.fct.unl.pt -u $user -o vpn_Username_Password -X true -T tcpt"

shortcut_file="VPN.desktop"
shortcut_script="[Desktop Entry]\nType=Application\nName=VPN\nExec=$home/$bash_file\nTerminal=true"

cd $home
touch $bash_file
echo -e $bash_script > $bash_file
chmod +x $bash_file

cd $desktop
touch $shortcut_file
echo -e $shortcut_script > $shortcut_file
chmod +x $shortcut_file