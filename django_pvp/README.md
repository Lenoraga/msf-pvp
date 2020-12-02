# Django App


## Docker

### Build image

```
docker build -t msf-api --file Dockerfile .
```


### Create volume
```
docker volume create --name=dbdata
```

### Login into container
```
docker exec -it msf_api_1 bash
```
