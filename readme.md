# build

docker build -t locust-cluster ./

# docker compose

cd ./test && docker-compose up -d

# stack

cd ./test && docker stack deploy -c ./stack.yml locust-cluster

## AWS Example

### 1. Create AMI, Create Template

### 2. Register Autoscaling Group

### 3. Test