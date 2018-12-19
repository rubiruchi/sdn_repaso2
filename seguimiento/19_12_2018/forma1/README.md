# Monitoreo de contenedores #

## Monitoreo empleando docker stats ##

Se llevaron a cabo los siguientes pasos como caso de uso:

1. Ser ejecuto un contenedor.

```bash
sudo docker run --rm --name host1 -h host1 -it ubuntu:trusty bash
```

2. Mirar con el comando docker stats (en consola las estadisticas)

```bash
sudo docker stats
```

La anterior forma despliega en tiempo real el uso de los recursos por contenedor. Sin embargo existen opciones para que solo se haga una
captura como la opcion ```--no-stream``` a continuacion se muestra un ejemplo y su respectiva salida:

```bash
CONTAINER ID        NAME                CPU %               MEM USAGE / LIMIT     MEM %               NET I/O             BLOCK I/O           PIDS
b947cb94afb4        couchbase           4.12%               396.8MiB / 7.689GiB   5.04%               9.59kB / 0B         0B / 1.02MB         220
```

## Monitoreo de contenedores mediante el docker remote API ##

Inicialmente se debe habilitar este API en un host. Para entender el proceso nos basamos en los siguientes enlaces:
1. [How to enable docker remote API on docker host?](https://medium.com/@ssmak/how-to-enable-docker-remote-api-on-docker-host-7b73bd3278c6)
2. [How do I enable the remote API for dockerd](https://success.docker.com/article/how-do-i-enable-the-remote-api-for-dockerd)

Los pasos fueron:
1. Editar el archivo **docker.service** ubicado en **/lib/systemd/system**:

```bash
cd /lib/systemd/system
sudo gedit docker.service
```
2. Actualizar la variable **ExecStart** al siguiente valor **/usr/bin/dockerd -H unix:// -H tcp://0.0.0.0:2376**: 

```
ExecStart=/usr/bin/dockerd -H unix:// -H tcp://0.0.0.0:2376
```

3. Guardar cambios.
4. Reoad el demonio docker:

```bash
sudo systemctl daemon-reload
```

5. Reiniciar el contenedor:

```bash
sudo service docker restart
```
6. Si todo esta bien puede ejecutar en el navegador la ruta **http://localhost:2376/images/json** y se deberia mostrar un archivo json asociado a las imagenes. Tambien de forma alterna se puede emplear el comando **curl http://localhost:2376/images/json** y este resultado sera mostrado en consola.

7. Para obtener las estadisticas tenemos el siguiente comando basico **http://localhost:2376/containers/ID_CONTAINER/stats**. Suponiendo para el caso que el **ID_CONTAINER** del contenedor asociado a la imagen ubuntu:trusty (previamente ejecutado es) **b91f79693dbf**. Se tiene los posibles comandos para obtener las estadisticas son:

   * **Forma 1**: En el navegador.
   
   ```
     http://localhost:2376/containers/b91f79693dbf/stats
   ```
   
   * **Forma 2**: En la consola.
   
   ```bash 
     curl http://localhost:2376/containers/b91f79693dbf/stats
   ```

## Referencias ##
1. [docker stats](https://docs.docker.com/engine/reference/commandline/stats/)
2. [Runtime metrics](https://docs.docker.com/config/containers/runmetrics/)
3. [docker container stats](https://docs.docker.com/engine/reference/commandline/container_stats/)
4. [Docker Stats (Memory, CPU, etc.) in JSON Format](https://kylewbanks.com/blog/docker-stats-memory-cpu-in-json-format)
5. [Enhanced docker stats command with total amount of RAM and CPU](https://stackoverflow.com/questions/47331106/enhanced-docker-stats-command-with-total-amount-of-ram-and-cpu)
