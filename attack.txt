# How the API is attacked
* The first thing will be to look for possible routes in the API
  * use [`dirbuster`](https://tools.kali.org/web-applications/dirbuster) or
  * /robots.txt
* `/api/help` - get the admin's email
* `/api/recover`- get the admin's `username`
* `/api/register` - register a new account
* `/api/login` - get `access_token`
* you will notice the `access_token` is based on `username` and `username` is not unique per account
* register a new user with `username` of the `admin` and login, the `access_token` you get will be able to get you to login as `admin` (with the admin's email)

###### The above concludes the first attack

* `/api/login` - get `access_token` of any user
* get a list of the [`first 5000 common passwords`](https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials)
* use [`pyjwt`](https://pyjwt.readthedocs.io/en/latest/usage.html#encoding-decoding-tokens-with-rs256-rsa) to read `Claimset without Validation` and to brute force the secret `key`.

###### This concludes the second attack
