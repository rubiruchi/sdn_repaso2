# Trabajo realizado #

## Resumen de la actividad ##
Se procederá a montar un entorno virtual de desarrollo sencillo en el cual se ejecute faucet siguiendo los pasos descritos en: https://inside-openflow.com/2016/08/23/faucet-virtual-infrastructure/. 


## Suposiciones ##
1. Se asume que ya se tiene instalado prometheus y grafana. Si esto aun no se cumple revisar los pasos descritos en: https://docs.faucet.nz/en/latest/tutorials/first_time.html
2. Hay detalles que cambian un poco respecto al tutorial que se sigue pues la version que se ejecula localmente es mas nueva.

# Instalación de Faucet en un entorno virtual #

## Instalación del entorno virtual ## 

En la [pagina seguida](https://inside-openflow.com/2016/08/23/faucet-virtual-infrastructure)

1. Instalar el entorno virtual:

```
# Install VirtualEnv (venv)
sudo apt install python-virtualenv

# Go to our workspace and setup the local venv
cd ~/ofworkspace
virtualenv venv

# Activate the venv
. ./venv/bin/activate
```

En nuestro caso, este procedimiento se llevo a cabo usando pycharm. A continuación se muestra como:
  1. Se crea un nuevo proyecto en pycharm:
  
  ![new_project](py_charm01.png)


2. En el directorio en el cual se vaya a trabajar clonar el repositorio del faucet:





