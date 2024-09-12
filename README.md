# abnTakeHome

## Introduction

* The following repo contains 3 stacks based on the interview questions of the take home assignment
* Each stack has its own individual helm chart and ansible playbook to install it to Kubernetes

## Prerequisites

- Python 3.10+
- Kubernetes 1.27+
- Helm 3+
- Ansible 2.13+
- Docker 23.06

## Stack organization

### backendApiStack

* This stack deploys the `backend_api` to kubernetes
* Detailed documentation can be found [here](./backendApiStack/README.md)

### dataApiStack

* This stack deploys the `data_api` stack to kubernetes
* Detailed documentation can be found [here](./dataApiStack/README.md)

### monitoringStack

* This stack deploys the prometheus operator for monitoring
* It uses existing helm chart for the prometheus operator https://github.com/prometheus-operator/kube-prometheus
* Detailed documentation can be found [here](./monitoringStack/README.md)

## Code improvements
* Re-use ansible module across the 2 application stacks
* Introduce `ansible-vault` or a cloud keystore for secure access of sensitive data like keys
* I use a personal docker repo for testing before running the code its adviced to use a separate docker repo with docker login 

