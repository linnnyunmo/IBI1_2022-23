# use matplotlib to generate a Pie chart
# list the kinds of movies and create a dictionary
# Also indicate the number of students
# list the words that can be replaced
# Make a pie chart and output it
import matplotlib.pyplot as plt
# kinds of genres and students amounts
genres = {'Comedy':73,'Action':42, 'Romance':38, 'Fantasy':28, 'Science-fiction':22, 'Horror':19, 'Crime':18, 'Documentary':12, 'History':8, 'War':7}
students = [73, 42, 38, 28, 22, 19, 18, 12, 8, 7]
# You can replace the words Comedy here, and the data will also change in the pie chart
print(genres['Comedy'])
# genre preferences among students uses pie chart
plt.pie(students, labels=genres,  autopct='%1.1f%%')
plt.title('Movie Genre Preferences among Students')
# show the results and the proportion shows the graph
plt.show()
