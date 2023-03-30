pkg update
pkg upgrade -y
pkg install python
pip install --upgrade pip
pkg install lolcat
sleep 4
figlet "JuanE" |lolcat -F 1
echo " ¿Que idioma Hablas? | What is your language? "
echo " (1) English | (2) Español "
read opcion

if [ $opcion -eq 1 ]; then
    clear
    figlet "JuanE" | lolcat -F 1
    cd Generator
    python generator.py
elif [ $opcion -eq 2 ]; then
    clear
    figlet "JuanE" | lolcat -F 1
    cd generator
    python generador.py
else
    clear
    figlet "JuanE" | lolcat -F 1
    echo "Opción inválida. Por favor ingresa 1 para inglés o 2 para español."
    echo "Invalid option. Please enter 1 for English or 2 for Spanish."
fi

sleep 1
exit
esac
