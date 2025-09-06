# Audio to MP4 변환기

이 프로젝트는 오디오 파일(MP3, WAV)을 MP4 비디오 파일로 변환하는 Python 라이브러리입니다. 오디오 파일에 배경 이미지나 단색 배경을 추가하여 비디오로 만들어줍니다.

## 기능

- **다양한 오디오 형식 지원**: MP3, WAV 파일 변환
- **유연한 배경 설정**: 배경 이미지 또는 단색 배경 지원
- **한글 경로 지원**: Windows 한글 경로 완벽 지원
- **배치 처리**: 폴더 내 모든 오디오 파일 자동 변환
- **클래스 기반 설계**: 재사용 가능한 모듈화된 구조
- **세밀한 제어**: 비디오 크기, 프레임레이트 등 커스터마이징 가능

## 설치 방법

### 1. Python 환경 설정
```bash
# 가상환경 생성 (권장)
conda create -n youtube python=3.9
conda activate youtube

# 또는 venv 사용
python -m venv youtube
# Windows
youtube\Scripts\activate
# macOS/Linux
source youtube/bin/activate
```

### 2. FFmpeg 설치
FFmpeg는 비디오 처리에 필수입니다.

**Windows (Conda 사용):**
```bash
conda install -c conda-forge ffmpeg
```

**Windows (직접 설치):**
1. [FFmpeg 공식 사이트](https://ffmpeg.org/download.html)에서 다운로드
2. 압축 해제 후 PATH 환경변수에 추가

**macOS:**
```bash
brew install ffmpeg
```

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install ffmpeg
```

### 3. Python 패키지 설치
```bash
pip install -r requirements.txt
```

## 사용 방법

### 1. 기본 사용법 (스크립트 실행)
```python
python main.py
```

### 2. 클래스 직접 사용
```python
from converter import AudioToMP4Converter

# 변환기 생성
converter = AudioToMP4Converter(
    input_dir="입력폴더경로",
    output_dir="출력폴더경로",
    background_image="배경이미지.jpg",  # 선택사항
    video_size=(1920, 1080),  # 비디오 크기
    fps=24  # 프레임레이트
)

# 모든 오디오 파일 변환
converter.convert_all()

# 특정 확장자만 변환
converter.convert_by_extension('.mp3')
converter.convert_by_extension('.wav')

# 단일 파일 변환
converter.convert_single_file('audio.mp3')
```

### 3. 기존 함수 방식 (호환성)
```python
from main import convert_mp3_to_mp4, convert_wav_to_mp4

# MP3 변환
convert_mp3_to_mp4("입력폴더경로", "출력폴더경로")

# WAV 변환
convert_wav_to_mp4("입력폴더경로", "출력폴더경로", "배경이미지.jpg")
```

## 설정

`main.py` 파일의 `if __name__ == "__main__":` 부분에서 경로를 수정하세요:

```python
if __name__ == "__main__":
    input_directory = r"입력폴더경로"
    output_directory = r"출력폴더경로"
    # background_img = "배경이미지.jpg"  # 선택사항
    
    # 클래스 방식 사용
    converter = AudioToMP4Converter(input_directory, output_directory)
    converter.convert_all()
    
    # 또는 기존 함수 방식
    convert_mp3_to_mp4(input_directory, output_directory)
```

## 주요 특징

### 클래스 기반 설계
- `AudioToMP4Converter` 클래스로 모든 변환 기능 제공
- 재사용 가능하고 확장 가능한 구조
- 세밀한 설정 제어 가능

### 지원 기능
- **오디오 형식**: MP3, WAV
- **배경 옵션**: 이미지 파일 또는 단색 배경
- **비디오 설정**: 크기, 프레임레이트 커스터마이징
- **배치 처리**: 폴더 내 모든 파일 자동 변환
- **단일 파일**: 개별 파일 변환 가능

### 사용 편의성
- 한글 경로 완벽 지원
- 기존 함수 호환성 유지
- 자동 출력 디렉토리 생성
- 상세한 진행 상황 표시

## 주의사항

- 한글 경로를 사용할 때는 `r"경로"` 형태로 raw string을 사용하세요
- 배경 이미지가 없으면 기본 크기(1920x1080)의 검은색 배경이 사용됩니다
- 기본 프레임레이트는 24fps입니다

## 문제 해결

### MoviePy 설치 오류
```bash
pip uninstall moviepy
pip install moviepy==1.0.3
```

### FFmpeg 관련 오류
FFmpeg가 제대로 설치되었는지 확인:
```bash
ffmpeg -version
```

### 한글 경로 문제
경로에 한글이 포함된 경우 raw string을 사용:
```python
path = r"C:\한글경로\폴더"
```
