from django.utils.deprecation import MiddlewareMixin  # 插入中间键


class BookMiddlewareMixin1(MiddlewareMixin):

    def process_request(self, request):
        print('111')

    def process_response(self, request, response):
        print('响应前111')

        return response# 响应要返回


class BookMiddlewareMixin2(MiddlewareMixin):
    def process_request(self, request):
        print('222')

    def process_response(self, request, response):
        print('响应前222')
