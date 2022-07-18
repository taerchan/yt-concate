from yt_concate.pipeline.steps.get_video_list import GetVideoList
from yt_concate.pipeline.steps.download_captions import DownloadCaptions
from yt_concate.pipeline.steps.step import StepException

from yt_concate.pipeline.pipeline import Pipeline
CHANNEL_ID = 'UCz4tgANd4yy8Oe0iXCdSWfA'


def main():
    inputs = {
        'channel_id': CHANNEL_ID
    }
    steps = [
        GetVideoList(),
        DownloadCaptions(),
        ]

    p = Pipeline(steps)
    p.run(inputs)


if __name__ == '__main__':
    main()
