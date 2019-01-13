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

```bash
# Install VirtualEnv (venv)
sudo apt install python-virtualenv

# Go to our workspace and setup the local venv
cd ~/ofworkspace
virtualenv venv

# Activate the venv
. ./venv/bin/activate
```

En nuestro caso, este procedimiento se llevo a cabo usando pycharm, por lo que los pasos anteriores no se ejecutaron. A continuación se muestra como:

**Paso 1**: Se crea un nuevo proyecto y un nuevo entorno virtual en pycharm:
  
![new_project](py_charm01.png)

El resultado del paso anterior es el siguiente:

![project](py_charm02.png)

2. En el directorio en el cual se vaya a trabajar instalar faucet tal y como se muestra en el siguiente [enlace](https://docs.faucet.nz/en/latest/installation.html#faucet-pip-install):

```bash
# Installation via pip
pip3 install git+https://github.com/faucetsdn/faucet.git
```

**Paso 2**: La aplicación del comando se muestra en la consola de pycharm:

![pip_install](py_charm03.png)

Una vez el resultado se completa salío algo como lo siguiente:

![pip_listo](py_charm04.png)

3. En los directorios /venv/etc/faucet y /venv/var/faucet, se ubicaran los archivos de configuración y los logs de faucet respectivamante. La siguiente figura muestra esto en el arbol de directorios de faucet. Para el caso se despliega el contenido del archivo de configuración faucet.yml:

![faucet_config](py_charm05.png)






