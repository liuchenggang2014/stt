def transcribe_gcs_jp(gcs_uri):
    """Asynchronously transcribes the audio file specified by the gcs_uri."""
    from google.cloud import speech

    client = speech.SpeechClient()

    audio = speech.RecognitionAudio(uri=gcs_uri)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.AMR_WB,
        sample_rate_hertz=16000,
        # language_code="en-US",
        language_code="ja-JP",
    )

    operation = client.long_running_recognize(config=config, audio=audio)

    print("Waiting for operation to complete...")
    response = operation.result(timeout=90)

    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        print(u"Transcript: {}".format(result.alternatives[0].transcript))
        print("Confidence: {}".format(result.alternatives[0].confidence))

def transcribe_gcs_en(gcs_uri):
    """Asynchronously transcribes the audio file specified by the gcs_uri."""
    from google.cloud import speech

    client = speech.SpeechClient()

    audio = speech.RecognitionAudio(uri=gcs_uri)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.FLAC,
        sample_rate_hertz=16000,
        language_code="en-US",
    )

    operation = client.long_running_recognize(config=config, audio=audio)

    print("Waiting for operation to complete...")
    response = operation.result(timeout=90)

    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        print(u"Transcript: {}".format(result.alternatives[0].transcript))
        print("Confidence: {}".format(result.alternatives[0].confidence))

transcribe_gcs_en("gs://cloud-samples-tests/speech/brooklyn.flac")

print("*******************...")

transcribe_gcs_jp("gs://cliu201-bucket/60_test.amr")
# transcribe_gcs_jp("gs://cliu201-bucket/60_10_2.wav")
# transcribe_gcs_jp("gs://cliu201-bucket/60_10_3.wav")
# transcribe_gcs_jp("gs://cliu201-bucket/60_10_4.wav")
# transcribe_gcs_jp("gs://cliu201-bucket/60_10_5.wav")
# transcribe_gcs_jp("gs://cliu201-bucket/60_10_6.wav")

