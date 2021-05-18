# layer4 proxy server 
layer4 proxy cluster 
 
# Architecture
  ![diagram](https://user-images.githubusercontent.com/80030346/118617397-d7204500-b7d7-11eb-8c4e-96d3cdc8b787.png)
  
  
  
  
## installation

```console
ansible-playbook ./ansible/master.yaml

ansible-playbook ./ansible/slave.yaml

edit lsyncd config on master 

systemctl restart lsyncd.service 

```

## add worker 


```console
add yoour worker ip to ansible hosts 

ansible-playbook ./ansible/slave.yaml

edit lsyncd config on master 

systemctl restart lsyncd.service 

```
