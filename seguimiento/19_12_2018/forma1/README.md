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

## Monitoreo de estadisticas de contenedores API mediante Go ##
Esta herramienta es desarrollada por **KyleBanks** y se encuentra displonible en el siguiente [enlace de github](https://github.com/KyleBanks/dockerstats). Para tratarla de poner en marcha se hizo lo siguiente:

1. Se instalo el paquete desde github?

```
go get -v github.com/KyleBanks/dockerstats
```

2. Se procedio a correr el ejemplo tal y como se sugiere en la pagina:

```
cd example
go run main.go "output.txt"
```

La salida para el caso fue la siguiente:

```
2018/12/19 15:51:33 Writing output to 'output.txt'
panic: nil

goroutine 1 [running]:
panic(0x0, 0x0)
	/usr/lib/go/src/runtime/panic.go:481 +0x3e6
main.main()
	/home/tigarto/dockerstats/example/main.go:34 +0x2c8
exit status 2
tigarto@fuck-pc:~/dockerstats/example$ 88
88: command not found

```

Al parecer el problema anterior era por la version del go. Por lo cual se procedio a actualizarla siguiendo el siguiente [enlace](https://github.com/golang/go/wiki/Ubuntu):

```bash
sudo add-apt-repository ppa:longsleep/golang-backports
sudo apt-get update
sudo apt-get install golang-go
```

Luego se volvio a probar el programa ejemplo ```sudo go run main.go "output.txt"``` empleandose ```Ctrl + C``` para salir tal y como se muestra a continuación:

```bash
tigarto@fuck-pc:~/dockerstats/example$ sudo go run main.go "output.txt"
2018/12/19 16:03:56 Writing output to 'output.txt'

^Csignal: interrupt
```

Finalmente se observa la salida del archivo **output.txt** la cual es la siguiente:

```bash
tigarto@fuck-pc:~/dockerstats/example$ cat output.txt 
2018-12-19 16:03:58.559649616 -0500 -05 m=+1.608204328: Container=8774ae727f68 Memory={Raw=2.07MiB / 7.689GiB Percent=0.03%} CPU=0.00% IO={Network=18.1kB / 0B Block=7.18MB / 0B} PIDs=1
2018-12-19 16:04:00.564749468 -0500 -05 m=+3.613304156: Container=8774ae727f68 Memory={Raw=2.07MiB / 7.689GiB Percent=0.03%} CPU=0.00% IO={Network=18.1kB / 0B Block=7.18MB / 0B} PIDs=1
2018-12-19 16:04:02.572251763 -0500 -05 m=+5.620806526: Container=8774ae727f68 Memory={Raw=2.07MiB / 7.689GiB Percent=0.03%} CPU=0.00% IO={Network=18.1kB / 0B Block=7.18MB / 0B} PIDs=1
2018-12-19 16:04:04.578296881 -0500 -05 m=+7.626851621: Container=8774ae727f68 Memory={Raw=2.07MiB / 7.689GiB Percent=0.03%} CPU=0.00% IO={Network=18.1kB / 0B Block=7.18MB / 0B} PIDs=1
2018-12-19 16:04:06.58629403 -0500 -05 m=+9.634848838: Container=8774ae727f68 Memory={Raw=2.07MiB / 7.689GiB Percent=0.03%} CPU=0.00% IO={Network=18.1kB / 0B Block=7.18MB / 0B} PIDs=1
2018-12-19 16:04:08.593388684 -0500 -05 m=+11.641943299: Container=8774ae727f68 Memory={Raw=2.07MiB / 7.689GiB Percent=0.03%} CPU=0.00% IO={Network=18.1kB / 0B Block=7.18MB / 0B} PIDs=1
2018-12-19 16:04:10.600496022 -0500 -05 m=+13.649050795: Container=8774ae727f68 Memory={Raw=2.07MiB / 7.689GiB Percent=0.03%} CPU=0.00% IO={Network=18.1kB / 0B Block=7.18MB / 0B} PIDs=1
2018-12-19 16:04:12.60576884 -0500 -05 m=+15.654323453: Container=8774ae727f68 Memory={Raw=2.07MiB / 7.689GiB Percent=0.03%} CPU=0.03% IO={Network=18.1kB / 0B Block=7.18MB / 0B} PIDs=1
2018-12-19 16:04:14.612790194 -0500 -05 m=+17.661344947: Container=8774ae727f68 Memory={Raw=2.07MiB / 7.689GiB Percent=0.03%} CPU=0.00% IO={Network=18.1kB / 0B Block=7.18MB / 0B} PIDs=1
```


## Obtener las estadisticas de los contenedores mediante APIs ##

1. https://medium.com/devopslinks/monitoring-docker-with-python-domonit-34440b8c6830
2. https://github.com/docker/docker-py
3. https://github.com/docker/docker-py/issues/1546


## Referencias ##
1. [docker stats](https://docs.docker.com/engine/reference/commandline/stats/)
2. [Runtime metrics](https://docs.docker.com/config/containers/runmetrics/)
3. [docker container stats](https://docs.docker.com/engine/reference/commandline/container_stats/)
4. [Docker Stats (Memory, CPU, etc.) in JSON Format](https://kylewbanks.com/blog/docker-stats-memory-cpu-in-json-format)
5. [Enhanced docker stats command with total amount of RAM and CPU](https://stackoverflow.com/questions/47331106/enhanced-docker-stats-command-with-total-amount-of-ram-and-cpu)
