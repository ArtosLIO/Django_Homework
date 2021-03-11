from django.contrib import admin
# from .models import Author, Person, BookInLibrary, BooksAuthors
from .models import Post, Comment, Like, Dislike
from .models import MyUser


# admin.site.register(Article, ArticleAdmin)

# admin.site.register(Author)
# admin.site.register(Person)
# admin.site.register(BooksAuthors)
# admin.site.register(BookInLibrary)

# admin.site.register(AuthorPost)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Dislike)
admin.site.register(MyUser)