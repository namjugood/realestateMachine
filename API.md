# 🏠 부동산 실거래가 분석 시스템 API 명세서

## 📋 개요
이 문서는 부동산 실거래가 분석 시스템의 API 엔드포인트들을 상세하게 설명합니다.

## 🔑 인증
현재 API는 인증이 필요하지 않습니다.(추후 적용용)

## 📡 API 엔드포인트

### 1. 아파트 매매 실거래가 조회
```http
GET /api/properties/getRealEstateAptList/
```

#### 요청 파라미터
| 파라미터 | 타입 | 필수 여부 | 설명 |
|----------|------|------------|------|
| regions_cd | string | Y | 지역코드 (예: 11110) |
| deal_ym | string | Y | 계약년년월 (예: 202403) |

#### 응답
```json
{
    "response": {
        "header": {
            "resultCode": "00",
            "resultMsg": "NORMAL SERVICE."
        },
        "body": {
            "items": [
                {
                    "거래금액": "95,000",
                    "건축년도": "2008",
                    "년": "2024",
                    "법정동": "서울특별시 강남구 역삼동",
                    "아파트": "래미안아파트",
                    "월": "3",
                    "일": "15",
                    "전용면적": "84.97",
                    "지번": "123-45",
                    "지역코드": "11680",
                    "층": "8"
                }
            ],
            "numOfRows": 10,
            "pageNo": 1,
            "totalCount": 1
        }
    }
}
```

### 2. 표준 지역 코드 조회
```http
GET /api/properties/getStanReginCd/
```

#### 요청 파라미터
| 파라미터 | 타입 | 필수 여부 | 설명 |
|----------|------|------------|------|
| regions | string | Y | 지역명(예 : '서울특별시') |

#### 응답
```json
{
    "response": {
        "header": {
            "resultCode": "00",
            "resultMsg": "NORMAL SERVICE."
        },
        "body": {
            "items": [
                {
                    "code": "11110",
                    "name": "서울특별시 종로구"
                }
            ],
            "numOfRows": 10,
            "pageNo": 1,
            "totalCount": 1
        }
    }
}
```

## ⚠️ 에러 코드
| 코드 | 설명 |
|------|------|
| 00 | 정상 처리 |
| 01 | 인증 오류 |
| 02 | 필수 파라미터 누락 |
| 03 | 데이터 없음 |
| 99 | 기타 오류 |

## 📝 응답 형식
모든 API 응답은 다음과 같은 공통 형식을 따릅니다:

```json
{
    "response": {
        "header": {
            "resultCode": "string",
            "resultMsg": "string"
        },
        "body": {
            "items": [],
            "numOfRows": "number",
            "pageNo": "number",
            "totalCount": "number"
        }
    }
}
```

## 🔄 페이지네이션
- `pageNo`: 현재 페이지 번호 (기본값: 1)
- `numOfRows`: 페이지당 항목 수 (기본값: 10)
- `totalCount`: 전체 항목 수

## 📌 주의사항
1. API 호출 시 반드시 유효한 API 키를 사용해야 합니다.
2. 요청 제한이 있을 수 있으므로 과도한 API 호출은 피해야 합니다.
3. 응답 데이터는 UTF-8 인코딩을 사용합니다.

## 🔜 향후 계획
1. JWT 기반 인증 시스템 추가
2. API 요청 제한 (Rate Limiting) 구현
3. 캐싱 시스템 도입
4. 추가 API 엔드포인트 구현
   - 부동산 시세 분석
   - 지역별 통계
   - 가격 추이 분석 