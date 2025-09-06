from converter import AudioToMP4Converter


# 기존 함수 호환성을 위한 래퍼 함수들
def convert_mp3_to_mp4(input_dir, output_dir, background_image=None):
    """MP3 파일을 MP4로 변환 (기존 함수 호환성)"""
    converter = AudioToMP4Converter(input_dir, output_dir, background_image)
    converter.convert_by_extension('.mp3')


def convert_wav_to_mp4(input_dir, output_dir, background_image=None):
    """WAV 파일을 MP4로 변환"""
    converter = AudioToMP4Converter(input_dir, output_dir, background_image)
    converter.convert_by_extension('.wav')



if __name__ == "__main__":
    # 사용 예시
    input_directory = r"C:\Users\User\Desktop\YouTube\만화자료main\drive-download-20250906T004714Z-1-001\(COMIC1☆12) [nul_Neverland (Navier Haruka 2T)] Ona-Club. _ 자위클럽 [Korean] [아카시의 개수공창]\오디오파일"
    output_directory = r"C:\Users\User\Desktop\YouTube\만화자료main\drive-download-20250906T004714Z-1-001\(COMIC1☆12) [nul_Neverland (Navier Haruka 2T)] Ona-Club. _ 자위클럽 [Korean] [아카시의 개수공창]\오디오파일\mp4_output"
    # background_img = None  # 배경 이미지 없이 검은색 배경 사용

    # convert_mp3_to_mp4(input_directory, output_directory)
    convert_wav_to_mp4(input_directory, output_directory)