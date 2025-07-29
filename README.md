# WizTLE: Multi-Satellite Scheduling and Tracking API

WizTLE is a tool for tracking satellite positions, particularly
built for LEO ground stations. It is the consists of a library, rest api and
server software. Making it suitable for a variety of purposes.

## Installation

### General Linux

```bash
./autoinstaller.sh
```

## Components

### wiztle-restapi

As a RESTful API it provides two endpoints **get_schedule** and **get_ptm**.

#### Usage

```bash
wiztle-restapi --port <PORTNUM>
```


### wiztle-server

Compared to the RESTful API this server software keeps most of the calculations
in memory so as to not repeat them, therefore the computational efficiency is a
lot better and it provides more endpoints for sophisticated use cases. But
currently it only supports a single request origin as it can not differentiate
between different connections.

## Troubleshooting

### Modifications to the source code are not applied

Modifications to the source code require the program to be uninstalled and
reinstalled using pip. Sometimes even after doing this some changes might not
be reflected in the program, in such cases it is best to clear the python
virtual environment and reconstruct it.

```bash
rm -r venv/
python -m venv venv
```

### pip doesn't work / externally managed system

In some linux distros system-wide pip installations are restricted by the
package manager. In such systems it is best to use a python virtual environment

```bash
python -m venv venv
```

### A certain python dependency can't be found

Remove the dependency entry from `requirements.txt` and install it
manually.

### Can't reach wiztle from outside the server

1. Make sure the chosen port is not closed/restricted.
2. Make sure the host ip in `__main__.py` files is `0.0.0.0` instead of 
`127.0.0.1`.

