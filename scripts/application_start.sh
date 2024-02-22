#!/bin/bash

echo 'run application_start.sh: ' >> /home/ec2-user/api/deploy.log

echo 'pm2 restart nodejs-express-app' >> /home/ec2-user/api/deploy.log
pm2 restart nodejs-express-app >> /home/ec2-user/api/deploy.log