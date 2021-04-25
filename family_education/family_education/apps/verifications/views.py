import random
from django_redis import get_redis_connection
from rest_framework import status

from celery_tasks.sms.yuntongxun.sms import CCP
from verifications import constants
from rest_framework.response import Response
from rest_framework.views import APIView


import logging
logger = logging.getLogger('django')


class SMSCodeView(APIView):
    def get(self, request, mobile):
        redis_conn = get_redis_connection('verify_codes')
        send_flag = redis_conn.get('send_flag_%s' % mobile)

        if send_flag:
            return Response({'message': '发送短信过于频繁'}, status=status.HTTP_400_BAD_REQUEST)

        sms_code = '%06d' % random.randint(0, 999999)

        pl = redis_conn.pipeline()

        pl.setex('sms_%s' % mobile, constants.SMS_CODE_REDIS_EXPIRES, sms_code)
        pl.setex('send_flag_%s' % mobile, constants.SEND_SMS_CODE_INTERVAL, 1)

        pl.execute()
        expires = constants.SMS_CODE_REDIS_EXPIRES // 60
        from celery_tasks.sms.tasks import send_sms_code
        send_sms_code.delay(mobile, sms_code, expires)

        return Response({'message': '发送短信成功'})


