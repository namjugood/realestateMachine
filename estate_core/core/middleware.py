import time
import logging
from django.conf import settings

logger = logging.getLogger('estate_core')  # 앱 로거 사용

class RequestLoggingMiddleware:
    """
    API 요청 로깅을 위한 미들웨어
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # 요청 시작 시간
        start_time = time.time()

        # API 요청인 경우에만 로깅
        if request.path.startswith('/api/'):
            logger.info(f"Request: {request.method} {request.path}")

        response = self.get_response(request)

        # API 요청인 경우에만 로깅
        if request.path.startswith('/api/'):
            # 요청 처리 시간 계산
            duration = time.time() - start_time
            logger.info(f"Response: {response.status_code} - {duration:.2f}s")

        return response 