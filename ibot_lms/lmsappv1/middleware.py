import logging
from django.utils.deprecation import MiddlewareMixin

# Configure a logger for request/response logging
logger = logging.getLogger('request_logger')

class RequestResponseLoggingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Log incoming request details
        logger.info(f"Request: {request.method} {request.get_full_path()}")
        logger.info(f"Headers: {dict(request.headers)}")
        logger.info(f"Body: {request.body.decode('utf-8', errors='ignore')}")
    
    def process_response(self, request, response):
        # Log outgoing response details
        logger.info(f"Response status: {response.status_code}")
        logger.info(f"Response body: {response.content.decode('utf-8', errors='ignore')}")
        return response