docker build . -t pysparkexampleimage:latest 
docker run --rm -e ENABLE_INIT_DAEMON=false --network hadoop --name pyspark3 pysparkexampleimage