import pandas as pd
import requests


def SDSS_image_scarper(ra , dec , name = None , scale = 0.2 , height = 1024 , width = 1024):
    """
    Parameters
    ----------
    ra : float [deg]
        Right ascension of the target. 
    dec : float [deg]
        Declination of the taget.
    name : string, optional
        The output file name.
    scale : float, optional
        Scale of image in arsec per pixel, by default 0.2
    height : int, optional
        The size of the image in pixels, by default 1024
    width : int, optional
        The size of the image in pixels, by default 1024
    """

    img_data = requests.get(f'https://skyserver.sdss.org/dr16/SkyServerWS/ImgCutout/getjpeg?ra={ra}&dec={dec}&scale={scale}&height={height}&width={width}&opt=G').content

    if name == None:
        with open(f'{int(ra)}_{int(dec)}.jpg', 'wb') as handler:
            handler.write(img_data)
    else:
        with open(f'{name}.jpg', 'wb') as handler:
            handler.write(img_data)


if __name__ == '__main__':

    SDSS_image_scarper(name = 'FileName', ra = 186.156492036, dec = 10.839043812)
