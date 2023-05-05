# DevOps-Tech-Assessment

DevOps Exercise
Rules and requirements
● There is no internet usage limit
● All generated code must be versioned using a public GitHub Repo created by the candidate.
Requirements:
Build a microservice that must have a REST endpoint named: /DevOps (use any preferred programming
language or framework).
This is the JSON payload for the endpoint. Please use a HTTP POST method:
{
“message” : “This is a test”,
“to”: “Juan Perez”,
“from”: “Rita Asturia”,
“timeToLifeSec” : 45
}
This is the JSON payload the endpoint must return:
{
“message” : “Hello Juan Perez your message will be send”
}
Other HTTP Methods calls must return the string “ERROR”
The EndPoint must be secured with this APIKey:
2f5ae96c-b558-4c7b-a590-a501ae1c3f6c
The APIKey must be included in HTTP Headers
In our side, we will use this command to test your endPoint
curl -X POST \
-H "X-Parse-REST-API-Key: 2f5ae96c-b558-4c7b-a590-a501ae1c3f6c" \
-H "X-JWT-KWY: ${JWT}" \
-H "Content-Type: application/json" \
-d '{ “message” : “This is a test”, “to”: “Juan Perez”, “from”: “Rita Asturia”, “timeToLifeSec” : 45 }' \
https://${HOST}/DevOps
Where the HOST variable is the URL sent by each participant (you), the JWT must be supplied to us (by
any means) and it has to be unique per transaction.
You must comply with the following requirements:
● The microservice must be containerized and can be deployed on any machine or in the cloud.
● It is required to use a load balancer with a minimum of two nodes with the same microservice.
● The infrastructure code must be versionated.
● The pipeline should be configured as a code and needs to be stored in a repository.
