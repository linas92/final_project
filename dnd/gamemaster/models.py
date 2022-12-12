from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()

    class Meta:
        ordering = ("name", )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/%s/" % self.slug
    

class Size(models.Model):
    size = models.CharField(max_length=255)
    short_description = models.TextField()
    slug = models.SlugField()

    class Meta:
        ordering = ("size", )

    def __str__(self):
        return self.size


class Monster(models.Model):
    ACTIVE = 'active'
    DRAFT = 'draft'

    CHOICES_STATUS = (
        (ACTIVE, 'Active'),
        (DRAFT, 'Draft')
    )

    name = models.CharField("name", max_length=50)
    about = models.TextField('summary')
    image = models.ImageField("image", upload_to='images', blank=True, null=True)
    slug = models.SlugField()
    size = models.ForeignKey(Size, related_name='monsters', on_delete=models.CASCADE)
    type = models.ForeignKey(Type, related_name='monsters', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=ACTIVE)

    class Meta:
        ordering = ("-created_at", )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/%s/%s/" % (self.type.slug, self.slug)


class Comment(models.Model):
    monster = models.ForeignKey(Monster, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

