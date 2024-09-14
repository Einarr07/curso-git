# Curso de git por soy dalto

Git es un sistema de control de versiones donde encontraremos 3 areas de desarrollo las cuales son:
1) El área de trabajo.
2) El área de staging area.
3) El repositorio.

## Principiante

### Configuración inicial
Git tiene tres niveles de configuración que determinan el alcance de las configuraciones aplicadas:

- **Alcance local:** Este es el repositorio en el que estamos trabajando, es decir, la carpeta del proyecto.
```
git config --local 
```
- **Alcance global:** Las configuraciones son aplicables a todos los repositorios de un usuario en una máquina específica.
```
git config --global user.name "nombre_usuario"
```
```
git config --global user.email "example@gmail.com"
```
- **Alcance system:** Las configuraciones se aplican a todos los usuarios de la máquina. Estas configuraciones son menos comunes y requieren permisos administrativos para ser modificadas.
```
git config --system 
```
---
Para ver la lista de configuraciones utilizamos:
```
git config --list
```
Y si quisiéramos ver la lista de configuraciones globales utilizamos:
```
git config --global --list
```
---
Configuración de un editor de código, en este caso se configura Visual Studio Code como el editor predeterminado:

```
git config --global core.editor "code --wait"
```

Configuración de la salida de pantalla de Git para que sea colorida:
```
git config --global color.ui true
```
Esta configuración es para el "carriage return" al trabajar en diferentes sistemas operativos:
- Windows
```
git config --global core.autocrlf true
```
- Linux/Mac
```
git config --global core.autocrlf input
```

### ADD y commits
1) Para poder iniciar y trabajar dentro de un proyecto en git debemos utilizar el comando:
```
git init
```
Este comando lo que hace es crear una **carpeta oculta** donde se implementa los detalles de configuracion.

2) Una vez que este inicializado nuestro proyecto ya podemos agregar archivos a nuestra area de preparación con los siguientes comandos:
- Para subir todos los archivos
```
git add .
```
- Para subir un archivo especifico
```
git add nombre_del_archivo.txt
```
- Para subir diferentes archivos en 1 solo comando
```
git add archivo1.py, archivo2.java, archivo3.txt
```

3) Para verificar el estado de nuestro git utilizaremos:
- Forma convencional
```
git status
```
- Forma simplificada
```
git status -s
```


4) Si queremos eliminar algun archivo antes de realizar un commit utilizaremos
```
git rm --cached nombre_del_archivo.txt
```

5) Para subir lo que tenemos agregado en nuestra área de preparación al repositorio utilizamos un commit
- Mensaje corto
```
git commit -m "Comentraio"
```
- Mensaje largo
```
git commit
```
- Para hacer un commit directamente al repositorio y saltarnos el área de preparación:
```
git commit -m "comentario" -a
```

### Git restore, checkout y más
1) Si eliminamos un archivo y lo queremos recuperar del área de preparación utilizamos:
```
git restore nombre_del_archivo.txt
```
2) Para volver hacia la ultima vez que guardamos los cambios utilizamos:
```
git checkout nombre_del_archivo.txt
```
3) Si ya subimos nuestro archivo al área de preparación pero queremos volver a una versión anterior utilizamos **(Descarta los cambios)**:
```
git reset --hard
```
4) Cambio de nombre de un archivo
```
git mv nombre_del_archivo.txt nuevo_nombre.txt
```

### Git diff y historial de commits
1) Para verificar los cambios que hicimos en comparación con los commits utilizamos:
```
git show nombre_del_archivo.txt
```
2) Comparar cambios en el área de preparación con el ultimo commit utilizamos:
```
git diff --staged
```
3) Historial de commits
- Versión completa
```
git log
```
- Versión reducida
```
git log --oneline
```
- Los identificadores de los commits pueden llegar a repetirce si tenemos un repositorio muy grande en ese caso nosotros tenemos que configurarlo manualmente con el siguiente comando, donde el número 9 va a hacer la cantidad de valores del identificador, para repositorios pequeños con 5 o 7 esta perfecto
```
git config --globla core.abbrev 9
```
4) Comparar entre commits
(4427b y 9ccc3 son el identificador del historial del commit con el que realizamos la comparación)
- Cambio de nombres
```
git diff --name-only 4427b 9ccc3
```
- Cambio de lineas
```
git diff --word-diff 4427b 9ccc3
```

### Modificar commits y deshacer commits

1) Comando para modificar el ultimo commit
2) Modificar y agregar un nuevo archivo.
- Lo primero que debemos hacer es agg el archivo al area de preparación, tanto el modificado como el que deseamos agregar y utilizamos el comando: 
```
git commit --amend
```
3) Para deshacer un commit debemos poner el HEAD en una versión anterior y para esto tenemos diferentes opciones.
Nota: después de la palabra reservada (soft-mixed-hard) va el hash del commit.
- Nº1 Esta opción nos regrese al punto que elejimos mediante el hash y todos los archivos que teniamos después de realizar ese commit se dirigen al área de preparación (staging area).
```
git reset --soft 45a55fc2
```
También se puede utilizar la notación relativa utilizando head~**numero**, el número representa cuantos espacios se va a desplazar hacia atras dependiendo la posición del head
```
git reset --soft head~1
```
- Nº2 Esta nos permite mantener nuestra área de trabajo intacta. *No* envia los archivos que estaban en el commit al área de preparación.
```
git reset --mixed d5r8e6d
```
- Nº3 Este comando sobre escribe todos los archivos y nos lo evia a nuestra área de trabajo, **si teniamos cambios los perdemos y de igual forma si teniamos archivos en el área de preparación.**
```
git reset --hard djf23d2j
```