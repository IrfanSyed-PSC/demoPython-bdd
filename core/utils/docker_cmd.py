from plumbum import local, ProcessExecutionError
import logging

class DockerManager:
    def __init__(self):
        self.docker = local["docker"]

    def list_containers(self):
        try:
            exit_code, stdout, stderr = self.docker["ps"].run()
            logging.debug(f"Exit code: {exit_code}")
            logging.debug(f"Output: {stdout}")
            if exit_code != 0:
                logging.error(f"Error: {stderr}")
            return stdout
        except ProcessExecutionError as e:
            logging.error(f"Failed with exit code {e.retcode}")
            logging.error(e.stderr)
        
    def list_images(self):
        try:
            docker_images = []
            exit_code, stdout, stderr = self.docker["images"].run()
            logging.debug(f"Exit code: {exit_code}")
            logging.debug(f"Output: {stdout}")
            if exit_code != 0:
                logging.error(f"Error: {stderr}")

            # Split the output into lines
            lines = stdout.split('\n')

            # Parse the lines to extract the information you need
            for line in lines[1:]:  # Skip the header line
                parts = line.split()
                if len(parts) >= 5:  # Check if it's a valid line
                    repository = parts[0]
                    tag = parts[1]
                    image_id = parts[2]
                    created = parts[3]
                    size = parts[4]
                    # Append the parsed information as a dictionary to the list
                    docker_images.append({
                        'Repository': repository,
                        'Tag': tag,
                        'Image ID': image_id,
                        'Created': created,
                        'Size': size
                    })

            return docker_images
     
     
        except ProcessExecutionError as e:
            logging.error(f"Failed with exit code {e.retcode}")
            logging.error(e.stderr)

    def list_image(self,filter):

        docker_images = self.list_images()

        # Filter the list of images based on the filter
        filtered_images = []
        for image in docker_images:
            if filter in image['Repository']:
                filtered_images.append(image)
        
        return filtered_images

    def pull_image(self, image_name):
        try:
            result = self.docker("pull", image_name)
            exit_code = result.retcode
            logging.debug(f"Exit code: {exit_code}")
            return result
        except ProcessExecutionError as e:
            logging.error(f"Failed to pull image {image_name} with exit code {e.retcode}")
            logging.error(e.stderr)

    def run_container(self, image_name, command):
        try:
            result = self.docker("run", "--rm", image_name, *command)
            exit_code = result.retcode
            logging.debug(f"Exit code: {exit_code}")
            return result
        except ProcessExecutionError as e:
            logging.error(f"Failed to run container {image_name} with exit code {e.retcode}")
            logging.error(e.stderr)

