from django.contrib import admin

from challenge.models import Challenge, SubChallenge


class SubChallengeInline(admin.StackedInline):
    model = SubChallenge
    extra = 1


@admin.register(Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    # TODO: 文件上传
    fields = ('id', 'index', 'name', 'category', 'detail', 'prompt')
    readonly_fields = ('id',)
    inlines = [SubChallengeInline]
