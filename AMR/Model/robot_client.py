import requests
import json
import robot

#testing purposes
#import mock_robot as robot

class robot_client:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_robot_info(self):
        response = requests.get(f"{self.base_url}/robot")
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to fetch robot info: {response.text}")

    def update_robot_info(self):
        robot_data = robot.to_json()  # Gather data using the to_json function from robot.py
        #image_data = robot.get_image()

        #if image_data is not None:
            #files = {'json': (None, json.dumps(robot_data), 'application/json'), 'image': ('image.jpg', image_data, 'image/jpeg')}
            #response = requests.post(f"{self.base_url}/robot", files=files)
        #else:
        headers = {'Content-Type': 'application/json'}
        response = requests.put(f"{self.base_url}/robot", headers=headers, data=json.dumps(robot_data))

        if response.status_code != 200:
            raise Exception(f"Failed to update robot: {response.text}")
        # Parsing the response
        try:
            response_data = response.json()  # Assuming the response is JSON

            if isinstance(response_data, list) and len(response_data) in [2, 4]:
                x_destination = response_data[0]
                y_destination = response_data[1]

                print(f"Robot's destination updated to X: {x_destination}, Y: {y_destination}")

                if len(response_data) == 4:
                    qr_x_position = response_data[2]
                    qr_y_position = response_data[3]
                    print(f"QR position at X: {qr_x_position}, Y: {qr_y_position}")
            else:
                print("Unexpected response format.")
        except json.JSONDecodeError:
            print("Invalid JSON response received.")
        except Exception as e:
            print(f"An error occurred: {e}")
        

        print("Robot information updated successfully.")


        # response should be a float[] 
        # array should be either size 2 or 4
        # float[0] - x destination
        # float[1] - y destination
        # float[2] - qr x position
        # float[3] - qr y position


if __name__ == "__main__":
    client = robot_client("http://localhost:8080")

    # Updating robot info using data from robot.py
    client.update_robot_info()

    # Getting robot info from the server
    robot_info = client.get_robot_info()
    print(robot_info)
