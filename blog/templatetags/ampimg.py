import re
from django import template

register = template.Library()

@register.filter(name="ampimg")
def ampimg(content):
    img_pattern = r'(<img [^>]+>)'
    img_tags = re.findall(img_pattern, content)
    img_src_pattern = r'src="([^"]+)"'
    for img in img_tags:
        try:
            img_src = re.findall(img_src_pattern, img)[0]
        except Exception as NoImgSrc:
            img_src = None
        if img_src:
            amp_img = "<amp-img class=\"storyimages\" src=\"{0}\" width=\"360\" height=\"320\" layout=\"responsive\" alt=\"storyimage\">".format(img_src)
            content = content.replace(img, amp_img)
    return content
