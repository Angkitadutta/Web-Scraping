from bs4 import BeautifulSoup
import requests



print('Put some skill that you are not familiar with')
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text
    #print(html_text)
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    for job in jobs:
        published_date = job.find('span', class_= 'sim-posted').span.text
        if 'few' in published_date:
            #print(job)
            #company_name = job.find('h3', class_ = 'joblist-comp-name')
            #company_name = job.find('h3', class_ = 'joblist-comp-name').text

            #repalce white spaces
            company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','')
            skills = job.find('span', class_= 'srp-skills').text.replace(' ','')
            more_info = job.header.h2.a['href']

            if unfamiliar_skill not in skills:

                print(f"Company Name: {company_name.strip()}")
                print(f"Required Skills: {skills.strip()}")
                print(f"More Information: {more_info}")
                #print(skills)
                #print(company_name)
                

                #published_date = job.find('span', class_= 'sim-posted').span.text
                #print(published_date)

                #print(f'''
                #company Name: {company_name}
                #Required Skills: {skills}
                #''')

                print('')

if __name__ == '__main__':
    while True:
        find_jobs()
        