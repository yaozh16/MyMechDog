# MechDog Site
## Struct

```
-mechDogSite(root)
    -redirect(main page)
-userManage(user check)
    -regist
        -su code
    -login
        -save cookie
    -logout
        -delete cookie
    -commandManage(after user check)
        -command
        -token check
-visiterManage(visiter can view--team introduction)
    -person list
```
## Fucntion
### -user manage
#### regisiter
* manually
* invitation code
* account contains:
1. uid(auto allocate as primary key)
1. username
1. password
#### log in
* allocate token:save with user\time into sql
* store cookie
#### log out
* time limit:token ttl
* delete cookie
### -command manage
* view video stream
* operate with json/post request
* receive instant dog status
### -visiter manage
* person list
* dog introduction
* team coorperation
## Method
