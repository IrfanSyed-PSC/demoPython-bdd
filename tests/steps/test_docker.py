import logging
import pytest
from pytest_bdd import scenarios, given, when, then, parsers

from core.utils.docker_cmd import DockerManager


scenarios('docker.feature')

@pytest.fixture
def docker_mgr():
    docker = DockerManager()
    return docker

@pytest.fixture
def docker_containers(docker_mgr):
    return docker_mgr.list_containers()

@pytest.fixture
def docker_images(docker_mgr):
    return docker_mgr.list_images()

@given('I have Docker installed on my machine')
def docker_container_instance(docker_mgr):
    ## check if the docker_instance is an object of DockerManager
    assert isinstance(docker_mgr, DockerManager)


@when('I run the command "docker ps"')
def docker_container_ps(docker_mgr):
    ## check the output is not empty
    assert docker_mgr.list_containers()

@then('I should get a list of running containers')
def list_containers(docker_containers):
    assert docker_containers is not None


###### Scenario: List all Docker images #####

@when('I run the command "docker images"')
def docker_images_list(docker_mgr):
    ## check the output is not empty
    assert docker_mgr.list_images()

@then('I should get a list of images available')
def list_images(docker_images):
    assert len(docker_images) > 0

###### Scenario: Check if docker image exist #####
@given(parsers.parse('I have "{image_name}" docker image'))
def docker_container_instance(docker_mgr):
    ## check if the docker_instance is an object of DockerManager
    assert isinstance(docker_mgr, DockerManager)

@when(parsers.parse('I run the command "docker images" and check for "{image_name}"'))
def run_docker_images_command_and_check(image_name, docker_mgr):
    images_list = docker_mgr.list_image(image_name)
    logging.debug(f"Images list: {images_list}")
    assert len(images_list) > 0