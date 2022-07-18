from pytube import YouTube

from .step import Step
from .step import StepException


class DownloadCaptions(Step):
    def process(self, data, inputs):
        for url in data:
            source = YouTube(url)
            if 'en' in source.captions:
                en_caption = source.captions.get_by_language_code('en')
                en_caption_convert_to_srt = (en_caption.generate_srt_captions())
                # save the caption to a file named Output.txt
                text_file = open("Output.txt", "w")
                text_file.write(en_caption_convert_to_srt)
                text_file.close()
