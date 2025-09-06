import os
from moviepy.editor import AudioFileClip, ImageClip, ColorClip


class AudioToMP4Converter:
    """
    오디오 파일을 MP4 비디오로 변환하는 클래스
    지원 형식: MP3, WAV
    """
    
    def __init__(self, input_dir, output_dir, background_image=None, video_size=(1920, 1080), fps=24):
        """
        변환기 초기화
        
        Args:
            input_dir (str): 입력 오디오 파일이 있는 디렉토리
            output_dir (str): 출력 MP4 파일을 저장할 디렉토리
            background_image (str, optional): 배경 이미지 파일 경로. None이면 검은색 배경 사용
            video_size (tuple): 비디오 크기 (width, height). 기본값: (1920, 1080)
            fps (int): 비디오 프레임레이트. 기본값: 24
        """
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.background_image = background_image
        self.video_size = video_size
        self.fps = fps
        
        # 지원하는 오디오 확장자
        self.supported_formats = ['.mp3', '.wav']
        
        # 출력 디렉토리 생성
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
    
    def _get_audio_files(self):
        """지원하는 오디오 파일 목록을 반환"""
        audio_files = []
        for file_name in os.listdir(self.input_dir):
            if any(file_name.lower().endswith(ext) for ext in self.supported_formats):
                audio_files.append(file_name)
        return audio_files
    
    def _create_background_clip(self, duration):
        """배경 클립 생성"""
        if self.background_image and os.path.exists(self.background_image):
            # 이미지 파일이 있으면 사용
            return ImageClip(self.background_image, duration=duration)
        else:
            # 이미지가 없으면 단색 배경 사용
            return ColorClip(size=self.video_size, color=(0, 0, 0), duration=duration)
    
    def convert_single_file(self, audio_file):
        """단일 오디오 파일을 MP4로 변환"""
        audio_path = os.path.join(self.input_dir, audio_file)
        mp4_name = os.path.splitext(audio_file)[0] + ".mp4"
        mp4_path = os.path.join(self.output_dir, mp4_name)
        
        print(f"[변환 중] {audio_file} → {mp4_name}")
        
        try:
            # 오디오 불러오기
            audio_clip = AudioFileClip(audio_path)
            
            # 배경 클립 생성
            background_clip = self._create_background_clip(audio_clip.duration)
            
            # 비디오 클립 생성
            video_clip = background_clip.set_audio(audio_clip)
            
            # MP4 저장
            video_clip.write_videofile(mp4_path, fps=self.fps)
            
            # 리소스 해제
            audio_clip.close()
            video_clip.close()
            background_clip.close()
            
            print(f"[완료] {mp4_name}")
            return True
            
        except Exception as e:
            print(f"[오류] {audio_file} 변환 실패: {str(e)}")
            return False
    
    def convert_all(self):
        """지원하는 모든 오디오 파일을 MP4로 변환"""
        audio_files = self._get_audio_files()
        
        if not audio_files:
            print("변환할 오디오 파일이 없습니다.")
            return
        
        print(f"총 {len(audio_files)}개의 파일을 변환합니다...")
        
        success_count = 0
        for audio_file in audio_files:
            if self.convert_single_file(audio_file):
                success_count += 1
        
        print(f"\n변환 완료! 성공: {success_count}/{len(audio_files)}")
    
    def convert_by_extension(self, extension):
        """특정 확장자의 파일만 변환"""
        if not extension.startswith('.'):
            extension = '.' + extension
        
        if extension not in self.supported_formats:
            print(f"지원하지 않는 확장자입니다: {extension}")
            print(f"지원 형식: {', '.join(self.supported_formats)}")
            return
        
        audio_files = [f for f in os.listdir(self.input_dir) 
                      if f.lower().endswith(extension)]
        
        if not audio_files:
            print(f"변환할 {extension} 파일이 없습니다.")
            return
        
        print(f"총 {len(audio_files)}개의 {extension} 파일을 변환합니다...")
        
        success_count = 0
        for audio_file in audio_files:
            if self.convert_single_file(audio_file):
                success_count += 1
        
        print(f"\n변환 완료! 성공: {success_count}/{len(audio_files)}")
