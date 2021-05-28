# auto_crypto

Yes, this could all be combined differently, but I like to mix shell and python.

# build/run
copy the crypto.env.template to crypto.env and update with your information

```
docker build -t auto_crypto .
```

```
docker run --rm --name crypto auto_crypto
```

# files

crypto.env - rename from crypto.env.template and fill in - used by shell script to execute what you want
exec_crypto.sh - simple shell script to simplify the deposits and buying
crypto.py - simple wrapper around the wrapper for coinbase pro ... using the cbpro python library

