# labkeeper

A tool developed by Ansible for deploying and managing OpenLab CI infrastructures

- License: Apache License, Version 2.0
- Source: https://github.com/theopenlab/labkeeper

## Description

Labkeeper is a collection of Ansible playbooks and roles used to deploy and manage
OpenLab CI infrastructures.

This project is initially forked from the [OpenStack Windmill project](https://github.com/openstack/windmill), and
modified for specific [OpenLab](https://github.com/theopenlab) CI system deployment.

## Steps to deploy a CI system using Labkeeper

1. Choose a deployment mode under the `inventory/` directory. Labkeeper now supports:

   - Production Mode (`openlab`):

     Using two nodes to create a new CI system. One is for nodepool services, the other is for zuul services

   - Production HA Mode (`openlab-ha`)

     Using five nodes to create a new CI system. Two is for Master cluster, the other two is for Slave cluster, the last one is for zookeeper cluster. In this mode, the service on slave cluster won't start. Only the service data will be synced.

   - All In One Mode (`allinone`)

     Using only one node to create a new CI system. All components will be deployed there.

   - ALL In One HA Mode (`allinone-ha`)

     Using two nodes to  create a new CI system. One is for Master, the other one is for Slave

   - New Slave for HA Mode(`new-slave`)

     There is not a specific inventory yaml file of this mode, you can use `--new-slave` argument
     and new slave hosts IPs specified by `--new-ip` argument of the `deploy.py` tool. For example,
      you can run following command to deploy a new *slave* part of a OpenLab environment:

     ```bash
     $ ./deploy.py openlab-ha --action new-slave --new-ip zuul02=192.168.5.5 --new-ip nodepool02=192.168.6.6
     ```

2. Check and modify the configuration yaml files base one the mode you choose.

   - Modify the `nodepool` and `zuul` servers IP address if needed, you can also specify hosts
     IP addresses with `--new-ip` argument of the `deploy.py` tool.
   - Replace the `github_acc_token` field with github personal access token, which need to be
     manually generated in [Github token](https://github.com/settings/tokens).
   - Check the `github_app_key_file`, `zuul_tenant_name`, `zuul_public_ip`, etc.

3. Create an `openlab.pem` file with SSH private key to access servers to deploy CI services,
   and `vault-password.txt`  file with ansible vault password as content.

4. Base on the mode you choose, you can deploy your OpenLab with the `deploy.py` tool, you run
   it with `--help` arguments to get help messages. For example, you can run with following
   command to deploy a OpenLab environment with production HA mode:

   ```
   $ ./deploy.py openlab-ha
   ```
   *NOTE:* this deployment tool need python and ansible related packages installed in ansible
   controller host, if not, you can run `./tools/install_requirements.sh` to install.

5. After finishing deploying, please update the github app webhook URL in your github app, e.g. modify the [theopenlab app](https://github.com/organizations/theopenlab/settings/apps/theopenlab-ci) webhook URL.

6. Update the log server `fqdn` and host key(`secrets.yaml`) in the jobs config repo (`openlab-zuul-jobs`).

## TODO items

- Fix some workaround approaches and make more variables in playbooks configurable.
- Add support for monitoring and heath check functions.
