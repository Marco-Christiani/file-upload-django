import requests
from requests_toolbelt.streaming_iterator import StreamingIterator
from requests_toolbelt.multipart import encoder
from clint.textui.progress import Bar as ProgressBar

def handle_uploaded_file(file, callback):
    """
    :param file: Of type UploadedFile
    """

    generator = file.chunks()  # Create generator
    size = file.size  # Get size
    # content_type = file.content_type  # Get the content-type of the data

    # def my_callback(monitor):
    #     bar.show(monitor.bytes_read)

    streamer = StreamingIterator(size, generator, callback=callback)
    # encoder_len = streamer.size
    # bar = ProgressBar(expected_size=encoder_len, filled_char='=')

    # r = requests.put('http://localhost:4444/', data=streamer,
    #                   headers={'Content-Type': content_type})
    http_url = 'http://localhost:4444/'
    params = {'dsName': 'BigDisk', 'dcPath': 'Datacenter'}
    headers = {'Content-Type': 'application/octet-stream'}
    cookie = {'chocolate_chip': ' "cd9c342ce3df6d2944d45132c6feca1e161f39bc"; $Path=/'}

    request = requests.put(http_url,
                           params=params,
                           data=streamer,
                           headers=headers,
                           cookies=cookie,
                           verify=False)

def handle_uploaded_file_monitor(file):
    """
    :param file: Of type UploadedFile
    """


    e = encoder.MultipartEncoder(
        fields={file.name : file.read()}
        )
    encoder_len = e.len
    bar = ProgressBar(expected_size=encoder_len, filled_char='=')
    def callback(monitor):
        bar.show(monitor.bytes_read)

    m = encoder.MultipartEncoderMonitor(e, callback)
    r = requests.put('http://localhost:4444/', data=m,
                      headers={'Content-Type': m.content_type})
    print('\nUpload finished! (Returned status {} {})'.format(
        r.status_code, r.reason
        ))

