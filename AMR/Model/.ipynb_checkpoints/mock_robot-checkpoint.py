# Mock data
mock_robot_data = {
    'id': 1,
    'status': 'Active',
    'message': 'Mock message',
    'x_pos': 100.0,
    'y_pos': 200.0,
    'rotation': 45.0,
    'x_destination': 150.0,
    'y_destination': 150.0,
    'qrScan': 'mockQRCode',
    'loggerList': ['Log1', 'Log2'],
    'image': None  # Example byte array for image
}

def to_json():
    return mock_robot_data

def get_image():
    return mock_robot_data['image']