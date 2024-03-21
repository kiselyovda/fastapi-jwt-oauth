# How to generate private and public keys

## Private key

```bash
openssl genrsa -out <name-private-key>.pem 2048
```

## Public key
> [!NOTE]
>
> Only after [Private key](#private-key)

```bash
openssl rsa -in <name-private-key>.pem -outform PEM -pubout -out <name-public-key>.pem
```

```bash
mkdir credentials
mv <name-private-key>.pem <name-private-key>.pem credentials
```
