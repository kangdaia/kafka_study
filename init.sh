docker network create kafka-network
sudo chown -R 472:472 ./visualization/grafana   
chown -R 65534:65534 ./visualization/prometheus  
chmod 777 ./visualization/prometheus/