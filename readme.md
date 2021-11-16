# build

docker build -t locust-cluster ./

# docker compose

cd ./test && docker-compose up -d

# stack

cd ./test && docker stack deploy -c ./stack.yml locust-cluster

## AWS Example

### 1. Create AMI, Create Template

```Connect```
Create ec2 instance. I selected t4g.small aws linux 2. You need to open port 22 for ssh and 9000 for locust web interface via aws secuirity group.
And connect to the instance. i used visual studio code remote ssh extension.

If you use visual studio code, then Ctrl + Shift + X and search Remote SSH extension.
next Ctrl + Shift + P execute Remote-SSH: Open SSH Configuration File.
and set like below.
```
Host AWS-LOCUST
	HostName your-ec2-ip
	User ec2-user
	IdentityFile C:\Users\home\Desktop\your-key.pem
```

next Ctrl + Shift + P, Remote-SSH: Connect to Host, Select AWS-LOCUST.

```Source```
```
sudo yum install git docker -y
sudo systemctl enable docker
sudo systemctl start docker

git clone https://github.com/dbwodlf3/locust-cluster-docker.git
cd locust-cluster-docker
sudo docker build ./ -t locust-cluster

sudo docker swarm init
cd test
docker stack deploy -c ./stack.yml locust-cluster

# check it works.
curl locahlost:9000
```

and open it with your web browser.
```http://your-ec2-public-ip:9000```
everything works then create AMIs from this ec2 instance.

```Launch Template```
Select the AMI, security group opend port, the ec2 instance type as t4g.small, the key pair and then create launch template.
This is be a master node.

And then will make a worker node.
create ec2 instance from the AMI.
```
# Worker EC2 instance
sudo docker swarm leave --force && sudo docker swarm leave
```

Then also create Worker AMI  and Worker Launch Template this will be used for autoscaling.
And add template initalize shell code.
(Template Advanced details, User data)
```
#/bin/sh
sudo docker swarm join --token your-token-key your-ip:port
```

### 2. Register Autoscaling Group

Create Target groups.
Choose a target type as Instances.
Select properly VPC.(select the same vpc as your EC2 template)
And then make it.

Create Application Load Balancer.
Select properly VPC.(select the same vpc as your EC2 template)
Select the target group made just before
And then make it.

Create Autoscaling Group
Select properly launch template, properly VPC, properly load balancer and make it.

### 3. Test

Release a autoscaling group.
and in master node you can chek it works.
```
sudo node ls
```

And make your test script and run it.
edit my_locustfile.py and update stack.
```
docker stack deploy -c ./stack.yml locust-cluster
```