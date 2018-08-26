from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Yalnızca bir nesnenin sahiplerinin onu düzenlemesine izin vermek için özel izin.
    """

    def has_object_permission(self, request, view, obj):
        #Okuma izinlerine herhangi bir istek için izin verilir,
        #bu yüzden her zaman GET, HEAD veya OPTIONS isteklerine izin verilir.
        if request.method in permissions.SAFE_METHODS:
            return True
        #Yazma izinleri yalnızca nesne sahibine izin verilir.
        return obj.owner == request.user
