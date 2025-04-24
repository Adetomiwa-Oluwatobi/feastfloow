from django.contrib import admin
from apps.posts.models import Post, Comment, Like

# Customizing the admin display for the Post model
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'created_at', 'content_snippet')
    search_fields = ('author__username', 'content')
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)

    def content_snippet(self, obj):
        """Provides a snippet of the content for easier viewing."""
        return obj.content[:50]  # Display first 50 characters
    content_snippet.short_description = 'Content Snippet'

    fieldsets = (
        (None, {
            'fields': ('author', 'content', 'image', 'created_at'),
        }),
    )

# Customizing the admin display for the Comment model
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_at', 'content_snippet')
    search_fields = ('author__username', 'post__content', 'content')
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)

    def content_snippet(self, obj):
        """Provides a snippet of the comment content for easier viewing."""
        return obj.content[:50]  # Display first 50 characters
    content_snippet.short_description = 'Content Snippet'

    fieldsets = (
        (None, {
            'fields': ('post', 'author', 'content', 'created_at'),
        }),
    )

# Customizing the admin display for the Like model
@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'post')
    search_fields = ('user__username', 'post__content')
    list_filter = ('post',)

    fieldsets = (
        (None, {
            'fields': ('user', 'post'),
        }),
    )
