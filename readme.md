
# Web Scapper that scraps off the Times Jobs Website for the latest jobs

This get all the latest jobs from the Times Jobs Website and saves them in a text file.


## Requirement

Ensure Docker is installed and running


## Test On Local Environment

To deploy this project run

1. Go into the repository directory
```bash
 cd web_scrapper
```
2. create the docker image with  the command below
```bash
 docker build -t scrapper . 
```
3. Verify the image has been created successfully
```bash
 docker images 
```
4. Run the container using the scrapper image in interractive mode
```bash
 docker run  -it scrapper 
```

## License

[MIT](https://choosealicense.com/licenses/mit/)


## Author

- [@nanakwafomensah](https://github.com/nanakwafo/web_scrapper)


## Roadmap

- Deploy a Docker App to AWS using Elastic Container Service (ECS



