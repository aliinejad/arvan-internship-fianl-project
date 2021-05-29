# layer4 proxy cluster 
light and easy sync layer4 proxy cluster 
 
# Architecture
  ![diagram](https://user-images.githubusercontent.com/80030346/118617397-d7204500-b7d7-11eb-8c4e-96d3cdc8b787.png)
  
  ## workflow
  primary : in primary server client can add upstream by calling api and making config file. after that lsyncd sync config files with secondary servers. 
  
  secondary : in secondary servers ,  changes detected by reload.service and inotify library . after that it reload nginx service  and proxy is ready . 

## api structure

{
	"input_port": "input port",
	"upstream": "upstream ip ",
	"upstream_port": "upstream port ",
	"proxy_protocolt": "on" 
}	
  
  
  
  
## installation

```console
ansible-playbook ./ansible/primary.yaml

ansible-playbook ./ansible/secondary.yaml

edit lsyncd config on primary 

systemctl restart lsyncd.service 

```

## add secondary


```console
add yoour worker ip to ansible hosts 

ansible-playbook ./ansible/secondary.yaml

proxyserver_add.sh $secondary_servers_ip
```
