Este ensayo se llevo a cabo siguiendo los pasos de: 
https://docs.faucet.nz/en/latest/tutorials/first_time.html

Instlaion:

```bash
sudo apt-get install curl gnupg apt-transport-https lsb-release
echo "deb https://packagecloud.io/faucetsdn/faucet/$(lsb_release -si | awk '{print tolower($0)}')/ $(lsb_release -sc) main" | sudo tee /etc/apt/sources.list.d/faucet.list
curl -L https://packagecloud.io/faucetsdn/faucet/gpgkey | sudo apt-key add -
sudo apt-get update
```
```bash
sudo apt-get install faucet-all-in-one
```

OK..

La parte de grafana jodio:

```bash
tigarto@fuck-pc:~$ sudo systemctl restart prometheus
tigarto@fuck-pc:~$ sudo systemctl daemon-reload
tigarto@fuck-pc:~$ sudo systemctl enable grafana-server
Synchronizing state of grafana-server.service with SysV init with /lib/systemd/systemd-sysv-install...
Executing /lib/systemd/systemd-sysv-install enable grafana-server
insserv: warning: script 'sonata' missing LSB tags and overrides
insserv: warning: script 'sonata' missing LSB tags and overrides
tigarto@fuck-pc:~$ sudo systemctl stop grafana-server
tigarto@fuck-pc:~$ sudo systemctl start grafana-server
tigarto@fuck-pc:~$ sudo systemctl enable grafana-server
Synchronizing state of grafana-server.service with SysV init with /lib/systemd/systemd-sysv-install...
Executing /lib/systemd/systemd-sysv-install enable grafana-server
insserv: warning: script 'sonata' missing LSB tags and overrides
insserv: warning: script 'sonata' missing LSB tags and overrides

```
La solucion fue con una parada

En el paso 3 es donde me quedo....

cuando doy 

faucet --verbose

sale esto:

```
tigarto@fuck-pc:~$ faucet --verbose
loading app faucet.faucet
Traceback (most recent call last):
  File "/usr/local/bin/ryu-manager", line 11, in <module>
    load_entry_point('ryu==4.24', 'console_scripts', 'ryu-manager')()
  File "/usr/local/lib/python2.7/dist-packages/ryu/cmd/manager.py", line 98, in main
    app_mgr.load_apps(app_lists)
  File "/usr/local/lib/python2.7/dist-packages/ryu/base/app_manager.py", line 415, in load_apps
    cls = self.load_app(app_cls_name)
  File "/usr/local/lib/python2.7/dist-packages/ryu/base/app_manager.py", line 392, in load_app
    mod = utils.import_module(name)
  File "/usr/local/lib/python2.7/dist-packages/ryu/utils.py", line 108, in import_module
    return importlib.import_module(modname)
  File "/usr/lib/python2.7/importlib/__init__.py", line 37, in import_module
    __import__(name)
ImportError: No module named faucet.faucet
```


Error:
```bash
tigarto@fuck-pc:/lib/systemd/system$ sudo systemctl status faucet
● faucet.service - "Faucet OpenFlow switch controller"
   Loaded: loaded (/lib/systemd/system/faucet.service; enabled; vendor preset: enabled)
   Active: failed (Result: start-limit-hit) since lun 2018-12-24 01:04:08 -05; 31min ago
     Docs: https://docs.faucet.nz
  Process: 7496 ExecReload=/bin/kill -HUP $MAINPID (code=exited, status=0/SUCCESS)
  Process: 7554 ExecStart=/usr/bin/faucet --ryu-config-file=${FAUCET_RYU_CONF} --ryu-ofp-tcp-listen
 Main PID: 7554 (code=exited, status=1/FAILURE)

dic 24 01:04:07 fuck-pc systemd[1]: faucet.service: Unit entered failed state.
dic 24 01:04:07 fuck-pc systemd[1]: faucet.service: Failed with result 'exit-code'.
dic 24 01:04:08 fuck-pc systemd[1]: faucet.service: Service hold-off time over, scheduling restart.
dic 24 01:04:08 fuck-pc systemd[1]: Stopped "Faucet OpenFlow switch controller".
dic 24 01:04:08 fuck-pc systemd[1]: faucet.service: Start request repeated too quickly.
dic 24 01:04:08 fuck-pc systemd[1]: Failed to start "Faucet OpenFlow switch controller".
dic 24 01:04:08 fuck-pc systemd[1]: faucet.service: Unit entered failed state.
dic 24 01:04:08 fuck-pc systemd[1]: faucet.service: Failed with result 'start-limit-hit'.
dic 24 01:29:48 fuck-pc systemd[1]: faucet.service: Unit cannot be reloaded because it is inactive.
tigarto@fuck-pc:/lib/systemd/system$ clear
```

solucion: 

```bash
tigarto@fuck-pc:/lib/systemd/system$ sudo systemctl stop faucet
tigarto@fuck-pc:/lib/systemd/system$ sudo systemctl disable faucet
Removed symlink /etc/systemd/system/multi-user.target.wants/faucet.service.
tigarto@fuck-pc:/lib/systemd/system$ sudo systemctl enable faucet
Created symlink from /etc/systemd/system/multi-user.target.wants/faucet.service to /lib/systemd/system/faucet.service.
tigarto@fuck-pc:/lib/systemd/system$ 
```
