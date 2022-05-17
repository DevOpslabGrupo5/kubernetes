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
k apply -f deplot-completo.yaml

k get all

#### Visitar
http://apiflask:30000/

http://apiflask:30000/configmap