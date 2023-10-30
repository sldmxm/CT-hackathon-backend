from rest_framework.pagination import PageNumberPagination


class TablePagePagination(PageNumberPagination):
    page_size = 30
