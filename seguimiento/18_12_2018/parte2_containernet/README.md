# Containernet + Ryu #

Para correr ejecute los siguientes comandos, cada uno en una consola diferente:

1. Ejecute el controlador:

```bash
ryu-manager --ofp-tcp-listen-port 6653 simple_switch_13.py 
```

**Nota**: $POX_HOME es la ruta del directorio del controlador pox.

2. Ejecute la topologia:

```bash
sudo python topo_test.py 
```

3. Hacer las pruebas en mininet.


Controlador: 
ryu-manager --ofp-tcp-listen-port 6653 simple_switch_13.py 
Para correr: 
sudo python topo_test.py 
'''
