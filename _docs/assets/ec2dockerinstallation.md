##---------------------
## Docker: Installation
##---------------------
## Update the installed packages and package cache on your instance.
sudo yum update -y
 
## Install the most recent Docker Community Edition package.
sudo yum install docker
 
## Check docker version
docker version
docker --version
 
## Add the ec2-user to the docker group so you can execute Docker commands without using sudo.
## Exit the terminal and re-login to make the change effective
sudo usermod -a -G docker ec2-user
exit
 
## Enable docker service
sudo systemctl enable docker
 
## Start docker service
sudo systemctl start docker
 
## Check the Docker service.
sudo systemctl status docker
 
##---------------------
## Docker: Getting Help
##---------------------
## Get docker details
docker info
 
## Get docker command details
docker
 
## Get help on specific command
## docker  --help
docker search --help
 
##----------------------------
## Docker: Search docker image
##----------------------------
docker search --limit 10 --no-trunc httpd #search for httpd image in docker hub


### Reference: 'https://cloudaffaire.com/how-to-install-docker-in-aws-ec2-instance/'