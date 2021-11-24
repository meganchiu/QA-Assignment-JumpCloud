import json
import base64
import hashlib
import requests

# Description: GET Request to the Password Hash Endpoint
# The GET Request to the Password Hash Endpoint should return 
# the corresponding encoded password when provided with a valid job identifier.
def getEncodedPasswordHash(jobIdentifier):
    endpoint = "/hash"
    url = "http://localhost:8088" + endpoint + "/" + str(jobIdentifier)
    response = requests.get(url)
    return response


# Description: POST Request to the Password Hash Endpoint
# The POST Request to the Password Hash Endpoint should return 
# a job identifier immediately and then calculate the password hash.
def postEncodedPasswordHash(password):
    endpoint = "/hash"
    param = {"password":password}
    url = "http://localhost:8088" + endpoint
    response = requests.post(url, json=param)
    return response


# Description: GET Request to the Stats Endpoint
# The GET Request to the Stats Endpoint should return 
# total number of password hash requests and the average time for a password hash request.
def getPasswordHashStats():
    endpoint = "/stats"
    url = "http://localhost:8088" + endpoint
    response = requests.get(url)
    return response


# Description: POST Request to the Password Hash Endpoint to Shutdown the Application
# The POST Request to the Password Hash Endpoint to initiate a shutdown of the application.
# It should not allow any new password hash requests afterwards.
def postInitiateShutdown():
    endpoint = "/hash"
    data = "shutdown"
    url = "http://localhost:8088" + endpoint
    response = requests.post(url, data=data)
    print response
    return response


def postRequestToHashEndpointIsSuccess(password):
    print "Test: postRequestToHashEndpointIsSuccess"

    postHashRespnse = postEncodedPasswordHash(password)

    if (postHashRespnse.status_code == 200):
        print "Test PASS - POST Request to Hash Endpoint is successful. Status code was: " + str(postHashRespnse.status_code)
    else:
        print "Test FAIL - POST Request to Hash Endpoint is unsuccessful. Status code was: " + str(postHashRespnse.status_code) 

    print "-----"

def postRequestToHashEndpointPasswordEncodedCorrectly(password):
    print "Test: postRequestToHashEndpointPasswordEncodedCorrectly"

    postHashRespnse = postEncodedPasswordHash(password)
    getHashResponse = getEncodedPasswordHash(postHashRespnse.text)

    print "Actual Encoded Value = " + getHashResponse.text

    expectedEncodedValue = base64.b64encode(hashlib.sha512(password).hexdigest())
    print "Expected Encoded Value = " + expectedEncodedValue

    if (getHashResponse.text == expectedEncodedValue):
        print "Test PASS - Encoded Value is equal to Expected Encoded Value"
    else:
        print "Test FAIL - Encoded Value is not equal to Expected Encoded Value"

    print "-----"

def postRequestToHashEndpointUsingEmptyString():
    print "Test: postRequestToHashEndpointUsingEmptyString"

    password = ""

    postHashRespnse = postEncodedPasswordHash(password)

    if (postHashRespnse.status_code != 200):
        print "Test PASS - POST Hash Endpoint did not allow for empty string to be passed"
    else:
        print "Test FAIL - POST Hash Endpoint allowed for empty string to be passed"

    print "-----"


def postRequestToHashEndpointUsingNullValue():
    print "Test: postRequestToHashEndpointUsingNullValue"

    password = None

    postHashRespnse = postEncodedPasswordHash(password)

    if (postHashRespnse.status_code != 200):
        print "Test PASS - POST Hash Endpoint did not allow for null value to be passed"
    else:
        print "Test FAIL - POST Hash Endpoint allowed for null value to be passed"

    print "-----"


def postRequestToHashEndpointUsingMalformedJson():
    print "Test: postRequestToHashEndpointUsingMalformedJson"

    endpoint = "/hash"
    param = "password"
    url = "http://localhost:8088" + endpoint
    response = requests.post(url, json=param)
    
    if (response.status_code != 200):
        print "Test PASS - POST Hash Endpoint using malformed JSON was not allowed"
    else:
        print "Test FAIL - POST Hash Endpoint using malformed JSON was allowed"

    print "-----"


def postRequestToHashEndpointUsingDifferentKeyThanPasswordKey(password):
    print "Test: postRequestToHashEndpointUsingDifferentKeyThanPasswordKey"

    endpoint = "/hash"
    param = {"random":password}
    url = "http://localhost:8088" + endpoint
    response = requests.post(url, json=param)
    
    if (response.status_code != 200):
        print "Test PASS - POST Hash Endpoint did not allow for a key other than password key to be used"
    else:
        print "Test FAIL - POST Hash Endpoint allowed for a key other than password key to be used"

    print "-----"

def getRequestToHashEndpointUsingValidIdentifier(password):
    print "Test: getRequestToHashEndpointUsingValidIdentifier"

    postResponse = postEncodedPasswordHash(password)
    getResponse = getEncodedPasswordHash(postResponse.text)

    if (getResponse.status_code == 200):
        print "Test PASS - GET Hash Endpoint was successful.  Encoded password hash was returned."
    else:
        print "Test FAIL - GET Hash Endpoint was not successful."

    print "-----"


def getRequestToHashEndpointUsingUnknownIdentifier():
    print "Test: getRequestToHashEndpointUsingUnknownIdentifier"

    jobIdentifier = 99999

    getResponse = getEncodedPasswordHash(jobIdentifier)

    if (getResponse.status_code == 200):
        print "Test FAIL - GET Hash Endpoint using unknown job identifier returned encoded password hash."        
    else:
        print "Test PASS - GET Hash Endpoint using unknown job identifier did not return encoded password hash."

    print "-----"


def getRequestToHashEndpointUsingInvalidIdentifier():
    print "Test: getRequestToHashEndpointUsingInvalidIdentifier"

    jobIdentifier = "abc"

    getResponse = getEncodedPasswordHash(jobIdentifier)

    if (getResponse.status_code == 200):
        print "Test FAIL - GET Hash Endpoint using invalid job identifier returned encoded password hash."        
    else:
        print "Test PASS - GET Hash Endpoint using invalid job identifier did not return encoded password hash."

    print "-----"


def getRequestToHashEndpointWithoutPassingAnIdentifier():
    print "Test: getRequestToHashEndpointWithoutPassingAnIdentifier"

    jobIdentifier = None

    getResponse = getEncodedPasswordHash(jobIdentifier)

    if (getResponse.status_code == 200):
        print "Test FAIL - GET Hash Endpoint without passing job identifier returned encoded password hash."        
    else:
        print "Test PASS - GET Hash Endpoint without passing job identifier did not return encoded password hash."

    print "-----"


def getRequestToStatsEndpointIsSuccess():
    print "Test: getRequestToStatsEndpointIsSuccess"

    getStatsResponse = getPasswordHashStats()

    if (getStatsResponse.status_code == 200):
        print "Test PASS - GET Request to Stats Endpoint was successful.  Response was: " + getStatsResponse.text
    else:
        print "Test FAIL - GET Request to Stats Endpoint was unsuccessful.  Response was: " + getStatsResponse.text

    print "-----"


def getRequestToStatsEndpointReturnsCorrectNumberOfRequests(password):
    print "Test: getRequestToStatsEndpointReturnsCorrectNumberOfRequests"

    getStatsResponse = getPasswordHashStats()
    statsResponseJson = getStatsResponse.json()

    currentTotalRequests = statsResponseJson['TotalRequests']
    expectedNextTotalRequests = currentTotalRequests + 1
    
    postResponse = postEncodedPasswordHash(password)

    getStatsResponse = getPasswordHashStats()
    statsResponseJson = getStatsResponse.json()
    actualNextTotalRequests = statsResponseJson['TotalRequests']

    if (expectedNextTotalRequests == actualNextTotalRequests):
        print "Test PASS - TotalRequests in the GET Request to Stats Endpoint is calculated correctly."
    else:
        print "Test FAIL - TotalRequests in the GET Request to Stats Endpoint was not calculated correctly." 

    print "-----"


def getRequestToStatsEndpointWhenNoRequestsHaveBeenMadeYet():
    print "Test: getRequestToStatsEndpointWhenNoRequestsHaveBeenMadeYet"

    getStatsResponse = getPasswordHashStats()
    statsResponseJson = getStatsResponse.json()

    totalRequests = statsResponseJson['TotalRequests']

    if (totalRequests == 0):
        print "Test PASS - TotalRequests is equal to 0 since no requests have been made once application was started."
    else:
        print "Test FAIL - Total Requests was not equal to 0 once the application was started."

    print "-----"


def postRequestToShutdownTheApplicationDoesNotAllowNewRequestsAfter(password):
    print "Test: postRequestToShutdownTheApplicationDoesNotAllowNewRequestsAfter"

    getShutdownResponse = postInitiateShutdown()
    
    postHashRespnse = postEncodedPasswordHash(password)

    print "-----"    


def main():
    password = "angryMonkey"

    getRequestToStatsEndpointWhenNoRequestsHaveBeenMadeYet()
    postRequestToHashEndpointIsSuccess(password)
    postRequestToHashEndpointPasswordEncodedCorrectly(password)
    postRequestToHashEndpointUsingEmptyString()
    postRequestToHashEndpointUsingNullValue()
    postRequestToHashEndpointUsingMalformedJson()
    postRequestToHashEndpointUsingDifferentKeyThanPasswordKey(password)
    getRequestToHashEndpointUsingValidIdentifier(password)
    getRequestToHashEndpointUsingUnknownIdentifier()
    getRequestToHashEndpointUsingInvalidIdentifier()
    getRequestToHashEndpointWithoutPassingAnIdentifier()
    getRequestToStatsEndpointIsSuccess()
    getRequestToStatsEndpointReturnsCorrectNumberOfRequests(password)
    #postRequestToShutdownTheApplicationDoesNotAllowNewRequestsAfter()

if __name__ == '__main__':
    main()