from django.contrib import admin
from .models import *

class Comment(admin.StackedInline):
    model = CommentCrm
    fields = ('comment_dt','comment_text')
    readonly_fields = ('comment_dt',)
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_status', 'order_name', 'order_phone', 'order_dt')
    list_display_links = ('id','order_name')
    search_fields = ('id','order_name','order_dt')
    list_filter = ('order_status',)
    list_editable = ('order_status', 'order_phone')
    list_per_page = 8
    list_max_show_all = 100
    readonly_fields = ('id', 'order_dt')
    fields = ('id', 'order_name', 'order_dt', 'order_phone', 'order_status')

    #comment class field
    inlines = [Comment,]
    

admin.site.register(Order, OrderAdmin)
admin.site.register(StatusCrm)
admin.site.register(CommentCrm)
