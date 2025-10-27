docker exec -it kafka bash -c "chmod +x /opt/kafka/acl-rules.sh && echo 'Permissions set!'"
docker exec -it kafka bash -c "/opt/kafka/acl-rules.sh && echo 'ACL rules applied!'"