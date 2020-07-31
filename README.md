sensitivity-app


### FAQ
> Pipenv fails to install psycopg2

```
export LDFLAGS="-L/usr/local/opt/openssl/lib" export CPPFLAGS="-I/usr/local/opt/openssl/include" 
```

After whihc, run pipenv install psycopg2 as per discussed [here](https://github.com/pypa/pipenv/issues/3991)

