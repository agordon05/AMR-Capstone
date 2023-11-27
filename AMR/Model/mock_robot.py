# from PIL import Image
# import io
# import base64
# Mock data
# mock_robot_data = {
#     'id': 1,
#     'status': 'Active',
#     'message': 'Mock message',
#     'x_pos': 100.0,
#     'y_pos': 200.0,
#     'rotation': 45.0,
#     'x_destination': 150.0,
#     'y_destination': 150.0,
#     'qrScan': 'mockQRCode',
#     'loggerList': ['Log1'],
#     'image': None  # Example byte array for image
# }

# def create_mock_image_base64():
#     image = Image.new('RGB', (100, 100), color = 'red')  # A 100x100 red image
    
#     img_byte_arr = io.BytesIO()
#     image.save(img_byte_arr, format='JPEG')
#     img_byte_arr = img_byte_arr.getvalue()

#     return base64.b64encode(img_byte_arr).decode('utf-8')

# mock_robot_data['image'] = create_mock_image_base64()

# def to_json():
#     mock_robot_data['image'] = create_mock_image_base64()
#     return mock_robot_data

# def get_image():
#     return mock_robot_data['image']