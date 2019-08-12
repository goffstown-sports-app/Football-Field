from picamera import PiCamera


def take_picture(photo_number):
    """Takes a picture using RPI camera
    
    Arguments:
        photo_number {int} -- number of consecutive photos
    
    Returns:
        string -- where the photo was written
    """
    camera = PiCamera()
    write_path = '/home/pi/Documents/image_{}.jpg'.format(str(photo_number))
    camera.capture(write_path)
    return write_path
