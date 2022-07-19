from pytube import YouTube
import time

from .step import Step
from .step import StepException


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        start = time.time()
        for yt in data:
            if utils.caption_file_exists(yt):
                print('found existing caption file')
                continue

            source = YouTube(yt.url)
            if 'en' in source.captions:
                en_caption = source.captions.get_by_language_code('en')
                en_caption_convert_to_srt = (en_caption.generate_srt_captions())
                text_file = open(utils.get_captions_filepath(yt.url), "w", encoding='utf-8')
                text_file.write(en_caption_convert_to_srt)
                text_file.close()

        end = time.time()
        print('took', end - start, 'seconds')

        return data

