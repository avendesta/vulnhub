###### Get help
```
curl --request GET \
  --url http://127.0.0.1:5000/api/help
```
###### Registers a user
```
curl --request POST \
  --url http://127.0.0.1:5000/api/register \
  --header 'content-type: application/json' \
  --data '{
	"username":"nemo-fish",
	"email":"funnyfish@ocean.net",
	"password":"catchmeifucan",
	"confirm_password":"catchmeifucan"
}'
```

###### Login as the previous user
```
curl --request POST \
  --url http://127.0.0.1:5000/api/login \
  --header 'content-type: application/json' \
  --data '{
	"email":"funnyfish@ocean.net",
	"password":"catchmeifucan"
}'
```

###### Get info, 
###### NOTE: replace the access_token with the one you got from login
```
curl --request GET \
  --url 'http://127.0.0.1:5000/api/get?email=aven%40gmail.com' \
  --header 'content-type: application/json' \
  --data '{
	"access_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1OTAzMzM2NzEsIm5iZiI6MTU5MDMzMzY3MSwianRpIjoiZjg2MGFlM2MtN2E3ZS00MjM3LTg3ODYtNGEyNjUzNGEwNzA4IiwiZXhwIjoxNTkwMzM1NDcxLCJpZGVudGl0eSI6ImF2ZW5kZXN0YSIsImZyZXNoIjpmYWxzZSwidHlwZSI6ImFjY2VzcyJ9.TpMTCvep-lhJbIc5IBdXHuyd_vPqbZdowv7aPZyw00M"
}'
```
