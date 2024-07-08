# Start the virtual hil setup

With this compose file it is possible to start a virtual three machine hardware in the loop.

bamboo <---> tester <---> target

One is the Agent, one is the testing platform (tester) and one ist the unit under test (target).

## Installation

First you need to install the virtual network with following command:

```bash
podman network create --subnet 20.0.0.0/16 mars
```

Adapt Network Config (rootless: ~/.config/cni/net.d/mars.conflist) from Version 1.0.0 to 0.4.0.

Then create a id_rsa file for the internal ssh communication:
```bash
ssh-keygen -t rsa -f ./id_rsa -q -N ""
```

To install the images use following command

```bash
podman-compose -f cicd_sim.yaml build
```

## Usage

Start the container.

```bash
podman-compose -f cicd_sim.yaml up
```

Then you can attache to each virtuel system with following command:
```bash
podman attach bamboo
```

```bash
podman attach tester
```

```bash
podman attach target
```

To enable the ssh daemon within the container please run following:

```bash
podman exec bamboo service ssh start
```

```bash
podman exec tester service ssh start
```

```bash
podman exec target service ssh start
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)