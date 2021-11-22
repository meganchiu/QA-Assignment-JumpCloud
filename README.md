# QA-Assignment-JumpCloud

### Assignment Details

JumpCloud has implemented a password hashing application in Golang and have intentionally left bugs in the application.  

The assignment is to:
* Write the test cases needed to test the application
* Explain your choices for test coverage
* Execute test cases
* Report any bugs found
* Consider implementing automated tests as well

### Password Hashing Application Details

-When the application is launched, it should wait for http connections

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



