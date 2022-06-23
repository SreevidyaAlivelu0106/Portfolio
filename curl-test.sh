#!/bin/bash
curl -request POST http://localhost:5000/api/timeline_post -d "name=Mike&email=mike@gmail.com&content=Just Added Database to my portfolio site!"
curl http://localhost:5000/api/timeline_post
curl -request DELETE http://localhost:5000/api/timeline_post -d "id=21"
