# Pebble Authentication Client for NodeJS

## Introduction

This library offer a client for authenticate user and licence management 
written in Python compatible with may python API Server.

## Installation

Installation instruction will be published soon

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