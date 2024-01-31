## Frontend React JS

This is the main repo for the front-end of the Cruddur social media app.
We are using React.

Basic commands to remember:
Install ssm
`curl "https://s3.amazonaws.com/session-manager-downloads/plugin/latest/ubuntu_64bit/session-manager-plugin.deb" -o "session-manager-plugin.deb"`

`sudo dpkg -i session-manager-plugin.deb`

Once environment is set up deploy with:
`aws ecs register-task-definition --cli-input-json file://aws/task-definitions/backend-flask.json`
`aws ecs create-service --cli-input-json file://aws/json/service-backend-flask.json`

`aws ecs register-task-definition --cli-input-json file://aws/task-definitions/frontend-react-js.json`
`aws ecs create-service --cli-input-json file://aws/json/service-frontend-react-js.json`

`curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"`
`unzip awscliv2.zip`
`sudo ./aws/install`