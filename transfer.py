""" ~~ transfer.py ~~
Transfer all the markdown files to html files
and save to the corresponding json file
"""

import os
import json
import timestring
from bs4 import BeautifulSoup


def run_pandoc(dr_folder, po_folder):
    """ This function transfers the markdown files
    inside drafts folder to html files in the
    posts folder.
    """
    for mkd in os.listdir(dr_folder):
        os.system('pandoc ' + os.path.join(dr_folder, mkd) +
                  ' -f markdown -t html -s -o ' +
                  os.path.join(po_folder, mkd.split('.')[0] + '.html'))

def to_json(po_folder):
    """ This function extracts the content and
    other information from the generated htmls
    and convert them to a single data json file.
    """
    json_ary = []
    for html in os.listdir(po_folder):
        data = ''
        dic = {}
        with open(os.path.join(po_folder, html)) as html_file:
            data = html_file.read()
        soup = BeautifulSoup(data, 'lxml')
        link = '/post/' + html.split('.')[0]
        title = soup.find('h3')['id']
        content = soup.find('body').contents
        str_content = ''
        for item in content:
            str_content += str(item)
        dic['link'] = link
        dic['title'] = title
        dic['content'] = str_content
        dic['date'] = '-'.join(html.split('-')[0:3])
        json_ary.append(dic)
    json_ary.sort(key=lambda item: timestring.Date(item['date']), reverse=True)

    with open('static/data.json', 'w') as out_json:
        json.dump(json_ary, out_json)

def main():
    """ Main function
    """
    run_pandoc('drafts', 'posts')
    to_json('posts')

if __name__ == '__main__':
    main()
