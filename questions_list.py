from bs4 import BeautifulSoup
# from tqdm import tqdm
from datetime import datetime
import requests


# main_url = "https://www.pepcoding.com/resources/online-java-foundation"
main_url = "https://www.pepcoding.com/resources/data-structures-and-algorithms-in-java-levelup"
# main_url = "https://www.pepcoding.com/resources/data-structures-and-algorithms-in-java-interview-prep"
html_text = requests.get(main_url).text
soup = BeautifulSoup(html_text, 'lxml')

topics = [topic.text.strip()
          for topic in soup.find_all('li', class_='collection-item row list-item')]

total_questions = 0

with open("log.txt", "a") as logfile:
    now = str(datetime.now())
    # current_time = now.strftime("%H:%M:%S")
    logfile.write("-----------------------------------\n\n")
    logfile.write(now+"\n\n")
    for i, topic in enumerate(topics):
        topic_url = main_url+'/'+topic.lower().replace(' ', '-')
        html_text = requests.get(topic_url).text
        topic_soup = BeautifulSoup(html_text, 'lxml')
        questions = topic_soup.find_all(
            'span', class_='name')

        print(f"{i}. {topic}: {len(questions)}")
        logfile.write(f"{i}. {topic}: {len(questions)}\n")
        total_questions += len(questions)

    #     for question in questions:
    #         question_name = question.find('span', class_='name').text.strip()
    #         print(question_name)

    print("\nTotal Questions:", total_questions)
    logfile.write(f"\nTotal Questions: {total_questions}\n\n")
