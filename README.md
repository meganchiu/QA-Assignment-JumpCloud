# QA-Assignment-JumpCloud

### Assignment Details

JumpCloud has implemented a password hashing application in Golang and have intentionally left bugs in the application.  

The assignment is to:
* Write the test cases needed to test the application
* Explain your choices for test coverage
* Execute test cases
* Report any bugs found
* Consider implementing automated tests as well

---

### Password Hashing Application Details

* Must specify the PORT environment variable before launching the application.
* When the application is launched, it should wait for http connections.
* Application should answer only on the `PORT` that was specified in the `PORT` environment variable.
* The application should support three endpoints:
    * `POST` to `/hash` should accept a password.  It should return a job identifier.  It should wait 5 seconds and then calculate the password hash.  The hashing algorithm should be SHA512.
    * `GET` to `/hash` should accept a job identifier.  It should return the base64 encoded password hash for the corresponding POST request.
    * `GET` to `/stats` does not accept any data.  It should return a JSON data structure for the total hash requests since the server started and average time of a hash request in milliseconds.
* Application should be able to process multiple connections simultaneously.  It should support graceful shutdown requests.  This means that it should allow any current requests for password hashing to complete, reject any new requests, and respond with a 200 status code and then shutdown.
* No new password requests should be allowed when the shutdown is pending.

---

### Sample Curl Request and Responses

#### Post to the /hash endpoint
```
curl -X POST -H "application/json" -d '{"password":"angrymonkey"}' http://127.0.0.1:8088/hash 
```
Output:
> 42


#### Retrieving the Base 64 encoded password
```
curl -H "application/json" http://127.0.0.1:8088/hash/1
```
Output:
> zHkbvZDdwYYiDnwtDdv/FIWvcy1sKCb7qi7Nu8Q8Cd/MqjQeyCI0pWKDGp74A1g== 


#### Get the stats
```
curl http://127.0.0.1:8088/stats
```
Output:
> {"TotalRequests":3,"AverageTime":5004625} 


#### Shutdown the application
```
curl -X POST -d 'shutdown' http://127.0.0.1:8088/hash 
```
Output:
> 200 Empty Response 



