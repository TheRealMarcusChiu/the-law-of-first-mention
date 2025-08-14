#! /bin/bash

ssh aws << EOF
  rm -rf first-mention/
  mkdir first-mention
EOF

scp -i ~/.ssh/keys/aws-marcuschiu.pem -r ./web ec2-user@www.marcuschiu.com:~/first-mention
