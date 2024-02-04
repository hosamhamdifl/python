from bs4 import BeautifulSoup

# try:
with open('i:/python course/python/web-scrp/home.html', 'r') as html_file:
    content = html_file.read()
    soup=BeautifulSoup(content,'lxml')
    course_cards=soup.find_all('div',class_='card')
    for course in course_cards:
        course_name=course.h5.text
        course_price=course.a.text.split()[-1]

        print(f'{course_name} costs {course_price}')
        


    # courses_html_tags= soup.find_all('h5')
    # for courses in courses_html_tags:
    #     print(courses.text)

    # print(coutses_html_tags)
    # print(soup.prettify)


#         print(content)  # Check if the file content is read correctly
# except FileNotFoundError:
#     print("Error: The 'home.html' file was not found.")
# except Exception as e:
#     print(f"An error occurred: {e}")
