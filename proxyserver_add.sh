echo "sync{
        default.rsyncssh,
        source = "/etc/nginx/stream",   
        targetdir = "/etc/nginx/stream",
        host = "$1",
        delay           = 5,
        rsync = { rsh="/usr/bin/ssh -l ubuntu -i /home/ubuntu/.ssh/id_rsa -o StrictHostKeyChecking=no"}
}
" >> /etc/lsyncd/lsyncd.conf.lua

systemctl restart lsyncd.service
