# Setup static IP address on Fedora

Do all of these commands below as a root user.

- List all connections

```bash
nmcli connection show
# Or
nmcli con show
```

- Set up IPv4 addresses

```bash
nmcli connection modify interface-name ipv4.addresses new-address/subnet-mask
# or
nmcli con mod interface-name ipv4.addresses new-address
```

- Set up IPv4 gateway

```bash
nmcli connection modify interface-name ipv4.gateway new-address
# or
nmcli con mod interface-name ipv4.gateway new-address
```

- Set up IPv4 method

Note: method-name could be `manual` for manual configuration.

```bash
nmcli connection modify interface-name ipv4.method method-name
# or
nmcli con mod interface-name ipv4.method method-name
```

- Restart connection

```bash
nmcli connection up interface-name
nmcli connection down interface-name
# or
nmcli con up interface-name
nmcli con down interface-name
```

- Auto connection

```bash
nmcli connection modify interface-name connection.autoconnect yes
# or
nmcli con mod interface-name connection.autoconnect yes
```