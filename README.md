# JWT_Auth_Implementation

working on implementation of JWT with email OTP
- Implementation is complete 
- Sliding token concept is not covered
- will update and rearrange documentation shortly

## Workflow

- User registers, gets an active account with ACCESS_TOKEN and REFRESH_TOKEN
- User also receives a mail with an OTP
- User goes to otp verification endpoint and verifies otp
- User gets better access
- User perform operations with protected data
- User ACCESS_TOKEN expires
- User gets new ACCESS_TOKEN and new REFRESH_TOKEN, requesting with the current REFRESH_TOKEN to refresh token endpoint
- User's old REFRESH_TOKEN gets blacklisted
- User logs out, current REFRESH_TOKEN gets blacklisted
