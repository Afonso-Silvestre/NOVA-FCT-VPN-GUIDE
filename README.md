# NOVA-FCT-VPN-GUIDE
Go [Here](https://github.com/ancwrd1/snx-rs/blob/main/docs/installation.md) and download the installation files that fit your system.

After installing run the following command in your terminal:
```bash
sudo snx-rs -s vpn.fct.unl.pt -u CLIP_USERNAME -o vpn_Username_Password -X true -T tcpt
```

Where `CLIP_USERNAME` should be the the username for your clip login.

If you wish to not have to write this everytime, create a .sh file e.g. vpn.sh<br>
For the first line of the file paste into it:
```bash
#!/bin/bash
```
And then the line above with your clip username already in it.<br>
Open a terminal in the directory where you created this file and run:
```
chmod +x vpn.sh
```
And done! Just run this file in a terminal each time and it'll launch the vpn.

**EXTRA:**<br>
If you wish to launch this by simply clicking a desktop icon, you can do it by manually<br>
creating a shortcut. To do so create a file on your desktop named e.g. VPN.desktop<br>
and paste into it:
```ini
[Desktop Entry]
Type=Application
Name=VPN
Exec=path_to_sh_file
Terminal=true
```

Where `path_to_sh_file` is the path to your vpn.sh file.
After this try to double click the shortcut created. If you run into problems
simply follow the prompts on your distro.
