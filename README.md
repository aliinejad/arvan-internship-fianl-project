# layer4 proxy cluster 
light and easy sync layer4 proxy cluster 
 
# Architecture
  ![diagram](https://user-images.githubusercontent.com/80030346/118617397-d7204500-b7d7-11eb-8c4e-96d3cdc8b787.png)
  
  ## workflow
  master : in master server client can add upstream by calling api and making config file. after that lsyncd sync config files with salve servers. 
  
  salve : in slave servers changes detected by reload.service and inotify library . after that it reload nginx service  and proxy is ready . 

## api structure

{
	"input_port": "input port",
	"upstream": "upstream ip ",
	"upstream_port": "upstream port ",
	"proxy_protocolt": "on" 
}	
  
  
  
  
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
