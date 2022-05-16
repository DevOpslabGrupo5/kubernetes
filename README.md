# Ejercicio Kubernetes

## Instalaciones previas
#### Addons para complementar minikube:
minikube addons enable metrics-server
    Permite generar metricas de los nodos

minikube addons enable ingress
    Para comunicarse con los nodos (Redes)

minikube addons enable metallb
     (Redes)

#### Instalar kubectx + kubens
https://github.com/ahmetb/kubectx

## Instalar minikube
https://minikube.sigs.k8s.io/docs/start/

## Iniciar cluster minikube
minikube start

## Comandos
### Crear namespace "test-flask"
k apply -f namespace.yaml
### Cambiar a namespace
kubens test-flask

### Crear servicio Cluster IP u Node Port en namespace
k apply -f service-clusterip.yaml
k apply -f service-nodeport.yaml

### Crear Deployment 
k apply -f depoy.yaml

### Ingress
k apply -f ingress.yaml

### Horizontal Pod Autoscalig
k apply -f hpa.yaml

#### How to Run Locally Built Docker Images in Kubernetes
(https://medium.com/swlh/how-to-run-locally-built-docker-images-in-kubernetes-b28fbc32cc1d)

#### (Para ocupar imagenes locales)
    minikube docker-env
    eval $(minikube -p minikube docker-env)
    docker build -t docker-demo -f flask_docker/Dockerfile .
