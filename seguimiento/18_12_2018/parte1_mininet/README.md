# Mininet + POX #

Para correr ejecute los siguientes comandos, cada uno en una consola diferente:

1. Ejecute el controlador:
```bash
cd $POX_HOME
./pox.py log.level --DEBUG openflow.of_01 --port=6653 forwarding.l2_learning 
```
**Nota**: $POX_HOME es la ruta del directorio del controlador pox.

2. Ejecute la topologia:

```bash
sudo python topo_test.py 
```

3. Hacer las pruebas en mininet.
