figlet "JuanE" | lolcat -F 1
echo "Installing"
clear
echo "Installing."
sleep 4
clear
echo "Installing.."
sleep 4
clear
echo "Installing..."
sleep 4
clear
echo "Start."
sleep 3
pkg update
pkg upgrade -y
pkg install python -y
pip install --upgrade pip
pkg install lolcat -y
pkg install figlet -y
clear
echo "Reqisites: OK" | lolcat
sleep 4
cd ..
rm -rf Random-Generator
rmdir Random-Generator
clear
echo "Updating?: ..."
sleep 4
clear
figlet "JuanE" | lolcat -F 1
pkg install git -y
clear
git clone https://github.com/JuanEGamerYT/Random-Generator
clear
echo "Updated: OK to last version avaible" | lolcat
sleep 4
clear
sleep 1