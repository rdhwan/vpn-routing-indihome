# VPN-Routing-Indihome
a solution to avoid FUP charges while using VPN on Indihome using split tunnelling. (OpenWrt)
wireguard split tunneling.

## Setup
1. Install `vpn-policy-routing`
2. Set default gateway to WAN.
Make sure to disable `Route Allowed IPs` on your Wireguard interface.
3. Clone scripts to `/etc/`
Example : `/etc/vpn-policy-routing.google.user`
4. Set permission to 755 for every scripts.
Example : `chmod +x /etc/vpn-policy-routing.google.user`
5. Go to vpn-policy-routing page, create a new policy to redirect all traffic to the Wireguard interface.
Local addresses / devices.
![policies](https://github.com/rdhwan/vpn-routing-indihome/raw/main/img/policies.png)
6.  Add path to the Custom User File Includes for every scripts.
![enter image description here](https://github.com/rdhwan/vpn-routing-indihome/raw/main/img/custom_userfile.png)
7. Save and Apply.
8. Finally enable and start vpn-policy-routing service.
![enter image description here](https://github.com/rdhwan/vpn-routing-indihome/raw/main/img/enable.png)

## Checking the connection
I wrote a simple Python script to check which CDN Google use for your network.
![enter image description here](https://github.com/rdhwan/vpn-routing-indihome/raw/main/img/result.png)
There should display your *Indihome's public IP address and Telkom's CDN* instead of your VPN provider. (in my case its *pttelkom-cgk5*)
