import requests
from bs4 import BeautifulSoup as bs
import csv
import os

cur_wrk_dir=os.getcwd()
folder_name='python-scraper-github/data'

# Collect the github page page = requests.get('https://github.com/trending')
page=requests.get('https://github.com/trending')
#print(page)

soup = bs(page.text, 'html.parser')
#print(soup)


# get the repo list
repo_list = soup.find_all(class_="Box-row")


print(len(repo_list))
# find all instances of that class (should return 25 as shown in the github main page)
#repo_list = repo.find_all(class_='Box-row')

#print(len(repo_list))
# Open writer with name
file_name = "github_trending_today.csv"
file_path=os.path.abspath(os.path.join(cur_wrk_dir,folder_name,file_name))
print(file_path)
# set newline to be '' so that that new rows are appended without skipping any
f = csv.writer(open(file_path, 'w', newline=''))
# write a new row as a header
f.writerow(['Developer', 'Repo Name', 'Number of Stars'])


print("Lets see the final list")
print('Developer \t repo_name \t no of stars')
for repo in repo_list:
    #print (repo)
    #print(repo.find(class_="h3 lh-condensed").parent.text.strip())
    full_repo_list=repo.find(class_="h3 lh-condensed")
    #check=repo.find(class_="h3 lh-condensed")
    #print(type(full_repo_list))
    #print(full_repo_list)
    #developer=full_repo_list.span.string
    repo_dtl=full_repo_list.a.text.strip() 
    #print(develop)
    #print('s')
    #print(type(star))
    #print(star.split('/'))
    repo_info=repo_dtl.split('/')
    repo_devloper=repo_info[0].strip()
    repo_name=repo_info[1].strip()

    #print(repo_devloper)
    #print(repo_name)

    # lets find the stars
    get_footer=repo.find(class_="f6 color-fg-muted mt-2")
    stars=get_footer.a.text.strip()
    #print(stars)
    print(repo_devloper,'\t',repo_name,'\t', stars)

    #add information as a row into the csv table
    f.writerow([repo_devloper, repo_name, stars])