# def analysis_three(book_list):
#     print("Analysis of which book has appeared the most in the book list, and how many times it has appeared")
#     list_of_book_titles = [book['name'] for book in book_list]
#     unique_set_of_book_titles = set(list_of_book_titles)
#     top_book = {'title':'fake','count':0}
#     for unique_book_title in unique_set_of_book_titles:
#         result_counts = len(list(filter(lambda real_title : real_title == unique_book_title, list_of_book_titles)))
#         if result_counts > top_book['count']:
#             top_book['count'] = result_counts
#             top_book['title'] = unique_book_title
#     print(f"\nThe Top Book in the book list is: {top_book['title']}, and it has been listed {top_book['count']} times.")


list_of_names = ['jen','george','joaquin','juice','gato','cyrus','solo','george','jen','gato','jen']
unique_names = set(list_of_names)
top_name = {'name':'fake','count':0}
for unique_name in unique_names:
    result_counts = len(list(filter(lambda name : name == unique_name, list_of_names)))
    if result_counts > top_name['count']:
        top_name['name'] = unique_name
        top_name['count'] = result_counts
print(top_name)