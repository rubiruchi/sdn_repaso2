Este ensayo se llevo a cabo siguiendo los pasos de: 
https://docs.faucet.nz/en/latest/tutorials/first_time.html


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
