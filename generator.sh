figlet "Generator" | lolcat
echo "by JuanEGamerYT" | lolcat
echo "   "

# Preguntar al usuario qué idioma habla
echo "Do you speak English or Spanish? / ¿Hablas Ingles o Español?"
echo "  "
echo "Coloca el idioma tal esta escrito en la pregunta."
echo "  "
echo "Put the language as it is written in the question."
echo "  "
echo "↓"
read lang
clear

if [ "$lang" == "Spanish" ] || [ "$lang" == "Español" ]; then
  # Preguntar al usuario cuántas combinaciones quiere generar
  figlet "Generator" | lolcat
  echo "by JuanEGamerYT" | lolcat
  echo "   "
  echo "¿Cuántas combinaciones desea generar?"
  echo "↓"
  read num_combinations
  echo "  "

  # Preguntar al usuario qué opción quiere elegir
  echo "¿Quiere hacer combinaciones aleatorias o usar un diccionario?"
  echo "1. Combinaciones aleatorias"
  echo "2. Usar un diccionario para hacer combinaciones"
  echo "  "
  echo "↓"
  read option
  clear

  if [ "$option" == "1" ]; then
    # Ejecutar generador.py en el directorio Generators
    figlet "Generator" | lolcat
    echo "by JuanEGamerYT" | lolcat
    echo "   "
    cd Generators
    python generador.py $num_combinations
  elif [ "$option" == "2" ]; then
    # Ejecutar diccionario.py
    figlet "Generator" | lolcat
    echo "by JuanEGamerYT" | lolcat
    echo "   "
    python diccionario.py $num_combinations
  else
    echo "Opción inválida. Inténtelo de nuevo."
  fi

elif [ "$lang" == "English" ] || [ "$lang" == "Ingles" ]; then
  # Preguntar al usuario cuántas combinaciones quiere generar
  figlet "Generator" | lolcat
  echo "by JuanEGamerYT" | lolcat
  echo "   "
  echo "How many combinations do you want to generate?"
  echo "  "
  echo "↓"
  read num_combinations
  echo "  "

  # Preguntar al usuario qué opción quiere elegir
  echo "Do you want to generate random combinations or use a dictionary to random combinations?"
  echo "1. Random combinations"
  echo "2. Use a dictionary to random combinations"
  echo "  "
  echo "↓"
  read option
  clear

  if [ "$option" == "1" ]; then
    # Ejecutar generator.py en el directorio Generator
    figlet "Generator" | lolcat
    echo "by JuanEGamerYT" | lolcat
    echo "   "
    cd Generator
    python generator.py $num_combinations
  elif [ "$option" == "2" ]; then
    # Ejecutar dictionary.py
    figlet "Generator" | lolcat
    echo "by JuanEGamerYT" | lolcat
    echo "   " 
    python dictionary.py $num_combinations
  else
    echo "Invalid option. Please try again."
  fi

else
  echo "Invalid language. Please try again. / Idioma inválido. Inténtelo de nuevo."
fi

