# backendApiStack

## Directory composition

- `backend_api` -> Flask api provided as part of the test
- `backendapiHelm` -> Helm chart to deploy backend API
- `install-backend.yaml` -> Ansible playbook to build and deploy  

## Code changes to backend_api
- Add flask env variables for IP and port
- Removed unused packages from `requirements.txt`
- Added api endpoint `/download_external_logs`, also imported `EXTERNAL_INTGERATION_KEY` from environment

## Code changes to health_check.sh
- Updated `health_check.sh` to run as service
- Changed `API_URL` to behave as it were in the same pod as `backend_api`
- Created log file before anything is logged for kubernetes to do its probes

## Ansible installation
* Ansible is used to build docker and deploy using helm
    ```
    ansible-playbook install-backend.yaml  -e "EXTERNAL_INTGERATION_KEY=<Key to be passed>"
    ```
* `EXTERNAL_INTGERATION_KEY` is passed as an environment variable, this can be done in a secure manner by adopting the following methods based on the requirements
    * Using ansible-vault
    * Using cloud provider secret store

* The  `EXTERNAL_INTGERATION_KEY` is passed as a secret and referenced by the helm chart

* Currently a docker public repository is used to deploy the built container however this can be chnaged to any repo by modifying the ansible installation command as
    ```
    ansible-playbook install-backend.yaml  -e "EXTERNAL_INTGERATION_KEY=<Key to be passed> docker_repo_name=<docker registry> app_name=<name of the application>"
    ```

* For multi environment setup `EXTERNAL_INTGERATION_KEY` can be passed from a CI/CD to deploy to environment

## General Notes
* The stack is a 2 container deployment
* The health check script runs every 5 minutes and logs the request
* We mount a volume to the health check script and the request is logged to the volume.
* We expose the service of the `backend_api` on port 80

