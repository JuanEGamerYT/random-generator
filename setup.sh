figlet "JuanE" | lolcat -F 1
echo "Installing"
clear
echo "Installing."
clear
echo "Installing.."
clear
echo "Installing..."
echo "Start."
pkg update
pkg upgrade -y
pkg install python
pip install --upgrade pip
pkg install lolcat -y
pkg install figlet -y
clear
echo "Reqisites: OK" | lolcat
cd ..
rm -rf Generator
clear
echo "Updating?: ..."
clear
figlet "JuanE" | lolcat -F 1
pkg install git -y
clear
git clone https://github.com/JuanEGamerYT/Generator
clear
echo "Updated: OK to last version avaible" | lolcat
clear
sleep 1