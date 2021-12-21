# Hacker-News-RESTful-api


## requirements
 - Docker  should be installed on your machine


## install and set up
 - download repo to your machine
 - in command terminal go this project directory 
 - run "docker-compose up"
 - browse apis in browser
 
## What URLs doing
###### Posts URLs 
   - host/api/post-list/                 - listing all post in Json format
   - host/api/api/post-detail/post_id/   - to view only Post 
   - host/api/add-post/                  - to adding post. You should send post in this format:
  
                                                 {
                                                        "id": "x"(id will be created automatically),
                                                        "content": "Your content",
                                                        "author": "author name",
                                                        "created": "XXXX"(date will be created automatically),
                                                        "upvote": 0,
                                                        "url": "your url"
                                                      }
                                                
   - host/api/delete-post/post_id       - delete post
   - host/api/update-post/post_id       - update post. For updae post you should post this format:
   
                                              {
                                                  "id": "x"(id will be created automatically),
                                                  "content": "Changed  content",
                                                  "author": "Changed author name",
                                                  "created": "XXXX"(date will be created automatically),
                                                  "upvote": 0,
                                                  "url": "Changed URl"
                                                }
                                                Note: you can change only "author", "content", "url" fields. Other will not chan
                                                
                                                
###### comments URLs                           
all comment URL works same as post url above     

  - host/api/add-comment/post_id
  - host/api/list-comment/post_id 
  - host/api/delete-comment/post_id 
  - host/api/update-comment/post_id 

For updating and adding comment format should be so:
 
          {
             "id": "X",
             "content": "Conetnt.",
             "author_name": "Author_name"
           }
 
###### upvote URLs

- host/api/increase-upvote/post_id  - will increase upvote 1 unit
- host/api/reset-upvote/            - will reset 0 all post's upvotes
                                                
