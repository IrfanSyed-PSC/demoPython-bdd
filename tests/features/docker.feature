@docker
Feature: Docker Command Testing

    Scenario: Running a Docker container
        Given I have Docker installed on my machine
        When I run the command "docker ps"
        Then I should get a list of running containers
    
    Scenario: List all Docker images
        Given I have Docker installed on my machine
        When I run the command "docker images"
        Then I should get a list of images available

    Scenario Outline: Check if docker image exist
        Given I have "<image_name>" docker image
        When I run the command "docker images" and check for "<image_name>"
        
        Examples: 
        | image_name |
        | alpine     |