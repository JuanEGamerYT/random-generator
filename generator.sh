sleep 4
figlet "JuanE" |lolcat -F 1
#!/bin/bash

# Preguntar al usuario qué idioma habla
echo "Do you speak English or Spanish? / ¿Hablas Inglés o Español?"
echo "  "
echo " ---Debes intruducir Español o Ingles (tal cual esta escrito arriba)"
echo "  "
echo " ---You must enter Spanish or English (as written above)" 
echo "↓"
read lang

clear 

if [ "$lang" == "Spanish" ] || [ "$lang" == "Español" ]; then
  # Preguntar al usuario qué opción quiere elegir
  figlet "JuanE" | lolcat
  echo "  "
  echo "¿Quiere hacer combinaciones aleatorias o usar un diccionario?"
  echo "1. Hacer combinaciones aleatorias"
  echo "2. Usar un diccionario para las combinaciones"
  echo "  "
  echo ">"
  read option

  if [ "$option" == "1" ]; then
    # Ejecutar generador.py en el directorio Generators
    cd Generator
    python generador.py
  elif [ "$option" == "2" ]; then
    # Ejecutar diccionario.py
    cd Generator
    python diccionario.py
  else
    echo "Opción inválida. Inténtelo de nuevo"
  fi

elif [ "$lang" == "English" ] || [ "$lang" == "Inglés" ]; then
  # Preguntar al usuario qué opción quiere elegir
  figlet "JuanE" | lolcat
  echo "  "
  echo "Do you want to generate random combinations or use a dictionary?"
  echo "1. Make random combinations"
  echo "2. Use dictionary to make combinations"
  echo "  "
  echo "> "
  read option

  if [ "$option" == "1" ]; then
    # Ejecutar generator.py en el directorio Generator
    figlet "JuanE" | lolcat
    echo "  "
    cd Generator
    python generator.py
  elif [ "$option" == "2" ]; then
    # Ejecutar dictionary.py
    figlet "JuanE" | lolcat
    echo "  "
    cd Generator
    python dictionary.py
  else
    echo "Invalid option. Please try again."
  fi

else
  echo "Invalid language. Please try again. / Idioma inválido. Inténtelo de nuevo."
fi
