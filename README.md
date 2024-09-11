# Curso de git por soy dalto

Git es un sistema de control de versiones donde encontraremos 3 areas de desarrollo las cuales son:
1) El area de trabajo.
2) El area de stashing.
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
