import os
import urllib.request
from urllib.parse import parse_qs, urlparse
from moviepy.editor import VideoFileClip


def get_gif_by_url(url: str) -> str:
    """
    Create a gif from video.
    :param url: Direct url to TikTok video
    :return: path to created Gif
    """

    path_to_vid = urllib.request.urlretrieve(url, 'tiktok_vid.mp4')[0]  # download video by DIRECT url

    # get unique ID from URL
    parsed_url = urlparse(url)
    tt_id = parse_qs(parsed_url.query)['l'][0]

    video_clip = VideoFileClip(path_to_vid)
    filename = f'TikTok_video_{tt_id}.gif'
    video_clip.write_gif(filename)

    fullpath = os.path.join(os.getcwd(), filename)

    if os.path.exists('tiktok_vid.mp4'):
        os.remove('tiktok_vid.mp4')

    return fullpath


def main() -> None:

    url = input("Enter Direct Link to TikTok video (or press ENTER to use the default one): ")
    if not url:
        url = 'https://v16-webapp.tiktok.com/07202de92617b01baa903e1bc3f6fbca/62e93a03/video/tos/useast2a/tos-useast2a-ve-0068c004/34e7aebcebf9455ebbf5352ebd2627ed/?a=1988&ch=0&cr=0&dr=0&lr=tiktok_m&cd=0%7C0%7C1%7C0&cv=1&br=2120&bt=1060&btag=80000&cs=0&ds=3&ft=ar5S8qT2mo0PD.Jv_uaQ9miJzObpkV1PC6&mime_type=video_mp4&qs=0&rc=Zmk1OjUzZ2loNWU3PDg0NkBpajk3eDw6ZnMzZTMzNzczM0BiNC8wYzI2Ni0xNl9hMC8uYSNeaDVucjRvLTFgLS1kMTZzcw%3D%3D&l=202208020851210102171342080C06AA8B'
    path_to_gif = get_gif_by_url(url)
    print(f'Successfully created GIF: {path_to_gif}')


if __name__ == '__main__':
    main()
