pkg update -y
pkg upgrade -y
pkg install python
pip install --upgrade pip
pkg install lolcat
sleep 4
figlet JuanE |lolcat -F 1
clear
figlet J-Tools |lolcat -F 1
clear
echo "Speaking? Hablas? (1) English o (2) Español"
read opcion

if [ $opcion -eq 1 ]; then
    python generator.py
elif [ $opcion -eq 2 ]; then
    python generador.py
else
    echo "Opción inválida. Por favor ingresa 1 para inglés o 2 para español."
    echo "Invalid option. Please enter 1 for English or 2 for Spanish."
fi

