# Analizando sdn-cockpit: Open-source teaching framework for software-defined networking (SDN) # 

## Introducción ##

Esta plataforma educativa es de extrema utilidad para propositos de entrenamiento y en el caso dado para el desarrollo gradual
de la aplicación solución en el controlador, sea cual sea la necesidad; seguridad en nuestro caso. Conviene revisar los siguientes
enlaces:
1. [Teaching network softwarization with SDN Cockpit: An open ecosystem for students, network administrators and others](https://dl.gi.de/bitstream/handle/20.500.12116/16581/DFN-Forum-Proceedings-008.pdf?sequence=1&isAllowed=y)
2. [Teaching network softwarization with SDN Cockpit](https://www.dfn.de/fileadmin/7Veranstaltungen/Technologieforum/2018/Folien_Vortraege/TF_2108_Teaching_Network_Softwarization_Heseding.pdf)
3. [Repositorio github de sdn-cockpit](https://github.com/kit-tm/sdn-cockpit)

## Instalacion ##

En el [repositorio github de sdn-cockpit](https://github.com/kit-tm/sdn-cockpit) se muestran los pasos, estos basicamente se redujeron a:

1. Clonar el repositorio: 

```bash
cd ~
git clone https://github.com/kit-tm/sdn-cockpit.git
cd sdn-cockpit
```

2. Arrancar la maquina virtual (se debe estar en la carpeta sdn-cockpit que es donde se encuentra el vagrantfile):

```bash
vagrant up
```

3. Acceder a la maquina virtual por ssh (se debe estar en la carpeta sdn-cockpit): 

```bash
vagrant ssh
```
4. Se llama el script run.sh:

```bash
# listando el directorio actual
ls
cwd  local  __mn_ready  remote  run.sh  templates  tmp_result_1545279556.93.yaml  tmp_topology.mn

# Ejecutando el script
./run.sh
```

5. Si todo esta bien aparece la siguiente interfaz de prueba:

![interfaz1]()




