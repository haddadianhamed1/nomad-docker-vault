# download a image with java 8
FROM dockerfile/java:oracle-java8

# Install maven into the image
RUN apt-get update && apt-get install -y maven

# create a work directory 'code' this is where we will build and run our application
WORKDIR /code

# Add the build tool files and source code, compile
COPY pom.xml /code/pom.xml
COPY src /code/src
RUN ["mvn", "package"]

# run the application hook
CMD ["bash"]
