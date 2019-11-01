# OpenBrokerAPI Skeleton

Basic skeleton to implement a service broker with [openbrokerapi](https://openbrokerapi.readthedocs.io/)

## What to implement

| Feature                            | Method                                     |
|------------------------------------|--------------------------------------------|
| Register service broker            | `catalog`                                  |
| Visible in marketplace             | `catalog`                                  |
| Create service                     | `provision`                                |
| Bind service                       | `bind`                                     |
| Unbind service                     | `unbind`                                   |
| Delete service                     | `deprovision`                              |
| Support async creation or deletion | `last_operation`                           |
| Support async bind or unbind       | `last_binding_operation` and `get_binding` |
| Retrievable instance               | `get_instance`                             |
| Retrievable binding                | `get_binding`                              |

## Setup

I recommend [Pipenv](https://docs.pipenv.org/en/latest/) for setup

```shell script
pip install pipenv
pipenv install
```


## Deploy on Cloud Foundry

```bash

# deploy
cf push --random-route

# register service broker in space
cf create-service-broker [broker name] [username] [password] [url] --space-scoped

```

> *Why is this not running out of the box?*
> The implementation for a dummy service broker would generate too much example code. 
> Because of this I just provide the skeleton of my service broker projects, without any further functionality.