
from .models import User
from rest_framework.authentication import BaseAuthentication
from rest_framework.authentication import get_authorization_header
from rest_framework.exceptions import AuthenticationFailed
import jwt


class PurchasedUserTokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        try:
            print("User inside the authenticate")
            token = get_authorization_header(request).decode("utf-8").split()
            if len(token) == 2:
                de_value = jwt.decode(token[1], "purchasedUser_key", algorithms=["HS256"])
                admin = User.objects.filter(id=de_value["id"])
                
                if admin.exists():
                    return admin, de_value["role"]
                else:
                    raise AuthenticationFailed("Token authentication failed.")
            else:
                raise AuthenticationFailed("Token authentication failed.")
        except (jwt.ExpiredSignatureError, jwt.InvalidSignatureError):
            raise AuthenticationFailed("Token authentication failed.")
        except Exception:
            raise AuthenticationFailed("Token authentication failed.")

class CourseSubscribedUserTokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        try:
            print("User inside the authenticate")
            token = get_authorization_header(request).decode("utf-8").split()
            if len(token) == 2:
                de_value = jwt.decode(token[1], "CourseSubscribedUser_key", algorithms=["HS256"])
                admin = User.objects.filter(id=de_value["id"])
                
                if admin.exists():
                    return admin, de_value["role"]
                else:
                    raise AuthenticationFailed("Token authentication failed.")
            else:
                raise AuthenticationFailed("Token authentication failed.")
        except (jwt.ExpiredSignatureError, jwt.InvalidSignatureError):
            raise AuthenticationFailed("Token authentication failed.")
        except Exception:
            raise AuthenticationFailed("Token authentication failed.")
        
class AdminTokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        try:
            print("User inside the authenticate")
            token = get_authorization_header(request).decode("utf-8").split()
            if len(token) == 2:
                de_value = jwt.decode(token[1], "admin_key", algorithms=["HS256"])
                admin = User.objects.filter(id=de_value["id"])
                
                if admin.exists():
                    return admin, de_value["role"]
                else:
                    raise AuthenticationFailed("Token authentication failed.")
            else:
                raise AuthenticationFailed("Token authentication failed.")
        except (jwt.ExpiredSignatureError, jwt.InvalidSignatureError):
            raise AuthenticationFailed("Token authentication failed.")
        except Exception:
            raise AuthenticationFailed("Token authentication failed.")
        
class VisitorTokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        try:
            print("User inside the authenticate")
            token = get_authorization_header(request).decode("utf-8").split()
            if len(token) == 2:
                de_value = jwt.decode(token[1], "visitor_key", algorithms=["HS256"])
                admin = User.objects.filter(id=de_value["id"])
                
                if admin.exists():
                    return admin, de_value["role"]
                else:
                    raise AuthenticationFailed("Token authentication failed.")
            else:
                raise AuthenticationFailed("Token authentication failed.")
        except (jwt.ExpiredSignatureError, jwt.InvalidSignatureError):
            raise AuthenticationFailed("Token authentication failed.")
        except Exception:
            raise AuthenticationFailed("Token authentication failed.")
        