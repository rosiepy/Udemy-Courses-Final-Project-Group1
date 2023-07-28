from courses.models import Udemy, Price

# Fetch all Udemy objects
all_courses = Udemy.objects.all()

# Check each course for a valid price
for course in all_courses:
    try:
        # This line will raise an exception if the price does not exist
        price = course.price
        print(f"Course {course.course_id} has price {price.id}")
    except Price.DoesNotExist:
        print(f"Course {course.course_id} has no price!")
