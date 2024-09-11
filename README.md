# Curso de git por soy dalto

Git es un sistema de control de versiones donde encontraremos 3 areas de desarrollo las cuales son:
1) El area de desarrollo 
2) El area de trabajo
3) El repositorio

## Principiante

### Configuración inicial
Alcance local: Este es el repositorio en el que estamos trabajando, es decir, la carpeta del proyecto
```
git config --local 
```
Alcance global: Aplica para todos los repositorios de un usuario
```
git config --global user.name "nombre_usuario"
```
```
git config --global user.email "example@gmail.com"
```
Alcance system: 
```
git config --system 
```
---
Para ver la lista de configuraciones utilizamos
```
git config --list
```
y si quisieramos ver la lista de configuraciones globales utilizamos:
```
git config --global --list
```
---
Configuración de un editor de código, en este caso se configura Visual Studio Code:

```
git config --global core.editor "code --wait"
```

Configuración de la salida de pantalla de git
```
git config --global color.ui true
```
Esta configuración es para el carriage return
- Windows
```
git config --global core.autocrlf true
```
- Linus/Mac
```
git config --global core.autocrlf input
```