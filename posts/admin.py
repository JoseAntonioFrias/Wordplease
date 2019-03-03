from django.contrib import admin
from django.utils.safestring import mark_safe

from blogs.models import Blog
from posts.models import Post

admin.site.site_header = 'Django Wordplease'
admin.site.index_title = 'Django Wordplease Admin'
admin.site.site_title = 'Django Wordplease Admin'


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('user_full_name', 'title', 'description', 'formatted_create_date', 'formatted_last_modification')

    def user_full_name(self, obj):
        return "{0} {1}".format(obj.owner.first_name, obj.owner.last_name)

    def formatted_create_date(self, obj):
        return obj.create_date.strftime('%d/%m/%Y %H:%M')
        return obj.create_date.strftime('%d/%m/%Y %H:%M')

        formatted_create_date.short_description = 'Create date'
        formatted_create_date.admin_order_field = 'create_date'

    def formatted_last_modification(self, obj):
        return obj.last_modification.strftime('%d/%m/%Y %H:%M')

    formatted_last_modification.short_description = 'Last modification date'
    formatted_last_modification.admin_order_field = 'last_modification'

    readonly_fields = ('last_modification',)
    fieldsets = (
        (None, {
            'fields': ('title', 'description')
        }),
        ("Información adicional", {
            'fields': ('create_date', 'last_modification')
        }))


class CategoryInLine(admin.TabularInline):
    model = Post.categories.through


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('imagen_html',)
    list_display = ('user_full_name', 'title', 'summary', 'body', 'imagen_html', 'get_categories',
                    'formatted_pub_date')

    list_filter = ['owner', 'blog', 'pub_date', 'categories']
    search_fields = ['owner__first_name', 'owner__last_name', 'owner__username', 'blog__title']

    def formatted_pub_date(self, post):
        return post.pub_date.strftime('%d/%m/%Y %H:%M')

    def user_full_name(self, post):
        return "{0} {1}".format(post.owner.first_name, post.owner.last_name)

    def imagen_html(self, post):
        if post.image:
            return mark_safe('<img src="{0}" alt="{1}" title="{1}" width="100" height="100">'.format(post.image.url,
                                                                                                     post.title))
        else:
            return

    formatted_pub_date.short_description = 'Pub date'
    formatted_pub_date.admin_order_field = 'pub_date'

    imagen_html.short_description = 'Image'

    fieldsets = [
        [None, {
            'fields': ['owner', 'blog', 'title']
        }],
        ['Multimedia', {
            'fields': ['imagen_html', 'video']
        }],
        ['Detalle', {
            'fields': ['summary', 'body', 'categories'],
        }],
        ['Fechas', {
            'fields': ['pub_date', 'creation_date', 'last_modification']
        }]
    ]

    inlines = [CategoryInLine]
