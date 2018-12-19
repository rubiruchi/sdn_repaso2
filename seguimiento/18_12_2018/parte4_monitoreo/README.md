# Containernet + Ryu (Full container) + Instrumentación#

Para correr ejecute los siguientes comandos, cada uno en una consola diferente:

1. Ejecute el controlador:

   * Inicie el contenedor asociado al controlador ryu:

     ```bash
     sudo docker run -h c0 --name c0 -p 6633:6633 -it --rm sonatanfv/sonata-ryu-vnf /bin/bash
     ```
   * Inicie la aplicacion que ejecutara el controlador ryu:

     ```bash
     cd ryu
     ryu-manager --ofp-tcp-listen-port 6633 ryu/app/simple_switch_13.py 
     ```

**Nota**: $POX_HOME es la ruta del directorio del controlador pox.

2. Ejecute la topologia:

```bash
sudo python topo_test.py 
```

3. Hacer las pruebas en mininet.

###TODO: Configuración y puesta en marcha de la instrumentación###
