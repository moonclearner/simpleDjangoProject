from django.contrib import admin
from bbs import models
# Register your models here.


class BBS_admin(admin.ModelAdmin):
    '''add display list'''
    list_display = ('title', 'summary', 'signature', 'author', 'Created_at')
    list_filter = ('Created_at',)
    search_fields = ('title', 'author__user__username')
    # because author is user table's ForeignKey

    def signature(self, obj):
        # because author link signature
        return obj.author.signature
    signature.short_description = 'rename_sinature'


admin.site.register(models.Bbs, BBS_admin)
admin.site.register(models.Category)
admin.site.register(models.BBS_user)
