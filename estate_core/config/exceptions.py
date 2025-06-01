from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import APIException

class ExceptionView(Response):
    """
    API 응답 형식을 통일하기 위한 커스텀 Response 클래스
    """
    def __init__(self, data=None, status=None, template_name=None, headers=None,
                 exception=False, content_type=None):
        if data is not None:
            # body에 header가 들어있으면 제거
            if isinstance(data, dict) and 'header' in data:
                data = {k: v for k, v in data.items() if k != 'header'}

            # body 안에 body가 있으면 한 번 벗겨냄
            if isinstance(data, dict) and 'body' in data and isinstance(data['body'], dict):
                data = data['body']

            # 예외 객체인 경우
            if isinstance(data, Exception):
                status = getattr(data, 'status_code', status.HTTP_500_INTERNAL_SERVER_ERROR)
                error_code = getattr(data, 'default_code', 'unknown_error')
                error_message = str(data) if str(data) else getattr(data, 'default_detail', '알 수 없는 오류가 발생했습니다.')
                
                formatted_data = {
                    "response": {
                        "header": {
                            "resultCode": str(status) if isinstance(status, int) else status,
                            "resultMsg": error_message
                        },
                        "body": data
                    }
                }
            # 에러 응답인 경우
            elif status and status >= 400:
                formatted_data = {
                    "response": {
                        "header": {
                            "resultCode": str(status) if isinstance(status, int) else status,
                            "resultMsg": str(data) if isinstance(data, (str, dict)) else "API 호출 실패"
                        },
                        "body": data
                    }
                }
            # 성공 응답인 경우
            else:
                formatted_data = {
                    "response": {
                        "header": {
                            "resultCode": "00",
                            "resultMsg": "API 호출 성공"
                        },
                        "body": data
                    }
                }
            super().__init__(formatted_data, status, template_name, headers, exception, content_type)
        else:
            super().__init__(data, status, template_name, headers, exception, content_type)

def custom_exception_handler(exc, context):
    """
    API 응답 메시지를 통일하기 위한 커스텀 예외 처리기
    """
    # 기본 예외 처리기 호출
    response = exception_handler(exc, context)

    if response is not None:
        # ExceptionView를 사용하여 응답 형식 통일
        return ExceptionView(
            data=response.data.get('detail', str(response.data)),
            status=response.status_code
        )

    return response

class ParameterException(APIException):
    status_code = "02"
    default_detail = '필수 파라미터가 누락되었습니다.'
    default_code = 'parameter_missing'

class AuthenticationException(APIException):
    status_code = "01"
    default_detail = '인증이 필요합니다.'
    default_code = 'authentication_required'

class PermissionException(APIException):
    status_code = "04"
    default_detail = '접근 권한이 없습니다.'
    default_code = 'permission_denied'

class ExternalAPIException(APIException):
    status_code = "05"
    default_detail = '외부 API 호출 중 오류가 발생했습니다.'
    default_code = 'external_api_error'

class DatabaseException(APIException):
    status_code = "06"
    default_detail = '데이터베이스 작업 중 오류가 발생했습니다.'
    default_code = 'database_error'

class BusinessLogicException(APIException):
    status_code = "07"
    default_detail = '비즈니스 로직 처리 중 오류가 발생했습니다.'
    default_code = 'business_logic_error'

class DataNotFoundException(APIException):
    status_code = "03"
    default_detail = '요청한 데이터가 존재하지 않습니다.'
    default_code = 'data_not_found'

class ServerException(APIException):
    status_code = "99"
    default_detail = '서버 오류가 발생했습니다.'
    default_code = 'server_error' 