import string
from django.utils.text import slugify

# def random_string_generator(size=10, chars = string.ascii_lowercase + sring.digits):
#     return ''.join(random.choice(chars) for _ in range(size))

# def unique_slug_generator(instance, new_slug=None):
#     if new_slug is not None:
#         slug = new_slug
#     else:
    slug = slugify(instance.title)
    # Klass = instance._class_
    # qs_exists = Klass.objects.filter(slug = slug).exists()
    # if qs_exists:
    #     new_slug = "{slug}-{randstr}".format(
    #         slug = slug, randstr = random_string_generator(size=4))
    #     return unique_slug_generator(instance, new_slug = slug)
    # return slug