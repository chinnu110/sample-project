
## ansible_ssh_key_copy
A simple ansible playbook to copy ssh key to the servers. Ansible is very easy to get started does not not required any agent on nodes.

```
cd ansible_ssh_key_copy
ansible-playbook copy_ssh_keys.yml -i inventory/hosts.inv -e usr_name=root
```

## weather-app
A simple python flask app to get the weather by zip code

to build Dockerfile
```
docker build -t weather-app .
```

## Deployment
Helm chart to deploy the `weather-app` docker container to Kubernetes cluster, it creates the Deployment, Service
and exposes the service using LoadBalancer

```
# cat weather-app-chart/values.yml
replicaCount: 3

image:
  repository: weather-app
  tag: latest
  pullPolicy: IfNotPresent

service:
  type: LoadBalancer
  port: 5000
```

to deploy the application

```
helm install weather-app-chart
```
