# 🏠 부동산 실거래가 분석 시스템

## 1. 📋 프로젝트 명
부동산 실거래가 분석 시스템 (Real Estate Transaction Analysis System)

## 2. 🎯 프로젝트 목표
- 📊 공공데이터포털의 부동산 실거래가 데이터를 활용한 분석 시스템 구축
- 💻 사용자 친화적인 웹 인터페이스를 통한 데이터 조회 및 분석 기능 제공
- 📈 실거래가 데이터의 시각화 및 통계 분석 기능 구현
- 📉 부동산 시장 동향 파악을 위한 데이터 기반 의사결정 지원

## 3. ⚙️ 개발환경
<details>
<summary>🔧 개발 환경 상세 보기</summary>

<table>
    <thead>
        <tr>
            <th>구분</th>
            <th>항목</th>
            <th>상세 내용</th>
        </tr>
    </thead>
    <tr>
        <td rowspan="5"><strong>백엔드</strong></td>
        <td>🐍 언어</td>
        <td>Python 3.13</td>
    </tr>
    <tr>
        <td>🎯 프레임워크</td>
        <td>Django 5.0</td>
    </tr>
    <tr>
        <td>🔄 API 프레임워크</td>
        <td>Django REST Framework</td>
    </tr>
    <tr>
        <td>💾 데이터베이스</td>
        <td>SQLite3</td>
    </tr>
    <tr>
        <td>🗄️ ORM</td>
        <td>Django ORM</td>
    </tr>
    <tr>
        <td rowspan="3"><strong>개발 도구</strong></td>
        <td>💻 IDE</td>
        <td>Visual Studio Code</td>
    </tr>
    <tr>
        <td>🔄 버전 관리</td>
        <td>Git</td>
    </tr>
    <tr>
        <td>📡 API 테스트</td>
        <td>Postman</td>
    </tr>
    <tr>
        <td rowspan="6"><strong>주요 라이브러리</strong></td>
        <td>🔌 requests</td>
        <td>HTTP 요청 처리</td>
    </tr>
    <tr>
        <td>📊 pandas</td>
        <td>데이터 분석 및 처리</td>
    </tr>
    <tr>
        <td>🔑 python-dotenv</td>
        <td>환경 변수 관리</td>
    </tr>
    <tr>
        <td>🔄 django-filter</td>
        <td>Django 필터링 기능</td>
    </tr>
    <tr>
        <td>🔒 django-cors-headers</td>
        <td>CORS 설정</td>
    </tr>
    <tr>
        <td>📊 matplotlib</td>
        <td>데이터 시각화 및 그래프 생성</td>
    </tr>
</table>
</details>

## 4. ⏱️ 타임라인
<details>
<summary>📅 개발 진행 상황 보기</summary>

### 완료된 작업
| 날짜 | 작업 내용 | 세부 사항 |
|------|-----------|-----------|
| 5월 23일 | 🏗️ 프로젝트 초기 설정 | • Django 프로젝트 생성<br>• 기본 디렉토리 구조 설정<br>• requirements.txt 생성<br>• core 앱 생성 및 기본 설정 |
| 5월 25일 | 💾 데이터베이스 및 API 설정 | • SQLite3 데이터베이스 초기화<br>• 공공데이터포털 API 키 설정<br>• .env 파일 구성<br>• 기본 API 호출 함수 구현 |
| 5월 30일 | 🔄 프로젝트 재설정 | • 프로젝트 완전 API 서버화<br>• 기본 앱 구조 생성<br>• 사용자 인증 시스템 구현<br>• 부동산 매물 기본 모델 설계<br>• 공통 유틸리티 함수 구현 |
| 5월 31일 | 🔄 앱 구조 개선 및 API 엔드포인트 구현 | • 부동산 매물 관리 앱 이름을 `properties`에서 `realEstate`로 변경<br>• 마이그레이션 파일 재설정 및 의존성 수정<br>• URL 패턴 재구성 및 라우팅 설정<br>• API 엔드포인트 구현<br>  - `/api/properties/getRealEstateAptList/`: 아파트 매매 실거래가 조회<br>  - `/api/properties/getStanReginCd/`: 표준 지역 코드 조회 |

### 진행 예정 작업
| 기간 | 작업 내용 | 세부 사항 |
|------|-----------|-----------|
| 6월 1일 ~ 6월 5일 | 🎨 프론트엔드 개발<br>🔄 기능 개선 | • 기본 UI 템플릿 구현<br>• jQuery UI datepicker 통합<br>• 데이터 표시 테이블 구현<br>• AJAX를 통한 비동기 데이터 로딩<br>• 에러 처리 및 사용자 피드백 개선<br>• UI/UX 개선 |
| 6월 6일 ~ 6월 10일 | 📈 데이터 시각화<br>🔍 검색 필터<br>⚡ 성능 최적화 | • 차트 및 그래프 구현<br>• 통계 분석 기능 추가<br>• 지역별 검색 기능<br>• 가격대별 필터링<br>• 데이터 캐싱 구현<br>• 쿼리 최적화 |
| 6월 11일 ~ 6월 15일 | ✅ 테스트<br>🚀 배포 준비 | • 단위 테스트 작성<br>• 통합 테스트 수행<br>• 배포 환경 구성<br>• 문서화 완료 |

### 진행률
- [x] 1단계: 프로젝트 초기화 (100%)
- [x] 2단계: 기본 API 연동 (100%)
- [ ] 3단계: 프론트엔드 개발 (0%)
- [ ] 4단계: 데이터 시각화 (0%)
- [ ] 5단계: 테스트 및 배포 (0%)
</details>

## 5. 🚀 설치 및 실행 방법
<details>
<summary>📋 설치 및 실행 방법 보기</summary>

### 필수 요구사항
- Python 3.8 이상
- pip (Python 패키지 관리자)
- Git
- 공공데이터포털 API 키 (https://www.data.go.kr)

### 설치 단계
1. 저장소 클론
```bash
git clone https://github.com/yourusername/realEstateMachine.git
cd realEstateMachine
```

2. 가상환경 생성 및 활성화
```bash
# 가상환경 생성
python -m venv venv

# 가상환경 활성화
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. 의존성 패키지 설치
```bash
# pip 업그레이드
python -m pip install --upgrade pip

# requirements.txt 설치
pip install -r requirements.txt
```

4. 환경 변수 설정
- `.env` 파일을 프로젝트 루트 디렉토리에 생성
- 공공데이터포털 API 키 설정
```
# .env 파일 예시
API_KEY=your_api_key_here
DEBUG=True
SECRET_KEY=your_secret_key_here
```

5. 데이터베이스 설정
```bash
# 마이그레이션 파일 생성
python manage.py makemigrations

# 데이터베이스 마이그레이션
python manage.py migrate

# 관리자 계정 생성 (선택사항)
python manage.py createsuperuser
```

6. 정적 파일 수집
```bash
python manage.py collectstatic
```

7. 서버 실행
```bash
# 개발 서버 실행
python manage.py runserver

# 특정 포트로 실행 (예: 8000번 포트)
python manage.py runserver 8000
```

### 실행 확인
1. 웹 브라우저에서 `http://localhost:8000` 접속
2. 관리자 페이지는 `http://localhost:8000/admin`에서 접근 가능

### 주의사항
- API 키는 절대 공개 저장소에 커밋하지 마세요
- `.env` 파일은 `.gitignore`에 포함되어 있어야 합니다
- 개발 환경과 프로덕션 환경의 설정을 분리하여 관리하세요

### 문제 해결
1. 패키지 설치 오류
```bash
# 가상환경 재활성화
deactivate
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# pip 캐시 삭제 후 재설치
pip cache purge
pip install -r requirements.txt
```

2. 데이터베이스 오류
```bash
# 데이터베이스 초기화
python manage.py flush
python manage.py migrate
```

3. 정적 파일 오류
```bash
# 정적 파일 재수집
python manage.py collectstatic --clear
```
</details>

## 6. 📁 프로젝트 구조
```
realEstateMachine/
├── src/                     # 소스 코드 디렉토리
│   ├── apps/                # 애플리케이션 디렉토리
│   │   ├── core/            # 핵심 기능
│   │   │   ├── __init__.py
│   │   │   ├── models.py    # 기본 모델 정의 (BaseModel)
│   │   │   ├── views.py     # 메인 페이지 뷰
│   │   │   └── urls.py      # URL 라우팅
│   │   │
│   │   ├── real_estate/     # 부동산 관련 기능
│   │   │   ├── __init__.py
│   │   │   ├── models.py    # 부동산 모델
│   │   │   ├── views.py     # 부동산 관련 뷰
│   │   │   └── urls.py      # URL 라우팅
│   │   │
│   │   ├── users/        # 사용자 관리 기능
│   │   │   ├── __init__.py
│   │   │   ├── models.py    # 사용자 모델
│   │   │   ├── views.py     # 사용자 관련 뷰
│   │   │   └── urls.py      # URL 라우팅
│   │   │
│   │   └── __init__.py
│   │
│   ├── config/           # 프로젝트 설정
│   │   ├── __init__.py
│   │   ├── settings.py     # 프로젝트 설정 (Django 설정, 앱 등록, 미들웨어 등)
│   │   ├── urls.py         # 메인 URL 설정 (앱 URL 포함)
│   │   ├── asgi.py         # ASGI 설정
│   │   └── wsgi.py         # WSGI 설정
│   │
│   ├── static/           # 정적 파일
│   │   ├── css/          # CSS 파일
│   │   └── js/           # JavaScript 파일
│   │
│   └── templates/        # 템플릿 파일
│       └── index.html    # 메인 페이지 템플릿
│
├── venv/                 # 가상환경
├── .env                  # 환경 변수 설정 (API 키, 시크릿 키 등)
├── .gitignore           # Git 제외 파일 목록
├── db.sqlite3           # SQLite 데이터베이스
├── manage.py            # Django 관리 스크립트
├── requirements.txt     # 의존성 패키지
└── README.md            # 프로젝트 문서
```

### 앱별 주요 기능

<details>
<summary>📱 앱별 주요 기능 상세 보기</summary>

<table>
    <thead>
        <tr>
            <th>앱</th>
            <th>기능</th>
            <th>상세 내용</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan="2"><strong>Common</strong></td>
            <td>API 호출 유틸리티</td>
            <td>
                • <code>callGetApi</code>: 외부 API 호출 및 응답 처리<br>
                • <code>xmlToJson</code>: XML 응답을 JSON으로 변환
            </td>
        </tr>
        <tr>
            <td>캐싱 유틸리티(추가예정)</td>
            <td>
                • API 응답 캐싱<br>
                • 캐시 관리 기능
            </td>
        </tr>
        <tr>
            <td rowspan="3"><strong>Real Estate</strong></td>
            <td>부동산 매물 관리</td>
            <td>
                • 매물 등록/수정/삭제<br>
                • 매물 조회 및 필터링
            </td>
        </tr>
        <tr>
            <td>실거래가 데이터 관리</td>
            <td>
                • 공공데이터포털 API 연동<br>
                • 실거래가 데이터 조회<br>
                • 지역 코드 관리
            </td>
        </tr>
        <tr>
            <td>API 엔드포인트</td>
            <td>
                • <code>/api/properties/getRealEstateAptList/</code>: 아파트 매매 실거래가 조회<br>
                • <code>/api/properties/getStanReginCd/</code>: 표준 지역 코드 조회
            </td>
        </tr>
        <tr>
            <td rowspan="2"><strong>Users(추가예정)</strong></td>
            <td>사용자 인증</td>
            <td>
                • JWT 기반 인증<br>
                • 권한 관리
            </td>
        </tr>
        <tr>
            <td>사용자 관리</td>
            <td>
                • 회원가입/로그인<br>
                • 사용자 정보 관리
            </td>
        </tr>
    </tbody>
</table>
</details>

## 7. 💡 주요 기능
자세한 API 명세는 [API.md](./API.md) 문서를 참조하세요.
- 📊 실시간 부동산 실거래가 데이터 조회
  - 아파트 매매 실거래가 조회 API (`/api/properties/getRealEstateAptList/`)
  - 지역별, 기간별 실거래가 데이터 제공
  - 상세 매물 정보 (거래금액, 건축년도, 면적 등) 제공

- 📅 기간별 데이터 필터링
  - 계약년월(`deal_ym`) 기준 데이터 조회
  - 최근 거래 데이터 우선 조회
  - 기간별 거래 동향 분석

- 📈 데이터 시각화 및 분석(추후 생성성)
  - 거래금액 추이 그래프
  - 지역별 가격 분포 분석
  - 면적대별 거래 현황 분석

- 🔍 지역별 검색 기능
  - 표준 지역 코드 조회 API (`/api/properties/getStanReginCd/`)
  - 시/도, 구/군 단위 지역 검색
  - 법정동 기준 상세 지역 검색

