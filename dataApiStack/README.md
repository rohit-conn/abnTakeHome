# dataApiStack

## Directory composition

- `data_api` -> Flask api provided as part of the test
- `dataapiHelm` -> Helm chart to deploy backend API
- `install-data.yaml` -> Ansible playbook to build and deploy  

## Code changes to data_api
- Add flask env variables for IP and port
- Removed unused packages from `requirements.txt`
- Introduce a `/healthz` endpoint for kubernetes to do its probes


## Ansible installation
- A docker public repo is used for deploying the container, the app can be installed with the followng command if we need to change that and use another repo
    ```
    ansible-playbook install-data.yaml  -e "EXTERNAL_INTGERATION_KEY=<Key to be passed> docker_repo_name=<docker registry> app_name=<name of the application>"
    ```
- For normal installation with the public repo we just use 
    ```
     ansible-playbook install-data.yaml 
    ```
