# Dictionaries
course = {
    "frontend": "react",
    "backend": "django"
}

social = dict(work="linkedin", family= "facebook")

print(course)
print(social)
print(type(social))
print(len(course))

# Access items in dictionaries
print(social["family"])
print(social.get('work'))

# list all keys
print(course.keys())

# list all values
print(course.values())

# list of key/value pairs as tuples
print(course.items())

# verify a key exist in a dict
print("frontend" in course)
print("nodejs" in course)

# changing values
course["backend"] = "nodejs"
social.update({"ai": "chatgpt"})

print(course)
print(social)

# Remove items
print(social.pop("ai"))
print(social)

social["forum"] = "nairaland"
print(social)

print(social.popitem())  # tuple
print(social)

# delete and clear

social["forum"] = "nairaland"
print(social)
del social["forum"]
print(social)


course.clear()
print(course)

del course


# copy dictionaries
