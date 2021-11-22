# QA-Assignment-JumpCloud

### Sample Curl Request and Responses

#### Post to the /hash endpoint
```
$ curl -X POST -H "application/json" -d '{"password":"angrymonkey"}' http://127.0.0.1:8088/hash 
```
Output:
> 42


#### Retrieving the Base 64 encoded password
```
$ curl -H "application/json" http://127.0.0.1:8088/hash/1
```
Output:
> zHkbvZDdwYYiDnwtDdv/FIWvcy1sKCb7qi7Nu8Q8Cd/MqjQeyCI0pWKDGp74A1g== 


#### Get the stats
```
$ curl http://127.0.0.1:8088/stats
```
Output:
> {"TotalRequests":3,"AverageTime":5004625} 


#### Shutdown the application
```
$ curl -X POST -d 'shutdown' http://127.0.0.1:8088/hash 
```
Output:
> 200 Empty Response 



