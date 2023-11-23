# Pebble Authentication Client for NodeJS

## Introduction

This library offer a client for authenticate user and licence management 
written in Python compatible with may python API Server.

## Installation

### Requirements

The following procedures explains the installation of the following packages :

- Python 3.9 or higher
- pip (provided with Python package)
- PyJWT (tested with version 2.8.0)
- cryptography (tested with version 41.0.5)

### Solution 1 : requirement.txt configuration

The best way to ensure that the correct version of all modules are correctly 
installed for your project is to use a requirement.txt file :

```
cryptography==41.0.5
PyJWT==2.8.0
```

Then run the following on your project :

```Shell
pip install -r requirements.txt
```

### Solution 2 : Local installation

Check python3 is properly installed on your local machine (with pip working), 
then run the following in the application directory.

```Shell
pip install cryptography PyJWT
```

### Solution 3 : Dockerfile configuration

Add the following in your Dockerfile after the initialization of docker image 
and the implementation of Python3 in the docker container :

```Dockerfile
RUN pip install cryptography PyJWT
```

_Dockerfile example_

WARNING : This is an example in order to explain when you have to run the pip
install command. Your own Dockerfile should vary from this configuration.

```Dockerfile
# syntax=docker/dockerfile:1.2
FROM ubuntu:20.04
RUN apt-get update && apt-get install -y python3.9 python3.9-dev
RUN pip install cryptography PyJWT
COPY . .
CMD ["python"]
```

## Usage

### Configuration

Before you can work with the library, you must define to a system environment 
variable the URI were is stored the public Json Web Key Set (JWKS file).

This file will be requested and store **temporary** on your API Server.
Your server should be able to write on _./var/credentials/auth/jwks.json_ .
If the file does not exist, it will be created.

**If you start your server directly from a terminal, run this command on
your terminal before starting your server :**

```Shell
export PBL_JWKS_REMOTE_URI=https://SERVER_URI/path/jwks.json
```

**If you start your server within a Docker container, you should add this
line to your Dockefile :**

```Dockerfile
RUN export PBL_JWKS_REMOTE_URI=https://SERVER_URI/path/jwks.json
```

### Test keys pair

**Warn :** These key files are not secured and must be used FOR TESTING PURPOSE 
ONLY on a local development environment !

**JWKS URI (for PBL_JWKS_REMOTE_URI environment variable)**

https://storage.googleapis.com/pebble-public-cdn/test_auth/jwks_test.json

**Public and private keys used to sign a token**

https://storage.googleapis.com/pebble-public-cdn/test_auth/public_test.pem

https://storage.googleapis.com/pebble-public-cdn/test_auth/private_test.pem

### Authenticate with token string

Content will be published soon.

### Authenticate with HTTP Authorization header

This might work only if an Authorization header has been sent in the current 
client request. Authorization header must start with _Bearer_ string followed by
a valid JWT.

Content will be published soon.