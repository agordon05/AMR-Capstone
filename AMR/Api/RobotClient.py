import requests
import json
import time

from Model import robot as bot
#testing
#import mock_robot as robot


__port = "http://192.168.0.4:8080"
__robot_URL = "/robot"
__sleep_time = 0.01 # sleep for 0.1 seconds


def set_robot_info():
    url = __port + __robot_URL
        
    response = requests.get(url)
        
    if response.status_code == 200:
        response_data = response.json()
        bot.set_x_pos(response_data['x_pos'])
        bot.set_y_pos(response_data['x_pos'])
        bot.set_rotation(response_data['rotation'])
        bot.set_x_destination(response_data['x_destination'])
        bot.set_y_destination(response_data['y_destination'])
        bot.set_log(response_data['loggerList'])
        
    
    else:
        raise Exception(f"Failed to fetch robot info: {response.text}")

        
def update_robot_info():
        
    url = __port + __robot_URL
    if bot.get_qr_scan() is not "":
        print("QR scan is here!!!")
    robot_data = bot.to_json()  # Gather data using the to_json function from robot.py
    #image_data = robot.get_image()

    #if image_data is not None:
        #files = {'json': (None, json.dumps(robot_data), 'application/json'), 'image': ('image.jpg', image_data, 'image/jpeg')}
        #response = requests.post(f"{self.base_url}/robot", files=files)
    #else:
    headers = {'Content-Type': 'application/json'}
    # response = requests.put(url, headers=headers, data=json.dumps(robot_data))

      
            
    # Parsing the response
    try:
        
        response = requests.put(url, headers=headers, data=json.dumps(robot_data))

        if response.status_code != 200:
            raise Exception(f"Failed to update robot: {response.text}")
            
        response_data = response.json()  # Assuming the response is JSON

        if isinstance(response_data, list) and len(response_data) in [2, 4]:
            x_destination = response_data[0]
            y_destination = response_data[1]
            
            if x_destination != bot.get_x_destination() or y_destination != bot.get_y_destination():
                bot.add_to_log("Jetbot Robot has been given a new destination")

            bot.set_x_destination(response_data[0])
            bot.set_y_destination(response_data[1])
                
            # print(f"Robot's destination updated to X: {x_destination}, Y: {y_destination}")
            # bot.add_to_log(f"Robot's destination updated to X: {x_destination}, Y: {y_destination}")


            if len(response_data) == 4:
                qr_x_position = response_data[2]
                qr_y_position = response_data[3]
                    
                bot.set_x_pos(response_data[2])
                bot.set_y_pos(response_data[3])
                bot.set_qr_scan("")
                # print(f"QR position at X: {qr_x_position}, Y: {qr_y_position}")
                # bot.add_to_log(f"QR position at X: {qr_x_position}, Y: {qr_y_position}")
        else:
            # print("Unexpected response format.")
            bot.add_to_log("Unexpected response format.")

                
    except json.JSONDecodeError:
        # print("Invalid JSON response received.")
        bot.add_to_log("Invalid JSON response received.")

    except Exception as e:
        # print(f"An error occurred: {e}")
        bot.add_to_log(f"An error occurred: {e}")

        

    # print("Robot information updated successfully.")


        # response should be a float[] 
        # array should be either size 2 or 4
        # float[0] - x destination
        # float[1] - y destination
        # float[2] - qr x position
        # float[3] - qr y position



def run():
    set_robot_info()
    bot.set_message("Connected to Server")
    while True:
        update_robot_info()
        time.sleep(__sleep_time)
        
        
# if __name__ == "__main__":
    # client = RobotClient("http://localhost:8080")

    # Updating robot info using data from robot.py
    # client.update_robot_info()

    # Getting robot info from the server
    # robot_info = client.get_robot_info()
    # print(robot_info)
