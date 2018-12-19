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

## Referencias ##
1. [docker stats](https://docs.docker.com/engine/reference/commandline/stats/)
2. [Runtime metrics](https://docs.docker.com/config/containers/runmetrics/)
3. [docker container stats](https://docs.docker.com/engine/reference/commandline/container_stats/)
4. [Docker Stats (Memory, CPU, etc.) in JSON Format](https://kylewbanks.com/blog/docker-stats-memory-cpu-in-json-format)
5. [Enhanced docker stats command with total amount of RAM and CPU](https://stackoverflow.com/questions/47331106/enhanced-docker-stats-command-with-total-amount-of-ram-and-cpu)
