# 🏠 부동산 실거래가 분석 시스템 API 명세서

## 📋 개요
이 문서는 부동산 실거래가 분석 시스템의 API 엔드포인트들을 상세하게 설명합니다.

## 🔑 인증
현재 API는 인증이 필요하지 않습니다.(추후 적용용)

## 📡 API 엔드포인트

### 1. 아파트 매매 실거래가 조회
```http
POST /api/properties/getRealEstateAptList/
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
            "resultMsg": "API 호출 성공"
        },
        "body": {
            "items": {
                "item": [
                    {
                        "aptDong": {},
                        "aptNm": "삼익",
                        "aptSeq": "11170-49",
                        "bonbun": "0300",
                        "bubun": "0301",
                        "buildYear": "1979",
                        "buyerGbn": {},
                        "cdealDay": {},
                        "cdealType": {},
                        "dealAmount": "105,000",
                        "dealDay": "30",
                        "dealMonth": "1",
                        "dealYear": "2016",
                        "dealingGbn": {},
                        "estateAgentSggNm": {},
                        "excluUseAr": "145.19",
                        "floor": "9",
                        "jibun": "300-301",
                        "landCd": "1",
                        "landLeaseholdGbn": "N",
                        "rgstDate": {},
                        "roadNm": "이촌로",
                        "roadNmBonbun": "00260",
                        "roadNmBubun": "00000",
                        "roadNmCd": "3102008",
                        "roadNmSeq": "02",
                        "roadNmSggCd": "11170",
                        "roadNmbCd": "0",
                        "sggCd": "11170",
                        "slerGbn": {},
                        "umdCd": "12900",
                        "umdNm": "이촌동"
                    }
                ],
                "numOfRows": 10,
                "pageNo": 1,
                "totalCount": 1
            }
        }
    }
}
```

### 2. 표준 지역 코드 조회
```http
POST /api/properties/getStanReginCd/
```

#### 요청 파라미터
| 파라미터 | 타입 | 필수 여부 | 설명 |
|----------|------|------------|------|
| regions | string | Y | 지역명(예 : '서울특별시', '장항동') |

#### 응답
```json
{
    "response": {
        "header": {
            "resultCode": "00",
            "resultMsg": "API 호출 성공"
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

### 3. 기간별 아파트 매매 실거래가 조회
```http
POST /api/properties/getRealEstateAptListDuration/
```

#### 요청 파라미터
| 파라미터 | 타입 | 필수 여부 | 설명 |
|----------|------|------------|------|
| regions_cd | string | Y | 지역코드 (예: 11110) |
| start_deal_ym | array | Y | 조회시작 계약년월 (예: "202403") |
| end_deal_ym | array | Y | 조회종료 계약년월 (예: "202405") |

#### 응답
```json
{
    "response": {
        "header": {
            "resultCode": "00",
            "resultMsg": "API 호출 성공"
        },
        "body": {
            "items": [
                {
                    "aptDong": {},
                    "aptNm": "삼익",
                    "aptSeq": "11170-49",
                    "bonbun": "0300",
                    "bubun": "0301",
                    "buildYear": "1979",
                    "buyerGbn": {},
                    "cdealDay": {},
                    "cdealType": {},
                    "dealAmount": "105,000",
                    "dealDay": "30",
                    "dealMonth": "1",
                    "dealYear": "2016",
                    "dealingGbn": {},
                    "estateAgentSggNm": {},
                    "excluUseAr": "145.19",
                    "floor": "9",
                    "jibun": "300-301",
                    "landCd": "1",
                    "landLeaseholdGbn": "N",
                    "rgstDate": {},
                    "roadNm": "이촌로",
                    "roadNmBonbun": "00260",
                    "roadNmBubun": "00000",
                    "roadNmCd": "3102008",
                    "roadNmSeq": "02",
                    "roadNmSggCd": "11170",
                    "roadNmbCd": "0",
                    "sggCd": "11170",
                    "slerGbn": {},
                    "umdCd": "12900",
                    "umdNm": "이촌동"
                }
            ],
            "totalCount": 1
        }
    }
}
```

## ⚠️ 에러 코드
 코드 | HTTP 상태 | 예외 클래스 | 설명 |
|------|-----------|---------------------------|--------------------------------|
| 00 | 200 | - | 정상 처리 |
| 01 | 401 | AuthenticationException | 인증 오류 |
| 02 | 400 | ParameterException | 필수 파라미터 누락 |
| 03 | 404/400 | DataNotFoundException | 데이터 없음 |
| 04 | 403 | PermissionException | 권한 없음 |
| 05 | 502 | ExternalAPIException | 외부 API 호출 오류 |
| 06 | 500 | DatabaseException | 데이터베이스 오류 |
| 07 | 400 | BusinessLogicException | 비즈니스 로직 오류 |
| 99 | 500 | ServerException | 기타 서버 오류 |

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
            "items":{
                "items": [],
                "numOfRows": "number",
                "pageNo": "number",
                "totalCount": "number"
            }
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