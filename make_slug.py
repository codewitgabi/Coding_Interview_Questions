import re


def make_slug(str_):
    comp = re.compile(r"\w+")
    return "-".join(comp.findall(str_))

print(make_slug("--hello world-"))
print(make_slug("hello world"))
print(make_slug("hello    world"))
